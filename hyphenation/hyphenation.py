import sys
import re

def hyphenate(p, word):
    
    places = [0] * (len(word) + 1)
    
    for x in p:
        for y in re.finditer(x[0],word):
            for z in x[1]:
                if x[1][z] > places[y.start()+z]:
                    places[y.start()+z] = x[1][z]
    hyph = ''
    for idex,x in enumerate(word):
        if places[idex] % 2 == 1:
            hyph += '-'
        hyph += x
    return hyph
    
def createDict():
    patterns = [re.sub('\\.$','$', y) for y in [re.sub('^\\.','^', x) for x in [line.strip('\n').replace('^.','^').replace('.$','$') for line in open('dict.txt')]]]
    numRegex = re.compile('[0-9]+')
    for x in patterns:
        a={}
        for c,y in enumerate(re.finditer(numRegex,x)):
            a[y.start()-c] = int(y.group(0))
        yield (re.sub(numRegex,'',x), a)


if __name__== "__main__":
    word = sys.argv[1]
    print hyphenate(createDict(),word)