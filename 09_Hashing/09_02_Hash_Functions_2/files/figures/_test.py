import _dictdraw, sys, _dictinfo

d = {'arya': 666, 'john': 858, 'snow':1, 'alive': 2, 'dead':3}
b = ['arya', 'john', 'snow', 'alive', 'dead']
l = [1, 'snow', 'alive', 'dead']
print _dictinfo.probe_all_steps(b)
print _dictinfo.probe_all_steps(l + ["fire"])