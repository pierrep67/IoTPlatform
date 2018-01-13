import tensorflow as tf
import numpy as np
import sys




def weight_variable(shape):
  initial = tf.truncated_normal(shape, stddev=0.1)
  return tf.Variable(initial)

def bias_variable(shape):
  initial = tf.constant(0.1, shape=shape)
  return tf.Variable(initial)





def conv2d(x, W):
  return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

def max_pool_2x2(x):
  return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],
                        strides=[1, 2, 2, 1], padding='SAME')


def main():
  with np.load("data.npz") as data:
    features = data["my_features"]
    labels = data["my_labels"]

  print(labels)
  print(features)

  # Assume that each row of `features` corresponds to the same row as `labels`.


  features_placeholder = tf.placeholder(features.dtype, features.shape)
  labels_placeholder = tf.placeholder(labels.dtype, labels.shape)

  dataset = tf.data.Dataset.from_tensor_slices((features_placeholder, labels_placeholder))

  dataset = dataset.repeat() 


  iterator = dataset.make_initializable_iterator()

  print(labels)
  print(features)


  next_element = iterator.get_next()


  print("features.shape :",features.shape)
  print("labels.shape :",labels.shape)



  W_conv1 = weight_variable([5, 5, 1, 32])
  b_conv1 = bias_variable([32])


  x = tf.placeholder(tf.float32, [784])
  x_image = tf.reshape(x, [-1, 28, 28, 1])

  h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
  h_pool1 = max_pool_2x2(h_conv1)

  W_conv2 = weight_variable([5, 5, 32, 64])
  b_conv2 = bias_variable([64])
  
  h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
  h_pool2 = max_pool_2x2(h_conv2)


  
  W_fc1 = weight_variable([7 * 7 * 64, 1024])
  b_fc1 = bias_variable([1024])

  h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])
  h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)



  keep_prob = tf.placeholder(tf.float32)
  h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)




  W_fc2 = weight_variable([1024, 1])
  b_fc2 = bias_variable([1])
  
  y_conv = tf.matmul(h_fc1_drop, W_fc2) + b_fc2
  
  

  y_ = tf.placeholder(tf.float32)


  cost = tf.reduce_sum(tf.sqrt(tf.pow(y_conv-y_, 2)))  
  
  
  train_step = tf.train.AdamOptimizer(1e-4).minimize(cost)


  sess=tf.Session()

  sess.run(tf.global_variables_initializer())

  sess.run(iterator.initializer, feed_dict={features_placeholder: features,labels_placeholder: labels})
  
  # Add ops to save and restore all the variables.
  saver = tf.train.Saver(max_to_keep=2500)

  # 13 000 run/min
  for i in range(15000):
      batch_xs, batch_ys = sess.run(next_element)
      sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys, keep_prob: 1})



      if(i%300)==0:
          print("step=", i, "   cost :", sess.run(cost,feed_dict={x: batch_xs, y_: batch_ys, keep_prob: 1}))
          print("\n")
      

  # 13 000 run/min
  # 25,47 model/Gio
  for i in range(2000):
      batch_xs, batch_ys = sess.run(next_element)
      sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys, keep_prob: 1})



      if(i%100)==0:
          print("step=", i, "   cost :", sess.run(cost,feed_dict={x: batch_xs, y_: batch_ys, keep_prob: 1}))
          # Save the variables to disk.
          save_path = saver.save(sess, "/home/mike/Bureau/model.ckpt", global_step=i, write_meta_graph=False)






if __name__ == '__main__':

    main()






