from models.Music_class.Music import Music

musica1 = Music("Fight for glory", "Two steps from hell", "3:00")
musica2 = Music("Sweet child'o mine", "Guns n roses", "6:00")
musica3 = Music("Ouro de tolo", "Raul Seixas", "12:00")

def main():
    Music.list_musics()

if __name__=='__main__':
    main()