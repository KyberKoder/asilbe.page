# 1) copy()
a = [1,2,3]
b = a.copy()
print(b)

x = ['ali','vali']
y = x.copy()
print(y)

nums = [10,20]
new_nums = nums.copy()
print(new_nums)

s = ['olma','anor']
ss = s.copy()
print(ss)

p = [5,6,7]
p2 = p.copy()
print(p2)

# 2) pop()
a = [10,20,30]
a.pop()
print(a)

b = [1,2,3,4]
b.pop(2)
print(b)

x = ['A','B','C']
x.pop(0)
print(x)

nums = [5,10,15]
nums.pop(-1)
print(nums)

m = [100,200,300,400]
m.pop(1)
print(m)

# 3) remove()
a = [1,2,3]
a.remove(2)
print(a)

x = ['ali','vali']
x.remove('ali')
print(x)

nums = [10,20,20,30]
nums.remove(20)
print(nums)

m = ['olma','banan','olma']
m.remove('olma')
print(m)

lst = [5,6,7]
lst.remove(6)
print(lst)

# 4) sort()
a = [4,1,3]
a.sort()
print(a)

nums = [10,3,5]
nums.sort(reverse=True)
print(nums)

names = ['ali','javlon','bek']
names.sort()
print(names)

s = [100,50,300]
s.sort()
print(s)

t = ['z','a','x']
t.sort()
print(t)

# 5) clear()
a = [1,2,3]
a.clear()
print(a)

nums = [10,20]
nums.clear()
print(nums)

x = ['olma','anor']
x.clear()
print(x)

s = [44,55]
s.clear()
print(s)

t = ['a','b']
t.clear()
print(t)

# 6) insert()
a = [1,3,4]
a.insert(1,2)
print(a)

names = ["ali","vali"]
names.insert(0,"anvar")
print(names)

s = [10,20,30]
s.insert(3,99)
print(s)

x = ['A','B']
x.insert(1,'C')
print(x)

arr = ["olma","anor"]
arr.insert(2,"banana")
print(arr)

# 7) append()
a = [1,2]
a.append(3)
print(a)

x = ['ali']
x.append('vali')
print(x)

nums = []
nums.append(10)
print(nums)

lst = ['a','b']
lst.append('c')
print(lst)

m = ['olma']
m.append('uzum')
print(m)

# 8) extend()
a = [1,2]
a.extend([3,4])
print(a)

x = ['ali']
x.extend(['vali','anvar'])
print(x)

nums = [10]
nums.extend([20,30])
print(nums)

lst = []
lst.extend([5,6,7])
print(lst)

m = ['a']
m.extend(['b','c'])
print(m)
