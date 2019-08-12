
import keras
import numpy
import pickle

x = numpy.array([0, 1, 2, 3, 4]) 
y = x * 2 + 1

model = keras.models.Sequential()
model.add(keras.layers.Dense(1,input_shape=(1,)))
model.compile('SGD', 'mse')



model.fit(x[:2], y[:2], epochs=1000, verbose=0)

# save the model to disk
filename = 'keras_model_1.sav'
pickle.dump(model, open(filename, 'wb'))

print(model.predict(x))



# load the model from disk
#loaded_model = pickle.load(open(filename, 'rb'))
#result = loaded_model.predict(x)
#