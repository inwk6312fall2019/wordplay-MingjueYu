def pairs_word(word):
  count = 0
  index = 0
  while index < len(word) - 1:
    if word[index] == word[index + 1]:
      count = count + 1
      if count == 3:
        return True
      index = index + 2
    else:
      count = 0
      index = index + 1
file = open("words.txt")
num = 0
for line in file:
  word = line.strip()
  if pairs_word(word) == True:
    print(word)
    num = num + 1
print(num)
# We can find 4 words with three consecutive double letters in words.txt
