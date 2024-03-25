a = int(input())
b = int(input())

c = int(input())
d = int(input())

rang = list(range(a, b + 1))

out_filter = filter(lambda x: x % c == 0 and x % d == 0, rang)
print(sum(list(out_filter)))

'''
a=2
b=12
c=2
d=3
'''