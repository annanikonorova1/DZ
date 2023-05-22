dict=      {1:"АВЕИОРСТAEIOULNSTR",
            2:"ДКЛМПУDG",
            3:"БГЁЬЯBCMP",
            4:"ЙЫFHVWY",
           5:"ЗЖХЦЧK",
           8:"ШЭЮJX",
           10:"ФЩЪQZ"}
world=input("Введите слово:").upper()
sum=0
for i in world:
    for key,val in dict.items():
        if i in val:
             sum +=key

print(f"Стоимость слова:{sum}")