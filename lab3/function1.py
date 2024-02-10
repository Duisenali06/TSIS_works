#ex1
def ounces(gramm):
    return 28.3495231 * gramm;
#print(ounces(N))

"""
gramm = 50;
ounce = ounces(gramm);
"""

#ex 2

def C(F):
    return (5 / 9) * (F - 32);

#f = 50;
#print(C(f))

#ex3
def solve(numheads, numlegs):
    x = numheads * 2;
    x -= numlegs;
    x /= -2;
    numheads -= x;
    return numheads, x;

'''
print(solve(35, 94))
'''