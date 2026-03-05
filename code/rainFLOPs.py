from tensorflow.python import pywrap_tensorflow
import os
import numpy as np
from util import *
from functools import reduce
from operator import mul
from models import *


def count_parameters():
    total_parameters = 0
    for variable in tf.trainable_variables():
        # shape is an array of tf.Dimension
        shape = variable.get_shape()
        variable_parameters = 1
        for dim in shape:
            variable_parameters *= dim.value
        total_parameters += variable_parameters
    print('Parameters:', total_parameters)
    return total_parameters


def count_flops(graph):
    flops = tf.profiler.profile(graph, options=tf.profiler.ProfileOptionBuilder.float_operation())
    print('FLOPs: {}'.format(flops.total_float_ops))


def get_num_params():
    num_params = 0
    for variable in tf.trainable_variables():
        shape = variable.get_shape()
        num_params += reduce(mul, [dim.value for dim in shape], 1)
    print('Parameters:', num_params)


sess = tf.Session()
training = tf.placeholder_with_default(False, shape=(), name='training')
input_decom = tf.placeholder(tf.float32, [1, 400, 600, 3], name='input_decom')
input_low_r = tf.placeholder(tf.float32, [1, 400, 600, 3], name='input_low_r')
input_low_i = tf.placeholder(tf.float32, [1, 400, 600, 1], name='input_low_i')
input_low_i_ratio = tf.placeholder(tf.float32, [1, 400, 600, 1], name='input_low_i_ratio')
[R_decom, I_decom] = ID_Net(input_decom)
output_r = RA_Net(input_low_r, input_low_i)
output_i = IA_Net(input_low_i, input_low_i_ratio)


count_flops(tf.get_default_graph())
count_parameters()

get_num_params()
