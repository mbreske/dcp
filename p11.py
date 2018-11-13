# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

# # Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

from collections import defaultdict

#O(n^2) space
#O(1) time lookup
def main():
  dictionary = ["dog", "deer", "deal", "cat", "cart", "cars", "bike", "bill", "brat"]
  lookup = buildTrie(dictionary)
  results = lookup.search("ca")
  print (results)

def buildLookup(dictionary):
  lookup = defaultdict(list)
  for word in dictionary:
    for i in range(len(word)):
      lookup[word[:i]].append(word)
  return lookup

def buildTrie(dictionary):
  trie = Trie()
  for word in dictionary:
    trie.insert(word)
  return trie
  
class Node():
  def __init__(self):
    self.value = None
    self.children = {}

class Trie():
  def __init__(self):
    self.root = Node()

  def insert(self, s):
    node = self.root
    newStartIndex = None
    for i,c in enumerate(s):
      if c in node.children:
        node = node.children[c]
      else:
        newStartIndex = i
        break
    
    if newStartIndex is not None:
      for char in s[newStartIndex:]:
        node.children[char] = Node()
        node = node.children[char]
    node.value = s
 
  def getWords(self, node):
    results = []
    for _,v in node.children.items():
      if v.value is not None:
        results.append(v.value)
      results.extend(self.getWords(v))
    return results

  def search(self, query):
    results = []
    node = self.root
    for char in query:
      if char in node.children:
        node = node.children[char]
        if node.value is not None:
          results.append(node.value)
    results.extend(self.getWords(node))
    return results

main()