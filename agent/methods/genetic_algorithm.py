import numpy as np
import random
import math

def create_initial_population(num_cities, population_size, list):
    population = []
    for _ in range(population_size):
        chromosome = list.copy()
        chromosome.remove((1, 1))  # Usuń punkt (1, 1) z listy
        random.shuffle(chromosome)
        chromosome.insert(0, (1, 1))  # Dodaj punkt (1, 1) na początku trasy
        population.append(chromosome)
    return population

def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

def calculate_fitness(individual):
    total_distance = 0

    num_cities = len(individual)

    for i in range(num_cities - 1):
        city1 = individual[i]
        city2 = individual[i + 1]
        distance = calculate_distance(city1, city2)
        total_distance += distance

    fitness = 1 / total_distance

    return fitness

def crossover(parent1, parent2):
    child = [(1, 1)] + [None] * (len(parent1) - 1)  # Inicjalizacja dziecka z punktem (1, 1) na początku
    start_index = random.randint(1, len(parent1) - 1)
    end_index = random.randint(start_index + 1, len(parent1))
    # Skopiuj fragment miast od parent1 do dziecka
    child[start_index:end_index] = parent1[start_index:end_index]
    # Uzupełnij brakujące miasta z parent2
    remaining_cities = [city for city in parent2 if city not in child]
    child[1:start_index] = remaining_cities[:start_index - 1]
    child[end_index:] = remaining_cities[start_index - 1:]
    return child

def mutate(individual, mutation_rate):
    for i in range(1, len(individual)):  # Rozpoczynamy od indeksu 1, aby pominąć punkt (1, 1)
        if random.random() < mutation_rate:
            j = random.randint(1, len(individual) - 1)  # Wybieramy indeks od 1 do ostatniego indeksu
            individual[i], individual[j] = individual[j], individual[i]
    return individual

def genetic_algorithm(list):
    chromosome_length = 21
    max_generations = 200
    population_size = 200
    crossover_rate = 0.25
    mutation_rate = 0.1
    num_cities = chromosome_length
    population = create_initial_population(num_cities, population_size, list)

    best_individual = None
    best_fitness = float('-inf')

    for generation in range(max_generations):
        # # Oblicz wartości fitness dla każdego osobnika w populacji
        # fitness_values = [calculate_fitness(individual) for individual in population]
        # population = [x for _, x in sorted(zip(fitness_values, population), reverse=True)]
        # fitness_values.sort(reverse=True)
        # max_fitness_index = np.argmax(fitness_values)
        # # Wybierz najlepszego osobnika z ostatniej populacji
        # if fitness_values[max_fitness_index] > best_fitness:
        #     best_fitness = fitness_values[max_fitness_index]
        #     best_individual = population[max_fitness_index]
       
        # # Twórz nową populację z krzyżówek
        # new_population = []
        # for _ in range(int(population_size / 2)):
        #     parent1, parent2 = random.choices(population[:population_size // 2], k=2)
        #     child1 = crossover(parent1, parent2)
        #     child2 = crossover(parent2, parent1)
        #     new_population.extend([child1, child2])
        # # Dokonaj mutacji na nowej populacji
        # new_population = [mutate(individual, mutation_rate) for individual in new_population]
        # population = new_population

        # Oblicz wartości fitness dla każdego osobnika w populacji
        fitness_values = [calculate_fitness(individual) for individual in population]
        population = [x for _, x in sorted(zip(fitness_values, population), reverse=True)]
        fitness_values.sort(reverse=True)
        best_individuals = population[:10]  # Wybierz k najlepszych osobników
        new_population = best_individuals.copy()

        # Twórz nową populację z krzyżówek i mutacji
        while len(new_population) < population_size:
            parent1, parent2 = random.choices(best_individuals, k=2)  # Wybierz rodziców spośród najlepszych osobników
            child = crossover(parent1, parent2)  # Krzyżowanie
            child = mutate(child, mutation_rate)  # Mutacja
            new_population.append(child)

        for individual in best_individuals:
            fitness = calculate_fitness(individual)
            if fitness > best_fitness:
                best_fitness = fitness
                best_individual = individual

        population = new_population[:population_size]

        
    print("Best path:", best_individual)
    return best_individual
