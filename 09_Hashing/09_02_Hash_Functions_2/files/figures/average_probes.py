import sys
import matplotlib.pyplot as plt

xa, ya1, ya2 = [], [], []
for line in open('data/average_probes.txt'):
    x, y1, y2 = line.split()
    xa.append(float(x)*2)
    ya1.append(float(y1))
    ya2.append(float(y2))

plt.figure(figsize=(8, 6))
plt.plot(xa, ya1, 'c', lw=3)
plt.text(2600, 2.5, 'average', color='c', fontsize=18)

plt.plot(xa, ya2, 'r', lw=3)
plt.text(2600, 9, 'worst', color='r', fontsize=18)

plt.plot([0, 6000], [1, 1], 'k--', lw=1)
plt.plot([0, 6000], [2, 2], 'k--', lw=1)
plt.axis([0, 6000, 0, 20])
plt.title('Probes per getitem vs. dictionary size', fontsize=16)
plt.savefig(sys.argv[1], dpi=96)
