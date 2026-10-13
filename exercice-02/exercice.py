def temperatures(n):

    if n < 0:
        return "gel"
    if n < 15:
        return "froid"
    if n < 25:
        return "doux"
    else:
        return "chaud"

print(f"-3°: {temperatures(-3)}")
print(f"0°: {temperatures(0)}")
print(f"15°: {temperatures(15)}")
print(f"31°: {temperatures(31)}")


def bissextile(annee):
  if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
    return "bissextile"
  else:
    return "non bissextile"

print(f"1900: {bissextile(1900)}")
print(f"2000: {bissextile(2000)}")
print(f"2024: {bissextile(2024)}")
