from typing import List


class MajorityElement:
    def majorityElement(self, nums: List[int]) -> int:
        vote : int = 0
        res : int = 0
        for num in nums:
            if vote == 0:
                ##前面都消完了，在重新赋值
                res = num
                vote = 1
            elif res == num:
                vote +=1
            else:
                vote -=1
        return res

if __name__ == '__main__':
    nums=[3,3,4]
    single = MajorityElement()
    num:int=single.majorityElement(nums)
    print(num)

