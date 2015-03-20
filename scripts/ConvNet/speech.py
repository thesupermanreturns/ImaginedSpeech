import numpy as np

from layers import *
from fast_layers import *
from layer_utils import *

from classifiers.convnet import *
from MultiLevelConvNet import MultiLevelConvNet

X_train = 
X_val = 

component_dim = (1, 64, 112)

fn1 = speech_convnet
y_train1 = 
y_val1 = 
num_components_per_img1 = 1
input_component_dim1 = (component_dim[0], component_dim[1], component_dim[2] * num_components_per_img1)
model1 = init_speech_convnet(input_shape = input_component_dim1, 
							num_classes = 10, filter_size = 3, num_filters = (32, 128, 256), weight_scale = 1e-4)
output_component_dim1 = fn1(X[0], model1, extract_features = True)[0].shape
stride1 = input_component_dim1[2]

fn2 = speech_convnet
y_train2 = 
y_val2 = 
num_components_per_img2 = 5
input_component_dim2 = (output_component_dim1[0], output_component_dim1[1], output_component_dim1[2] * num_components_per_img2)
model2 = init_speech_convnet(input_shape = input_component_dim2, 
							num_classes = 2, filter_size = 3, num_filters = (32, 128, 256), weight_scale = 1e-4)
output_component_dim2 = fn2(X[0], model2, extract_features = True)[0].shape
stride2 = input_component_dim2[2]

fn3 = speech_convnet
y_train3 = 
y_val3 = 
num_components_per_img3 = 1
input_component_dim3 = (output_component_dim2[0], output_component_dim2[1], output_component_dim2[2] * num_components_per_img2)
model3 = init_speech_convnet(input_shape = input_component_dim3, 
							num_classes = 2, filter_size = 3, num_filters = (32, 128, 256), weight_scale = 1e-4)
output_component_dim2 = fn3(X[0], model3, extract_features = True)[0].shape
stride3 = input_component_dim3[2]

##############################################################################################################################################

net = MultiLevelConvNet(X_train, X_val, 3)
net.set_level_parameters(0, fn1, model1, y_train1, y_val1, input_component_dim1, num_components1, stride1)
net.set_level_parameters(1, fn2, model2, y_train2, y_val2, input_component_dim2, num_components2, stride2)
net.set_level_parameters(2, fn3, model3, y_train3, y_val3, input_component_dim3, num_components3, stride3)
net.set_level_learning_parameters(0, reg = 0.0000, learning_rate = 0.0015, batch_size = 250, num_epochs = 5, 
										learning_rate_decay = 0.999, update = 'rmsprop', verbose=True, dropout=1.0)
net.set_level_learning_parameters(1, reg = 0.0000, learning_rate = 0.0015, batch_size = 250, num_epochs = 5, 
										learning_rate_decay = 0.999, update = 'rmsprop', verbose=True, dropout=1.0)
net.set_level_learning_parameters(2, reg = 0.0000, learning_rate = 0.0015, batch_size = 250, num_epochs = 5, 
										learning_rate_decay = 0.999, update = 'rmsprop', verbose=True, dropout=1.0)

if net.check_level_continuity():
	return "IT WORKED"
else:
	return "It didn't work"