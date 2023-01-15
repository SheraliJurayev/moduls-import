# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 11:01:38 2023

@author: Sh_Jurayeff
"""

def avto_info(kompaniya,model,rangi,karobka,yili,narhi=None):
    avto={'kompaniya':kompaniya,
          'model':model,
          'rangi':rangi,
          'karobka':karobka,
          'yili':yili,
          'narhi':narhi }    
   
    return avto
    
print("Saytimizdagi mashinalar ro'yxatini shakllantramiz.")
avtolar=[]
while True:
    print("\n Quyidagi ma'lumotlarni kiriting",end="")
    kompaniya=input("Ishlab chiqaruvchi: ")
    model=input("Modeli: ")
    rangi=input("Rangi: ")
    karobka=input("Karobka: ")
    yili=input("Yili: ")
    narhi=input("Narhi: ")
    avtolar.append(avto_info(kompaniya, model, rangi, karobka, yili,narhi))
    javob=input("Yana avto qo'shasizmi? yes/no ")
    
    if javob=='no':
        break
print("\n Salonimizdagi avtolar:")
for avto in avtolar:
    if avto['narhi']:
        narh=avto['narhi']
    else:
        narh="Noma'lum"
    print(f"{avto['rangi'].title()} {avto['model'].title()},{karobka} karobka. Narhi:{narhi}")
    
    
    
    
    
    
    
    