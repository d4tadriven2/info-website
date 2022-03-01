import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import hypergeom

[N, M, n] = [32, 4, 14]
rv = hypergeom(N, M, n)
# n+1 fuer M=k, ansonsten M+1
x = np.arange(0, M+1)
pmf_dogs = rv.pmf(x)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, pmf_dogs, 'bo')
ax.vlines(x, 0, pmf_dogs, lw=3)
ax.set_xlabel('Anzahl der Buben')
ax.set_ylabel('Wahrscheinlichkeit')
plt.show()
