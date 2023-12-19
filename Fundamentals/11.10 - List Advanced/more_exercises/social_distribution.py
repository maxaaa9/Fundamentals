population = list(map(int, input().split(", ")))
minimum_wealth = int(input())

if sum(population) < len(population) * minimum_wealth:
    population = "No equal distribution possible"
else:
    for wealth in range(len(population)):
        max_wealth = max(population)
        index = population.index(max_wealth)
        if population[wealth] < minimum_wealth and max_wealth > minimum_wealth:
            max_wealth -= minimum_wealth - population[wealth]
            population[wealth] += minimum_wealth - population[wealth]
            population[index] = max_wealth

print(population)
