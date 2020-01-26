from slow_stuff import monte_carlo_pi
min_i  = 0
max_i =  25
pots  = range(min_i,max_i)
for i in pots:
	n = 2**i
	monte_carlo_pi(n)
