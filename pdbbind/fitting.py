import tensorflow as tf
from keras.layers import Input, Dense, Lambda
import matplotlib.pyplot as plt
import numpy as np


def best_fit_line(x,y):
    x_tensor = tf.placeholder(shape=(None,), dtype=tf.float32)
    y_tensor = tf.placeholder(shape=(None,), dtype=tf.float32)
    x_tensor_exp_dim = tf.expand_dims(x_tensor, axis=-1)
    print(x_tensor_exp_dim)
    output_tensor = Dense(1, activation='linear')(x_tensor_exp_dim)
    output_tensor = tf.squeeze(output_tensor)
    loss = tf.reduce_mean(tf.abs(output_tensor-y_tensor))
    train_ops = tf.train.AdamOptimizer(0.1).minimize(loss)
    trainable_weight_list = tf.trainable_variables()

    sess = tf.Session()
    init_step = tf.global_variables_initializer()
    sess.run(init_step)
    loss_before = 1000.0
    while True:
        loss_value, _ = sess.run([loss, train_ops], feed_dict={x_tensor:x, y_tensor:y})
        diff = np.abs(loss_value-loss_before)
        print(diff)
        if diff < 0.000001:
            break
        loss_before = loss_value
    return sess.run(output_tensor, feed_dict={x_tensor:x})


if __name__ == "__main__":
    with open('./tani_simi.txt', 'r') as f:
        cont = f.readlines()
    indexoft = map(lambda x:x*3, range(24))
    for i in indexoft[14:]:

        x, y = [], []
        try:
            x.extend(map(float, cont[i+1].strip().split(',')[1:]))
            y.extend(map(float, cont[i+2].strip().split(',')[1:]))
            d = {}
            for ii in zip(x, y):
                d[ii[0]] = ii[1]
            x, y = [], []
            for key in sorted(d.keys()):
                x.append(key)
                y.append(d[key])
            y_predict = best_fit_line(x,y)
            #line_x = [0.0, 1.0]
            #line_y = [line_x[0]*w[0]+w[1], line_x[1]*w[0]+w[1]]
            plt.scatter(x,y)
            #    print line_x
            #    print line_y
            plt.plot(x, np.squeeze(y_predict))
            plt.xlabel('Similarity_rdkit')
            plt.ylabel('TanimotoCombo_ROCS')
            plt.title('{0}, r = {1}'.format(cont[i][6:].strip(), np.corrcoef(x,y)[0][1]))
            plt.show()
        except ValueError:
            pass


'''
#Overall
if __name__=="__main__":
    with open('./tani_simi.txt', 'r') as f:
        cont = f.readlines()
    indexoft = map(lambda x:x*3, range(24))
    x, y = [], []
    for i in cont[1::3]:
        x.extend(map(float, i.strip().split(',')[1:]))
    for i in cont[2::3]:
        y.extend(map(float, i.strip().split(',')[1:]))
    w = best_fit_line(x,y)
    line_x = [0.0, 1.0]
    line_y = [line_x[0]*w[0]+w[1], line_x[1]*w[0]+w[1]]
    plt.scatter(x,y)
#    print line_x
#    print line_y
    plt.plot(line_x, np.squeeze(line_y))
    plt.xlabel('Similarity_rdkit')
    plt.ylabel('TanimotoCombo_ROCS')
    plt.title('Overall, r = {}'.format(np.corrcoef(x,y)[0][1]))
    plt.show()
'''