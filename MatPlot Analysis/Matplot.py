import matplotlib.pyplot as plt   # we can now use plt to refer to the library
from math import log

# create the plot
def plot(title, x, y, xvals,vals):
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    for y in vals:
        plt.plot(xvals[(len(xvals)-len(y[0])):], y[0], '-'+y[1], label=y[2])

    plt.legend(loc='upper right')
    # display the plot
    plt.show()

if __name__ == "__main__":
    # lists of our x and y vals (points are x[n],y[n])
    xvals = [0,1,2,3,4,5,6]
    vals = [[[log(x) for x in xvals[1:]],'s','log(x)'],[[log(x,2) for x in xvals[1:]],'c','log2(x)'],[[x*log(x) for x in xvals[1:]],'o','xlog(x)'],[[2**x for x in xvals],'r','2^x'],[[x**2 for x in xvals],'b','x^2'],[[x**3 for x in xvals],'g','x^3'],[[1 for x in xvals],'y','1'],[[0,1,2,3,4,5,6],'m','x']]
    plot(xvals,vals)
