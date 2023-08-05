import manim_ml
from manim_ml.neural_network.neural_network import NeuralNetwork
from manim_ml.neural_network.layers.feed_forward import FeedForwardLayer

class FeedForwardNeuralNetwork(NeuralNetwork):
    """NeuralNetwork with just feed forward layers"""

    def __init__(
        self, 
        layer_node_count, 
        node_radius=0.08, 
        node_color=manim_ml.config.color_scheme.primary_color, 
        **kwargs
    ):
        # construct layer
        layers = []
        for num_nodes in layer_node_count:
            layer = FeedForwardLayer(
                num_nodes, node_color=node_color, node_radius=node_radius
            )
            layers.append(layer)
        # call super class
        super().__init__(layers, **kwargs)
