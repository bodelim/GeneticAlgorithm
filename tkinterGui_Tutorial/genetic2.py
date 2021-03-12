import numpy
import pandas as pd
import random
import ga

# 방정식의 입력입니다.
equation_inputs = [4,-2,3.5,5,-11,-4.7]
 # 최적화하려는 가중치의 수입니다.
num_weights = 6

sol_per_pop = 8
# Defining the population size.

pop_size = (sol_per_pop,num_weights)

new_population =[]

# Defining the population size.

pop_size = (sol_per_pop,num_weights) # The population will have sol_per_pop chromosome where each chromosome has num_weights genes.

#Creating the initial population.

new_population = numpy.random.uniform(low=-4.0, high=4.0, size=pop_size)

#def init_pop(num_weights, sol_per_pop):
#    for j in range(sol_per_pop):
#        #sol_per_pop개 행 / num_weights개 열의 형태로 만들어줌
#        chromosome = []
#        for i in range(num_weights): # chromosome에 gene난수를 6개 담아줌
#            chromosome.append(numpy.random.uniform(low=-4.0, high=4.0))
#        new_population.append(chromosome)
#    return pd.DataFrame(new_population)
#
#print(init_pop(num_weights, sol_per_pop))


num_generations = 3
num_parents_mating = 4
for generation in range(num_generations):
     # 모집단 내 각 염색체의 적합성을 측정합니다.
     fitness = ga.cal_pop_fitness(equation_inputs, new_population)

    # 교배에 가장 적합한 모집단을 선택합니다.
     parents = ga.select_mating_pool(new_population, fitness, 
                                       num_parents_mating)
 
     # 크로스오버를 사용하여 다음 세대를 생성하는 중입니다.
     offspring_crossover = ga.crossover(parents,
                                        offspring_size=(pop_size[0]-parents.shape[0], num_weights))
 
     # 돌연변이를 사용하여 오프스프링에 일부 변형 추가.
     offspring_mutation = ga.mutation(offspring_crossover)

    # 부모와 자손을 기반으로 새로운 인구 창출.
    # 이전 최고의 솔루션(부모)을 새로운 모집단에서 유지.
     new_population[0:parents.shape[0], :] = parents
     new_population[parents.shape[0]:, :] = offspring_mutation
     
     print("Best result : ", numpy.max(numpy.sum(new_population*equation_inputs, axis=1)))

# Getting the best solution after iterating finishing all generations.
#At first, the fitness is calculated for each solution in the final generation.
fitness = ga.cal_pop_fitness(equation_inputs, new_population)
# Then return the index of that solution corresponding to the best fitness.
best_match_idx = numpy.where(fitness == numpy.max(fitness))

print("Best solution : ", new_population[best_match_idx, :])
print("Best solution fitness : ", fitness[best_match_idx])