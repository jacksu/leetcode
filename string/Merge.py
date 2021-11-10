from typing import List


class Merge:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m;
        j = n;
        while i + j > 0 and j > 0:
            if (i > 0 and nums1[i - 1] > nums2[j - 1]):
                nums1[i + j - 1] = nums1[i - 1]
                i -= 1
            else:
                nums1[i + j - 1] = nums2[j - 1]
                j -= 1
        for num in nums1:
            print(num)


if __name__ == '__main__':
    nums1 = [2, 0]
    m = 1
    nums2 = [1]
    n = 1
    merge = Merge()
    num: int = merge.merge(nums1, m, nums2, n)
    print(num)
