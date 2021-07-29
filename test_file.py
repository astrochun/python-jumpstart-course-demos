from final.actors import SmallAnimal, Creature, Dragon, Wizard

nums = [1, 1, 2, 3, 5, 8, 13 , 21]

for i, fib in enumerate(nums):
    print("{}. {}".format(i+1, fib))

creatures = [
    SmallAnimal('Toad', 1),
    Creature('Tiger', 12),
    SmallAnimal('Bat', 3),
]

hero = Wizard('Gandolf', 75)

print("Hero battles: {}".format(hero.attack(creatures[0])))