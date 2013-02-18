import sys
from random import randint, random, choice as randomly_choose_cake
from math import exp

class Cake(object):
    '''
    A cake has four ingredients 
    *butter*, *caster sugar*, *self-raising flour* & *eggs*
    '''
    def __init__(self, a=None, b=None, c=None, d=None):
        # Make the cake
        if isinstance(a, tuple) or isinstance(a, list):
            self.ingredients = tuple(a)
        elif isinstance(a, int):
            self.ingredients = (a,b,c,d)
        else:
            self.ingredients = tuple([randint(1,1000) for _ in range(4)])
        #self.bake()
    
    def bake(self):
        # Bake the cake
        # Here the possibility of mutation arises
        changed_ingredients = []
        for ingredient in self.ingredients:
            if random() < 0.01:
                changed_ingredients.append(randint(1,1000))
            else:
                changed_ingredients.append(ingredient)
        self.ingredients = changed_ingredients
        return self
                        
    def mix(self, cake2):
        # "Mix" (mate) with another cake
        return Cake([a if random()<0.5 else b 
                     for (a,b) in zip(self.ingredients, cake2.ingredients)])
    
    def score(self, miss_kipling_cake):
        # miss_kipling_cake is the "best" cake, the cake we are looking for
        diffs = [abs(a-b) 
                 for (a,b) in zip(miss_kipling_cake.ingredients,
                                  self.ingredients)]
        score = sum(diffs)
        if not self.ingredients[0] == self.ingredients[1] == self.ingredients[2]:
            score += 10
        return score
        
    def fitness(self, miss_kipling_cake):
        comparison = [1 if a==b else 0 
                      for (a,b) in zip(miss_kipling_cake.ingredients,
                                       self.ingredients)]
        return int(exp(sum(comparison)+1))
    
    def __str__(self):
        return str(self.ingredients)
    
    def __repr__(self):
        return self.__str__()
    
# Miss Kipling's secret cake
SECRET = Cake(255, 255, 255, 4)
        
# Bakery - A place to store cakes! The population of cakes.
bakery = []

# Parents
parents = []

# Cupcakes - The "children" of two cakes
cupcakes = []

# Scoring
total_score = 0
 
def calculate_total(cakes):
    internal_score = 0
    for cake in cakes:
        internal_score += cake.score(SECRET)
    return internal_score

# Initialisation
num_iters = 0
for i in range(10):
    bakery.append(Cake())
    
while True:
    total_score = calculate_total(bakery)
    # Add the members of the population to the parents bakery by probablility
    for i in range(len(bakery)):
        for j in range(bakery[i].fitness(SECRET)):
            if bakery[i].fitness(SECRET) == 148:
                print bakery
                print "\n\n"
                print "Correct Member Found! \t"
                print bakery[i]
                print num_iters    
                sys.exit()
            parents.append(bakery[i])
    
    # Pick 10 random parents and mate them
    for _ in range(50):
        cupcakes.append(randomly_choose_cake(parents).mix(randomly_choose_cake(parents)).bake())
    
    bakery[:]=cupcakes
    del parents[:]
    del cupcakes[:]
    num_iters+=1
    

