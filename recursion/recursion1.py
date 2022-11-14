# 1) Detect palindromes
#    palidrome: read the same forward or backword
def is_palindrome_loop(word):
  for i in range(len(word) // 2):
    if word[i] != word[len(word) - i - 1]:
      return False
  return True

def is_palindrome_recur(word):
  if len(word) <= 1:
    return True
  return word[0] == word[len(word) - 1] and is_palindrome_recur(word[1:len(word) - 1])
  
# print(is_palindrome_loop("")) # -> True
# print(is_palindrome_loop("a")) # -> True
# print(is_palindrome_loop("aba")) # -> True
# print(is_palindrome_loop("abb")) # -> False
# print(is_palindrome_recur("")) # -> True
# print(is_palindrome_recur("a")) # -> True
# print(is_palindrome_recur("aba")) # -> True
# print(is_palindrome_recur("abb")) # -> False

# 2) Traverse a Nested List:
#    Count the number of integers in the given list
#    Examples:
#      [] -> 0
#      [1]  -> 1
#      [1, 2] -> 2
#      [1, 2, [3, 4, [5]], 6] -> 6
def count_integers_recur(lst):
  count = 0
  for item in lst:
    if type(item) == list:
      count += count_integers_recur(item)
    else:
      count += 1
      
  return count

def count_integers_loop(lst): # Use Stack
  count = 0
  stack = []
  current_list = lst
  i = 0
  
  while True:
    if i == len(current_list):
      if current_list == lst:
        return count
      else:
        current_list, i = stack.pop()
        i += 1
        continue

    if isinstance(current_list[i], list):
      stack.append([current_list, i])
      current_list = current_list[i]
      i = 0
    else:
      count += 1
      i += 1

# 3) An input string is valid if:
#    Open brackets must be closed in the correct order.
#    Every close bracket has a corresponding open bracket
#    Examples:
#       (()()()) -> True
#       ()()()() -> True
#       (())) -> False
#       )( -> False
def is_valid(string):
  stack = []
  for char in string:
    if char == "(":
      stack.append(char)
    else:
      if len(stack) == 0:
        return False
      stack.pop(char)
  if len(stack) == 0:
    return True
  return False