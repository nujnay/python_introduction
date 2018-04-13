
list_one = [('111', 'aaa'), ('222', 'bbb'), ('333', 'ccc')]
list_one_new = sorted(list_one, key=lambda zz: zz[0], reverse=True)
print(list_one_new)
