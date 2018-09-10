#矩阵的乘法
import tensorflow as tf

m1 = tf.constant([[3, 4]])
m2 = tf.constant([[2], [3]])

product = tf.matmul(m1, m2)

sess = tf.Session()
result = sess.run(product)

print(result)
sess.close()

