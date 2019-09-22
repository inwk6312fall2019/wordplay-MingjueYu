def avoid(word, long_forbidden):
  if word in long_forbidden.strip():
    return False
  else:
    return True
file = open("words.txt")
num = 0
forbidden_characters = input("Type forbidden characters: ")
for line in file:
  word = line.strip()
  if avoids(word, forbidden_characters) == True:
        num = num + 1
print(num)
# q,v,y,z,x
