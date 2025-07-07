def water(heights):
    left,right = 0,len(heights)-1
    left_max,right_max=0,0
    trapped_water=0
    while left<right:
        if heights[left] < heights[right]:
            if heights[left] >= left_max:
                left_max = heights[left]
            else:
                trapped_water += left_max-heights[left]
            left+=1
        else:
            if heights[right] >= right_max:
                right_max = heights[right]
            else:
                trapped_water += right_max-heights[right]
            right-=1
    print(trapped_water)
water([3,1,1,3])
