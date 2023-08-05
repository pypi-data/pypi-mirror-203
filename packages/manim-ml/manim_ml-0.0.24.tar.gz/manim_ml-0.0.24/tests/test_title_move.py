from manim import *
from PIL import Image
from manim_ml.neural_network.layers.feed_forward import FeedForwardLayer
from manim_ml.neural_network.neural_network import NeuralNetwork
import numpy as np


class NeuralNetworkScene(Scene):
    """Test Scene for the Neural Network"""

    def construct(self):
        # Make the neural network
        nn = NeuralNetwork([
                FeedForwardLayer(4),
                FeedForwardLayer(5),
                FeedForwardLayer(5),
                FeedForwardLayer(2),
            ],
            layer_spacing=0.5,
            title="Test title"
        )
        #make it bigger
        nn.scale(3)
        # Center the neural network
        nn.move_to(ORIGIN)
        # Add the neural network to the scene with a fade in animation
        self.play(FadeIn(nn))
        # Make a forward pass animation
        forward_pass = nn.make_forward_pass_animation(run_time=2)
        # Play animation
        self.play(forward_pass)
