from .palette import palette

# Subset of css4
class palette(palette):

    def __init__(self):

        self.__source__ = 'basic'

        self.__colours__ = {
              "#ff0000": {"name": "red"},
              "#ffa500": {"name": "orange"},
              "#ffff00": {"name": "yellow"},
              "#7fff00": {"name": "chartreuse"},
              "#008000": {"name": "green"},
              "#00ff7f": {"name": "spring green"},
              "#00ffff": {"name": "cyan"},
              "#1e90ff": {"name": "dodger blue"},
              "#0000ff": {"name": "blue"},
              "#8a2be2": {"name": "blue violet"},
              "#ff00ff": {"name": "magenta"},
              "#ff1493": {"name": "deep pink"},
              "#ffffff": {"name": "white"},
              "#808080": {"name": "grey"},
              "#a52a2a": {"name": "brown"},
              "#000000": {"name": "black"}
            }
