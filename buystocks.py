def price(nums):
    n=len(nums)
    arr=[]
    for i in range(0,n):
        for j in range(i+1,n):
            if nums[i]<nums[j]:
                arr.append(nums[j]-nums[i])
    max_price=max(arr)
    return max_price
"""nums=list(map(int, input().strip("[]").split(", ")))"""
nums= [215, 265, 250, 200, 240, 260, 230]
result=price(nums)
print(result)