def uses_all(word, characters):
  required_words = characters.split()
  for letter in required_words:
    if letter not in word:
      return False
  return True
file = open("words.txt")
num = 0
for line in file:
    word = line.strip()
    if uses_all(word, 'a e i o u') == True:
        print(word)
        num = num + 1
print(num)
# How many words are there that use all the vowels aeiou? How about aeiouy?
# 598，42
