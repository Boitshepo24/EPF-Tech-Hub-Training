#Project Ecler number 2

nterms =0
n1, n2 = 0, 1
count = 0

while nterms < 4000000:
        nterms= n1+n2

        n1 =n2
        n2 =nterms
        if nterms % 2 == 0:
         count += nterms

print(count)

  