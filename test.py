def change(num,str):
    # nums = int(num)
    b = str.split(' ')
    convermap = {}
    for i in range(1,10):
        convermap[b[i]] = i
    res = []
    for j in range(len(num)):
        res.append(convermap[num[j]])

    return int(res)


import math

def mianji(num,nums):
    res = 0
    for i in range(num):
        res += (nums[i]**2)*(-1)**(i)
    return format(res*math.pi,'.5f')









a = 'sdfas'
print(a[2])
num = input()
b = int(num)
print(b)
str = input()
print(type(num),num)

print(type(str),str)
print(change(num,str))

if __name__ == '__main__':
    num = input()
    str = input()
    print(change(num, str))