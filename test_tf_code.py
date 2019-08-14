import tensorflow as tf

a = tf.constant(2.0)
b = tf.constant(3.0)

c = tf.add(a,b)


with tf.Session() as sess:
  print(sess.run(c))
