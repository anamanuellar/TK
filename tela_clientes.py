"""
    Algoritmo desenvolvido por José Antonio (Stunt106), 2022
    https://github.com/stun106/
"""
from typing import Optional, List
from tkinter import *
from tkinter import ttk
import datetime as dt 
import pkg_resources
#import awesometkinter as atk
from insert_cliente import inserirCliente
from select_cliente import *
from tkinter.messagebox import showinfo

# Constantes
# Cores: 
#   https://matplotlib.org/stable/gallery/color/named_colors.html
COR_FRAME1 = "azure"
COR_FRAME2 = "turquoise"    
COR_BG_LABEL_FRM1 = "mintcream"
COR_BG_ENTRYS_FRM1 = "azure"
RELEVO=(SUNKEN, GROOVE, RAISED, FLAT, RIDGE, SOLID)

ListaCli:ttk.Treeview

class telaClientes:

    def __init__(self, root) -> None:
        self.root = root
        self.FrameClientes()
        self.FrameTabelaClientes()
        self.LabelsandEntrys()
        self.btnSubmit()
        self.ListaClientes()
        
    
    def atkInstalado(self) -> bool:
        modulo = "awesometkinter".upper()
        instalados = {pkg.key.upper() for pkg in pkg_resources.working_set}
        return (True if modulo in instalados else False)


    def FrameClientes(self):
        self.Frame1 = Frame(self.root, bg = COR_FRAME1, relief=RELEVO[0])
        self.Frame1.place(relx = 0.05, rely = 0.05, relwidth=0.9, relheight = 0.4)
    

    def FrameTabelaClientes(self):
        self.Frame2 = Frame(self.root, bg=COR_FRAME2, bd=3, relief=RELEVO[0] )
        self.Frame2.place(relx = 0.05, rely = 0.47, relwidth=0.9, relheight = 0.4)
    
    # Labels&Entrys
    def LabelsandEntrys(self):  
        nameVar = StringVar()
        self.NameLb = Label(self.Frame1,text = 'Nome*', bg = COR_BG_LABEL_FRM1)
        self.NameLb.place(relx = 0.05, rely = 0.05)
        self.NameEntry = Entry(self.Frame1, bg=COR_BG_ENTRYS_FRM1, textvariable=nameVar)
        self.NameEntry.place(relx = 0.05, rely = 0.15)
        
        addressVar = StringVar()
        self.addressLb = Label(self.Frame1,text = 'Endereço*', bg = COR_BG_LABEL_FRM1)
        self.addressLb.place(relx = 0.55, rely = 0.05)
        self.addressEntry = Entry(self.Frame1, bg = COR_BG_ENTRYS_FRM1, textvariable=addressVar)
        self.addressEntry.place(relx = 0.55, rely = 0.15)

        emailVar = StringVar()
        self.EmailLB = Label (self.Frame1, text = 'Email*', bg = COR_BG_LABEL_FRM1)
        self.EmailLB.place(relx = 0.05, rely = 0.25)
        self.EmailEntry = Entry(self.Frame1, bg = COR_BG_ENTRYS_FRM1, textvariable=emailVar)
        self.EmailEntry.place(relx = 0.05, rely = 0.35)
        
        telVar = StringVar()
        self.TelLB = Label(self.Frame1,text = 'Telefone', bg = COR_BG_LABEL_FRM1)
        self.TelLB.place(relx = 0.55, rely = 0.25)
        self.TelEntry = Entry(self.Frame1, bg = COR_BG_ENTRYS_FRM1, textvariable=telVar)
        self.TelEntry.place(relx = 0.55, rely = 0.35)

        self.dateLB = Label(self.Frame1, text = f'{dt.datetime.now():%a,%b,%d,%y}', bg = COR_BG_LABEL_FRM1)
        self.dateLB.place(relx = 0.35, rely = 0.9)
              
        self.matriculaEntry = Label(self.Frame1, bg = COR_BG_ENTRYS_FRM1)
        self.matriculaEntry.place(relx = 0.05, rely = 0.9,relwidth=0.08, relheight = 0.04)
        

    def btnSubmit(self):
        '''
        A condicional abaixo permite usar o botão padrão da TkInter ou o
          botão melhorado na biblioteca awesometkinter (atk).
        if self.atkInstalado():
            self.SubmitBtn = atk.Button3d(
                self.Frame1,
                text = 'S u b m i t', 
                bg ='#16878c', 
                command=lambda: inserirCliente([
                    self.NameEntry.get(),
                    self.andressEntry.get(),
                    self.EmailEntry.get(),
                    self.TelEntry.get()
                ])
            )
            self.SubmitBtn.place(relx = 0.2, rely = 0.74, relwidth=0.1, relheight = 0.05)
        
            self.SubmitBtn2 = atk.Button3d(self.Frame2,text = 'S u b m i t', bg ='#16878c')
            self.SubmitBtn2.place(relx = 0.69, rely = 0.93, relwidth=0.23, relheight = 0.055)
        
        else:
        '''
        self.SubmitBtn = Button(self.Frame1,text = "S a l v a r", 
                        command=lambda: self.salvarCliente([
                            self.NameEntry.get(),
                            self.addressEntry.get(),
                            self.EmailEntry.get(),
                            self.TelEntry.get()
                        ]) )
        self.SubmitBtn.place(relx = 0.2, rely = 0.74, relwidth=0.1, relheight = 0.1)


    def limpaCampos(self):
        self.NameEntry.delete(0, END)
        self.addressEntry.delete(0, END)
        self.EmailEntry.delete(0, END)
        self.TelEntry.delete(0, END)


    def salvarCliente(self, lista:List):
        inserirCliente(lista)
        self.limpaCampos()        
        '''
            TODO
            O Recurso abaixo foi utilizado para atualização do
            objeto TreeView sempre que um novo registro for
            incluído. Trocar por método mais eficiente, tal como 
            obj.update() ou algo parecido.
        ''' 
        telaClientes(self.root)


    def selecionarCliente(self, event):
        global ListaCli
        for itemSelecionado in ListaCli.selection():
            item = ListaCli.item(itemSelecionado)
            registro = item['values']
        self.limpaCampos()
        self.NameEntry.insert(0, registro[1])
        self.addressEntry.insert(0, registro[2])
        self.EmailEntry.insert(0, registro[3])
        self.TelEntry.insert(0, registro[4])
        self.SubmitBtn['text'] = "A l t e r a r" 
        
        
        
    '''
        O treeview irá gerar eventos virtuais <<TreeviewSelect>>,   <<TreeviewOpen>> e <<TreeviewClose>>, que nos permitem monitorar  as alterações feitas no widget pelos usuários. Podemos usar o    método de seleção para determinar a seleção atual (a seleção   também pode ser alterada no seu programa)
    '''

    # TreeView: Lista os Registros
    '''
        TODO
        Refatorar este código para uma nova Classe (ListaRegistros)
    '''
    def ListaClientes(self):
        # ScrollBar Vertical
        vScroll = Scrollbar(self.Frame2, orient=VERTICAL)
        vScroll.pack(side=RIGHT, fill=Y)

        # ScrollBar Horizontal
        hScroll = Scrollbar(self.Frame2, orient=HORIZONTAL)
        hScroll.pack(side=BOTTOM, fill=X)
        
        # Cria o Objeto TreeView
        global ListaCli
        ListaCli = ttk.Treeview(self.Frame2, height = 3, 
                    columns = ('#1' , '#2', '#3', '#4', '#5'),
                    show='headings',
                    yscrollcommand=vScroll.set,
                    xscrollcommand=hScroll.set
                    )
        
        for cliente in lista_clientes():
            ListaCli.insert('', END, values=cliente)

        # Cabeçalho
        ListaCli.heading('#0', text='')
        ListaCli.heading('#1', text='Matrícula', anchor=CENTER)                               
        ListaCli.heading('#2', text='Nome', anchor=CENTER)
        ListaCli.heading('#3', text='Endereço', anchor=CENTER)
        ListaCli.heading('#4', text='Email', anchor=CENTER)
        ListaCli.heading('#5', text='Telefone', anchor=CENTER)
        
        # Colunas
        ListaCli.column("#0", width=0, stretch=NO)
        ListaCli.column("#1", width=80, stretch=NO)
        ListaCli.column("#2", width=200, stretch=YES)
        ListaCli.column("#3", width=200, stretch=YES)
        ListaCli.column("#4", width=200, stretch=YES)
        ListaCli.column("#5", width=200, stretch=YES)

        ListaCli.place(relx = 0.00, rely = 0.04, relwidth=0.98, relheight = 0.9)

        # Habilita o recurso 'Scroll' Vertical/Horizontal á TreeView
        vScroll.config(command=ListaCli.yview)
        hScroll.config(command=ListaCli.xview)
        
        ListaCli.bind('<<TreeviewSelect>>', self.selecionarCliente)
