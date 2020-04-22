from random import randint
import numpy
from numpy.random import uniform, normal
from math import e
from itertools import permutations
from individual import Individual
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
        self.pool.sort(reverse=True)
        worst = self.find_worst()
        best = self.find_worst()
        self.worst_ever.append(worst)
        self.individuals.append(best)

        # mu - 1 tickets
        tickets = []
        for i in range(len(self.pool) - 2):
            for j in range(len(self.pool) - i):
                tickets.append(self.pool[i + 1].pers_id)
        
        # make a better permutation here !!!!!
        for p in permutations(tickets):
            tickets = list(p)
            break

        chosen = []
        for i in range(self.mu):
            index = randint(0, len(tickets) - 1)
            for el in self.pool:
                if el.pers_id == tickets[index]:
                    chosen.append(el)
                    break
            # remove all the used tickets
            tickets = list(filter((tickets[index]).__ne__, tickets))
        
        for el in self.pool:
            if el in self.individuals:
                self.individuals.remove(el)
        self.individuals += chosen

    # we do need sort!
    def find_best(self):
        return self.pool[0]

    # we do not sort, 'cause it's expensive
    def find_worst(self):
        return self.pool[-1]

    def produce(self):
        selected = self.selection()
        mothers, fathers = selected[::2], selected[1::2]
        offsprings = [] # r_population
        for mother, father in zip(mothers, fathers):
            # mutation here doesn't depend on chance
            child1, child2 = self.mutation(*self.crossover(mother, father))
            offsprings.append(child1)
            offsprings.append(child2)
        return offsprings


    def selection(self):
        self.pool = self.individuals.copy()
        t_population = []
        for i in range(self.lambd):
            generated = randint(0, len(self.individuals) - 1)
            el = self.individuals[randint(0, generated)]
            t_population.append(el)
            self.individuals.remove(el)
                # print(f"Exception: {e}, iteration: {i}, generated: {generated}")
        return t_population

    # interpolation crossover
    def crossover(self, mother: Individual, father: Individual):
        a = uniform(0, 1)
        child1_args = [a * mother.arguments[i] + (1 - a) * father.arguments[i] for i in range(len(father.arguments))]
        child2_args = [a * father.arguments[i] + (1 - a) * mother.arguments[i] for i in range(len(mother.arguments))]
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
        sharing_rand = normal(0, 1)
        unique1, unique2 = normal(0, 1), normal(0, 1)

        
        sigmas_r1, sigmas_r2 = offspring1.sigmas.copy(), offspring2.sigmas.copy()
        for i in range(len(sigmas_r1)):
            sigmas_r1[i], sigmas_r2[i] = sigmas_r1[i] * e ** (tau1 * sharing_rand + tau2 * unique1), sigmas_r2[i] * e ** (tau1 * sharing_rand + tau2 * unique2)

        offspring1.arguments = [offspring1.arguments[i] + unique1 * sigmas_r1[i] for i in range(len(offspring1.arguments))]
        offspring2.arguments = [offspring2.arguments[i] + unique1 * sigmas_r2[i] for i in range(len(offspring2.arguments))]
        return offspring1, offspring2
        