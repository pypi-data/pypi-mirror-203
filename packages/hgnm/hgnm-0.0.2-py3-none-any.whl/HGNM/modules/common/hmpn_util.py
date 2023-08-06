from collections import Counter
from typing import Dict, Tuple

import torch
import torch_geometric
import copy

from HGNM.util.Types import *
from HGNM.util import Keys, Keys as Keys
from HGNM.util.Keys import AGGR_AGGR, CONCAT_AGGR, AGENT


def get_default_edge_relation(sender_node_type: str, receiver_node_type: str,
                              include_nodes: bool = True) -> Union[str, Tuple[str, str, str]]:
    """
    Wrapper function for uniform edge identifiers. Builds a string 'sender_node_type+"2"+receiver_node_type'

    Args:
        sender_node_type: Node type that sends a message along the specified edge
        receiver_node_type: Node type that receives a message along the specified edge
        include_nodes: If True, return a 3-tuple of strings
        (sender_node_type, 'sender_node_type+"2"+receiver_node_type', receiver_node_type).
        If False, return a string 'sender_node_type+"2"+receiver_node_type'

    Returns: If include_nodes,a 3-tuple of strings
        (sender_node_type, 'sender_node_type+"2"+receiver_node_type', receiver_node_type).

        Else a string 'sender_node_type+"2"+receiver_node_type'

    """
    edge_relation = sender_node_type + "2" + receiver_node_type
    if include_nodes:
        return sender_node_type, edge_relation, receiver_node_type
    else:
        return edge_relation


def tuple_to_string(input_tuple: Tuple) -> str:
    """
    Converts a tuple to a string.
    Args:
        input_tuple: The tuple to convert

    Returns: The string representation of the tuple

    """
    return "".join(input_tuple)


def noop(*args, **kwargs):
    """
    No-op function.
    Args:
        *args: Arguments to be passed to the function
        **kwargs: Keyword arguments to be passed to the function

    Returns: None

    """
    return None


def get_scatter_reducers(names: Union[List[str], str]) -> List[callable]:
    """
    Translates a list of strings to the appropriate functions from torch_scatter.
    Args:
        names: (List of) the names of the scatter operations: "std", "mean", "max", "min", "sum"

    Returns: (List of) the appropriate functions from torch_scatter with signature (src, index, dim, dim_size)

    """
    if type(names) == str:  # fallback case for single reducer
        names = [names]
    names: List[str]

    return [get_scatter_reduce(name) for name in names]


def get_scatter_reduce(name: str) -> callable:
    """
    Translates a string to the appropriate function from torch_scatter.
    Args:
        name: the name of the scatter operation: "std", "mean", "max", "min", "sum"

    Returns: the appropriate function from torch_scatter with signature (src, index, dim)

    """
    if name == "mean":
        from torch_scatter import scatter_mean
        scatter_reduce = scatter_mean
    elif name == "min":
        from torch_scatter import scatter_min
        scatter_reduce = lambda *args, **kwargs: scatter_min(*args, **kwargs)[0]
    elif name == "max":
        from torch_scatter import scatter_max
        scatter_reduce = lambda *args, **kwargs: scatter_max(*args, **kwargs)[0]
    elif name == "sum":
        from torch_scatter import scatter_add
        scatter_reduce = scatter_add
    elif name == "std":
        from torch_scatter import scatter_std
        scatter_reduce = scatter_std
    else:
        raise ValueError(f"Unknown scatter reduce '{name}'")
    return scatter_reduce


def unpack_homogeneous_features(graph: Data, agent_node_type: str = AGENT):
    """
    Unpacking important data from homogeneous graphs.
    Args:
        graph (): The input homogeneous observation
        agent_node_type: The name of the type of graph node that acts as the agent
     Returns:
        Tuple of edge_features, edge_index, node_features, global_features and batch
    """
    # edge features
    edge_features = graph.edge_attr
    edge_index = graph.edge_index.long()  # cast to long for scatter operators

    # node features
    node_features = graph.x if graph.x is not None else graph.pos

    # global features
    global_features = get_global_features(graph=graph) if hasattr(graph, "u") else None
    batch = graph.batch if hasattr(graph, "batch") else None
    if batch is None:
        batch = torch.zeros(node_features.shape[0]).long()

    return ({agent_node_type: node_features},
            {get_default_edge_relation(agent_node_type, agent_node_type): {"edge_index": edge_index,
                                                                           "edge_attr": edge_features}},
            global_features,
            {agent_node_type: batch})


def unpack_heterogeneous_features(graph: Batch):
    # todo clean up!
    """
    Unpacking important data from heterogeneous graphs.
    Args:
        graph (): The input heterogeneous observation

    Returns:
        Tuple of edge_features, edge_index, node_features, global_features and batch
    """
    # edge features
    edge_features = [edge_store.edge_attr for edge_store in graph.edge_stores]  # todo previously had a copy.deepcopy
    edge_indices = [edge_store.edge_index for edge_store in graph.edge_stores]

    # node features
    node_features = [node_store.x
                     for node_store in graph.node_stores]  # todo previously had a copy.deepcopy

    # global features
    global_features = get_global_features(graph=graph) if hasattr(graph, "u") else None
    batches = [node_store.batch if hasattr(node_store, "batch")
               else torch.zeros(node_store.num_nodes).long()
               for node_store in graph.node_stores]

    # package updated features
    node_types = graph.node_types
    edge_types = graph.edge_types
    edge_index_dict = dict(zip(edge_types, edge_indices))
    edge_feature_dict = dict(zip(edge_types, edge_features))
    edge_dict = {}
    for key, value in edge_index_dict.items():
        edge_dict[key] = {"edge_index": edge_index_dict[key], "edge_attr": edge_feature_dict[key]}
    return dict(zip(node_types, node_features)), edge_dict, global_features, dict(zip(node_types, batches))


