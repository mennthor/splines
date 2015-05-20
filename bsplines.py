# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as si


def bspline(x, i, p, t):
	"""
	Returns values of the ith BSpline basis function at given values x with
	given knots t and polynomial degree k.
	x: x values at which the spline is evaluated.
	i: Number of basis function. i=0,...,n-p-2 with n number of knots.
	p: Degree of bspline. Curve is piecewise polynomial of degree p.
	t: Array of n knots t=(t0,...,tn-1) with: ti<=ti+1, ti<ti+p and n>=2p.
	"""
	x = np.array(x, copy=False, ndmin=1)
	y = np.zeros_like(x)
	# If degree 0, recursion start is reached
	if p == 0:
		# ith basis function is zero everywhere except in [ti,ti+1[
		mask = (x>=t[i]) & (x<t[i+1])
		y[mask] = 1
	# Else do a recursion step
	else:
		c1 = 0
		c2 = 0
		# make sure the denominators are nonzero. if not set ci to zero.
		den = t[i+p] - t[i]
		if den != 0:
			c1 = (x - t[i]) / den
		den = t[i+p+1] - t[i+1]
		if den != 0:
			c2 = (t[i+p+1] - x) / den

		y = c1 * bspline(x, i, p-1, t) + c2 * bspline(x, i+1, p-1, t)
	return y


## points for function drawing
x = np.linspace(-1, 12, 1000)
## polynomial degree
p = 3
## inner spline knots
t = np.array([3,4,5,6,7,8])
# t = np.array([0, 2, 3, 4, 5, 7, 10])
## p extra outer knots on every side to fullfill sum=1 condition inside all inner knots.
nouter = p
mirror = False
pre = np.zeros(nouter)
post = np.zeros(nouter)
if mirror:
	# Mirror internal knots at t0, tn-1
	for i in range(nouter):
		pre[i] = t[0] - (t[i+1] - t[0])
		post[i] = t[-1] + (t[-1] - t[-(i+2)])
	pre = pre[::-1]
else:
	# Just repeat the outermost knots p times each
	pre.fill(t[0])
	post.fill(t[-1])

t = np.concatenate((pre, t, post))
print t

## Coefficient array for every spline. Default is np.ones(len(t)-p-1), as there
## are len(t)-p-1 basis function with equal weight 1. The length of t is
## counted with the outer knots included.
c = np.ones(len(t)-p-1)
# c = 1 + 0.1 * np.random.normal(0,1,len(t)-p-1)

## plot knot positions
yl = -0.2
yu = 1.5
plt.plot(t[nouter:-nouter], np.zeros_like(t[nouter:-nouter]), "o", color="red", label="inner knots")
plt.plot(t[:nouter], -np.arange(1, 4)[::-1]*0.02, "o", color="green", label="outer knots")
plt.plot(t[-nouter:], -np.arange(1, 4)*0.02, "o", color="green")
plt.vlines(t, yl, yu, color="k", linestyles="dashed", alpha=0.5)
## plot all basis functions
y = np.zeros((len(t)-p-1, len(x)))
for i in range(len(t)-p-1):
	y[i] = c[i] * bspline(x, i, p, t)
	plt.plot(x, y[i])
## plot spline sum
plt.plot(x, np.sum(y, axis=0), 'k', lw=2, label="sum", alpha=.5)

plt.legend(loc="best")
plt.xlim(-1, 12)
plt.ylim(yl, yu)
plt.show()

