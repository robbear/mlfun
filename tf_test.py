import os
# Turn off TensorFlow library compilation warnings
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

import tensorflow as tf

hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print('TensorFlow version: ', tf.__version__)
print(sess.run(hello))