# python2
s=raw_input()
c=dict()
m=dict()
c['$']=0
flag=0
p=[]
e=[]
for i, v in enumerate(s):
    if v in m:
        m[v].append(i)
    else:
        m[v] = [i]
#print m
for i in xrange(len(s)):
    p.append(s[i])
p.sort()
#print p
for u in xrange(len(p)):
    if u<len(p)-1:
        if p[u]!=p[u+1]:
            c[p[u+1]]=u+1
#print c
for j in xrange(len(s)):
    if s[j]=='$':
        if p[j] in c.keys():
            a=j-c[p[j]]
            e.append(p[j])
            b=m[p[j]][a]
            j=b
            flag=1
            break
    if flag==1:
        break
while s[j]!='$':
    if p[j] in c.keys():
        a=j-c[p[j]]
        e.append(p[j])
        b=m[p[j]][a]
        j=b
print ('').join(e)      