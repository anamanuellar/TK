from tkinter import *
from menu import *

PERC_LARGURA = 80
PERC_ALTURA = 80
TITULO = "Sistema de Registro e Controle"

win = Tk()
# Janela principal
telaLarg=win.winfo_screenwidth()
telaAlt=win.winfo_screenheight()
win.title(TITULO)
win.configure(background = "#16878c")
win.resizable(True,True)
win.maxsize(width = 1080, height = 720)
win.minsize(width = 600, height = 500)

win.geometry(f"{str(int(telaLarg*(PERC_LARGURA/100)))}x{str(int(telaAlt*(PERC_ALTURA/100)))}")
app = MainMenu(win, TITULO)
win.mainloop()