def get_global_features(graph: Batch) -> torch.Tensor:
    """
    Unpacks the global features of Batch
    Args:
        graph: The graph to unpack global features from
    Returns:
        Empty graph if no global features could be found, otherwise the global features
    """
    """
    global_features = graph_tensor.u
    if not hasattr(graph_tensor, "batch"):  # only one graph.
        global_features = global_features[None, :]
    else:  # Reshape global features to fit the graph
        num_graphs = graph_tensor.batch[-1] + 1
        if len(global_features > 0):  # Reshape global features to fit the graph
            global_features = global_features.reshape((-1, int(len(global_features) / num_graphs)))
        else:  # No global features. make a bigger placeholder
            global_features = global_features[None, :][[0] * num_graphs]
    global_features = global_features.float()
    """
    global_features = graph.u
    num_graphs = graph.u.shape[0]  # [-1] + 1
    if len(global_features > 0):  # Reshape global features to fit the graph
        global_features = global_features.reshape((-1, int(len(global_features) / num_graphs)))
    else:  # No global features. make a bigger placeholder
        global_features = global_features[None, :][[0] * num_graphs]
    global_features = global_features.float()
    return global_features


def make_batch(data: Union[HeteroData, Data]):
    """
    adds the .batch-argument with zeros
    Args:
        data:

    Returns:

    """
    if type(data) in [torch_geometric.data.HeteroData, torch_geometric.data.Data]:
        return Batch.from_data_list([data])

    return data


# todo from original heterogeneous architecture
# def get_global_features(graph_tensor: Union[Data, HeteroData]) -> torch.Tensor:
#     """
#     Unpacks the global features of Data or HomoData
#     Args:
#         graph_tensor: The graph to unpack global features from
#     Returns:
#         Empty graph if no global features could be found, otherwise the global features
#     """
#     global_features = graph_tensor.u if hasattr(graph_tensor, "u") else torch.graph([])
#     batch = graph_tensor.batch if hasattr(graph_tensor, "batch") else None
#
#     if batch is None:  # only one graph
#         global_features = global_features[None, :]
#     else:  # Reshape global features to fit the graph
#         assert hasattr(graph_tensor, "ptr"), "Need pointer for graph ids when using batch and global features"
#         num_graphs = len(graph_tensor.ptr) - 1
#         if len(global_features > 0):
#             # Reshape global features such that each graph can easily be assigned its own global feature set
#             global_features = global_features.reshape((-1, int(len(global_features) / num_graphs)))
#         else:  # No global features. make a bigger placeholder
#             global_features = global_features[None, :][[0] * num_graphs]
#     global_features = global_features.float()
#
#     return global_features


def get_create_copy(create_graph_copy: bool):
    """
    Returns a function that creates a copy of the graph.
    Args:
        create_graph_copy: Whether to create a copy of the graph or not
    Returns: A function that creates a copy of the graph, or an empty function if create_graph_copy is False
    """
    if create_graph_copy:
        return lambda x: copy.deepcopy(x)
    else:
        return lambda x: x


def count_in_node_features(
        in_edge_features: Dict[Tuple[str, str, str], int],
        in_node_features: Dict[str, int],
        latent_dimension: int,
        outer_aggregation: str,
        n_scatter_ops) -> Tuple[Dict[str, int], Dict[str, int]]:
    """
    Counts the number of features per node type and number of edge types.
    Args:
        in_edge_features:
            Dict of edge types and number of features per edge type.
        in_node_features:
            Dict of node types and number of features per node type.
        latent_dimension:
            Dimension of the latent space.
        outer_aggregation:
            Outer aggregation type. (str: Keys.CONCAT_AGGR or Keys.AGGR_AGGR)
        n_scatter_ops:
            number of scatter reductions. e.g. 2 if we have "mean" and "std".
    Returns:
        Tuple of in_node_features and num_edge_types, which are dictionaries per node.

    """
    destination_list = [dest_name for (src_name, relation_name, dest_name) in in_edge_features.keys()]
    destination_counts = Counter(destination_list)
    num_edge_types = {node_name: destination_counts.get(node_name, 0)
                      for node_name in in_node_features.keys()}
    if outer_aggregation == CONCAT_AGGR:  # do not aggregate types, i.e., use full edge features
        in_node_features = {node_name: latent_dimension * (num_edge_types.get(node_name) * n_scatter_ops + 1)
                            for node_name in in_node_features.keys()}
    elif outer_aggregation == AGGR_AGGR:  # aggregate over all types
        in_node_features = {node_name: latent_dimension * n_scatter_ops * n_scatter_ops + latent_dimension
                            for node_name in in_node_features.keys()}
    else:
        raise ValueError(f"Unknown outer aggregation '{outer_aggregation}'")
    return in_node_features, num_edge_types
