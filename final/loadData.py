import numpy as np
from keras.utils import np_utils

class loadData:
	"""
	Class for loading in the testing, 
	training, and validation datasets.

	Functions:
		_loadTest()
		_loadTrain()
		_loadValid()
	"""


	def __load(self, dir, abs=False):
		features = np.load(dir + "X_data.npy")
		labels = np.load(dir + "label.npy")
		classes = np_utils.to_categorical(labels)

		chi = np.load(dir + "chi.npy")
		depth = np.load(dir + "depth.npy")
		flux = np.load(dir + "flux.npy")
		sig = np.load(dir + "sig.npy")		

		if abs:
			features = np.abs(features[:,:,0] + 1j * features[:,:,1])

		return(features, classes, labels, chi, depth, flux, sig) 


	def _loadTrain(self, dir, abs=False):
		"""
		Function for loading the features and
		labels associated with the training
		dataset.

		To call:
			_loadTrain(dir)

		Parameters:
			dir	data directory
		"""
		if dir[-1] != '/':
			dir += '/'

		self.trainX_, self.trainY_, self.trainLabel_, self.trainChi_, self.trainDepth_, self.trainFlux_, self.trainSig_ = self.__load(dir, abs)


	def _loadTest(self, dir, abs=False):
		"""
		Function for loading the features and
		labels associated with the testing
		dataset.

		To call:
			_loadTest(dir)

		Parameters:
			dir	data directory
		"""
		if dir[-1] != '/':
			dir += '/'

		self.testX_, self.testY_, self.testLabel_, self.testChi_, self.testDepth_, self.testFlux_, self.testSig_ = self.__load(dir, abs)


	def _loadValid(self, dir, abs=False):
		"""
		Function for loading the features and
		labels associated with the validation
		dataset.

		To call:
			_loadValid(dir)

		Parameters:
			dir	data directory

		Postcondition:
		"""
		if dir[-1] != '/':
			dir += '/'

		self.validX_, self.validY_, self.validLabel_, self.validChi_, self.validDepth_, self.validFlux_, self.validSig_ = self.__load(dir, abs)

