# coding:utf-8

import tkinter
import tkinter.messagebox
import os
import os.path
import threading

rubbishExt = ['.tmp', '.bak', '.old', '.wbk', '.xlk', '_mp', '.gid',
              '.chk', '.syd', '.$$$', '.@@@', ".~*"]


def GetDrives():
    drives = []
    for i in range(65, 91):
        vol = chr(i) + ":/"
        if os.path.isdir(vol):
            drives.append(vol)
    return tuple(drives)


class Window:
    def __init__(self):
        self.root = tkinter.Tk()

        # Create menu.
        menu = tkinter.Menu(self.root)

        # Create 'System' submenu
        submenu = tkinter.Menu(menu, tearoff=0)
        submenu.add_command(label="Sobre...", command=self.MenuAbout)
        submenu.add_separator()
        submenu.add_command(label="Sair", command=self.MenuExit)
        menu.add_cascade(label="Sistema", menu=submenu)

        # Create 'Clean' submenu
        submenu = tkinter.Menu(menu, tearoff=0)
        submenu.add_command(label="Varredura", command=self.MenuScanRubbish)
        submenu.add_command(label="Deletar", command=self.MenuDelRubbish)
        menu.add_cascade(label="Limpar", menu=submenu)

        # Create 'Search' submenu
        submenu = tkinter.Menu(menu, tearoff=0)
        submenu.add_command(label="Procurar grandes arquivos",
                            command=self.MenuScanBigFile)
        submenu.add_separator()
        submenu.add_command(label="Procurar grandes arquivos por nomes",
                            command=self.MenuSearchFile)
        menu.add_cascade(label="Procurar", menu=submenu)

        self.root.config(menu=menu)

        # Create labels to show info
        self.progress = tkinter.Label(self.root, anchor=tkinter.W,
                                      text='Status', bitmap='hourglass',
                                      compound='left')
        self.progress.place(x=10, y=370, width=480, height=15)

        # Create text box to show file list
        self.flist = tkinter.Text(self.root)
        self.flist.place(x=10, y=10, width=480, height=350)

        # Create scroll bar for text box
        self.vscroll = tkinter.Scrollbar(self.flist)
        self.vscroll.pack(side='right', fill='y')
        self.flist['yscrollcommand'] = self.vscroll.set
        self.vscroll['command'] = self.flist.yview

    def MainLoop(self):
        self.root.title("A+Cleaner")
        self.root.minsize(500, 400)
        self.root.maxsize(500, 400)
        self.root.mainloop()

    def MenuAbout(self):
        tkinter.messagebox.showinfo("A+Cleaner",
                                    "Este é um programa de limpeza de disco. Bem-vindo a usar e dar" +
                                    " Seu conselho.")

    def MenuExit(self):
        self.root.quit()

    def MenuScanRubbish(self):
        result = tkinter.messagebox.askquestion("A+Cleaner", "Digitalizando" +
                                                "Arquivos inúteis podem custar muito tempo. Continuar?")
        if result == 'no':
            return
        tkinter.messagebox.showinfo("A+Cleaner", "Scaning in no time!")
        # self.ScanRubbish()
        self.drives = GetDrives()
        t = threading.Thread(target=self.ScanRubbish, args=(self.drives,))
        t.start()

    def MenuDelRubbish(self):
        result = tkinter.messagebox.askquestion("A+Cleaner",
                                                "Deleting junk files may cost much time. Continue?")
        if result == 'no':
            return
        tkinter.messagebox.showinfo("A+Cleaner", "Deleting in no time!")
        self.drives = GetDrives()
        t = threading.Thread(target=self.DeleteRubbish, args=(self.drives,))
        t.start()

    def MenuScanBigFile(self):
        result = tkinter.messagebox.askquestion("A+Cleaner",
                                                "Scaning big files may cost much time. Continue?")
        if result == 'no':
            return
        tkinter.messagebox.showinfo("A+Cleaner", "Scaning in no time!")

    def MenuSearchFile(self):
        result = tkinter.messagebox.askquestion("A+Cleaner",
                                                "Searching big files by name may cost much time. Continue?")
        if result == 'no':
            return
        tkinter.messagebox.showinfo("A+Cleaner", "Searching in no time!")

    def ScanRubbish(self, scanpath):
        global rubbishExt
        total = 0
        filesize = 0
        for drive in scanpath:
            for root, dirs, files in os.walk(drive):
                try:
                    for fil in files:
                        filesplit = os.path.splitext(fil)
                        if filesplit[1] == '':
                            continue
                        try:
                            if rubbishExt.index(filesplit[1]) >= 0:
                                fname = os.path.join(
                                    os.path.abspath(root), fil)
                                filesize += os.path.getsize(fname)
                                if total % 20 == 0:
                                    self.flist.delete(0.0, tkinter.END)
                                self.flist.insert(tkinter.END, fname+'\n')
                                l = len(fname)
                                if l > 60:
                                    self.progress['text'] = fname[:30] + '...' + \
                                        fname[l-30:l]
                                else:
                                    self.progress['text'] = fname
                                total += 1
                        except ValueError:
                            pass
                except Exception as e:
                    print(e)
                    pass
        self.progress['text'] = "Find %s junk files, occupy %.2f M disk space" \
            % (total, filesize/1024/1024)

    def DeleteRubbish(self, scanpath):
        global rubbishExt
        total = 0
        filesize = 0
        for drive in scanpath:
            for root, dirs, files in os.walk(drive):
                try:
                    for fil in files:
                        filesplit = os.path.splitext(fil)
                        if filesplit[1] == '':
                            continue
                        try:
                            if rubbishExt.index(filesplit[1]) >= 0:
                                fname = os.path.join(
                                    os.path.abspath(root), fil)
                                filesize += os.path.getsize(fname)
                                try:
                                    os.remove(fname)
                                    l = len(fname)
                                    if l > 50:
                                        fname = fname[:25] + "..." + \
                                            fname[l-25:l]
                                    if total % 15 == 0:
                                        self.flist.delete(0.0, tkinter.END)
                                    self.flist.insert(tkinter.END, 'Deleted '
                                                      + fname + '\n')
                                    self.progress['text'] = fname
                                    total += 1
                                except:
                                    pass
                        except ValueError:
                            pass
                except Exception as e:
                    print(e)
                    pass
        self.progress['text'] = f"Deleted {total} junk files, recover {filesize/1024/1024} M disk space"


if __name__ == "__main__":
    window = Window()
    window.MainLoop()