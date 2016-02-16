#Girrven an array of ints, return True if .. 1, 2, 3, .. appears in the array somewhere. ?

def array123(nums):
 n1 = set(nums)
 if 1 and 2 and 3 in n1:
  return True
  
 return False 


""" here is another with 1,2,3 in sequence

def array123(nums):
  # Note: iterate with length-2, so can use i+1 and i+2 in the loop
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False

"""

