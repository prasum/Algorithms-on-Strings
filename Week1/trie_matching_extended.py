# python2
def allindices(string, sub, listindex=[], offset=0):
    i = string.find(sub, offset)
    while i >= 0:
        listindex.append(i)
        i = string.find(sub, i + 1)
    return listindex
o=[]
listindex=[]
str1=raw_input()
n=int(input())
offset=0
for i in xrange(n):
    str2=raw_input()
    j = str1.find(str2, offset)
    while j >= 0:
        listindex.append(j)
        j = str1.find(str2, j + 1)
    str2=''
r=set(listindex)
listindex=list(r)
#str1="AAA"
#str2="AA"
#p=allindices(str1,str2)
listindex.sort()
for y in xrange(len(listindex)):
    listindex[y]=str(listindex[y])
#p.sort()
print ' '.join(listindex)
#k=[m.start() for m in re.finditer('(?=str2)', str1)]
