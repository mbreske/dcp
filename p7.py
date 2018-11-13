# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

# You can assume that the messages are decodable. For example, '001' is not allowed.

from collections import defaultdict

def main():
  count = countDecodes('111')
  print (count)

#time O(2^n)
#space O(1)
# def countDecodes(str):
#   if len(str) == 0:
#     return 1
#   singleSum = doubleSum = 0
#   if len(str) >= 1:
#     singleSum += countDecodes(str[1:])
#   if len(str) >= 2:
#     if int(str[:2]) <= 26:
#       doubleSum += countDecodes(str[2:])
#   return singleSum + doubleSum

#time O(n)
#space O(n)
#cache[i] = # of ways to encode the substring s[:i]
def countDecodes(s):
  cache = defaultdict(int)
  cache[-1] = 1
  for i in range(len(s)):
    if s[i] == '0':
      cache[i] = 0
    elif i == 0:
      cache[i] == 1
    else:
      if int(s[i:i+2]) <= 26:
        cache[i] = cache[i-2]
    cache[i] += cache[i-1]
  return cache[len(s)-1]

if __name__ == "__main__":
  main()