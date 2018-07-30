import numpy
import click
import timeit


@click.command()
@click.option("-n", default=4000)
@click.option("-a", default=0.8)
@click.option("-b", default=1.0)
def main(n, a, b):
    start = timeit.default_timer()
    nhits = 0
    for i in range(n):
        xcenter = numpy.random.uniform(0, b / 2)
        
        deltax = numpy.random.uniform(0, 1)
        deltay = numpy.random.uniform(0, 1)
        hypo = numpy.sqrt(deltax**2 + deltay**2)
        while (hypo > 1):
            deltax = numpy.random.uniform(0, 1)
            deltay = numpy.random.uniform(0, 1)
            hypo = numpy.sqrt(deltax**2 + deltay**2)

        xtip = xcenter - (a / 2) * (deltax / hypo)
        if (xtip < 0):
            nhits += 1
    estimated_pi = (a / b) * (2 / (nhits / n))
    stop = timeit.default_timer()
    print(f"nhits = {nhits}; pi = {estimated_pi}; time = {stop - start} seconds")

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
if __name__ == '__main__':
    main()