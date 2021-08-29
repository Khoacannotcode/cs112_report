import os
os.system("cls")
def leve_Dist(str1, str2, m, n, rank):
  base = "--"
  BASE = "=="
  print(base*rank, "|", '"{}" - "{}"'.format(str1[:m], str2[:n]))
  if m == 0:
    print(base*rank, "|", "return ", n)
    return n
  if n == 0:
    print(base*rank, "|", "return ", m)
    return m
  if str1[m-1] == str2[n-1]:
    print(base*rank, "|", "end = end ")
    return leve_Dist(str1, str2, m-1, n-1, rank+1)
  # print("\n")
  cost =  1 + min(
                  leve_Dist(str1, str2, m, n-1, rank+1),
                  leve_Dist(str1, str2, m-1, n, rank+1),
                  leve_Dist(str1, str2, m-1, n-1, rank+1)
                )
  print(BASE*rank, "|", '"{}" - "{}" ==> cost = {}'.format(str1[:m], str2[:n], cost))
  print("\n")
  return cost

# Driver code
str1 = "cocacola"
str2 = "colacoca"
print(leve_Dist(str1, str2, len(str1), len(str2), rank=0))