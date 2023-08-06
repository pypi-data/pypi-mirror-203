import numpy as np
import numpy.typing as npt
import matplotlib.pyplot as plt
from scipy.stats import hypergeom, _distn_infrastructure
from typing import Union, List, Mapping, Tuple, Optional, Any
from typeguard import typechecked

### CONSTANTS
_GENOME_CONC_PG = 6.6
_PG_TO_NG = 0.001
_GENOME_CONC_NG = _GENOME_CONC_PG * _PG_TO_NG
_UG_TO_NG = 1000

@typechecked
def simulate_gRNA_library_prep(guide_library_size: int, PCR1_input_ug: float, MOI: float,  perfection_rate: float, genome_conc_ng: float = _GENOME_CONC_NG, _PCR1_input_number_duplicate:float = 1, PCR1_cycles: int = 5, _PCR1_purification_yield: float = 0.6,
                              _PCR1_purification_eluted_volume: int = 50, _PCR2_input_volume: float = 22.5,
                              PCR2_cycles:int = 7, _PCR2_purification_yield: float = 0.6,
                              _total_target_reads: int = 150000, plot=True):
    '''
    PCR1 input
    '''
    _PCR1_input_number_molecules: float = (((PCR1_input_ug*_UG_TO_NG)/genome_conc_ng)) * MOI
    _PCR1_input_guide_coverage: float = ((_PCR1_input_number_molecules*perfection_rate)/_PCR1_input_number_duplicate)/guide_library_size
    #print(_PCR1_input_guide_coverage)
    '''
        PCR1 amplification
    '''
    
    _PCR1_product_number_molecules: float = _PCR1_input_number_molecules * 2**PCR1_cycles
    _PCR1_product_number_duplicates: float = _PCR1_input_number_duplicate * 2**PCR1_cycles
    _PCR1_product_guide_coverage: float = (_PCR1_product_number_molecules*perfection_rate) / guide_library_size

    #print(_PCR1_product_guide_coverage)
    '''
    PCR1 purification
    '''
    
    _PCR1_product_purified_number_molecules: float = _PCR1_product_number_molecules * _PCR1_purification_yield
    _PCR1_product_purified_number_duplicates: float = _PCR1_product_number_duplicates * _PCR1_purification_yield 

    '''
    PCR2 input
    '''
    _PCR2_input_fraction: float = _PCR2_input_volume/_PCR1_purification_eluted_volume
    _PCR2_input_number_molecules: float  = _PCR2_input_fraction * _PCR1_product_purified_number_molecules
    _PCR2_input_guide_coverage: float = _PCR2_input_number_molecules / guide_library_size
    #print(_PCR2_input_guide_coverage)
    
    '''
    Determine distribution of number of duplicates in PCR2 input
    
    Assuming PCR purification yield is deterministic
    '''
    population_size: int = int(_PCR1_product_purified_number_molecules)
    success_size: int = int(_PCR1_product_purified_number_duplicates)
    trial_count: int = int(_PCR2_input_number_molecules)

    #print(f"Number duplicates in PCR2 distribution: hypergeom(N={population_size}, M={success_size}, n={trial_count})")
    num_dups_in_PCR2_input_DIST: _distn_infrastructure.rv_frozen = hypergeom(population_size, success_size, trial_count)
    #num_dups_in_PCR2_input_EXPECTED_VALUE = hypergeom.mean(population_size, success_size, trial_count)

    #print(f"PCR2 input hypergeom interval inputs: hypergeom.interval({0.99}, population_size={population_size}, success_size={success_size}, trial_count={trial_count})")
    num_dups_in_PCR2_input_VALUES_LEFT_QUANTILE, num_dups_in_PCR2_input_VALUES_RIGHT_QUANTILE = hypergeom.interval(0.99, population_size, success_size, trial_count)

    num_dups_in_PCR2_input_VALUES_LEFT_QUANTILE: int = int(num_dups_in_PCR2_input_VALUES_LEFT_QUANTILE)
    num_dups_in_PCR2_input_VALUES_RIGHT_QUANTILE: int = int(num_dups_in_PCR2_input_VALUES_RIGHT_QUANTILE)
    #print(f"Considering PCR duplicates in range: {num_dups_in_PCR2_input_VALUES_LEFT_QUANTILE} to {num_dups_in_PCR2_input_VALUES_RIGHT_QUANTILE}")

    num_dups_in_PCR2_input_VALUES: np.ndarray  = np.arange(num_dups_in_PCR2_input_VALUES_LEFT_QUANTILE, num_dups_in_PCR2_input_VALUES_RIGHT_QUANTILE)

    # For each x-value in the interval of interest, get the probability of that number of rarities in the PCR1 input
    num_dups_in_PCR2_input_PROB: np.ndarray = num_dups_in_PCR2_input_DIST.pmf(num_dups_in_PCR2_input_VALUES)

    
    '''
    PCR2 amplification
    '''
    _PCR2_product_number_molecules: float = _PCR2_input_number_molecules * 2**PCR2_cycles
    num_dups_in_PCR2_prod_VALUES: np.ndarray = num_dups_in_PCR2_input_VALUES * 2**PCR2_cycles
    
    '''
    PCR2 purification
    '''
    _PCR2_product_purified_number_molecules: float = _PCR2_product_number_molecules * _PCR2_purification_yield
    num_dups_in_PCR2_prod_purified_VALUES: np.ndarray = num_dups_in_PCR2_prod_VALUES * _PCR2_purification_yield

    '''
        NGS
    '''
    population_size: int = int(_PCR2_product_purified_number_molecules)
    success_sizes: np.ndarray = num_dups_in_PCR2_prod_purified_VALUES.astype(int)
    trial_count: int = _total_target_reads

    num_dups_in_NGS_input_2D_DIST: np.ndarray = np.asarray([hypergeom(population_size, success_size, trial_count) for success_size in success_sizes]) # for each potential amount of duplicates of a PCR1 input molecule, get distribution of number of duplicates in reads
    num_dups_in_NGS_input_1D_DIST_MARGINAL_NGS_VALUES: np.ndarray = np.arange(0, 1000) # number of reads per input molecule
    num_dups_in_NGS_input_1D_DIST_MARGINAL_NGS_PROBS: np.ndarray = np.asarray([sum([num_dups_in_NGS_input_2D_DIST[i].pmf(num_reads_per_input) *  num_dups_in_PCR2_input_PROB[i] for i in range(len(num_dups_in_PCR2_input_PROB))]) for num_reads_per_input in num_dups_in_NGS_input_1D_DIST_MARGINAL_NGS_VALUES])
    
    average_num_of_duplicates_per_PCR1_input_molecule: float = sum(num_dups_in_NGS_input_1D_DIST_MARGINAL_NGS_PROBS[np.where(np.isin(num_dups_in_NGS_input_1D_DIST_MARGINAL_NGS_VALUES,np.arange(2,1000)))[0]] * (np.arange(2,1000)-1)) * _PCR1_input_number_molecules
    
    num_dups_in_NGS_input_1D_DIST_MARGINAL_NGS_VALUES_ZT: np.ndarray = num_dups_in_NGS_input_1D_DIST_MARGINAL_NGS_VALUES[1:]
    num_dups_in_NGS_input_1D_DIST_MARGINAL_NGS_PROBS_ZT: np.ndarray = num_dups_in_NGS_input_1D_DIST_MARGINAL_NGS_PROBS[1:]
    

    # Plot the hypergeometric distribution for number of duplicates in PCR1 input
    if plot:
        threshold=15
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(num_dups_in_NGS_input_1D_DIST_MARGINAL_NGS_VALUES[:threshold], num_dups_in_NGS_input_1D_DIST_MARGINAL_NGS_PROBS[:threshold], 'bo', label="Exact Hypergeometric")
        ax.vlines(num_dups_in_NGS_input_1D_DIST_MARGINAL_NGS_VALUES[:threshold], 0, num_dups_in_NGS_input_1D_DIST_MARGINAL_NGS_PROBS[:threshold], lw=2)
        ax.set_xlabel('Number of average reads per\nPCR1 input molecule')
        ax.set_ylabel('Probability')
        ax.set_title("Number of Reads per PCR1 Input Molecule\nread coverage = {}".format(_total_target_reads))
        ax.set_xticklabels(ax.get_xticks(), rotation = 45)

        plt.show()

    # Get the exact guide coverage
    guide_coverage_exact = (((_PCR1_input_number_molecules*(1-num_dups_in_NGS_input_1D_DIST_MARGINAL_NGS_PROBS[0]))*perfection_rate)/_PCR1_input_number_duplicate)/guide_library_size
    
    return guide_coverage_exact




