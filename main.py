from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox, filedialog
import subprocess
import os
class Rise_editor:
    def __init__(self,root):
        self.root = root
        self.root.title("Welcome to RiseEditior")
        self.root.geometry("500x500")
        self.root.state('zoomed')
        self.root.iconbitmap('rise.ico')

        self.path_name=''
        self.color_theme = StringVar()

        self.color_theme.set('Light Default')
        self.font_size = 18
        #=====================Menu Icon start =====================

        #craete file icons
        self.new_icon = ImageTk.PhotoImage(file='icons/open.png')
        self.open_icon=ImageTk.PhotoImage(file='icons/new-file.png')
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

        #====================================================== Menu Start =========================================================

        Mymenu = Menu(self.root)

        Filemenu = Menu(Mymenu,tearoff=False)
        Filemenu.add_command(label = '  New File', image=self.new_icon, compound=LEFT, accelerator='Ctl+N', font=('Arial',10), command=self.new_file)
        Filemenu.add_command(label='  Open File', image=self.open_icon, compound=LEFT, accelerator='Ctl+O',font=('Arial', 10), command=self.open_file)
        Filemenu.add_command(label='  Save', image=self.save_icon, compound=LEFT, accelerator='Ctl+S',font=('Arial', 10), command=self.save_file)
        Filemenu.add_command(label='  Save As', image=self.save_as_icon, compound=LEFT, accelerator='Ctl+Alt+S',font=('Arial', 10), command=self.save_as_file)
        Filemenu.add_command(label='  Exit', image=self.exit_icon, compound=LEFT, accelerator='Ctl+Q',font=('Arial', 10), command=self.exit_function)

        Editmenu = Menu(Mymenu, tearoff=False)
        Editmenu.add_command(label=" Cut", image=self.cut_icon, compound=LEFT, font=('Arial', 10), accelerator='Ctrl+X',command=lambda:self.txt_editor.event_generate("&lt;Control x&gt;"))
        Editmenu.add_command(label=' Copy', image=self.copy_icon, compound=LEFT, font=('Arial', 10), accelerator='Ctrl+C',command=lambda:self.txt_editor.event_generate("<Control c>"))
        Editmenu.add_command(label=' Paste', image=self.paste_icon, compound=LEFT, font=('Arial', 10), accelerator='Ctrl+V',command=lambda:self.txt_editor.event_generate("&lt;Control v&gt;"))
        color_theme = Menu(Mymenu, tearoff=False)
        color_theme.add_radiobutton(label='Light Default', value='Light Default', variable=self.color_theme, image=self.light_default, compound=LEFT, command=self.color_change)
        color_theme.add_radiobutton(label='Dark', value='Dark', variable=self.color_theme, image=self.dark, compound=LEFT,command=self.color_change)
        color_theme.add_radiobutton(label='Red', value='Red', variable=self.color_theme, image=self.red, compound=LEFT,command=self.color_change)
        color_theme.add_radiobutton(label='Night Blue', value='Night Blue', variable=self.color_theme, image=self.night_blue, compound=LEFT,command=self.color_change)
        color_theme.add_radiobutton(label='MonoKai', value='MonoKai', variable=self.color_theme,  image=self.monokai, compound=LEFT,command=self.color_change)
        color_theme.add_radiobutton(label='Cocolate', value='Cocolate', variable=self.color_theme, image=self.cocolate, compound=LEFT,command=self.color_change)

        Mymenu.add_cascade(label = 'File', menu=Filemenu)
        Mymenu.add_cascade(label='Edit', menu=Editmenu)
        Mymenu.add_cascade(label='Theme', menu=color_theme)
        Mymenu.add_separator()
        Mymenu.add_command(label = 'Clear', command=self.clear_all)
        Mymenu.add_separator()
        Mymenu.add_command(label = 'Run', command=self.run)
        Mymenu.add_separator()
        Mymenu.add_command(label='Help')
        self.root.config(menu = Mymenu)

        #=================================== Menu End ========================================================



        #===================================input EditorFrame  start ==========================================

        EditorFrame = Frame(self.root, bg="white")
        EditorFrame.place(x=0, y=0, relwidth=1, height=600)

        scrolly = Scrollbar(EditorFrame, orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)

        self.txt_editor = Text(EditorFrame, bg="white", font=('times new roman', self.font_size),yscrollcommand=scrolly.set)
        self.txt_editor.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_editor.yview)

        #===================================input EditorFrame  end ==========================================


        #================================== Output EditorFrame  start ==========================================

        OutputFrame = Frame(self.root, bg="white")
        OutputFrame.place(x=0, y=600, relwidth=1, height=230)

        scrolly = Scrollbar(OutputFrame, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)

        self.txt_output = Text(OutputFrame, bg="white", font=('times new roman', 18), yscrollcommand=scrolly.set)
        self.txt_output.pack(fill=BOTH, expand=1)
        scrolly.config(command=self.txt_output.yview)
        #===================================Output EditorFrame  end ==========================================

        #==========shortcuts key=========================
        self.root.bind('<Control-plus>',self.font_size_inc)
        self.root.bind('<Control-minus>', self.font_size_dec)

        self.root.bind('<Control-o>', self.open_file)
        self.root.bind('<Control-n>', self.new_file)
        self.root.bind('<Control-s>', self.save_file)
        self.root.bind('<Control-Alt-s>', self.save_as_file)
        self.root.bind('<Control-q>', self.exit_function)

