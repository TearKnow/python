#矩阵的乘法
import tensorflow as tf
import numpy as np

print("\n")
print('--------- constant --------')
m1 = tf.constant([[3, 4]])
m2 = tf.constant([[2], [3]])
product = tf.matmul(m1, m2)
sess = tf.Session()
result = sess.run(product)
print(result)
sess.close()
print("\n")



print('--------- variable --------')
#变量
x = tf.Variable([1, 2])
a = tf.constant([3, 4])
#一个减法的op（节点）
sub = tf.subtract(x, a)
add = tf.add(x, sub)

#变量初始化
init = tf.global_variables_initializer()
with tf.Session() as sess:
	sess.run(init)
	print(sess.run(sub))
	print(sess.run(add))
print("\n")
	

#创建一个变量初始化为0
print('--------- counter --------')
state = tf.Variable(0, name='counter')
new_value = tf.add(state, 1)
#赋值
update = tf.assign(state, new_value)
init = tf.global_variables_initializer()
with tf.Session() as sess:
	sess.run(init)
	print(sess.run(state))
	for i in range(5):
		print(sess.run(update))
print("\n")



#fetch
print('--------- fetch --------')
input1 = tf.constant(3.0)
input2 = tf.constant(2.0)
input3 = tf.constant(5.0)

add = tf.add(input2, input3)
mul = tf.multiply(input1, add)

with tf.Session() as sess:
#一次多个op
	result = sess.run([mul, add])
	print(result)
print("\n")


#feed
#创建占位符
print('--------- feed --------')
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
output = tf.multiply(input1, input2)

with tf.Session() as sess:
#字典的形式传入
	print(sess.run(output, feed_dict={input1:[7.0], input2:[2.0]}))
print("\n")


print('--------- simple demo, y = 0.1x+0.2 --------')
#使用numpy生成100个随机点
x_data = np.random.rand(100)
y_data = x_data * 0.1 + 0.2

#构造一个线性模型
b = tf.Variable(0.)
k = tf.Variable(0.)
y = k * x_data + b


#二次代价函数(损失函数)
loss = tf.reduce_mean(tf.square(y_data - y))#这里不确定的就是k和b的值###########
#定义一个梯度下降法来训练的优化器
optimizer = tf.train.GradientDescentOptimizer(0.2)
#最小化代价函数
train = optimizer.minimize(loss)

#初始化变量
init = tf.global_variables_initializer()
with tf.Session() as sess:
	sess.run(init)
	for step in range(201):
		sess.run(train)
		if step % 20 == 0:
			print(step, sess.run([k, b]))

print("\n")




