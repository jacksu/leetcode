from typing import List


class SearchMatrix:

    def binarySearch(self, arr: List[int], l: int, r: int, x: int) -> int:
        # 基本判断
        if r >= l:
            mid = int(l + (r - l) / 2)
            # 元素整好的中间位置
            if arr[mid] == x:
                return mid

                # 元素小于中间位置的元素，只需要再比较左边的元素
            elif arr[mid] > x:
                return self.binarySearch(arr, l, mid - 1, x)

                # 元素大于中间位置的元素，只需要再比较右边的元素
            else:
                return self.binarySearch(arr, mid + 1, r, x)

        else:
            # 不存在
            return l

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n: int = len(matrix)
        m: int = len(matrix[0])
        mid = self.binarySearch(matrix[n - 1], 0, m - 1, target)
        if (mid >= m):
            return 0
        while mid < m:
            if (matrix[n - 1][mid] == target):
                return 1
            b = [x[mid] for x in matrix]
            test = self.binarySearch(b, 0, n - 1, target)
            if (b[test] == target):
                return 1
            mid += 1
        return 0;


if __name__ == '__main__':
    nums = [[1,4,7,11,15],[2,5,8,12,20],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    search = SearchMatrix()
    print(search.searchMatrix(nums, 20))
