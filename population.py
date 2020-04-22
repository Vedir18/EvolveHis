from random import randint
import numpy
from math import e

class Population():
    
    def __init__(self, init_params):
        self.dim = init_params['dim']
        self.individuals = init_params['individuals']
        self.lambd = init_params['lambda']
        self.mu = init_params['mu']
        self.worst_ever = []
        self.pool = []
    
    # a function that decides who lives and who dies
    def living_selector(self):
        # the worst automatically gets the ticket to worst_ever
        # the best automatically gets the ticket to new generation
        # else: Roulette selection

        worst = find_worst()
        best = find_worst()
        self.worst_ever.append(worst)
        self.individuals.append(best)

        # mu - 1 tickets
        # TODO: Roulette selection
        tickets = []


    
    def find_best(self):
        return self.individuals[0]

    def find_worst(self):
        return self.individuals[-1]

    def produce(self):
        selected = self.selection()
        mothers, fathers = selected[::2], selected[1::2]
        offsprings = [] # r_population
        for mother, father in zip(mothers, fathers):

            # mutation here doesn't depend on chance
            child1, child2 = mutation(crossover(mother, father))
            offsprings.append(child1)
            offsprings.append(child2)
        return offsprings


    def selection(self):
        t_population = []
        temp = self.individuals.copy()
        for i in range(self.lambd):
            el = temp[randint(0, len())]
            t_population.append(el)
            temp.remove(el)
        return t_population

    # interpolation crossover
    def crossover(self, mother: Individual, father: Individual):
        a = uniform(0, 1)
        chil1_args = [a * mother.arguments[i] + (1 - a) * father.arguments[i] for i in range(len(father.arguments))]
        chil2_args = [a * father.arguments[i] + (1 - a) * mother.arguments[i] for i in range(len(mother.arguments))]
        child1_sigmas = [a * mother.sigmas[i] + (1 - a) * father.sigmas[i] for i in range(len(father.sigmas))]
        child2_sigmas = [a * father.sigmas[i] + (1 - a) * mother.sigmas[i] for i in range(len(mother.sigmas))]
        return Individual({
            'arguments': child1_args,
            'sigmas': child1_sigmas
        }), Individual({
            'arguments': child2_args,
            'sigmas': child2_sigmas
        })

    def mutation(self, offspring1: Individual, offspring2: Individual):
        tau1 = 1 / numpy.sqrt(2 * self.dim)
        tau2 = 1 / numpy.sqrt(2 * numpy.sqrt(self.dim))
        sharing_rand = numpy.normal(0, 1)
        unique1, unique2 = numpy.normal(0, 1), numpy.normal(0, 1)
        
        sigmas_r1, sigmas_r2 = offspring1.sigmas.copy(), offsprings2.sigmas.copy()
        for i in range(len(sigmas_r1)):
            sigmas_r1[i], sigmas_r2[i] = sigmas_r1[i] * e ** (tau1 * sharing_rand + tau2 * unique1), sigmas_r2 * e ** (tau1 * sharing_rand + tau2 * unique2)

        offspring1.arguments = numpy.multiply(offspring1.arguments + unique1 * sigmas_r1)
        offspring2.arguments = numpy.multiply(offspring2.arguments + unique2 * sigmas_r2)
        return offsprint1, offspring2
        