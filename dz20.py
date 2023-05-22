dict=      {1:"АВЕИОРСТ",
            2:"ДКЛМПУ",
            3:"БГЁЬЯ",
            4:"ЙЫ",
           5:"ЗЖХЦЧ",
           8:"ШЭЮ",
           10:"ФЩЪ"}
world=input("Введите слово:").upper()
sum=0
for i in world:
    for key,val in dict.items():
        if i in val:
             sum +=key

print(f"Стоимость слова:{sum}")