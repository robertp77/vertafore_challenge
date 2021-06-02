import random
def scrambled(inp):
    random.shuffle(inp)
    return inp

#enter array here
print(scrambled([1,2,3,4,5]))

def abbrev(s):
    return s[0]+str(len(s)-2)+s[len(s)-1]

#enter word here
print(abbrev('internationalization'))

def isunique(words,word):
    indict=False
    for w in words:
        if word!=w and word[0]==w[0] and len(word)==len(w) and word[len(word)-1]==w[len(w)-1]:
            return False
        if word==w:
            indict=True
    if indict==True:
        return True
    else:
        return False

#enter dict and word here
print(isunique(["internationalization","localization","accessibility","automatically"],"automatically"))