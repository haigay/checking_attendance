from define import *

class App():
    def __init__(self, window):
        window.title("Meow_Collector")
        window.resizable(False, False)
        
        window.geometry("{}x{}".format(WINDOW_WIDTH, WINDOW_HEIGHT))
        window.iconbitmap(PATH_ICON_IMAGE)
        window.config(background=BG_COLOR)