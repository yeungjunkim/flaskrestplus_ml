
import keras
import numpy
import pickle

def keras_predict(arg1, arg2) :
	x = numpy.array([0, 1, 2, 3, 4]) 
	y = x * 2 + 1

	#model = keras.models.Sequential()
	#model.add(keras.layers.Dense(1,input_shape=(1,)))
	#model.compile('SGD', 'mse')

	# save the model to disk
	filename = 'keras_model_1.sav'

	#pickle.dump(model, open(filename, 'wb'))

	#print(model.predict(x))

	# load the model from disk
	loaded_model = pickle.load(open(filename, 'rb'))
	result = loaded_model.predict(x)
	print(arg1)
	print(arg2)
	print(result)
	#result1 = result + arg1 + arg2
	#print(result1)
	return result


if __name__ == "__main__" : 
	keras_predict(1, 2)
