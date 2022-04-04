n = int(input())
nums = list(map(int, input().split()))
nums.sort()

if n % 2 == 0:
  print(nums[0] * nums[-1])
elif n % 2 ==1:
  print(nums[int(n//2)]*nums[int(n//2)])
