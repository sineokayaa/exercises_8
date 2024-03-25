a = int(input())
b = int(input())

c = int(input())
d = int(input())

rang = list(range(a, b + 1))

out_filter = map(lambda x: x % c != 0 and x % 10 == d, rang)
print(list(out_filter).count(True))

'''
a=10
b=15
c=2
d=5
'''