import json

json_dane = """
{
"name":"Jan Kot",
"age":30,
"city":"Gdańsk",
"is_student":"False",
"last_ids":[23,67,224],
"address":{
        "street":"Złota",
        "local_nb":"6/45"
    }
}
"""

print(type(json_dane))
print(json_dane)

#parsowanie danych -> wyświetlanie danych ze żródła json
try:
    data_dict = json.loads(json_dane)
    print(type(data_dict))
    print(data_dict)

    print("_"*60)

    print("wyświetlenie danych:")
    print(f"Imię i nazwisko: {data_dict['name']}\n"
          f"wiek: {data_dict['age']}\n"
          f"miasto: {data_dict['city']}\n"
          f"czy jest studentem? {data_dict['is_student']}\n"
          f"id zmówień: {data_dict['last_ids']}\n"
          f"ulica: {data_dict['address']['street']}\n"
          f"numer lokalu: {data_dict['address']['local_nb']}\n")

    json_d = json.dumps(data_dict,indent=4)
    with open("zamowienia.json","w",encoding="utf-8") as f:
        f.write(json_d)

    print("_"*60)
    print("odczyt danych z pliku json:")
    with open('zamowienia.json','r',encoding='utf-8') as file:
        data = json.load(file)

    print(data)
    print(type(data))


except json.JSONDecodeError as e:
    print(f"błąd parsowania: {e}")
