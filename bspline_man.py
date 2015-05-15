# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# BSplines vom Grad 4 (stückweise kubisch) mit äquidistanten Knoten,
# wie in Blobel S. 232. Bei äquidistanten Knoten gibt es 5 Knoten und
# damit 4 Intervalle, in denen der BSpline nicht von 0 verschieden ist.
# Beispielhaft werden hier die 3 möglichen BSplines in [1, 4] mit d=0.5
# per Hand gezeichnet.


def bspline(x, start, end, N):
	"""
	Returns numpy array with N values of the BSpline of degree 4 with 5
	equidistant knots in the interval [start, end] at given values of x,
	the knots array and the values of the BSpline at the knots.
	"""
	x = np.array(x, copy=False, ndmin=1)
	degree = 4
	knots = np.linspace(start, end, degree+1)
	d = knots[1] - knots[0]

	y = np.zeros_like(x)
	yk = np.zeros_like(knots)

	values = np.array([
		lambda z: 1./6. * z**3,
		lambda z: 1./6. * (1. + 3. * (1.+z*(1.-z)) * z),
		lambda z: 1./6. * (1. + 3. * (1.+z*(1.-z)) * (1.-z)),
		lambda z: 1./6. * (1. - z)**3
	])

	i = 0
	for a, b in zip(knots[:-1], knots[1:]):
		xmask = (x >= a) & (x < b)
		z = (x - a) / d
		y[xmask] = values[i](z)[xmask]
		yk[i] = values[i](0.)
		i += 1

	yk[4] = values[3](1.)

	return y, knots, yk


N = 200

s1 = 1.0
e1 = 3.0
x1 = np.linspace(s1, e1, N)
y1, k1, yk1 = bspline(x1, s1, e1, N)

s2 = 1.5
e2 = 3.5
x2 = np.linspace(s2, e2, N)
y2, k2, yk2 = bspline(x2, s2, e2, N)

s3 = 2.0
e3 = 4.0
x3 = np.linspace(s3, e3, N)
y3, k3, yk3 = bspline(x3, s3, e3, N)

plt.plot(x1, y1)
plt.plot(k1, yk1, "o")
plt.plot(x2, y2)
plt.plot(k2, yk2, "o")
plt.plot(x3, y3)
plt.plot(k3, yk3, "o")
plt.show()