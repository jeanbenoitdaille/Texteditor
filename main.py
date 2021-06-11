from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

class PyEditor:
    def __init__(self, master):
        self.master = master
        self.filename = None

    def create_window(self):
        self.master.title("Nouveau document - Editeur de texte")
        self.master.geometry("1200x700")

    def create_textaera(self):
        self.textaera = Text(self.master, font=("ubuntu", 18))
        self.textaera.pack(side = LEFT, expand = True, fill = BOTH )

        self.scroll = Scrollbar(self.master, command = self.textaera.yview())
        self.textaera.configure(yscrollcommand = self.scroll.set)
        self.scroll.pack(side = RIGHT, fill = Y)

        self.raccourcis()

    def new_document(self, *args):
        if len(self.textaera.get(1.0, END+ '-1c')) >0:
            message_save = messagebox.askyesno("ENREGISTRER", "L'editeur va quitter le document ouvert, voulez vous l'enregistrer ?")

            if message_save >0:
                self.save()
        self.textaera.delete(1.0, END)
        self.filename = None
        self.set_title_window(self.filename)

    def open_document(self, *args):
        if len(self.textaera.get(1.0, END+ '-1c')) >0:
            message_save = messagebox.askyesno("ENREGISTRER", "L'editeur va quitter le document ouvert, voulez vous l'enregistrer avant d'ouvrir un autre document?")

            if message_save >0:
                self.save()
            self.textaera.delete(1.0,END)


        self.filename = filedialog.askopenfilename(initialdir="/", title = "Ouvrir un document",

                                                defaultextension = ".txt",
                                                filetypes = [('Fichier texte', '*.txt'),
                                                             ('Script Python', '*.py'),
                                                             ('Script html', '*.html'),
                                                             ('Script Javascript', '*.js'),
                                                             ('Tous fichiers', '*.*')

                                                ])

        if self.filename:
            try:
                file = open(self.filename, "r")
                fr = file.read()
                file.close()
                self.textaera.insert("1.0", fr)
                self.set_title_window(self.filename)

            except Exception as e:
                messagebox.showerror("Ouvrir document",e)



    def save_as(self, *args):

        try:
            file = filedialog.asksaveasfilename(initialdir="/", title = "Enregistrer sous",
                                                initialfile = "Inserer un nom",
                                                defaultextension = ".txt",
                                                filetypes = [('Fichier texte', '*.txt'),
                                                             ('Script Python', '*.py'),
                                                             ('Script html', '*.html'),
                                                             ('Script Javascript', '*.js'),
                                                             ('Tous fichiers', '*.*')

                                                ])

            content_file = self.textaera.get(1.0, END)
            if file:
                f = open(file, "w")
                f.write(content_file)
                f.close()
                self.filename = file
                self.set_title_window(self.filename)

        except Exception as e:
            messagebox.showerror("Exception", e)

    def save(self, *args):
        if self.filename:

            try:

                content_file = self.textaera.get(1.0, END)
                with open(self.filename, "w") as f:
                    f.write(content_file)

            except Exception as e:
                messagebox.showerror("Exception", e)

        else:
            self.save_as()


    def close_document(self, *args):
        if len(self.textaera.get(1.0, END + '-1c'))>0:
            save = messagebox.askyesno("ENREGISTRER", "Voulez-vous enregistrer votre document?")
            if save <=0:
                self.textaera.quit()
            else:
                self.save()
                self.textaera.quit()
        else:
            self.textaera.quit()



    def copy(self, *args):
        self.textaera.event_generate('<<Copy>>')

    def cut(self, *args):
        self.textaera.event_generate('<<Cut>>')

    def paste(self, *args):
        self.textaera.event_generate('<<Paste>>')

    def selectAll(self, *args):
        self.textaera.event_generate('<<SelectAll>>')

    def set_title_window(self, name=None):
        if name:
            self.master.title(name + " - PyEditor")
        else:
            self.master.title("Nouveau document - Pyeditor")


    def add_menu(self):
        barMenu = Menu(self.master)

        self.master.config(menu = barMenu)

        #Menu Fichier
        filesMenu = Menu(barMenu, font=("ubunto", 14))

        filesMenu.add_command(label="Nouveau document", accelerator= "Ctrl+N", command = self.new_document)
        filesMenu.add_command(label="Ouvrir ",accelerator= "Ctrl+O", command=self.open_document)
        filesMenu.add_separator()
        filesMenu.add_command(label="Enrergistrer sous ",accelerator= "Ctrl+Shift+S", command=self.save_as)
        filesMenu.add_command(label="Enrergistrer ", accelerator= "Ctrl+S",command=self.save)
        filesMenu.add_separator()
        filesMenu.add_command(label="Fermer ", accelerator= "Ctrl+F",command=self.close_document)

        barMenu.add_cascade(label="Fichier", menu = filesMenu)


        #Menu Edition
        editionMenu = Menu(barMenu, font=("ubunto", 14))

        editionMenu.add_command(label="Copier",accelerator= "Ctrl+C", command=self.copy)
        editionMenu.add_command(label="Couper ", accelerator= "Ctrl+X",command=self.cut)
        editionMenu.add_separator()
        editionMenu.add_command(label="Coller ", accelerator= "Ctrl+V",command=self.paste)
        editionMenu.add_separator()
        editionMenu.add_command(label="Selectionner tous ", accelerator="Ctrl+A", command=self.selectAll)

        barMenu.add_cascade(label="Edition", menu=editionMenu)

    def raccourcis(self):
        self.textaera.bind('<Control-n>', self.new_document)
        self.textaera.bind('<Control-o>', self.open_document)
        self.textaera.bind('<Control-s>', self.save)
        self.textaera.bind('<Control-Shift-s>', self.save_as)
        self.textaera.bind('<Control-c>', self.copy)
        self.textaera.bind('<Control-x>', self.cut)
        self.textaera.bind('<Control-v>', self.paste)
        self.textaera.bind('<Control-a>', self.selectAll)



if __name__ == "__main__":
    master = Tk()
    editeur = PyEditor(master)
    editeur.create_window()
    editeur.create_textaera()
    editeur.add_menu()

    master.mainloop()




