s1 = {1,2,3}
s2 = [[2,5],[1,2]]
s3 = {1,2,3,4,5}

list = []
for s in s2:
    if s1 <= set(s):
        print('test')

print([s1 <= set(s) for s in s2])

print(s1 <= s3)