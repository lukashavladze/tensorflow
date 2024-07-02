import tensorflow as tf
import numpy as np

# creating tensors
string = tf.Variable("this is a string", tf.string)
number = tf.Variable(324, tf.int16)
floating = tf.Variable(3.567, tf.float64)

# ranks of tensors

rank1_tensor = tf.Variable(["test", "Ok", "luka"], tf.string)
rank2_tensor = tf.Variable([["test", "ok"], ["test", "yes"]], tf.string)

print(tf.rank(rank1_tensor))

# shape
# gveubneba ramdeni listia da ramdeni elementia tito listshi, mgoni listshi tanabrad unda iyos elementebis raodenoba
print(rank2_tensor.shape)
print(rank1_tensor.shape)

# chaging shape
tensor1 = tf.ones([1,2,3])
tensor2 = tf.reshape(tensor1, [2,3,1])
tensor3 = tf.reshape(tensor2, [3, -1])

print(tensor1)
print(tensor2)
print(tensor3)

# types of tensors
#variable
#constant
#placeholder
#SparseTensor

# evaluating Tensors
#with tf.Session() as sess:
 #   tensor1.eval()
