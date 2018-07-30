import numpy
import click
import timeit
from matplotlib import pyplot


def figure_1_8(a, b, points=201):
    # figure of the landing pad for th Buffon needle experiment for a < b (figure 1.8)
    xcenter = numpy.linspace(0, b / 2, points)
    phi = numpy.linspace(0, numpy.pi / 2, points)
    XCENTER, PHI = numpy.meshgrid(xcenter, phi)
    Nhits = numpy.zeros_like(XCENTER)
    Nhits[(XCENTER < (a / 2)) & (numpy.abs(PHI) < numpy.arccos(XCENTER / (a / 2)))] = 1.0
    
    pyplot.figure(figsize=(5, 4))
    mesh = pyplot.pcolormesh(xcenter, phi, Nhits, cmap="summer",
                             vmin=0.0, vmax=1.0, edgecolors="face", shading="gouraud")
    pyplot.plot(xcenter, numpy.arccos(xcenter / (a / 2)), lw=3, color="black")
    pyplot.xlim(0, b / 2)
    pyplot.ylim(0, numpy.pi / 2)
    pyplot.yticks(numpy.linspace(0, numpy.pi / 2, 3))
    pyplot.gca().set_yticklabels(['0', r"$\pi/4$", r"$\pi/2$"])
    pyplot.xlabel(r"$x_{\rm center}$", fontsize=20)
    pyplot.ylabel(r"$\phi$", fontsize=20)
    cbar = pyplot.colorbar(mesh)
    cbar.set_label(r"$N_{\rm hits}$", fontsize=20)
    cbar.set_ticks([0, 1])
    pyplot.title(rf"$a = {a}; \ b = {b}$")
    pyplot.tight_layout()
    pyplot.savefig("figure_1.8.pdf")
    pyplot.close()


@click.command()
@click.option("-n", default=4000)
@click.option("-a", default=0.8)
@click.option("-b", default=1.0)
def main(n, a, b):
    assert (a <= b)
    # figure_1_8(a, b)

    start = timeit.default_timer()
    nhits = 0
    for i in range(n):
        xcenter = numpy.random.uniform(0, b / 2)
        phi = numpy.random.uniform(0, numpy.pi / 2)
        xtip = xcenter - (a / 2) * numpy.cos(phi)
        if (xtip < 0):
            nhits += 1
    stop = timeit.default_timer()
    print(f"nhits = {nhits}; time = {stop - start} seconds")


if __name__ == '__main__':
    main()