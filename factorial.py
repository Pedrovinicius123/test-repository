import math
import matplotlib.pyplot as plt

def calc_factorial_range(theta:int=20):
    max_k_int = theta
    maximum, i_max = 0, 0
    items = []

    for i in range(max_k_int):
        value = int(math.factorial(theta))/int(math.factorial(i) * math.factorial(theta-i))
        items.append((i, value))

        if value >  maximum:
            maximum = value
            i_max = i

    plt.scatter(maximumlabel="Complexidade dado o número de contradições")
