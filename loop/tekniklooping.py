# teknik looping

nama_hero = ['Bruno',
             'Alucard',
             'Jhonson',
             'Saber']

jenis_role = ['Marksman',
              'Fighter',
              'Tank',
              'Assasin']

# enumerate

for index,hero in enumerate(nama_hero):
    print(index,':',hero)

# zip

for nama,role in zip(nama_hero,jenis_role):
    print(nama,'role :',role)