from random import randint, random, choice as randomChoice
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
    
# The secret cake
SECRET = Cake(255, 255, 255, 4)
        
# Pool
pool = []

# Parents
parents = []

# Offspring
offspring = []

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
    pool.append(Cake())
    
while True:
    total_score = calculate_total(pool)
    # Add the members of the population to the parents pool by probablility
    for i in range(len(pool)):
        for j in range(pool[i].fitness(SECRET)):
            if pool[i].fitness(SECRET) == 148:
                print pool
                print "\n\n"
                print "Correct Member Found! \t"
                print pool[i]
                print num_iters    
                sys.exit()
            parents.append(pool[i])
    
    # Pick 10 random parents and mate them
    for _ in range(50):
        offspring.append(randomChoice(parents).mix(randomChoice(parents)).bake())
    
    #print "Start"
    #for p in pool: print p
    #print "End"
    #for c in offspring: print c

            
    pool[:]=offspring
    del parents[:]
    del offspring[:]
    num_iters+=1
    

