def has_no_e(word):
  for character in word:
    if character != 'e':
      return True
  return False
file = open("words.txt")
num = 0
total_words = 113809
for line in file:
  word = line.strip()
  if def has_no_e(word) == True:
    num = num + 1
    print(word)
percentage = num / total_words * 100
print(percentage, '%')
