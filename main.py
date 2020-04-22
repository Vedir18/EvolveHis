from numpy.random import uniform


def main():
    optimization = Optimization()

    # by now generated the initial population
    generations = 0
    # later make a better stop condition
    while generation < 1000:

        # selection here (lambda individuals)
        # optimization.population.selection()

        # produces the offsprings
        new_individs = optimization.population.produce()
        optimization.population.pool += new_individs()
        optimization.population.pool.sort(reverse=True) # implement better sorting here
        optimization.population.living_selector()
    
    print(optimization.population.find_best())

