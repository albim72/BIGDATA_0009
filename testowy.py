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


#operacja na plikach csv
import csv

#utworzenie pliku csv

with open("osoby.csv","w",encoding="utf-8" ,newline="") as f:
    writer = csv.writer(f)
    #CTRL+D - duplikacja linii/bloku tekstu
    #CTRL+/  - komentowanie/odkomentowanie linii/bloku tekstu
    writer.writerow(['Imię','Nazwisko','Wiek'])
    writer.writerow(['Anna','Kos','23'])
    writer.writerow(['Jan','Kot','52'])
    writer.writerow(['Nadia','Kowal','37'])

#odczyt pliku csv

with open("osoby.csv","r",encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(f"imię: {row[0]}, nazwisko: {row[1]}, wiek: {row[2]}")
