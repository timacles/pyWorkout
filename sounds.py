from PyQt5.QtMultimedia import QSoundEffect
from PyQt5.QtCore import QUrl

class Sounds:
    wav_gameover = 'sounds/gameover.wav'
    wav_select = 'sounds/itemopen.wav'
    wav_delete = 'sounds/exit.wav'
    wav_itemused = 'sounds/itemused.wav'

    def __init__(self, parent=None):
        self.parent = parent

        # iterate over class attributes
        sounds = [k for k in Sounds.__dict__.keys() if k.startswith('wav_')]

        for sound in sounds:
            self.create_sounds_attr(sound)

    def create_sounds_attr(self, name: str):
        """Create attributes for class with all necessarry components.

        Registers the play() sound function to the sound name.
        """

        path = Sounds.__dict__.get(name)
        sound_name = name.strip("wav_")
        sound_class_name = "_" + sound_name

        sound = QSoundEffect(self.parent)
        sound.setSource(QUrl.fromLocalFile(path))

        setattr(self, sound_class_name, sound)
        setattr(self, sound_name, sound.play) 
