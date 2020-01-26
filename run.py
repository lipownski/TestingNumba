from numba import jit
import random
from slow_stuff import monte_carlo_pi
import time 
import matplotlib.pyplot as plt
import numpy as np
min_i  = 0
max_i =  25
pots  = range(min_i,max_i)
timing = np.zeros([len(pots),2])


@jit(nopython=True)
def jit_monte_carlo_pi(nsamples):
    acc = 0
    for i in range(nsamples):
        x = random.random()
        y = random.random()
        if (x ** 2 + y ** 2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples


def py_monte_carlo_pi(nsamples):
	acc = 0
	for i in range(nsamples):
		x = random.random()
		y = random.random()
		if (x ** 2 + y ** 2) < 1.0:
			acc += 1
	return 4.0 * acc / nsamples
  
  
    
    
for i in pots:
	n = 2**i
	
	t0 = time.time()	
	py_monte_carlo_pi(n)
	timing[i-min_i][0] = time.time() -t0
	
	
	t0 = time.time()	
	jit_monte_carlo_pi(n)
	timing[i-min_i][1] = time.time() -t0

plt.plot(pots,timing, label=["Python","Jit"])
plt.xlabel("log_2(n)")
plt.ylabel("Laufzeit /s")
print(np.sum(timing,axis=0))
plt.show()

