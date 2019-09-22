def is_abecedarian(word):
  pre_letter = word[0]
  for character in word:
    if ord(character) <ord(pre_letter):
      return False
    pre_letter = character # update letter
  return True
file = open("words.txt")
num = 0
for line in file:
  word = line.strip()
  if is_abecedarian(word) == True:
    print(word)
    num = num + 1
print(num)
# How many abecedarian words?
# 596
