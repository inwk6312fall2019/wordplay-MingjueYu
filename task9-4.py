def uses_only(word, characters):
  for letter in word:
    if letter not in characters:
      return False
  return True
file = open("words.txt")
num = 0
for line in file:
  word = line.strip()
  if uses_only(word, 'a c e f h l o') == True:
    print(word)
    num = num + 1
print(num)
# Yes, there are about 188 words meet the requirements and we can select these words to make a sentence
