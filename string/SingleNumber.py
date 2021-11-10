from typing import List


class SingleNumber:
    def singleNumber(self, nums: List[int]) -> int:
        res: int = 0
        for num in nums:
            res=res^num
        return  res


if __name__ == '__main__':
    nums=[0,0,3]
    single = SingleNumber()
    num:int=single.singleNumber(nums)
    print(num)
