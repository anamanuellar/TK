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
from insert_produto import inserirProduto
from select_produto import *
from tkinter.messagebox import showinfo

# Constantes
# Cores: 
#   https://matplotlib.org/stable/gallery/color/named_colors.html
COR_FRAME1 = "azure"
COR_FRAME2 = "turquoise"    
COR_BG_LABEL_FRM1 = "mintcream"
COR_BG_ENTRYS_FRM1 = "azure"
RELEVO=(SUNKEN, GROOVE, RAISED, FLAT, RIDGE, SOLID)

ListaProd:ttk.Treeview

class telaProdutos:

    def __init__(self, root) -> None:
        self.root = root
        self.FrameProdutos()
        self.FrameTabelaProdutos()
        self.LabelsandEntrys()
        self.btnSubmit()
        self.ListaProdutos()
        
    
    def atkInstalado(self) -> bool:
        modulo = "awesometkinter".upper()
        instalados = {pkg.key.upper() for pkg in pkg_resources.working_set}
        return (True if modulo in instalados else False)


    def FrameProdutos(self):
        self.Frame1 = Frame(self.root, bg = COR_FRAME1, relief=RELEVO[0])
        self.Frame1.place(relx = 0.05, rely = 0.05, relwidth=0.9, relheight = 0.4)
    

    def FrameTabelaProdutos(self):
        self.Frame2 = Frame(self.root, bg=COR_FRAME2, bd=3, relief=RELEVO[0] )
        self.Frame2.place(relx = 0.05, rely = 0.47, relwidth=0.9, relheight = 0.4)
    
    # Labels&Entrys
    def LabelsandEntrys(self):  
                       
        descricaoVar = StringVar()
        self.descriptionLb = Label(self.Frame1,text = 'Descrição*', bg = COR_BG_LABEL_FRM1)
        self.descriptionLb.place(relx = 0.05, rely = 0.05)
        self.descriptionEntry = Entry(self.Frame1, bg = COR_BG_ENTRYS_FRM1, textvariable=descricaoVar)
        self.descriptionEntry.place(relx = 0.05, rely = 0.15)

        precoVar = DoubleVar()
        self.priceLB = Label (self.Frame1, text = 'Preço*', bg = COR_BG_LABEL_FRM1)
        self.priceLB.place(relx = 0.55, rely = 0.05)
        self.priceEntry = Entry(self.Frame1, bg = COR_BG_ENTRYS_FRM1, textvariable=precoVar)
        self.priceEntry.place(relx = 0.55, rely = 0.15)
        
        estoqminVar = IntVar()
        self.stockminLB = Label(self.Frame1,text = 'Estoque Mínimo', bg = COR_BG_LABEL_FRM1)
        self.stockminLB.place(relx = 0.05, rely = 0.25)
        self.stockminEntry = Entry(self.Frame1, bg = COR_BG_ENTRYS_FRM1, textvariable=estoqminVar)
        self.stockminEntry.place(relx = 0.05, rely = 0.35)

        estoqmaxVar = IntVar()
        self.stockmaxLB = Label(self.Frame1,text = 'Estoque Atual', bg = COR_BG_LABEL_FRM1)
        self.stockmaxLB.place(relx = 0.55, rely = 0.25)
        self.stockmaxEntry = Entry(self.Frame1, bg = COR_BG_ENTRYS_FRM1, textvariable=estoqmaxVar)
        self.stockmaxEntry.place(relx = 0.55, rely = 0.35)

        self.dateLB = Label(self.Frame1, text = f'{dt.datetime.now():%a,%b,%d,%y}', bg = COR_BG_LABEL_FRM1)
        self.dateLB.place(relx = 0.35, rely = 0.9)
              
        
    def btnSubmit(self):
        '''
        A condicional abaixo permite usar o botão padrão da TkInter ou o
          botão melhorado na biblioteca awesometkinter (atk).
        if self.atkInstalado():
            self.SubmitBtn = atk.Button3d(
                self.Frame1,
                text = 'S u b m i t', 
                bg ='#16878c', 
                command=lambda: inserirProduto([
                    self.NameEntry.get(),
                    self.andressEntry.get(),
                    self.priceEntry.get(),
                    self.stockminEntry.get()
                    self.stockmaxEntry.get()
                ])
            )
            self.SubmitBtn.place(relx = 0.2, rely = 0.74, relwidth=0.1, relheight = 0.05)
        
            self.SubmitBtn2 = atk.Button3d(self.Frame2,text = 'S u b m i t', bg ='#16878c')
            self.SubmitBtn2.place(relx = 0.69, rely = 0.93, relwidth=0.23, relheight = 0.055)
        
        else:
        '''
        self.SubmitBtn = Button(self.Frame1,text = "S a l v a r", 
                        command=lambda: self.salvarProduto([
                            self.descriptionEntry.get(),
                            self.priceEntry.get(),
                            self.stockminEntry.get(),
                            self.stockmaxEntry.get()
                        ]) )
        self.SubmitBtn.place(relx = 0.2, rely = 0.74, relwidth=0.1, relheight = 0.1)


    def limpaCampos(self):
        self.descriptionEntry.delete(0, END)
        self.priceEntry.delete(0, END)
        self.stockminEntry.delete(0, END)
        self.stockmaxEntry.delete(0, END)


    def salvarProduto(self, lista:List):
        inserirProduto(lista)
        self.limpaCampos()        
        '''
            TODO
            O Recurso abaixo foi utilizado para atualização do
            objeto TreeView sempre que um novo registro for
            incluído. Trocar por método mais eficiente, tal como 
            obj.update() ou algo parecido.
        ''' 
        telaProdutos(self.root)


    def selecionarProduto(self, event):
        global ListaProd
        for itemSelecionado in ListaProd.selection():
            item = ListaProd.item(itemSelecionado)
            registro = item['values']
        self.limpaCampos()
        self.descriptionEntry.insert(0, registro[1])
        self.priceEntry.insert(0, registro[2])
        self.stockminEntry.insert(0, registro[3])
        self.stockmaxEntry.insert(0, registro[4])
        self.SubmitBtn['text'] = "A l t e r a r" 
        
        
        
    '''
        O treeview irá gerar eventos virtuais <<TreeviewSelect>>,   <<TreeviewOpen>> e <<TreeviewClose>>, que nos permitem monitorar  as alterações feitas no widget pelos usuários. Podemos usar o    método de seleção para determinar a seleção atual (a seleção   também pode ser alterada no seu programa)
    '''

    # TreeView: Lista os Registros
    '''
        TODO
        Refatorar este código para uma nova Classe (ListaRegistros)
    '''
    def ListaProdutos(self):
        # ScrollBar Vertical
        vScroll = Scrollbar(self.Frame2, orient=VERTICAL)
        vScroll.pack(side=RIGHT, fill=Y)

        # ScrollBar Horizontal
        hScroll = Scrollbar(self.Frame2, orient=HORIZONTAL)
        hScroll.pack(side=BOTTOM, fill=X)
        
        # Cria o Objeto TreeView
        global ListaProd
        ListaProd = ttk.Treeview(self.Frame2, height = 3, 
                    columns = ('#1' , '#2', '#3', '#4', '#5'),
                    show='headings',
                    yscrollcommand=vScroll.set,
                    xscrollcommand=hScroll.set
                    )
        
        for Produto in lista_Produtos():
            ListaProd.insert('', END, values=Produto)

        # Cabeçalho
        ListaProd.heading('#0', text='')
        ListaProd.heading('#1', text='Código', anchor=CENTER)                               
        ListaProd.heading('#2', text='Descrição', anchor=CENTER)
        ListaProd.heading('#3', text='Preço', anchor=CENTER)
        ListaProd.heading('#4', text='Mínimo', anchor=CENTER)
        ListaProd.heading('#5', text='Estoque', anchor=CENTER)
        
        # Colunas
        ListaProd.column("#0", width=0, stretch=NO)
        ListaProd.column("#1", width=80, stretch=NO)
        ListaProd.column("#2", width=200, stretch=YES)
        ListaProd.column("#3", width=200, stretch=YES)
        ListaProd.column("#4", width=200, stretch=YES)
        ListaProd.column("#5", width=200, stretch=YES)
     
      

        ListaProd.place(relx = 0.00, rely = 0.04, relwidth=0.98, relheight = 0.9)

        # Habilita o recurso 'Scroll' Vertical/Horizontal á TreeView
        vScroll.config(command=ListaProd.yview)
        hScroll.config(command=ListaProd.xview)
        
        ListaProd.bind('<<TreeviewSelect>>', self.selecionarProduto)
