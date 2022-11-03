import os
import time
import webbrowser

import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk


Font_tuple = ("Monaco Menlo Consolas", 10, "normal")
# root = tk.Tk()

class App():
    file_name = ''
    extension_file = ''
    path_file = ''

    def __init__(self):
        tk.Tk().withdraw()
        self.path_file = filedialog.askopenfilename(
            title="Selecciona un archivo")
        base_name = os.path.basename(self.path_file).split(".")
        self.file_name = base_name[0]
        self.extension_file = base_name[1]

    def getContent(self):
        file = open(self.path_file, "r")
        content = file.read()
        file.close()
        return content

    def openFile(self):
        tk.Tk().withdraw()
        self.path_file = filedialog.askopenfilename()
        base_name = os.path.basename(self.path_file).split(".")
        self.file_name = base_name[0]
        self.extension_file = base_name[1]

    def go_to_repo(self):
        webbrowser.open('https://github.com/estiven-lg/Dragon-Paper')


class MenuBar(tk.Menu):
    def __init__(self, master):
        super().__init__()
        tk.Menu.__init__(self, master)
        self.configure(background='#151e21', fg='#00c8e0')
        # self.master
        file_menu = tk.Menu(
            self, tearoff=0, background='#151e21', fg='#00c8e0')
        file_menu.add_command(label="Abrir", command=master.openFile)
        file_menu.add_command(
            label="Guardar", command=master.saveFile)
        file_menu.add_command(label="Guardar Como", command=master.saveFileAs)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.quit)

        edit_menu = tk.Menu(
            self, tearoff=0, background='#151e21', fg='#00c8e0')
        edit_menu.add_command(
            label="Deshacer", command=master.inputTxt.edit_undo)
        edit_menu.add_command(
            label="Resacer", command=master.inputTxt.edit_redo)

        help_menu = tk.Menu(
            self, tearoff=0, background='#151e21', fg='#00c8e0')
        help_menu.add_command(label="Informacion", command=master.openInfo)
        help_menu.add_command(label="Manual de Usuario", command=master.openDoc)
        help_menu.add_command(label="Integrantes", command=master.openAuthorInfo)
        help_menu.add_command(label="Repositorio", command=app.go_to_repo)

        self.add_cascade(label="Archivo", menu=file_menu, background='#151e21')
        self.add_cascade(label="Editar", menu=edit_menu, background='#151e21')
        self.add_cascade(label="Ayuda", menu=help_menu, background='#151e21')


