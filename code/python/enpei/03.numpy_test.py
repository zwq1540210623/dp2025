import numpy as np

#todo

list_a = [1, 2, 3, 4]
print(type(list_a))

my_arr = np.array(list_a)
print(type(my_arr))

print(np.arange(1, 20, 2))
print(np.ones(shape=(3, 4)))
print(np.zeros(shape=(4, 5)))

print(np.random.randint(0, 100, 10))
print(my_arr.max())