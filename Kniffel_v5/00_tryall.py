import random

ones  = [random.randrange(2, 3),random.randrange(2, 3),random.randrange(2, 3)]

print(ones)

onecount = ones.count(1)
print(onecount)
reward = onecount if onecount > 0 else -1
print(reward)

