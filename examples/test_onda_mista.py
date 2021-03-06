#!/usr/bin/env python
# *-* coding:latin-1 *-*

"""
Soma de duas s�ries de Fourier: Onda Quadrada + Dente de Serra
Com aplica��o de Transformada de Fourier R�pida (FFT)
"""
from pylab import *
import sys

rcParams['legend.loc'] = 'best'


def grafico(m):
    x = linspace(-3 * pi, 3 * pi, 500)
    y = 0
    for h in range(1, 2 * m, 1):
        y = y + (4 / pi) * (sin((2 * h - 1) * x)) / (2 * h - 1) + ((2 / pi) * sin(h * x) / (h))
        dft = fft(y)
    plot(x, y, 'b-', label="m = " + str(2 * m))
    grid(True)
    xlabel('t[s]')
    ylabel('y[t]')
    legend()


for m in range(9):
    subplot(3, 3, m + 1)
    grafico(m + 1)

show()
