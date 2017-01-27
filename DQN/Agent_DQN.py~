import numpy as np
import tensorflow as tf
import cv2

class DQN:
	def __init__(self,generic_params,name):

		self.learner_params = {
			'steps_per_epoch': 200000,
			'num_epochs': 250,
			'eval_freq':100000,
			'steps_per_eval':10000,
			'copy_freq' : 10000,
			'disp_freq':20000,
			'save_interval':20000,
			'batch': 32,
			'num_act': 0,
			'learning_interval': 1,
			'eps': 1.0,
			'eps_step':1000000,
			'eps_min' : 0.1,
			'eps_eval' : 0.05,
			'discount': 0.99,
			'lr': 0.00025,
			'rms_decay':0.95,
			'rms_eps':0.01,
			'clip_delta' : 1,
			'train_start':50000,
			'batch_accumulator':'sum'
		}

		self.network_type = 'DeepQ'
		self.params = params
		self.network_name = name
		self.x = tf.placeholder('float32', [None,84,84,4], name=self.network_name + '_x')
		self.q_t = tf.placeholder('float32', [None], name=self.network_name + '_q_t')
		self.actions = tf.placeholder('float32', [None, params['num_act']], name=self.network_name + '_actions')
		self.rewards = tf.placeholder("float32", [None],name=self.network_name + '_rewards')
		self.terminals = tf.placeholder("float32", [None],name=self.network_name + '_terminals')

		#conv1
		layer_name = 'conv1' ; size = 8 ; channels = 4 ; filters = 32 ; stride = 4
		self.w1 = tf.Variable(tf.random_normal([size,size,channels,filters], stddev=0.01),name=self.network_name + '_'+layer_name+'_weights')
		self.b1 = tf.Variable(tf.constant(0.1, shape=[filters]),name=self.network_name + '_'+layer_name+'_biases')
		self.c1 = tf.nn.conv2d(self.x, self.w1, strides=[1, stride, stride, 1], padding='VALID',name=self.network_name + '_'+layer_name+'_convs')
		self.o1 = tf.nn.relu(tf.add(self.c1,self.b1),name=self.network_name + '_'+layer_name+'_activations')


		#conv2
		layer_name = 'conv2' ; size = 4 ; channels = 32 ; filters = 64 ; stride = 2
		self.w2 = tf.Variable(tf.random_normal([size,size,channels,filters], stddev=0.01),name=self.network_name + '_'+layer_name+'_weights')
		self.b2 = tf.Variable(tf.constant(0.1, shape=[filters]),name=self.network_name + '_'+layer_name+'_biases')
		self.c2 = tf.nn.conv2d(self.o1, self.w2, strides=[1, stride, stride, 1], padding='VALID',name=self.network_name + '_'+layer_name+'_convs')
		self.o2 = tf.nn.relu(tf.add(self.c2,self.b2),name=self.network_name + '_'+layer_name+'_activations')


		#conv3
		layer_name = 'conv3' ; size = 3 ; channels = 64 ; filters = 64 ; stride = 1
		self.w3 = tf.Variable(tf.random_normal([size,size,channels,filters], stddev=0.01),name=self.network_name + '_'+layer_name+'_weights')
		self.b3 = tf.Variable(tf.constant(0.1, shape=[filters]),name=self.network_name + '_'+layer_name+'_biases')
		self.c3 = tf.nn.conv2d(self.o2, self.w3, strides=[1, stride, stride, 1], padding='VALID',name=self.network_name + '_'+layer_name+'_convs')
		self.o3 = tf.nn.relu(tf.add(self.c3,self.b3),name=self.network_name + '_'+layer_name+'_activations')


		#flat
		o3_shape = self.o3.get_shape().as_list()

		#fc3
		layer_name = 'fc4' ; hiddens = 512 ; dim = o3_shape[1]*o3_shape[2]*o3_shape[3]
		self.o3_flat = tf.reshape(self.o3, [-1,dim],name=self.network_name + '_'+layer_name+'_input_flat')
		self.w4 = tf.Variable(tf.random_normal([dim,hiddens], stddev=0.01),name=self.network_name + '_'+layer_name+'_weights')
		self.b4 = tf.Variable(tf.constant(0.1, shape=[hiddens]),name=self.network_name + '_'+layer_name+'_biases')
		self.ip4 = tf.add(tf.matmul(self.o3_flat,self.w4),self.b4,name=self.network_name + '_'+layer_name+'_ips')
		self.o4 = tf.nn.relu(self.ip4,name=self.network_name + '_'+layer_name+'_activations')

		#fc4
		layer_name = 'fc5' ; hiddens = params['num_act'] ; dim = 512
		self.w5 = tf.Variable(tf.random_normal([dim,hiddens], stddev=0.01),name=self.network_name + '_'+layer_name+'_weights')
		self.b5 = tf.Variable(tf.constant(0.1, shape=[hiddens]),name=self.network_name + '_'+layer_name+'_biases')
		self.y = tf.add(tf.matmul(self.o4,self.w5),self.b5,name=self.network_name + '_'+layer_name+'_outputs')

		#Q,Cost,Optimizer
		self.discount = tf.constant(self.params['discount'])
		self.yj = tf.add(self.rewards, tf.mul(1.0-self.terminals, tf.mul(self.discount, self.q_t)))
		self.Qxa = tf.mul(self.y,self.actions)
		self.Q_pred = tf.reduce_max(self.Qxa, reduction_indices=1)

		self.diff = tf.sub(self.yj, self.Q_pred)
		if self.params['clip_delta'] > 0 :
			self.quadratic_part = tf.minimum(tf.abs(self.diff), tf.constant(self.params['clip_delta']))
			self.linear_part = tf.sub(tf.abs(self.diff),self.quadratic_part)
			self.diff_square = 0.5 * tf.pow(self.quadratic_part,2) + self.params['clip_delta']*self.linear_part


		else:
			self.diff_square = tf.mul(tf.constant(0.5),tf.pow(self.diff, 2))

		if self.params['batch_accumulator'] == 'sum':
			self.cost = tf.reduce_sum(self.diff_square)
		else:
			self.cost = tf.reduce_mean(self.diff_square)

		self.global_step = tf.Variable(0, name='global_step', trainable=False)
		self.rmsprop = tf.train.RMSPropOptimizer(self.params['lr'],self.params['rms_decay'],0.0,self.params['rms_eps']).minimize(self.cost,global_step=self.global_step)
