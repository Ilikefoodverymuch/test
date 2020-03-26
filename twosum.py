
List = []



class solution:

    def __init__(self,nums,target):
        self.nums = nums
        self.target = target
        self.list = []

    def twoSum(self):
        hashmap = {}
        for key, value in enumerate(self.nums):
            print('key:',key,'value:',value)
            another_num = target - value
            print('another_num:',another_num)
            if another_num in hashmap:
                self.list.append(hashmap[another_num])
                print('hashmap:',hashmap[another_num])
                self.list.append(key)
            hashmap[value] = key
        return self.list

if __name__ == "__main__":
    nums = (10, 20, 30, 40, 50, 60, 70, 80, 90)
    target = 100
    t = solution(nums,target)
    print(t.twoSum())
