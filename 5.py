import functools

a = int(input())
b = int(input())
c = int(input())

rang = range(a, b+1)

out_filter = filter(lambda x: x ** 0.5 == int(x ** 0.5) and x % c == 0, rang)
if not out_filter:
    out_filter = [0]

res = functools.reduce(lambda x, y: x * y, out_filter)
print(res)

'''
a=1
b=40
c=2
'''