from numpy.random import uniform

class Optimization():
    def __init__(self):
        self.dim = init_params['dim']
        self.lmbd = init_params['lmbd']
        self.mu = init_params['mu']
        self.initial_len = init_params['initial_len']
        
        initial = {
            'individuals': generate_population(),
            'lambda': self.lmbd,
            'mu': self.mu
        }
        self.population = Population(initial)

    def generate_population(self):
        individs = []
        for i in range(self.initial_len):
            arguments, sigmas = [], []
            for j range(self.dim):
                # give it some use!!!
                argument = random(0, 1)
                sigma = random(0, 1) 
                arguments.append(value)
            individs.append(arguments)
        return individs