@typechecked
def get_target_coverage_linear_interop(guide_coverages_np: np.ndarray, total_reads_targets_np: np.ndarray, target_coverage: float = 100):
    '''
        Provided the list of reads and their simulated guide coverage, get the interpolated reads given the target coverage
    '''
    # Get the closest simulated coverages to the guide coverages
    target_coverage_indices = np.argsort(abs(guide_coverages_np-target_coverage))[0:2]
    target_coverage_indices = target_coverage_indices[np.argsort(-total_reads_targets_np[target_coverage_indices])]

    # Calculate the interpolation and return
    return np.ceil(total_reads_targets_np[target_coverage_indices[0]]  - ((total_reads_targets_np[target_coverage_indices[0]] - total_reads_targets_np[target_coverage_indices[1]]) * (guide_coverages_np[target_coverage_indices[0]] - target_coverage)/(guide_coverages_np[target_coverage_indices[0]] - guide_coverages_np[target_coverage_indices[1]])))




@typechecked
def get_target_coverage_per_sample(gDNA_amounts_and_moi: Tuple[List[int], int], perfection_rate: float, guide_library_size:int, genome_conc_ng: float = _GENOME_CONC_NG, target_coverage_input=None, target_coverage_percentage: float=0.9, max_target_coverage_input: int = 2000, read_intervals_count: int= 20):
    
    gDNA_amounts = gDNA_amounts_and_moi[0]
    moi = gDNA_amounts_and_moi[1]

    # Iterate through all gDNA amounts
    for gDNA_amount in gDNA_amounts:
        
        PCR1_input_coverage = (((((gDNA_amount*_UG_TO_NG)/genome_conc_ng)*moi))*perfection_rate)/guide_library_size
        target_coverage_suggested = PCR1_input_coverage * target_coverage_percentage
        max_reads = PCR1_input_coverage * guide_library_size * 5
        
        # Retrieve list of reads to pass into simulation then run simulation
        total_reads_targets_res = np.arange(max_reads/read_intervals_count, max_reads, max_reads/read_intervals_count)
        guide_coverages_res = [simulate_gRNA_library_prep(guide_library_size = guide_library_size, PCR1_input_ug = gDNA_amount, MOI = moi,
                                      _total_target_reads=int(total_reads), perfection_rate=perfection_rate, genome_conc_ng=genome_conc_ng, plot=False) for total_reads in total_reads_targets_res]
        
        # Get the reads for the target coverage
        target_read_amount_suggested = get_target_coverage_linear_interop(np.asarray(guide_coverages_res), np.asarray(total_reads_targets_res), target_coverage=target_coverage_suggested)
        if target_coverage_input is not None:
            target_read_amount_input = get_target_coverage_linear_interop(np.asarray(guide_coverages_res), np.asarray(total_reads_targets_res), target_coverage=target_coverage_input)

        # Visualize
        print(f"gDNA: {gDNA_amount}; MOI: {int(moi)}; Desired Coverage={int(target_coverage_input)}, Suggested Coverage={int(target_coverage_suggested)}, Max Coverage={int(PCR1_input_coverage)}, \n Reads for Desired Coverage={int(target_read_amount_input)}, Reads for Suggested Coverage={int(target_read_amount_suggested)}")
        plt.scatter(total_reads_targets_res, guide_coverages_res)
        
        # Show coverage indicators
        plt.axhline(y=PCR1_input_coverage, color="blue", label="Maximum coverage based on input values")
        plt.axhline(y=target_coverage_input, color="blue", linestyle="dashed", label=f"Desired coverage: {int(target_coverage_input)}")
        plt.axhline(y=target_coverage_suggested, color="blue", linestyle="dotted", label=f"Suggested coverage: {int(target_coverage_suggested)}")
        
        plt.axvline(x=target_read_amount_input, color="black", linestyle="dashed", label=f"For desired coverage {int(target_coverage_input)}, target reads for coverage={int(target_read_amount_input)}")
        plt.axvline(x=target_read_amount_suggested, color="black", linestyle="dotted", label=f"For suggested coverage {int(target_coverage_suggested)}, target reads ={int(target_read_amount_suggested)}")
        
        plt.xlabel("Total Reads Sequenced")
        plt.ylabel("Guide Coverage")
        plt.title("Guide Coverage by Total Reads Sequence\ngDNA amount={}, MOI={}".format(gDNA_amount,moi))
        plt.ylim(0, PCR1_input_coverage + 20)
        plt.xlim(0, np.maximum(max_reads + (max_reads/10), target_read_amount_suggested + (target_read_amount_suggested/10)))
        plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
        plt.show()
        
        