#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tensorflow as tf
import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)