# python2
d=raw_input()
#t=[]
t=[]
p=[]
v=''
for i in xrange(len(d)):
    t.append(d[i])
t.sort()
#print t
for i in xrange(len(d)):
    p.append(d[i:]+d[:i])
p.sort()
for j in xrange(len(p)):
    v=v+p[j][-1]
print v
    