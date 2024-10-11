#!/usr/bin/python3
from typing import List
from typing import Optional

class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    expectedNums = []
    return
 
  def saysomething(str):
    print(str)
    return

  def changeme(mylist):
    print('before: ', mylist)
    mylist[2] = 50
    print('after : ', mylist)
    return

  class ListNode:
    def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

  def testFunction( mynum):
    print('before: ', mynum)
    mynum = 3
    print('after : ', mynum)
    return

  #def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> int:
     linky = ListNode()
     curr = list1._first
     while (curr is not None):
          print(curr.val)
          curr = list1.next
     return 0
     
  #  list3 = []
  #  if (len(list1) > 0):
  #    ctr1 = 0
  #  if (len(list2) > 0):
  ##    ctr2 = 0
  #
  ##  while (ctr1 < len(list1) and ctr2 < len(list2)):
  #    if (list1[ctr1] < list2[ctr2]):
  #      list3.append(list1[ctr1])
  #      ctr1 += 1
  #    elif (list1[ctr1] > list2[ctr2]):
  #      list3.append(list2[ctr2])
  #      ctr2 += 1
  #    else:
  #      list3.append(list1[ctr1])
  #      list3.append(list1[ctr2])
  #      ctr1 += 1
  #      ctr2 += 1
  #  return list3
   
    
##################################################  
  def removeDuplicates(self, nums: List[int]) -> int:
    print(nums) 
    expectedNums = []
    ilen = len(nums)
    if (ilen > 0):
      ilen = len(nums) - 1
      expectedNums.append(nums[0])
      i = 0
      j = 0
    else:
      return []
    
    while (i < ilen):
      if (expectedNums[j] < nums[i]):
       expectedNums.append(nums[i])
       j += 1
      i += 1
    i -= 1
    while j < i:
      expectedNums.append( '_')
      j += 1

    return expectedNums

##################################################  
  def longestCommonPrefix(self, strs: List[str]) -> str:
    longestPrefix = ''

    lenStr = len(strs)
    if (lenStr > 0):
      if (len(strs[0]) > 0):
        lenStr = lenStr -1
      else:
        return ''
    else:
        return ''


    shortestStrs= len(strs[0])
    for i in strs:
      if (len(i) < shortestStrs):
        shortestStrs = len(i)
    shortestStrs -=1

    i = 0
    totmatch = 0
    shortLetter = strs[0][0]

    while i <= shortestStrs:
      totmatch=0
      j = 0
      shortLetter = strs[j][i]
      while j <= lenStr:
        if (shortLetter == strs[j][i:i+1]):
          totmatch += 1
        j +=1
      if (totmatch == (lenStr + 1)):
        longestPrefix = longestPrefix + shortLetter
      else:
        i = i + shortestStrs  ## to break from loop

      i +=1

    
    return longestPrefix
##################################################  


  def convertToTitle(self, columnNumber: int) -> str:
    titleStr = ''
    while (columnNumber > 26):
      carryover = columnNumber % 26
      if (carryover > 0):
        titleStr = chr(int(carryover) +64) + titleStr
        columnNumber = int(columnNumber / 26)
      else:
        titleStr = 'Z' + titleStr
        columnNumber = (columnNumber / 26) - 1
    
    titleStr = ((chr(int(columnNumber) + 64)) + titleStr)
    return titleStr
    
##################################################  
  def romanToInt(self, s: str) -> int:
    romanDict={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    i, ilen, tot = 1, len(s), 0

    curr = romanDict[s[0]]

    while i < ilen:
      if (curr > romanDict[s[i]]):
        tot += curr
        curr = romanDict[s[i]]
 
      elif (curr < romanDict[s[i]]):
        curr = romanDict[s[i]] - curr
      else:
        curr += romanDict[s[i]]
      i += 1

    tot += curr  
    return tot

##################################################  
  def majorityElement(self, nums: List[int]) -> int:
    ElementsDct = {}
    hkey, htot = 0, 0
    for i in nums:
      if i in ElementsDct:
        ElementsDct[i]=ElementsDct[i]+1
      else:
        ElementsDct[i] = 1
      if(ElementsDct[i] > htot):
        htot=ElementsDct[i]
        hkey=i
    
    #for key, val in ElementsDct.items():
    #  if( val >= htot):
    #    hkey=key   
    #    htot=val
    return hkey

##################################################  
  def searchInsert(self, nums: List[int], target: int) -> int:
    i = 0
    pos = 0
    while i < len(nums):
      if(target > nums[i]):
        pos = i
      elif(target <= nums[i]):
        pos = i
        break
      i += 1
    
    if(i == len(nums)):
      return i
    else:
      return pos

##################################################  
  def lengthOfLastWord(self, s:str) -> int:
    wordList = s.split()
    return len(wordList[len(wordList)-1])

##################################################  
  def strStr(self, haystack: str, needle: str) -> int:
    i = 0
    endneedle=len(needle)
    while i < len(haystack):
      if (needle==haystack[i:endneedle]):
        return i
      i +=1
      endneedle+=1
    return -1

##################################################  
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    i = 0
    listlen=len(nums)
    
    for i in range(listlen-1):
      j = i+1
      while j < listlen:
        if(target ==  (nums[i] + nums[j])):
          return([i,j])
        j += 1
  
##################################################  
  def isPalindrome(self,x: int) -> bool:
    strx = str(x)
    if(strx == strx[::-1]):
      return True
    else:
      return False
  
  def isValid(self, s: str) -> bool:
    lstOpen = []
    lstClose = []
    i = 0 
    strlen=len(s)
    if ( (strlen % 2) > 0):
      return False
    while i < strlen:
      if ( s[i] == '{' or s[i] == '(' or s[i] == '['):
        lstOpen.extend(s[i])
      elif ( s[i] == ']' or s[i] == ')' or s[i] == '}'):
        lstClose.extend(s[i])
      else:
        return False
      i += 1
    while i < strlen:
      if ((lstOpen(i) == '[' and lstClose[i] == ']') or  (lstOpen(i) == '{' and lstClose[i] == '}') or  (lstOpen(i) == '(' and lstClose[i] == ')')):
        i += 1
      else:
        return False
    return True

