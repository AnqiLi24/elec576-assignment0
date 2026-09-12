import numpy as np
import scipy.linalg
from scipy import signal
from scipy.sparse.linalg import eigs, cg
np.set_printoptions(precision=4, suppress=True, linewidth=100)
a = np.array([[1., 2., 3.], [4., 5., 6.], [7., 8., 10.]])
a
m = np.arange(1., 190.).reshape(21, 9)
m
v = np.array([0.1, 0.6, 0.9])
u = np.array([[0.2, 0.8, 0.5], [0.6, 0.4, 0.9]])
np.ndim(a)
a.ndim
np.size(a)
a.size
np.shape(a)
a.shape
a.shape[1]
np.array([[1., 2., 3.], [4., 5., 6.]])
p = np.array([[1., 2.], [3., 4.]]); q = np.array([[5., 6.], [7., 8.]])
np.block([[p, q], [q, p]])
v[-1]
m[1, 4]
m[1]
m[1, :]
m[0:5]
m[:5]
m[0:5, :]
m[-5:]
m[0:3, 4:9]
m[np.ix_([1, 3, 4], [0, 2])]
m[2:21:2, :]
m[::2, :]
m[::-1, :]
a[np.r_[:len(a), 0]]
a.transpose()
a.T
c = a + 1j * np.eye(3)
c.conj().transpose()
c.conj().T
a @ a
a * a
a / a
a ** 3
(u > 0.5)
np.nonzero(u > 0.5)
u[:, np.nonzero(v > 0.5)[0]]
u[:, v.T > 0.5]
w = u.copy(); w[w < 0.5] = 0; w
u * (u > 0.5)
w[:] = 3; w
x = a.copy()
y = x.copy(); y
y = x[1, :].copy(); y
y = x.flatten(); y
x.flatten('F')
np.arange(1., 11.)
np.r_[1.:11.]
np.r_[1:10:10j]
np.arange(10.)
np.r_[:10.]
np.r_[:9:10j]
np.arange(1., 11.)[:, np.newaxis]
np.zeros((3, 4))
np.zeros((3, 4, 5))
np.ones((3, 4))
np.eye(3)
np.diag(a)
np.diag(v, 0)
from numpy.random import default_rng
rng = default_rng(42)
rng.random((3, 4))
np.random.rand(3, 4)
np.linspace(1, 3, 4)
np.mgrid[0:9., 0:6.]
np.meshgrid(np.r_[0:9.], np.r_[0:6.])
np.ogrid[0:9., 0:6.]
np.ix_(np.r_[0:9.], np.r_[0:6.])
np.meshgrid([1, 2, 4], [2, 4, 5])
np.ix_([1, 2, 4], [2, 4, 5])
np.tile(p, (2, 3))
np.concatenate((p, q), 1)
np.hstack((p, q))
np.column_stack((p, q))
np.c_[p, q]
np.concatenate((p, q))
np.vstack((p, q))
np.r_[p, q]
a.max()
np.nanmax(a)
a.max(0)
a.max(1)
np.maximum(p, q)
np.sqrt(v @ v)
np.linalg.norm(v)
ba = np.array([True, False, True]); bb = np.array([True, True, False])
np.logical_and(ba, bb)
np.logical_or(ba, bb)
np.array([12, 10, 7]) & np.array([10, 6, 5])
np.array([12, 10, 7]) | np.array([10, 6, 5])
scipy.linalg.inv(a)
scipy.linalg.pinv(m[:3, :4])
np.linalg.matrix_rank(a)
b = np.array([[6.], [15.], [25.]])
scipy.linalg.solve(a, b)
scipy.linalg.lstsq(m[:, :3], m[:, 3])
br = np.array([[6., 15., 25.]])
scipy.linalg.solve(a.T, br.T).T
U, S, Vh = scipy.linalg.svd(a); V = Vh.T
U
S
V
spd = np.array([[4., 2.], [2., 3.]])
scipy.linalg.cholesky(spd)
D, V = scipy.linalg.eig(a)
D
V
spd2 = np.array([[2., 0.], [0., 1.]])
D, V = scipy.linalg.eig(spd, spd2)
D
V
big = np.diag(np.arange(1., 7.))
D, V = eigs(big, k=3)
D
V
Q, R = scipy.linalg.qr(a)
Q
R
P, L, U = scipy.linalg.lu(a)
P
L
U
np.allclose(a, P @ L @ U)
cg(spd, np.array([1., 2.]))
np.fft.fft(v)
np.fft.ifft(np.fft.fft(v))
np.sort(a)
as0 = a.copy(); as0.sort(axis=0); as0
np.sort(a, axis=1)
as1 = a.copy(); as1.sort(axis=1); as1
s = np.array([[3., 9.], [1., 8.], [2., 7.]])
I = np.argsort(s[:, 0]); bs = s[I, :]; bs
Z = np.c_[np.ones(5), np.arange(5.)]; yv = np.array([1., 3., 5., 7., 9.])
scipy.linalg.lstsq(Z, yv)
sig = np.sin(np.linspace(0, 2 * np.pi, 20)); qd = 4
signal.resample(sig, int(np.ceil(len(sig) / qd)))
np.unique(np.array([3, 1, 2, 3, 1]))
np.zeros((1, 3, 1)).squeeze()
