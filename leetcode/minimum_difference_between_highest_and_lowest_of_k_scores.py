from typing import List


def solve(nums: List[int], k: int) -> int:
    if len(nums) <= 1:
        return 0
    
    ans = 0
    for num in nums:
        pass


    


if __name__ == "__main__":
    # nums = [90]
    # k = 1
    # output = 0
    # ans = solve(nums=nums, k=k)
    # print(output, ans)

    # nums = [9,4,1,7]
    # k = 2
    # expected = 2
    # ans = solve(nums=nums, k=k)
    # print(expected, ans)

    # nums = [87063,61094,44530,21297,95857,93551,9918]
    # k = 6
    # expected = 74560
    # ans = solve(nums=nums, k=k)
    # print(expected, ans)

    nums = [41900,69441,94407,37498,20299,10856,36221,2231,54526,79072,84309,76765,92282,13401,44698,17586,98455,47895,98889,65298,32271,23801,83153,12186,7453,79460,67209,54576,87785,47738,40750,31265,77990,93502,50364,75098,11712,80013,24193,35209,56300,85735,3590,24858,6780,50086,87549,7413,90444,12284,44970,39274,81201,43353,75808,14508,17389,10313,90055,43102,18659,20802,70315,48843,12273,78876,36638,17051,20478]
    k = 5
    expected = 1428
    ans = solve(nums=nums, k=k)
    print(expected, ans)
