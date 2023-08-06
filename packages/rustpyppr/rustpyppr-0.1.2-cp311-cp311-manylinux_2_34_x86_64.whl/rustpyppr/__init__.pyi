from typing import Dict, List



def forward_push(edge_dict: Dict[int, List[int]],
                          source: int,
                          damping_factor: float = 0.85,
                          r_max: float = 1e-2) -> Dict[int, float]:
    """Computes the Personalized PageRank using Forward Push, using vectors lazily.

     Nodes that are visited are converted in indices, allowing fast lookup using a vector instead of HashMap.
     This conversion is done for only for the nodes the algorithm encounters, in a lazy way.
     See [forward_push_vec] for the eager version.

     # Arguments
     * `edge_dict` - Dictionary mapping each node (positive integer) to the list of its neighbouring nodes (also positive integers).
     * `source` - The node from which the PPR starts.
     * `damping_factor` - The parameter that controls the probability of the random surfer to continue surfing. Typically 0.85.
     * `r_max` - controls the precision of the calculation. The computation will stop when at most `r_max` residual probability is left in total in the nodes.
     # Examples

     ```Python3
     d = {3:[5, 1], 1:[3], 5:[3]}
     source = 3
     ppr = forward_push(d, source, 0.85, 1e-2)
     ```"""
    ...

def multiple_forward_push(edge_dict: Dict[int, List[int]],
                                   sources: List[int],
                                   damping_factor: float = 0.85,
                                   r_max: float = 1e-2) -> Dict[int, Dict[int, float]]:
    """Performs multiple forward push ppr on the same graph with different sources.

    The result is logically equivalent to calling the regular forward_push function sequentially.
    However, the results are computed in parallel. Performs parallel calls to [forward_push].
    # Arguments
    * `edge_dict` - Dictionary mapping each node (positive integer) to the list of its neighbouring nodes (also positive integers).
    * `sources` - The list of nodes from which the PPR computations start.
    * `damping_factor` - The parameter that controls the probability of the random surfer to continue surfing. Typically 0.85.
    * `r_max` - controls the precision of the calculation. The computation will stop when at most `r_max` residual probability is left in total in the nodes.
    # Examples

    ```Python
    d = {3:[5, 1], 1:[3], 5:[3]}
    sources = [3, 5]
    ppr = multiple_forward_push(d, sources, 0.85, 1e-2)
    ```"""
    ...

def parallel_forward_push(edge_dicts: List[Dict[int, List[int]]],
                                   sources: List[int],
                                   damping_factor: float = 0.85,
                                   r_max: float = 1e-2) -> Dict[int, Dict[int, float]]:
    """Performs multiple forward push ppr on different graphs with different sources.

    The result is logically equivalent to calling the regular forward_push function sequentially.
    However, the results are computed in parallel. Performs parallel calls to [forward_push].
    # Arguments
    * `edge_dicts` - List of dictionaries mapping each node (positive integer) to the list of its neighbouring nodes (also positive integers).
    * `sources` - The list of nodes from which the PPR computations start.
    * `damping_factor` - The parameter that controls the probability of the random surfer to continue surfing. Typically 0.85.
    * `r_max` - controls the precision of the calculation. The computation will stop when at most `r_max` residual probability is left in total in the nodes.
    # Examples

    ```Python
    d1 = {3:[5, 1], 1:[3], 5:[3]}
    d2 = {3:[5, 1], 1:[3,5], 5:[3]}
    sources = [3, 5]
    ppr = parallel_forward_push([d1, d2], sources, 0.85, 1e-2)
    ```"""
    ...
