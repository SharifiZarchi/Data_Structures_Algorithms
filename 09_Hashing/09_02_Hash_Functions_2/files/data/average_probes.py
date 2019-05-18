import sys
import my_inspect

words = open('/usr/share/dict/words').read().split()
output = open(sys.argv[1], 'w')
for n in range(1, 3000):
    probe_map = my_inspect.probe_all_steps(words[:n*2])
    seqlens = [ len(seq) for seq in probe_map.values() ]
    a = float(sum( seqlens )) / len(seqlens)
    m = max( seqlens )
    output.write('%d %f %d\n' % (n, a, m))
