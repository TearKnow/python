import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

x_data = np.linspace(-1, 1, 200)[:, np.newaxis]
prediction_value = np.linspace(-0.1, 0.1, 200)[:, np.newaxis]

plt.figure()
plt.plot(x_data, prediction_value, 'r-', lw = 5)#x���꣬y����
plt.show()
