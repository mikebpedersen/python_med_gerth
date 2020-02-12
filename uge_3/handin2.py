'''
HANDIN 2 (palindromes)

Afleveringen er lavet af:
    
    201807850 (Jens Trolle)
    201806389 (Mike Pedersen)
    201805266 (Frederik Thaibert)

Reflektion:

Oprindeligt tænkte vi at tjekke for palindromer af længde 7 og 8 først,
også at øge størrelsen på det interval vi tjekkede på med 1 i hver side, hvis
man ikke var nået slutningen af teksten. Vi kom frem til dette, da vi ved
at større palindromer er indeholdt i mindre palindromer.

Vi endte med at bruge en slags "brute-force" metode, men vi stopper allerede
programmet, hvis vi ikke finder et palindrom af længde j + 2, da vi så må have
tjekket alle mulige palindromer. Vi slutter af med at printe alle
palindromerne, vha. join og map(str, <list>).
'''

# Vi bruger koden som Gerth havde lagt inde i opgaven
# til at importere en tekst.
from string import ascii_letters, digits

s = open("saxo.txt").read()
s = s.lower()
s = "".join([c for c in s if c in ascii_letters or c in digits])

# Vi lader j være vores minimumlængde vores palindrom kan have.
j = 7

# Vi definerer en variabel til at være maksimumlængden af vores palindrom på
# et givet tidspunkt.
palindrome_max = j

# Vi laver en tom liste til alle palindromerne
palindromelist = []

print("The text which was input has the following palindromes of size 7",
      "or greater, in order of ascending length: ")

# Vi starter et while-loop, og tjekker om længden vi tjekker er mindre end 
# længden af hele teksten OG at længden vi tjekker - 2, er mindre end længden
# af det længden af det længste palindrom vi har fundet. Hvis vi har fundet et
# palindrom, så bliver det tilføjet til palindromelist, og længden vi har
# brugt til at finde det, bliver sat til at være det samme som palindrome_max.
# Det gør vi for alle værdier af n op til len(s)-j.

while j < len(s) and j - 2 <= palindrome_max:
    for n in range(0, len(s)-j+1):
        if s[n:n+j] == s[n:n+j][::-1]:
            palindromelist.append(s[n:n+j])
            palindrome_max = j
    j += 1

# Vi printer alle palindromerne med kommaer bagved, og slutter med 
# " and <palindrome>."
print(", ".join(map(str, palindromelist[:-1])), end=" ")
print("and", str(palindromelist[-1]), end=".")
