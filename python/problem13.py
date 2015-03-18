import os

if __name__ == "__main__":
    # safely load script without caring about CWD
    script_dir = os.path.dirname(__file__)
    data_path = "../data/problem13.txt"
    fpath = os.path.join(script_dir, data_path)

    # this uninspired question gets an uninspired solution
    # python tacitly converts ints to longs to save us the trouble
    with open(fpath, 'r') as f:
        bigsum = sum(int(line) for line in f)
        firstn = str(bigsum)[0:10]
        print firstn
