
#@title Genetic Algorithm
import random

"""# TASK 1"""

#@title Fitness Calculator
def price_calculation(chromosome_set, history, capita):
  history_data = history
  # chromosome1, chromosome2, chromosome3, chromosome4 = chromosome_set
  # chromosome theke jinis gula nibo
  stop_loss = chromosome_set[0]
  take_profit = chromosome_set[1]
  trade_size = chromosome_set[2]
  capita = capita
  # capita ke update kora lagbe oita ekta var e rakhbo
  updated_capita = capita
  for i in history_data:
    # koto tuku taka trade korbo
    trade_money = updated_capita * (trade_size / 100)
    # print(trade_money)
    goccha = 0
    # amader i ki stop losss er theke beshi  na kom?
    if i < (stop_loss * -1):
      # tahole ami cap koira dibo loss
      goccha = trade_money * (- stop_loss / 100 )
      updated_capita = updated_capita + goccha
      # print("hit stop loss")
      # print("updated capita: ", updated_capita)

    # ebar dekhi je lav er ki hal !
    elif i > take_profit:
      goccha = trade_money * (take_profit / 100)
      updated_capita = updated_capita + goccha
      # print("hit take profit")
      # print("updated capita: ", updated_capita)

    else:
      goccha = trade_money * (i / 100)
      updated_capita = updated_capita + goccha
      # print("updated capita: ", updated_capita)

  fitness = updated_capita - capita
  # print("fitness: ", fitness)

  return fitness

#@title Parent Generation Process
def generate_parents():
  stop_loss = random.randint(1, 99)
  take_profit = random.randint(1, 99)
  trade_size = random.randint(1, 99)
  return [stop_loss, take_profit, trade_size]

def population(size = 4):
  initial_population_set = []
  for i in range(size):
    initial_population_set.append(generate_parents())
  return initial_population_set

#@title Select best 2 parents
def select_best_parents(population_set):
  fitnessOfParents = []
  historical_prediction = [-1.2, 3.4, -0.8, 2.1, -2.5, 1.7, -0.3, 5.8, -1.1, 3.5]

  for i in range(0, len(population_set)):
    # fitnessOfParents[i] = price_calculation(population_set[i], historical_prediction, 1000)
    fitnessOfParents.append([i, price_calculation(population_set[i], historical_prediction, 1000)])


  fitnessOfParents = sorted(fitnessOfParents, key=lambda x: x[1], reverse=True)

  # print(fitnessOfParents)
  selected_parents = []
  selected_parents.append(population_set[fitnessOfParents[0][0]])
  selected_parents.append(population_set[fitnessOfParents[1][0]])
  return selected_parents

#@title Crossover (1 point crossover)
def crossover(parent1, parent2):
    # Random crossover point
    crossover_point = random.randint(1, len(parent1) - 1)

    # Create offspring by combining parts of parent1 and parent2
    offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
    offspring2 = parent2[:crossover_point] + parent1[crossover_point:]

    return offspring1, offspring2

#@title Crossover (2 point crossover)
def two_point_crossover(parent1, parent2):
    point1, point2 = sorted(random.sample(range(len(parent1)), 2))
    offspring1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
    offspring2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]

    return offspring1, offspring2

#@title Mutate
def mutation(offspring, mutation_rate=0.05):
    for i in range(len(offspring)):
        #5% mutation
        if random.random() < mutation_rate:
            offspring[i] = random.randint(1, 99)  # Random mutation
    return offspring

#@title Evolve
def evolve(population, generations=10):
    best_chromosome = None
    best_fitness = -float('inf')

    for generation in range(generations):
        print(f"Generation {generation + 1}:")

        # Select the best two parents
        parents = select_best_parents(population)

        # Generate offspring
        offspring1, offspring2 = crossover(parents[0], parents[1])

        # Apply mutation to offspring
        offspring1 = mutation(offspring1)
        offspring2 = mutation(offspring2)

        # Replace the worst parents in the population with the new offspring
        population.append(offspring1)
        population.append(offspring2)

        # Sort population based on fitness
        historical_prediction = [-1.2, 3.4, -0.8, 2.1, -2.5, 1.7, -0.3, 5.8, -1.1, 3.5]
        population = sorted(population, key=lambda x: price_calculation(x, historical_prediction, 1000), reverse=True)

        # Update the best chromosome
        current_best_fitness = price_calculation(population[0], historical_prediction, 1000)
        if current_best_fitness > best_fitness:
            best_fitness = current_best_fitness
            best_chromosome = population[0]

        # Keep only the best 4 individuals (elitism)
        population = population[:4]
        print("4 elite population")
        print(population)
    print("Best Chromosome:", best_chromosome)
    print("Best Fitness:", best_fitness)
    return best_chromosome

# @title Runner
# Run Forrest Runnnnnnnnnnnnn
# Initialize population
initial_population = population(4)
print(initial_population)
# Evolve for 10 generations
best_chromosome = evolve(initial_population, generations=10)

"""# TASK 2

"""

#@title Evolve
def evolve_updated(population, generations=10):
    best_chromosome = None
    best_fitness = -float('inf')

    for generation in range(generations):
        print(f"Generation {generation + 1}:")

        # Select the best two parents
        parents = select_best_parents(population)

        # Generate offspring
        offspring1, offspring2 = two_point_crossover(parents[0], parents[1])

        # Apply mutation to offspring
        offspring1 = mutation(offspring1)
        offspring2 = mutation(offspring2)

        # Replace the worst parents in the population with the new offspring
        population.append(offspring1)
        population.append(offspring2)

        # Sort population based on fitness
        historical_prediction = [-1.2, 3.4, -0.8, 2.1, -2.5, 1.7, -0.3, 5.8, -1.1, 3.5]
        population = sorted(population, key=lambda x: price_calculation(x, historical_prediction, 1000), reverse=True)

        # Update the best chromosome
        current_best_fitness = price_calculation(population[0], historical_prediction, 1000)
        if current_best_fitness > best_fitness:
            best_fitness = current_best_fitness
            best_chromosome = population[0]

        # Keep only the best 4 individuals (elitism)
        population = population[:4]
        print("4 elite population")
        print(population)
    print("Best Chromosome:", best_chromosome)
    print("Best Fitness:", best_fitness)
    return best_chromosome

# @title Runner
# Run Forrest Runnnnnnnnnnnnn
# Initialize population
initial_population = population(4)
print(initial_population)
# Evolve for 10 generations
best_chromosome = evolve_updated(initial_population, generations=10)