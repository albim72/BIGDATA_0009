#odczyt pliku txt
with open("dane.txt","r",encoding="utf-8") as f:
    zawartosc = f.read()
    print(zawartosc)

print(f.closed)

f = open("dane.txt","r",encoding="utf-8")
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

print(f.closed)

with open("nowedane.txt","w",encoding="utf-8") as f:
    info = "Ładne Słonce, ładny wrzesień.\n 674857 34594395894 39485934\nJola,Kazik,Jan,Maria\n"
    f.write(info)
    f.write("Jeszcze jedna linia tekstu")
