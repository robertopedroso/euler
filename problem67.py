import os

def read_triangle_from_file(fpath):
    tri = [line.strip().split(' ') for line in open(fpath, 'r')]
    for i, line in enumerate(tri):
        tri[i] = [int(n) for n in line]
    return tri

def sumrow(tri, n):
    for i in xrange(len(tri[n])):
        tri[n][i] += max([tri[n+1][i], tri[n+1][i+1]])

    if len(tri[n]) == 1: return tri[n][0]
    else: return sumrow(tri, n-1)

if __name__ == "__main__":
    # safely load script without caring about CWD
    script_dir = os.path.dirname(__file__)
    data_path = "data/problem67.txt"
    fpath = os.path.join(script_dir, data_path)

    tri = read_triangle_from_file(fpath)
    maxpath = sumrow(tri, len(tri) - 2)
    print maxpath
