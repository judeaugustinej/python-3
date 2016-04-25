"""
 The theorem states that a monkey hitting keys at random
 on a typewriter keyboard for an infinite amount of time will almost surely type a given text,
 such as the complete works of William Shakespeare.
"""
import random

def generatorOne(strlen):
    letters = "abcdefghijklmnopqrstuvwxyz "
    return ''.join(random.choice(letters) for x in range(strlen))

def score(goal, teststring):
    numScore = 0
    for l, t in zip(goal, teststring):
        if l == t:
            numScore = numScore+1
    return numScore/len(goal)

def main():
    
    goalstring = "methinks it is like a weasel"
    newstring = generatorOne(28)
    best = 0
    newscore = score(goalstring, newstring)

    while newscore < 1:
        if newscore > best:
            print(newscore, newstring)
            best = newscore
        newstring = generatorOne(28)
        newscore  = score(goalstring, newstring)

if __name__ == "__main__":
    print(generatorOne(5))
    print(score("god is good", generatorOne(8)))
    main()
