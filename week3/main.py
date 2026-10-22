
import json

f = open("notes.json", "r")
notes = json.load(f)
f.close()

while True:
    print("1 - Добавить")
    print("2 - Удалить")
    print("3 - Найти")
    print("0 - Выход")

    x = input("Выбери: ")

    if x == "1":
        note = input("Запись: ")
        notes.append(note)

        f = open("notes.json", "w")
        json.dump(notes, f)
        f.close()

        print("Сохранено")

    elif x == "2":
        print(notes)
        n = int(input("Номер: "))
        notes.pop(n)

        f = open("notes.json", "w")
        json.dump(notes, f)
        f.close()

    elif x == "3":
        word = input("Найти: ")

        for i in notes:
            if word in i:
                print(i)

    elif x == "0":
        break
