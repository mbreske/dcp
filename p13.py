# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
import sys

def main():
  longestSubstring("abcba", 2)

def longestSubstring(s,k):
  print (generateSubstrings(s, 2))

def generateSubstrings(s,k):
  max = s[0]
  for i in range(len(s)):
    chars = {}
    distinctCount = 0
    prev = ''
    if len(s) - i <= len(max):
      return max
    for j in range(i,len(s)):
      if s[j] not in chars:
        distinctCount += 1
        chars[s[j]] = 1
      if distinctCount > k :
        break
      sub = prev + s[j]
      if len(sub) > len(max):
        max = sub
      prev = sub

main()