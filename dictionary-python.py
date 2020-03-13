#Contoh cara membuat Dictionary pada Python
dict = {'Name' : 'ilham', 'Age': 21, 'Hobby' : 'Fishing'}
print("dict['Name]: ", dict['Name'])
print("dict['Age']: ", dict['Age'])
print("dict['Hobby]: ", dict['Hobby'])
print("\n")

#Update dictionary python
dict = {'Name':'ilham', 'Age':21, 'Hobby':'Fishing'}
dict['Age'] = 22 #mengubah entry yang sudah ada
dict['Name'] = "Ilham Mustofa Pradana" #mengubah entry yang sudah ada
dict['Address'] = "Lampung" #menambahkan entry baru

print("dict['Name]: ", dict['Name'])
print("dict['Age']: ", dict['Age'])
print("dict['Address']: ", dict['Address'])
print("dict['Hobby]: ", dict['Hobby'])
print("\n")

#Contoh cara menghapus pada Dictionary Python

dict = {'Name':'ilham', 'Age':21, 'Hobby':'Fishing'}

del dict['Name'] # hapus entri dengan key 'Name'
dict.clear()     # hapus semua entri di dict
del dict         # hapus dictionary yang sudah ada

#print ("dict['Age']: ", dict['Age'])
#print ("dict['Address']: ", dict['Address'])
