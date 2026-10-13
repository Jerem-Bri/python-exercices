temperatures = [12.5, 14, 9.5, 17, 21, 19.5, 11]
L = []
a = 0
b = 0

Minimum = min(temperatures)
maximum = max(temperatures)
print(f" Max : {maximum} / Min : {Minimum}")

for i in temperatures :
    a += i
    b += 1
moy = a/b
moyenne = round(moy, 2)
print(f"Moyenne :{moyenne}")

for i in temperatures :
    if i >= 15 :
        L.append (i)
print (L)

for i, temperatures in enumerate(temperatures):
    print (f"Jour {i} : {temperatures}°C")

