def divisors(n):
    k = int(n) // 2 + 1
    for i in range(1, k):
        if n % i == 0:
            a.append(list(str(i)))


def findmax(a):
    l = 0
    bb = {}
    for key in a.keys():
        if a[key] > l:
            l = a[key]
            bb.clear()
            bb[str(key)] = a[key]
        if a[key] == l:
            l = a[key]
            bb[str(key)] = a[key]
    return bb


a = []
sum_a = {}
kk = 0
mm = []

n = int(input("Number: "))
divisors(n)

for i in a:
    for j in i:
        kk += int(j)
    b = int("".join(str(x) for x in i))
    sum_a[str(b)] = kk
    kk = 0

bb = findmax(sum_a)
for key in bb.keys():
    mm.append(int(key))

kk = min(mm)
print(kk)
