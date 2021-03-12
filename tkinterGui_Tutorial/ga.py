import numpy
import pandas as pd
import random


# 방정식의 입력입니다.
equation_inputs = [4,-2,3.5,5,-11,-4.7]
 # 최적화하려는 가중치의 수입니다.
num_weights = 6

sol_per_pop = 8
# Defining the population size.

pop_size = (sol_per_pop,num_weights)


num_generations = 5
num_parents_mating = 4

def cal_pop_fitness(equation_inputs, pop):
     # 현재 모집단의 각 솔루션의 적합성 값 계산.
     # 적합성 함수는 각 입력과 해당 가중치 사이의 제품 합계를 계산합니다.
     fitness = numpy.sum(pop*equation_inputs, axis=1)
     return fitness

def select_mating_pool(pop, fitness, num_parents):

    # 다음 세대의 자손을 낳기 위한 부모로서 현 세대 최고의 인간을 선발한다.

    parents = numpy.empty((num_parents, pop.shape[1]))
    #위 함수는 현재 모집단을 순환하면서 가장 높은 적합성 값의 인덱스를 얻는다

    for parent_num in range(num_parents):

        max_fitness_idx = numpy.where(fitness == numpy.max(fitness))

        max_fitness_idx = max_fitness_idx[0][0]

        parents[parent_num, :] = pop[max_fitness_idx, :]

        fitness[max_fitness_idx] = -99999999999

    return parents

def crossover(parents, offspring_size):
     offspring = numpy.empty(offspring_size)
     # 두 부모 사이에서 교차하는 지점. 보통, 그것은 중앙에 있습니다.
     crossover_point = numpy.uint8(offspring_size[1]/2)
 
     for k in range(offspring_size[0]):
         # 
         parent1_idx = k%parents.shape[0]
         # 교배를 할 첫 번째 부모의 색인입니다.
         parent2_idx = (k+1)%parents.shape[0]
         # 이 새로운 자손은 첫 번째 부모로부터 유전자를 물려받을 것입니다.
         offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
         # 이 새로운 자손은 두 번째 부모로부터 유전자를 물려받을 것입니다.
         offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]
     return offspring

def mutation(offspring_crossover):

    # 돌연변이는 각 자손의 단일 유전자를 무작위로 변화시킵니다.

    for idx in range(offspring_crossover.shape[0]):

        # 유전자에 추가할 랜덤 값입니다.

        random_value = numpy.random.uniform(-1.0, 1.0, 1)

        offspring_crossover[idx, 4] = offspring_crossover[idx, 4] + random_value

    return offspring_crossover