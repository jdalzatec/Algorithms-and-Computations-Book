import numpy
import click
import timeit

@click.command()
@click.option("-n", default=40000)
@click.option("-seed", default=numpy.random.randint(10000))
def main(n, seed):
    numpy.random.seed(seed)
    start = timeit.default_timer()
    nhits = 0
    for i in range(n):
        x = numpy.random.uniform(-1, 1)
        y = numpy.random.uniform(-1, 1)
        if (x**2 + y**2) < 1:
            nhits += 1
    estimated_pi = 4 * (nhits / n)
    stop = timeit.default_timer()
    print(nhits, "pi = ", estimated_pi, "time = ", stop - start, "seconds")


    # A faster implementation
    numpy.random.seed(seed)
    start = timeit.default_timer()
    x, y = numpy.random.uniform(-1, 1, size=(n, 2)).T
    inner = (x**2 + y**2) < 1
    nhits = numpy.count_nonzero(inner)
    estimated_pi = 4 * (nhits / n)
    stop = timeit.default_timer()
    print(nhits, "pi = ", estimated_pi, "time = ", stop - start, "seconds")



if __name__ == '__main__':
    main()