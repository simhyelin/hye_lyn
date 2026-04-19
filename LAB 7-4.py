import math
for i in range(2, 11):
    res = math.pow(4, i)
    print("4**{:2d} = {:10.1f}".format(i, res))

import math
for degree in range(0, 181, 10):
    radian = math.radians(degree)
    print("{:3d} degree = {:.3f} radian".format(degree, radian))

import math
for degree in range(0, 181, 10):
    radian = math.radians(degree)
    sin_val = math.sin(radian)
    print("sin({:3d}) = {:.2f}".format(degree, sin_val))
