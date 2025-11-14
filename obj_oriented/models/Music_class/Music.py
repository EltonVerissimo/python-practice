class Music:
    musics = []
    
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Music.musics.append(self)
    
    def __str__(self):
        return f"Nome: {self.nome}, artista: {self.artista}, duração: {self.duracao}"

    def list_musics():
        for music in Music.musics:
            print(f"Nome: {music.nome}, artista: {music.artista}, duração: {music.duracao}")