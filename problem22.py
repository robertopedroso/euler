from string import ascii_uppercase
import os

def alphascore(word):
    """Scores a word based on its letters, where each letter is worth its
    position in the alphabet. E.g. a=1, z=26"""
    return sum([ascii_uppercase.index(l)+1 for l in word])

if __name__ == "__main__":
    # safely load script without caring about CWD
    script_dir = os.path.dirname(__file__)
    data_path = "data/problem22.txt"
    fpath = os.path.join(script_dir, data_path)

    # read list of names, split by comma, remove parens, and sort alphabetically
    with open(fpath, 'r') as f:
        names = sorted(f.read().replace('"','').split(','))
         
    score = sum(i * alphascore(name) for i, name in enumerate(names, 1))
    print score
