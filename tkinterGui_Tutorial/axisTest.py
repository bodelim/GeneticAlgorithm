import numpy as np
import pandas as pd
import random
import ga

num_weights = 6

sol_per_pop = 8
# Defining the population size.

new_population =[]
def init_pop(num_weights, sol_per_pop):
    for j in range(sol_per_pop):
        #sol_per_pop개 행 / num_weights개 열의 형태로 만들어줌
        chromosome = []
        for i in range(num_weights): # chromosome에 gene난수를 6개 담아줌
            chromosome.append(np.random.randint(10))
        new_population.append(chromosome)
    return pd.DataFrame(new_population)

print(init_pop(num_weights, sol_per_pop))

pop_size = (sol_per_pop,num_weights) # The population will have sol_per_pop chromosome where each chromosome has num_weights genes.

#Creating the initial population.

new2_population = np.random.randint(10, size=pop_size)
new2_population = new_population
print(new2_population)
