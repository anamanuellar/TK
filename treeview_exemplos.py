"""
    Para fazer algo útil com a visualização em árvore, precisaremos adicionar um ou mais
    itens a ela. Cada item representa um único nó na árvore, seja um nó folha ou um nó interno contendo outros nós. Os itens são referidos por um id exclusivo. Você pode atribuir esse id quando o item for criado pela primeira vez ou o widget pode gerar um automaticamente. Os itens são criados inserindo-os na árvore, usando o método insert do treeview. Para inserir um item, precisamos saber onde inseri-lo. Isso significa especificar o item pai e onde, na lista de filhos existentes do pai, o novo item deve ser inserido. O widget de visualização em árvore cria automaticamente um nó raiz (que não é exibido). Seu id é a string vazia. Ele serve como pai do primeiro nível de itens adicionados. As posições dentro da lista de filhos de um nó são especificadas por índice (0 sendo o primeiro e end significando inserir após todos os filhos existentes). Normalmente, você também especificará o nome de cada item, que é o texto exibido na árvore. Outras opções 
    permitem adicionar uma imagem ao lado do nome, especificar se o nó está aberto ou fechado, etc.
"""
from tkinter import ttk
from tkinter import *
import tkinter as tk
"""
 Nos widgets Tk clássicos, todas as personalizações de aparência exigem a especificação de cada detalhe em widgets individuais, semelhante a sempre usar o atributo 'style' no HTML. Nos widgets Tk temáticos, todas as personalizações de aparência são feitas anexando um estilo a um widget, semelhante ao uso do atributo 'class' em HTML. Separadamente, você define como os widgets com esse estilo aparecerão, semelhante a escrever CSS. Ao contrário do HTML, você não pode misturar e combinar livremente. Você não pode personalizar algumas entradas ou botões temáticos com estilos e outros alterando diretamente as opções de aparência.

"""

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # root window
        self.title('Theme Demo')
        self.geometry('400x300')
        self.style = ttk.Style(self)

        # label
        l = tk.Label()
        
        label = ttk.Label(self, text='Nome:')
        label.grid(column=0, row=0, padx=10, pady=10,  sticky='w')
        # entry
        textbox = ttk.Entry(self)
        textbox.grid(column=1, row=0, padx=10, pady=10,  sticky='w')
        # button
        btn = ttk.Button(self, text='OK', style='Emergency.TButton')
        btn.grid(column=2, row=0, padx=10, pady=10,  sticky='w')

        # radio button
        self.selected_theme = tk.StringVar()
        theme_frame = ttk.LabelFrame(self, text='Temas')
        theme_frame.grid(padx=10, pady=10, ipadx=20, ipady=20, sticky='w')

        for theme_name in self.style.theme_names():
            rb = ttk.Radiobutton(
                theme_frame,
                text=theme_name,
                value=theme_name,
                variable=self.selected_theme,
                command=self.change_theme)
            rb.pack(expand=True, fill='both')

    def change_theme(self):
        self.style.theme_use(self.selected_theme.get())



if __name__ == "__main__":
    app = App()
    app.mainloop()

parent = Tk()

s = ttk.Style()
# Estilos pré embutidos win: 'winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative'

s.theme_use('winnative')
# Podemos obter os nomes de temas incorporados:
print( s.theme_names() )


"""
    A visualização em árvore pode exibir uma ou mais informações adicionais sobre cada item. Eles são mostrados como colunas à direita da exibição da árvore principal. Cada coluna é referenciada por um nome simbólico que atribuímos. Podemos especificar a lista de colunas usando a opção de configuração de colunas do widget treeview, ao criar o widget pela primeira vez ou posteriormente.
"""
tree = ttk.Treeview(parent, columns=('size', 'modified'))
tree['columns'] = ('size', 'modified', 'owner')
"""
    Podemos especificar a largura da coluna, como a exibição das informações do item na coluna é alinhada e muito mais. Também podemos fornecer informações sobre o cabeçalho da coluna, como o texto a ser exibido, uma imagem opcional, alinhamento e um script para invocar quando o item for clicado (por exemplo, para classificar a árvore).
"""
tree.column('size', width=100, anchor='center')
tree.heading('size', text='Size')

# Inserido na raiz, o programa escolhe o id:
tree.insert('', 'end', 'clientes', text='Clientes')
# Inserido abaixo de um nó existente:
tree.insert('clientes', 'end','cli1' ,text='Cliente 1')
# Inserido abaixo de um nó filho já existente:
tree.insert('cli1', 'end', text='Cliente 1.1')
# Inserido ao final de um nó filho já existente:
tree.insert('cli1', 'end', text='Cliente 1.2')
# Mesma coisa, mas inserido como primeiro filho:
tree.insert('', 0, 'tabelas', text='Tabelas')
# Inserido abaixo de um nó existente com ID:
prod = tree.insert('', 'end', text='Produtos')
# Inserindo por ID:
tree.insert(prod, 'end', text='Produto 1')
# Inserindo por ID ao final:
tree.insert(prod, 'end', text='Produto 2')

"""
    O que exibir em cada coluna para cada item pode ser especificado individualmente usando o método 'set'. Você também pode fornecer uma lista descrevendo o que exibir em todas as colunas do item. Isso é feito usando a opção de configuração do item de valores. Ele pode ser usado ao inserir o item pela primeira vez ou para atualizá-lo posteriormente). Leva uma lista de valores. A ordem da lista deve ser igual à ordem na opção de configuração do widget de colunas.
"""
tree.set('clientes', 'size', '12KB')
size = tree.set('clientes', 'size')
tree.insert('', 'end', text='Listbox', values=('15KB', 'Yesterday', 'mark'))


"""
    Assim como os widgets de texto e tela, o widget de visualização em árvore usa tags para modificar a aparência dos itens na árvore. Podemos atribuir uma lista de tags a cada item usando a opção de configuração de itens de tags (novamente, ao criar o item ou posteriormente). As opções de configuração podem ser especificadas na tag, que será aplicada a todos os itens com essa tag. As opções de tag válidas incluem primeiro plano (cor do texto), plano de fundo, fonte e imagem (não usado se o item especificar sua própria imagem). Também podemos criar associações de eventos em tags, o que nos permite capturar cliques de mouse, eventos de teclado, etc.
"""
def clicked(event):
    print( tree.focus() )
    tree.tag_configure('ttk', background='red')

tree.insert('', 'end', text='Botão', tags=('ttk', 'simple'))
tree.tag_configure('ttk', background='yellow')
tree.tag_bind('ttk', '<1>', clicked)
'''
    O treeview irá gerar eventos virtuais <<TreeviewSelect>>, <<TreeviewOpen>> e <<TreeviewClose>>, que nos permitem monitorar as alterações feitas no widget pelos usuários. Podemos usar o método de seleção para determinar a seleção atual (a seleção também pode ser alterada no seu programa)
'''

# the item clicked can be found via tree.focus()

tree.pack()
parent.mainloop()

