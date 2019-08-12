import pickle
my_list = ['a', 'b', 'c']

## Save pickle
with open("data.pickle", "wb") as fw:
	pickle.dump(my_list,fw)



## Load pickle
with open("data.pickle", "rb") as fr:
    data = pickle.load(fr)

print(data)
