from tkinter import *
from Models.cliente import Cliente
from tela_clientes import telaClientes

class MainMenu(Frame):
    def __init__(self, master = None, titulo=''):
        self.master = master
        self.titulo = titulo
        menubar = Menu(master)
          
        cliMenu = Menu(menubar, tearoff=False)
        self.subMenu(cliMenu, "Clientes")
        menubar.add_cascade(label="Clientes", menu=cliMenu, underline=0)
        
        prodMenu = Menu(menubar, tearoff=False)
        self.subMenu(prodMenu, "Produtos")
        menubar.add_cascade(label="Produtos", menu=prodMenu, underline=0)

        fornMenu = Menu(menubar, tearoff=False)
        self.subMenu(fornMenu, "Fornecedores")
        menubar.add_cascade(label="Fornecedores", menu=fornMenu, underline=0)

        confMenu = Menu(menubar, tearoff=False)
        menubar.add_cascade(label="coNfigurações", menu=confMenu, underline=2)
        # add a submenu
        sub_menu = Menu(cliMenu, tearoff=False)
        sub_menu.add_command(label="Parâmetros")
        sub_menu.add_command(label='Temas e Cores')
        confMenu.add_cascade(label="Preferências", menu=sub_menu)
        
        ajudaMenu = Menu(menubar, tearoff=False)
        ajudaMenu.add_command(label="Índice", command=self.nadaFaz)
        ajudaMenu.add_command(label="Sobre...", command=self.nadaFaz)
        ajudaMenu.add_separator()
        ajudaMenu.add_command(label="Teclas de Atalho...", command=self.nadaFaz)
        menubar.add_cascade(label="Ajuda", menu=ajudaMenu)

        sairMenu = Menu(menubar, tearoff=False, activebackground="blue")
        sairMenu.add_command(label="Fechar App...", command=self.sair)
        menubar.add_cascade(label="Sair", menu=sairMenu)    
        
        master.config(menu=menubar)
 
    def subMenu(self, qualMenu, cadastro:str):
        qualMenu.add_command(label="Cadastro", command=lambda: self.Inclusao(cadastro))
        qualMenu.add_separator()
        qualMenu.add_command(label="Relatório", command=self.nadaFaz)
    

    def Inclusao(self, cadastro):
        self.master.title(self.titulo + " - " + cadastro.upper()) 
        if cadastro == "Clientes":
            telaClientes(self.master)
        elif cadastro == "Produtos":
            pass


    def sair(self):
        exit()
    
    def nadaFaz(self):
        button = Button(self.master, text="Reservado para uso Futuro!!")
        button.pack()