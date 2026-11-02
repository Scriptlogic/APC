class Media:
    def play(self):
        print("Playing media")


class Audio(Media):
    def play(self):
        print("Playing Audio")


class Video(Media):
    def play(self):
        print("Playing Video")


class Podcast(Media):
    def play(self):
        print("Playing Podcast")


m = Audio()
m.play()

m = Video()
m.play()

m = Podcast()
m.play()