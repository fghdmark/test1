import numpy as np
sales = np.array([

    [100, 120, 90],

    [110, 130, 95],

    [105, 125, 100]

])

print("每天銷售:", sales.sum(axis=1))

print("每商品銷售:", sales.sum(axis=0))

print("總銷售:", sales.sum())