#====================================All Function================================================

    def font_size_inc(self, event=None):
        self.font_size+=1
        self.txt_editor.config(font=('times new roman', self.font_size))
    def font_size_dec(self, event=None):
        self.font_size-=1
        self.txt_editor.config(font=('times new roman', self.font_size))

    def run(self):
        if self.path_name=='':
            messagebox.showerror('Error',"Please save the file execute the code", parent=self.root)
        else:
            command = f'python {self.path_name}'
            run_file = subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
            output,error = run_file.communicate()
            self.txt_output.delete('1.0',END)
            self.txt_output.insert('1.0',output)
            self.txt_output.insert('1.0',error)

    def clear_all(self):
        self.txt_editor.delete('1.0',END)
        self.txt_output.delete('1.0', END)

    # change theme function code start
    def color_change(self):
        if self.color_theme.get()=='Light Default':
            self.txt_editor.config(bg='#ffffff', fg='#000000')
            self.txt_output.config(bg='#ffffff', fg='#000000')
        if self.color_theme.get() == 'Dark':
            self.txt_editor.config(bg='#e0e0e0', fg='#474747')
            self.txt_output.config(bg='#e0e0e0', fg='#474747')
        if self.color_theme.get() == 'Red':
            self.txt_editor.config(bg='#ff0000', fg='#ffffff')
            self.txt_output.config(bg='#ff0000', fg='#ffffff')
        if self.color_theme.get() == 'Night Blue':
            self.txt_editor.config(bg='#0000ff', fg='#ffffff')
            self.txt_output.config(bg='#0000ff', fg='#ffffff')
        if self.color_theme.get() == 'MonoKai':
            self.txt_editor.config(bg='#d3b774', fg='#474747')
            self.txt_output.config(bg='#d3b774', fg='#474747')
        if self.color_theme.get() == 'Cocolate':
            self.txt_editor.config(bg='#6b9dc2', fg='#ededed')
            self.txt_output.config(bg='#6b9dc2', fg='#ededed')
    # change theme function code end

    def new_file(self, event=None):
        self.path_name=''
        self.txt_editor.delete('1.0',END)
        self.txt_output.delete('1.0', END)

    def open_file(self, event=None):
        path = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=[('Python Files','*.py')],defaultextension=('.py'))
        if path!='':
            self.path_name=path
            fp = open(self.path_name, 'r')
            data = fp.read()
            self.txt_editor.delete("1.0",END)
            self.txt_editor.insert('1.0', data)
            fp.close()

    def save_file(self, event=None):
        if self.path_name=="":
            self.save_as_file()
        else:
            fp = open(self.path_name,'w')
            fp.write(self.txt_editor.get("1.0", END))
            fp.close()


    def save_as_file(self, event=None):
        path = filedialog.asksaveasfilename(filetypes=[('Python Files','*.py')],defaultextension=('.py'))
        if path!='':
            self.path_name=path
            fp = open(self.path_name, 'w')
            fp.write(self.txt_editor.get("1.0", END))
            fp.close()

    def exit_function(self, event=None):
        self.root.destroy()

root = Tk()
obj = Rise_editor(root)
root.mainloop()