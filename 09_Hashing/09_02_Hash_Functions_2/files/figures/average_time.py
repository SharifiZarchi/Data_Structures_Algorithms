import sys
import matplotlib.pyplot as plt

t1 = 66.5
t16 = 116.8
tper = (t16 - t1) / (16 - 1)
t0 = t1 - tper

def probes_to_time(n):
    """Given a number of probes, return the time getitem should take."""
    # Based on tests with timeit() on my Dell Latitude D630 laptop.
    return t0 + n * tper

xa, ya1, ya2 = [], [], []
for line in open('data/average_probes.txt'):
    x, y1, y2 = line.split()
    xa.append(float(x)*2)
    ya1.append(probes_to_time(float(y1)))
    ya2.append(probes_to_time(float(y2)))

plt.figure(figsize=(8, 6))
plt.plot(xa, ya1, 'c', lw=2)
plt.text(2600, 70, 'average', color='c', fontsize=18)

plt.plot(xa, ya2, 'r', lw=2)
plt.text(2600, 95, 'worst', color='r', fontsize=18)

plt.plot([0, 6000], [t1, t1], 'b', lw=2)
plt.text(2600, 55, 'best', color='b', fontsize=18)

plt.axis([0, 6000, 0, 140])
plt.title('Duration of getitem call (ns) vs. dictionary size', fontsize=16)
plt.savefig(sys.argv[1], dpi=96)
