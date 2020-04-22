from optimization import Optimization


def main():

    inits = {
        'arguments': None,
        'sigmas': None,
        'dim': 2,
        'lmbd': 100,
        'mu': 150,
        'initial_len': 200
    }
    optimization = Optimization(inits)

    # by now generated the initial population
    generation = 0
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
        print(generation)
    
    print(optimization.population.find_best())


if __name__ == '__main__':
    main()