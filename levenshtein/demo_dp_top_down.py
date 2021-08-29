import os
os.system("cls")
def levenshtein_TopDown_DP(str1, str2, m, n):
  # base case 1
  if m == 0:
    return n
  if n == 0:
    return m
  
  # if this exists in memoi
  if memoi[m][n] is not -1:
    return memoi[m][n]
  
  # base case 2
  if str1[m - 1] is str2[n - 1]:
    if memoi[m-1][n-1] is not -1:
      return memoi[m-1][n-1]
    else:
      memoi[m-1][n-1] = levenshtein_TopDown_DP(str1, str2, m-1, n-1)
      return memoi[m-1][n-1]
  
  # base case 3
  else:
    # insert
    if memoi[m][n-1] is not -1:
      insert = memoi[m][n-1]
    else:
      insert = levenshtein_TopDown_DP(str1, str2, m, n-1)
    # delete
    if memoi[m-1][n] is not -1:
      delete = memoi[m-1][n]
    else:
      delete = levenshtein_TopDown_DP(str1, str2, m-1, n)
    # update
    if memoi[m-1][n-1] is not -1:
      update = memoi[m-1][n-1]
    else:
      update = levenshtein_TopDown_DP(str1, str2, m-1, n-1)
    
    memoi[m][n] = 1+ min(insert, delete, update)
    return memoi[m][n]

# Driver Code
str1 = "cocacola"
str2 = "colacoca"
m = len(str1)
n = len(str2)
memoi = [[-1 for x in range(n + 1)] for i in range(m + 1)]
resu = levenshtein_TopDown_DP(str1, str2, m, n)
for item in memoi:
  print(item)
print("result: ", resu)