from Part1 import *

a = np.array([[10,50,30],[60,20,40]])
(i, j) = unravel_index(a.argmax(), a.shape)
print(np.sum(a))
