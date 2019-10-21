a = ['foo','bar','baz','qux','corge']
while a:
    if len(a) < 3:
        break
    print(a.pop(), end=' ')
print('Done.')

print(a) if a == 1 else print("nope")


d={'j':1, 'b':2, 'g':3}
while d:
    print(d.popitem(), end='')
print('koniec')
