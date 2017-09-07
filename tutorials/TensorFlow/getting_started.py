# Turn off TensorFlow library compilation warnings
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
######################################

import tensorflow as tf

'''
Simple Linear Regression Model example for TensorFlow
'''

# Model parameters
W = tf.Variable([.3], dtype=tf.float32)
b = tf.Variable([-.3], dtype=tf.float32)

# Model input and output
x = tf.placeholder(tf.float32)
linear_model = W * x + b
y = tf.placeholder(tf.float32)

# Loss
loss = tf.reduce_sum(tf.square(linear_model - y)) # sum of the squares

# Optimizer
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

# Training data
x_train = [1, 2, 3, 4]
y_train = [0, -1, -2, -3]

# Training loop
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init) # reset values to wrong
print('Initial [W, b] tensor prior to training: ', sess.run([W, b]))
for i in range(1000):
  sess.run(train, {x: x_train, y: y_train})

# Evaluate training accuracy
curr_W, curr_b, curr_loss = sess.run([W, b, loss], {x: x_train, y: y_train})
print("Trained W: %s, Trained b: %s, resulting in loss: %s"%(curr_W, curr_b, curr_loss))