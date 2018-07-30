import numpy
import click
import timeit
from matplotlib import pyplot
from matplotlib.patches import Ellipse


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

def figure_1_10(n, a, b, height, ncracks=18):
    # Buffon's experiment with n needles of size a and ncracks of size b
    
    pyplot.figure()

    for i in range(ncracks):
        pyplot.axvline(i * b, ls="-", color="black")

    for i in range(n):
        xcenter = numpy.random.uniform(0, (ncracks - 1) * b)
        ycenter = numpy.random.uniform(0, height)
        phi = numpy.random.uniform(0, 2*numpy.pi)
        xtip1 = xcenter - (a/2)*numpy.cos(phi)
        xtip2 = xcenter + (a/2)*numpy.cos(phi)
        ytip1 = ycenter - (a/2)*numpy.sin(phi)
        ytip2 = ycenter + (a/2)*numpy.sin(phi)
        ellipse = Ellipse(((xtip1 + xcenter) * 0.5, (ytip1 + ycenter) * 0.5),
            0.1, a / 2, 90 + numpy.degrees(phi), fill=False, lw=1)
        pyplot.gca().add_artist(ellipse)
        pyplot.plot([xcenter, xtip2], [ycenter, ytip2], "-", color="black", lw=1)
    
    pyplot.xlim(-b / 2, (ncracks - 1) * b + (b / 2))
    pyplot.ylim(0, height)
    pyplot.xticks([])
    pyplot.yticks([])
    pyplot.gca().set_aspect("equal")
    pyplot.axis('off')
    pyplot.tight_layout()
    pyplot.savefig("figure_1.10.pdf")
    pyplot.close()


@click.command()
@click.option("-n", default=2000)
@click.option("-a", default=1.0)
@click.option("-b", default=1.0)
def main(n, a, b):
    assert (a <= b)
    # figure_1_8(a, b)
    # figure_1_10(n, a, b, 20*b)
    
    start = timeit.default_timer()
    nhits = 0
    for i in range(n):
        xcenter = numpy.random.uniform(0, b / 2)
        phi = numpy.random.uniform(0, numpy.pi / 2)
        xtip = xcenter - (a / 2) * numpy.cos(phi)
        if (xtip < 0):
            nhits += 1
    estimated_pi = (a / b) * (2 / (nhits / n))
    stop = timeit.default_timer()
    print(f"nhits = {nhits}; pi = {estimated_pi}; time = {stop - start} seconds")


if __name__ == '__main__':
    main()