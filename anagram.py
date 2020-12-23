# Anagram solver
from collections import Counter



def contains(container, contained):
    return all(container[x] >= contained[x] for x in contained)
    
    '''
    Check that b is an anagram of a. 
    A can be larger than b. 
    E.g. a = house, b = hoe, res = True
    '''
def check_anagram(a: str, b:str)->bool:
    if len(b) > len(a):
        return False
    return contains(Counter(a), Counter(b))

def get_anagrams(n: int, letters: str)->list:
    assert (n >= 1 and n <= len(letters)), "Invalid anagram"
    
    anagrams = []
    with open("./words.txt") as f:
        anagrams = [ word.strip() for word in f.readlines() if len(word.strip()) == n and check_anagram(letters, word.strip())]

    return anagrams

if __name__ == "__main__":
    a = get_anagrams(4, "eeeeddoonnnsssrv")
    print(a)
    
