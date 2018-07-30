import numpy
import click
import timeit

def markov(n, delta, xinitial=1.0, yinitial=1.0):
    nhits = 0
    x, y = xinitial, xinitial
    for i in range(n):
        deltax = numpy.random.uniform(-delta, delta)
        deltay = numpy.random.uniform(-delta, delta)
        if numpy.abs(x + deltax) < 1 and numpy.abs(y + deltay) < 1:
            x += deltax
            y += deltay
        if (x**2 + y**2) < 1:
            nhits += 1
    estimated_pi = 4 * (nhits / n)
    return (nhits, estimated_pi, x, y)

@click.command()
@click.option("-n", default=4000)
@click.option("-delta", default=0.1)
def main(n, delta):
    print("First run: ")
    start = timeit.default_timer()
    nhits, estimated_pi, x, y = markov(n, delta, 1, 1)
    stop = timeit.default_timer()
    print(f"nhits = {nhits}; pi = {estimated_pi}; time = {stop - start} seconds")

    print()
    print("Second run taking as initial point the last one of the first run: ")
    start = timeit.default_timer()
    nhits, estimated_pi, x, y = markov(n, delta, x, y)
    stop = timeit.default_timer()
    print(f"nhits = {nhits}; pi = {estimated_pi}; time = {stop - start} seconds")


if __name__ == '__main__':
    main()