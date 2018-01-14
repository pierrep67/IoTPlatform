from numpy import genfromtxt
import numpy
my_features = genfromtxt('features.csv', delimiter=',')
my_labels = genfromtxt('labels.csv', delimiter=',')
print("my_labels ",my_labels,"\n")
print("my_features ",my_features,"\n")

numpy.savez('data.npz', my_features=my_features, my_labels=my_labels)
print('\n\n\n')
my_data = numpy.load('data.npz') # loads your saved array into variable a
print(my_data['my_features'])
print(my_data['my_labels'])




