
from tkinter import*
from PIL import ImageTk
from tkinter import messagebox, filedialog
import os
class Rise_editor:
    def __init__(self,root):
        self.root = root
        self.root.title("Welcome to RiseEditior")
        self.root.geometry("500x500")
        self.root.state('zoomed')
        self.root.iconbitmap(r'rise.ico')

        self.path_name = ''
        # =====================Menu Icon start =====================

        # craete file icons
        self.new_icon = ImageTk.PhotoImage(file='icons/open.png')
        self.open_icon = ImageTk.PhotoImage(file='icons/new-file.png')
        self.save_icon = ImageTk.PhotoImage(file='icons/save.png')
        self.save_as_icon = ImageTk.PhotoImage(file='icons/save-as.png')
        self.exit_icon = ImageTk.PhotoImage(file='icons/exit.png')

        self.undo_icon = ImageTk.PhotoImage(file='icons/undo.png')
        self.cut_icon = ImageTk.PhotoImage(file='icons/cut.png')
        self.copy_icon = ImageTk.PhotoImage(file='icons/copy.png')
        self.paste_icon = ImageTk.PhotoImage(file='icons/paste.png')
        self.clear_icon = ImageTk.PhotoImage(file='icons/clear.png')

        self.light_default = ImageTk.PhotoImage(file='icons/light.png')
        self.dark = ImageTk.PhotoImage(file='icons/Dark.png')
        self.red = ImageTk.PhotoImage(file='icons/red.png')
        self.night_blue = ImageTk.PhotoImage(file='icons/blue.png')
        self.monokai = ImageTk.PhotoImage(file='icons/monaki.png')
        self.cocolate = ImageTk.PhotoImage(file='icons/chocolate.png')
        # =====================Menu Icon end =====================

        #======================menu start ========================================

        Mymenu = Menu(self.root)

        Filemenu = Menu(Mymenu, tearoff=False)
        Filemenu.add_command(label='  New File', image=self.new_icon, compound=LEFT, accelerator='Ctl+N', font=('Arial', 10))
        Filemenu.add_command(label='  Open File', image=self.open_icon, compound=LEFT, accelerator='Ctl+O', font=('Arial', 10))
        Filemenu.add_command(label='  Save', image=self.save_icon, compound=LEFT, accelerator='Ctl+S',font=('Arial', 10))
        Filemenu.add_command(label='  Save As', image=self.save_as_icon, compound=LEFT, accelerator='Ctl+Alt+S',font=('Arial', 10), command=self.save_as_file)
        Filemenu.add_command(label='  Exit', image=self.exit_icon, compound=LEFT, accelerator='Ctl+Q',font=('Arial', 10))

        Editmenu = Menu(Mymenu, tearoff=False)
        Editmenu.add_command(label=' Undo', image=self.undo_icon, compound=LEFT, accelerator='Ctl+Z', font=('Arial',10))
        Editmenu.add_command(label=" Cut", image=self.cut_icon, compound=LEFT, accelerator='Ctl+X', font=('Arial', 10))
        Editmenu.add_command(label=' Copy', image=self.copy_icon, compound=LEFT, accelerator='Ctl+C', font=('Arial', 10))
        Editmenu.add_command(label=' Paste', image=self.paste_icon, compound=LEFT, accelerator='Ctl+V', font=('Arial', 10))
        Editmenu.add_command(label=' Clear', image=self.clear_icon, compound=LEFT, accelerator='Ctl+L', font=('Arial', 10))

        color_theme = Menu(Mymenu, tearoff=False)
        color_theme.add_radiobutton(label='Light Default',  image=self.light_default, compound=LEFT)
        color_theme.add_radiobutton(label='Dark',  image=self.dark, compound=LEFT)
        color_theme.add_radiobutton(label='Red',  image=self.red, compound=LEFT)
        color_theme.add_radiobutton(label='Night Blue',  image=self.night_blue, compound=LEFT)
        color_theme.add_radiobutton(label='MonoKai',   image=self.monokai, compound=LEFT)
        color_theme.add_radiobutton(label='Cocolate',  image=self.cocolate, compound=LEFT)

        Mymenu.add_cascade(label='File', menu=Filemenu)
        Mymenu.add_cascade(label='Edit', menu=Editmenu)
        Mymenu.add_cascade(label='Theme', menu=color_theme)
        Mymenu.add_separator()
        Mymenu.add_command(label='Clear')
        Mymenu.add_separator()
        Mymenu.add_command(label='Run')
        Mymenu.add_separator()
        Mymenu.add_command(label='Help')
        self.root.config(menu=Mymenu)

        #======================menu end ========================================

        # ===================================input EditorFrame  start ==========================================

        font_size=18

        EditorFrame = Frame(self.root, bg="white")
        EditorFrame.place(x=0, y=0, relwidth=1, height=600)

        scrolly = Scrollbar(EditorFrame, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)

        self.txt_editor = Text(EditorFrame, bg="white", font=('times new roman',font_size),
                               yscrollcommand=scrolly.set)
        self.txt_editor.pack(fill=BOTH, expand=1)
        scrolly.config(command=self.txt_editor.yview)

        # ===================================input EditorFrame  end ==========================================

        #================================== Output EditorFrame  start ==========================================

        OutputFrame = Frame(self.root, bg="white")
        OutputFrame.place(x=0, y=600, relwidth=1, height=230)

        scrolly = Scrollbar(OutputFrame, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)

        self.txt_output = Text(OutputFrame, bg="white", font=('times new roman', 18), yscrollcommand=scrolly.set)
        self.txt_output.pack(fill=BOTH, expand=1)
        scrolly.config(command=self.txt_output.yview)
        #===================================Output EditorFrame  end ==========================================


    # new file function code start
    def new_file(self, event=None):
        self.path_name=''
        self.txt_editor.delete('1.0',END)
        self.txt_output.delete('1.0', END)
    # new file function code end


    # open file function code start
    def open_file(self, event=None):
        path = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=[('Python Files','*.py')],defaultextension=('.py'))
        if path!='':
            self.path_name=path
            fp = open(self.path_name, 'r')
            data = fp.read()
            self.txt_editor.delete("1.0",END)
            self.txt_editor.insert('1.0', data)
            fp.close()
    # open file function code end

    # save file function code start
    def save_file(self, event=None):
        if self.path_name=="":
            self.save_as_file()
        else:
            fp = open(self.path_name,'w')
            fp.write(self.txt_editor.get("1.0", END))
            fp.close()
    # save file function code end


    #save as file function code start
    def save_as_file(self, event=None):
        path = filedialog.asksaveasfilename(filetypes=[('Python Files','*.py')],defaultextension=('.py')) # open filedailog box
        if path!='':
            self.path_name=path
            fp = open(self.path_name, 'w')
            fp.write(self.txt_editor.get("1.0", END))
            fp.close()
    # save as file function code end


root = Tk()
obj = Rise_editor(root)
root.mainloop()