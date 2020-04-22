class Individual():

    individ_id = 0
    def __init__(self, init_params=None):
        self.arguments = init_params['arguments']
        self.sigmas = init_params['sigmas']
        Individual.individ_id += 1
        self.pers_id = Individual.individ_id

    def __repr__(self):
        return f"ID: {self.pers_id}, arguments: {self.arguments}"