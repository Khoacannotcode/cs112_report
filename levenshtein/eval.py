import os
import random
from random import choice
from string import ascii_uppercase
import time
import sys
# from Levenshtein import distance as lev
sys.setrecursionlimit(150000)

# gen data
limit_list = [x for x in range(5000) if x%300==0][1:]
quest_list = []
for limit in limit_list:
  m = random.randint(limit/2, limit)
  n = random.randint(limit/2, limit)
  base = ''.join(choice(ascii_uppercase) for i in range(m))
  string_m = base + ''.join(choice(ascii_uppercase) for i in range(m))
  string_n = base + ''.join(choice(ascii_uppercase) for i in range(n))
  quest_list.append([string_m, string_n])


print("max")
for quest in quest_list:
  print(max(len(quest[0]), len(quest[1])))
print("\nm x n")
for quest in quest_list:
  print(len(quest[0]) * len(quest[1]))

def bruteforce(str1, str2, m, n, rank):
  if m == 0:
    return n
  if n == 0:
    return m
  if str1[m-1] == str2[n-1]:
    return bruteforce(str1, str2, m-1, n-1, rank+1)
  # print("\n")
  cost =  1 + min(
                  bruteforce(str1, str2, m, n-1, rank+1),
                  bruteforce(str1, str2, m-1, n, rank+1),
                  bruteforce(str1, str2, m-1, n-1, rank+1)
                )
  return cost

def DP_BU(X, Y):
    (m, n) = (len(X), len(Y))
    T = [[0 for x in range(n + 1)] for y in range(m + 1)]
    for i in range(1, m + 1):
        T[i][0] = i                    # (case 1)
    for j in range(1, n + 1):
        T[0][j] = j                    # (case 1)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:            # (case 2)
                T[i][j] = T[i-1][j-1]
            else:
                T[i][j] = 1 + min(
                                    T[i][j-1],
                                    T[i-1][j],
                                    T[i-1][j-1]
                                )
    return T[m][n]

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

# Driver code
print("")
for quest in quest_list:
  t0 = time.time()
  # brute force
  # bruteforce(quest[0], quest[1], len(quest[0]), len(quest[1]), rank=0)

  # DP bottom up
  DP_BU(quest[0], quest[1])

  # DP top down
  # m = len(quest[0])
  # n = len(quest[1])
  # memoi = [[-1 for x in range(n + 1)] for i in range(m + 1)]
  # levenshtein_TopDown_DP(quest[0], quest[1], m, n)

  # Original levenshtein
  # lev(quest[0], quest[1])

  print(round(time.time() - t0, 4))

# Check accuracy:
for quest in quest_list:
  # brute force
  # resu1 = bruteforce(quest[0], quest[1], len(quest[0]), len(quest[1]), rank=0)

  # DP bottom up
  resu1 = DP_BU(quest[0], quest[1])

  # DP top down
  # m = len(quest[0])
  # n = len(quest[1])
  # memoi = [[-1 for x in range(n + 1)] for i in range(m + 1)]
  # resu1 = levenshtein_TopDown_DP(quest[0], quest[1], m, n)

  resu2 = lev(quest[0], quest[1])
  if resu1 != resu2:
    print("Wrong!")
    break
print("Correct!")