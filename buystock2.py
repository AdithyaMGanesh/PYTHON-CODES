nums=[215, 265, 250, 200, 240, 260, 230]
minval=1000
maxval=0
for i in range(0,len(nums)):
    minval=min(minval,nums[i])
    maxval=max(maxval,nums[i]-minval)
print(maxval)