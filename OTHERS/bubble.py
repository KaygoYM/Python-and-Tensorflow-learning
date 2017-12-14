def bubbleSort(nums):
    for i in range(len(nums)-1):    # 这个循环负责设置冒泡排序进行的次数
        for j in range(len(nums)-i-1):  # ｊ为列表下标
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums
def binarysearch(nums):
    minn=0
    maxn=len(nums)-1
    key=int(input("input:"))
    
    if key in nums:
        while True:
            center=int((maxn+minn)/2)
            if key>nums[center]:
                minn=center+1
            elif key<nums[center]:
                maxn=center-1
            elif key==nums[center]:
                print("the index is "+str(center+1))
                return center+1    
    else:
        print("no such number!")


if __name__=='__main__':
    nums = [5,2,45,6,8,2,1]
    print(bubbleSort(nums))
    binarysearch(nums)