class PopupWindowConfirmation:
    def __init__(self, parent):
        self.parent = parent
        self.gui = tk.Toplevel(self.parent)
        self.gui.resizable(False, False)
        self.gui.title("Dragon Paper")
        self.parent.update_idletasks()
        width = 500
        height = 200
        x = (self.parent.winfo_screenwidth() // 4) - (width // 4)
        y = (self.parent.winfo_screenheight() // 4) - (height // 4)
        self.gui.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.gui.wait_visibility()

        self.header = tk.Frame(self.gui, bg="#151e21", width=500, height=100)
        self.header.grid(row=0, column=0, sticky="NW")
        self.header.grid_propagate(0)
        self.header.update()
        self.title = tk.Label(self.header, text="No has guardado el archivo, que deseas hacer?",
                              background='#151e21', fg='#00c8e0')
        self.title.place(x=250, y=50, anchor="center",)

        self.body = tk.Frame(self.gui, bg="#151e21", width=500, height=100)
        self.body.grid(row=1, column=0, sticky="NW")
        self.body.grid_propagate(0)
        self.body.update()

        self.buttonCancel = tk.Button(
            self.body, text="Cancelar",  background='#151e21', fg='#00c8e0', command=self.cancel)
        self.buttonCancel.place(x=25, y=50, anchor="w")
        self.buttonSave = tk.Button(
            self.body, text="Guardar", background='#151e21', fg='#00c8e0', command=self.save)
        self.buttonSave.place(x=275, y=50, anchor="w")
        self.buttonNotSave = tk.Button(
            self.body, text="No Guardar", background='#151e21', fg='#00c8e0', command=self.notSave)
        self.buttonNotSave.place(x=375, y=50, anchor="w")

    def cancel(self):
        self.gui.destroy()

    def save(self):
        self.gui.destroy()
        self.parent.saveFile()
        app.openFile()
        self.parent.title(app.file_name)
        self.parent.path['text'] = app.path_file
        self.parent.inputTxt.delete('1.0', tk.END)
        self.parent.inputTxt.insert("1.0", app.getContent())
        self.parent.inputTxt.edit_reset()
        return 0

    def notSave(self):
        self.gui.destroy()
        app.openFile()
        self.parent.title(app.file_name)
        self.parent.path['text'] = app.path_file
        self.parent.inputTxt.delete('1.0', tk.END)
        self.parent.inputTxt.insert("1.0", app.getContent())
        self.parent.inputTxt.edit_reset()
        return


class PopupWindowInfo:
    def __init__(self, parent):
        super().__init__()
        
        self.parent = parent
        self.gui = tk.Toplevel(self.parent, background="#151e21")
        self.gui.resizable(False, False)
        self.gui.title("Dragon Paper")
        self.parent.update_idletasks()
        width = 600
        height = 200
        x = (self.parent.winfo_screenwidth() // 4) - (width // 4)
        y = (self.parent.winfo_screenheight() // 4) - (height // 4)
        self.gui.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.gui.wait_visibility()

        self.image = tk.Frame(self.gui, bg="#151e21", width=250, height=200)
        self.image.grid(row=0, column=0, sticky="NW")
        self.image.grid_propagate(0)
        self.image.update()

        img = ImageTk.PhotoImage(Image.open(
            "assets/Dragon_icon.png").resize((250, 200)))

        label = tk.Label(self.image, image=img, background="#151e21")
        label.image = img
        label.pack()
        self.Content = tk.Frame(self.gui, bg="#151e21", width=300, height=200)
        self.Content.grid(row=0, column=1, sticky="NW")
        self.Content.grid_propagate(0)
        self.Content.update()

        tk.Label(self.Content,
                 text="Dragon Paper",
                 fg="light green",
                 bg="#151e21",
                 font="Helvetica 16 bold italic").pack()
        tk.Label(self.Content,
                 text="Este programa se distribuye con la esperanza de que sea útilpara modificar y crear archivos de Texto. de mas misma manera intuitivo de usar.",
                 fg="#00c8e0",
                 bg="#151e21",
                 wraplength=300,
                 anchor='w'
                 ).pack(fill='both')
        

        tk.Label(self.Content,
                 text="Dragon Paper es software libre: puede redistribuirlo y/o modificarlo bajo los términos de la Licencia Pública General",
                 fg="#00c8e0",
                 bg="#151e21",
                 wraplength=300,
                 anchor='w'
                 ).pack(fill='both')


class PopupWindowAuthor:
    def __init__(self, parent):
        self.parent = parent
        self.gui = tk.Toplevel(self.parent, background="#151e21")
        self.gui.resizable(False, False)
        self.gui.title("Dragon Paper")
        self.parent.update_idletasks()
        width = 600
        height = 200
        x = (self.parent.winfo_screenwidth() // 4) - (width // 4)
        y = (self.parent.winfo_screenheight() // 4) - (height // 4)
        self.gui.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.gui.wait_visibility()

        self.image = tk.Frame(self.gui, bg="#151e21", width=250, height=200)
        self.image.grid(row=0, column=0, sticky="NW")
        self.image.grid_propagate(0)
        self.image.update()

        img = ImageTk.PhotoImage(Image.open(
            "assets/author.png").resize((250, 200)), format="png")

        label = tk.Label(self.image, image=img, background="#151e21")
        label.image = img
        label.pack()
        self.Content = tk.Frame(self.gui, bg="#151e21", width=300, height=200)
        self.Content.grid(row=0, column=1, sticky="NW")
        self.Content.grid_propagate(0)
        self.Content.update()

        tk.Label(self.Content,
                 text="Nombre:Estiven Joel Laferre Guevara",
                 fg="#00c8e0",
                 bg="#151e21",
                 wraplength=300,
                 anchor='w'
                 ).pack(fill='both')
        
        tk.Label(self.Content,
                 text="Carnet:7690-22-2644",
                 fg="#00c8e0",
                 bg="#151e21",
                 wraplength=300,
                 anchor='w'
                 ).pack(fill='both')
        tk.Label(self.Content,
                 text="No. Grupo canvas :7690-22-2644",
                 fg="#00c8e0",
                 bg="#151e21",
                 wraplength=300,
                 anchor='w'
                 ).pack(fill='both')

class Window(tk.Toplevel):
    pending_save = False

    def __init__(self):
        super().__init__()

        self.geometry("800x600+100+100")
        self.configure(background='#151e21')
        self.title("Dragon File")
        img = tk.Image("photo", file="assets/Dragon_icon.png")
        self.tk.call('wm', 'iconphoto', self._w, img)
        self.path = tk.Label(self, text=app.path_file,
                             background="#151e21", fg='#00c8e0')
        self.path.pack(side=tk.TOP, padx=5, pady=5)

        self.inputTxt = tk.Text(
            self,
            relief=tk.RAISED,
            borderwidth=1,
            background="#151e21",
            fg='#00c8e0',
            font=Font_tuple,
            insertbackground="#00c8e0",
            undo=True,
            maxundo=-2
        )

        def OnKeyPress(e):
            self.pending_save = True
        self.inputTxt.bind("<KeyPress>", OnKeyPress)
        self.inputTxt.insert("1.0", app.getContent())
        self.inputTxt.edit_reset()
        self.inputTxt.pack(fill="both", expand=True, padx=25, pady=25)
        self.config(menu=MenuBar(self))
        self.mainloop()

    def openFile(self):
        if(self.pending_save):
            window = PopupWindowConfirmation(self)
        else:
            app.openFile()
            self.title(app.file_name)
            self.path['text'] = app.path_file
            self.inputTxt.delete('1.0', tk.END)
            self.inputTxt.insert("1.0", app.getContent())
            self.inputTxt.edit_reset()

    def saveFile(self):
        content = self.inputTxt.get("1.0", tk.END)
        file = open(app.path_file, 'w')
        file.write(content)
        file.close
        self.inputTxt.edit_reset()
        self.pending_save = False

    def saveFileAs(self):
        tk.Tk().withdraw()
        path_file = filedialog.asksaveasfilename()
        content = self.inputTxt.get("1.0", tk.END)
        file = open(path_file, 'w')
        file.write(content)
        file.close
        self.inputTxt.edit_reset()
        self.pending_save = False

    def openInfo(self):
        PopupWindowInfo(self)
    def openAuthorInfo(self):
        PopupWindowAuthor(self)
    def openDoc(self):
        webbrowser.open_new('./assets/Doc.pdf')
        
app = App()
root = Window()
