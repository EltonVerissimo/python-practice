class Music:
    nome = ""
    artista = ""
    duracao = ""

musica1 = Music()
musica2 = Music()
musica3 = Music()

musica1.nome = "Fight for glory"
musica1.artista = "Two steps from hell"
musica1.duracao = "3:00"

musica2.nome = "Sweet child'o mine"
musica2.artista = "Guns n roses"
musica2.duracao = "6:00"

musica3.nome = "Ouro de tolo"
musica3.artista = "Raul Seixas"
musica3.duracao = "12:00"

print(musica1.nome)
print(vars(musica1), vars(musica2), vars(musica3))