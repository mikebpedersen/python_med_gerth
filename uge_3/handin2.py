'''

'''

from string import ascii_letters, digits

s = open("saxo.txt").read()
s = s.lower()
s = "".join([c for c in s if c in ascii_letters or c in digits])

j = 7
palindromelist = [j*"a"]

print("The text which was input has the following palindromes, in order of",
      "ascending length: ")

while j < len(s) and j - 3 <= len(max(palindromelist[:])):
    for n in range(0, len(s)-j+1):
        if s[n:n+j] == s[n:n+j][::-1]:
            print(s[n:n+j], end=", ")
            palindromelist.append(s[n:n+j])
    j += 1
