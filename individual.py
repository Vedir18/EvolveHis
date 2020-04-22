from tests import quadratic_sum
class Individual():

    individ_id = 0
    def __init__(self, init_params=None):
        self.arguments = init_params['arguments']
        self.sigmas = init_params['sigmas']
        Individual.individ_id += 1
        self.pers_id = Individual.individ_id
        self.fitness_func = quadratic_sum
        self.value = self.fitness_func(self.arguments)

    def __repr__(self):
        return f"ID: {self.pers_id}, args: {self.arguments}"

    def __lt__(self, other):
        self.value < other.value