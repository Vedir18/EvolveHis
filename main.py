from optimization import Optimization


def main():

    inits = {
        'arguments': None,
        'sigmas': None,
        'dim': 1,
        'lmbd': 90,
        'mu': 150,
        'initial_len': 200
    }
    optimization = Optimization(inits)

    # by now generated the initial population
    generation = 0
    breakpoint()
    # later make a better stop condition
    while generation < 1000:

        # selection here (lambda individuals)
        # optimization.population.selection()

        # produces the offsprings
        new_individs = optimization.population.produce()
        optimization.population.pool += new_individs
        optimization.population.pool.sort(reverse=True) # implement better sorting here
        optimization.population.living_selector()
        generation += 1
        print(f"Generation {generation}, num_of_individs = {len(optimization.population.individuals)}. Best: {optimization.population.find_best()}")
    
    print(optimization.population.find_best())


if __name__ == '__main__':
    main()