import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Film Flix")
        #setting window size
        width=613
        height=570
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_739=tk.Label(root)
        ft = tkFont.Font(family='Times',size=48)
        GLabel_739["font"] = ft
        GLabel_739["fg"] = "#333333"
        GLabel_739["justify"] = "center"
        GLabel_739["text"] = "Film Flix"
        GLabel_739.place(x=0,y=30,width=614,height=53)

        GButton_812=tk.Button(root)
        GButton_812["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=14)
        GButton_812["font"] = ft
        GButton_812["fg"] = "#000000"
        GButton_812["justify"] = "center"
        GButton_812["text"] = "Delete"
        GButton_812.place(x=130,y=470,width=150,height=30)
        GButton_812["command"] = self.GButton_812_command

        GButton_749=tk.Button(root)
        GButton_749["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=14)
        GButton_749["font"] = ft
        GButton_749["fg"] = "#000000"
        GButton_749["justify"] = "center"
        GButton_749["text"] = "Amend details"
        GButton_749.place(x=330,y=470,width=150,height=30)
        GButton_749["command"] = self.GButton_749_command

        GButton_743=tk.Button(root)
        GButton_743["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=14)
        GButton_743["font"] = ft
        GButton_743["fg"] = "#000000"
        GButton_743["justify"] = "center"
        GButton_743["text"] = "Back"
        GButton_743.place(x=220,y=520,width=150,height=30)
        GButton_743["command"] = self.GButton_743_command

        GLineEdit_28=tk.Entry(root)
        GLineEdit_28["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_28["font"] = ft
        GLineEdit_28["fg"] = "#333333"
        GLineEdit_28["justify"] = "center"
        GLineEdit_28["text"] = "Entry"
        GLineEdit_28.place(x=10,y=200,width=591,height=261)

        GButton_643=tk.Button(root)
        GButton_643["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=14)
        GButton_643["font"] = ft
        GButton_643["fg"] = "#000000"
        GButton_643["justify"] = "center"
        GButton_643["text"] = "Search"
        GButton_643.place(x=230,y=160,width=150,height=30)
        GButton_643["command"] = self.GButton_643_command

        GLabel_520=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_520["font"] = ft
        GLabel_520["fg"] = "#333333"
        GLabel_520["justify"] = "center"
        GLabel_520["text"] = "ID"
        GLabel_520.place(x=20,y=90,width=70,height=25)

        GLineEdit_394=tk.Entry(root)
        GLineEdit_394["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_394["font"] = ft
        GLineEdit_394["fg"] = "#333333"
        GLineEdit_394["justify"] = "center"
        GLineEdit_394["text"] = "ID"
        GLineEdit_394.place(x=20,y=120,width=70,height=25)

        GLabel_695=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_695["font"] = ft
        GLabel_695["fg"] = "#333333"
        GLabel_695["justify"] = "center"
        GLabel_695["text"] = "Title"
        GLabel_695.place(x=120,y=90,width=70,height=25)

        GLineEdit_230=tk.Entry(root)
        GLineEdit_230["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_230["font"] = ft
        GLineEdit_230["fg"] = "#333333"
        GLineEdit_230["justify"] = "center"
        GLineEdit_230["text"] = "Title"
        GLineEdit_230.place(x=120,y=120,width=70,height=25)

        GLabel_416=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_416["font"] = ft
        GLabel_416["fg"] = "#333333"
        GLabel_416["justify"] = "center"
        GLabel_416["text"] = "Release year"
        GLabel_416.place(x=220,y=90,width=77,height=30)

        GLineEdit_408=tk.Entry(root)
        GLineEdit_408["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_408["font"] = ft
        GLineEdit_408["fg"] = "#333333"
        GLineEdit_408["justify"] = "center"
        GLineEdit_408["text"] = "release_year"
        GLineEdit_408.place(x=220,y=120,width=70,height=25)

        GLabel_208=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_208["font"] = ft
        GLabel_208["fg"] = "#333333"
        GLabel_208["justify"] = "center"
        GLabel_208["text"] = "Rating"
        GLabel_208.place(x=320,y=90,width=70,height=25)

        GLineEdit_73=tk.Entry(root)
        GLineEdit_73["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_73["font"] = ft
        GLineEdit_73["fg"] = "#333333"
        GLineEdit_73["justify"] = "center"
        GLineEdit_73["text"] = "rating"
        GLineEdit_73.place(x=320,y=120,width=70,height=25)

        GLabel_889=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_889["font"] = ft
        GLabel_889["fg"] = "#333333"
        GLabel_889["justify"] = "center"
        GLabel_889["text"] = "Duration"
        GLabel_889.place(x=420,y=90,width=70,height=25)

        GLineEdit_203=tk.Entry(root)
        GLineEdit_203["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_203["font"] = ft
        GLineEdit_203["fg"] = "#333333"
        GLineEdit_203["justify"] = "center"
        GLineEdit_203["text"] = "duration"
        GLineEdit_203.place(x=420,y=120,width=70,height=25)

        GLabel_674=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_674["font"] = ft
        GLabel_674["fg"] = "#333333"
        GLabel_674["justify"] = "center"
        GLabel_674["text"] = "Genre"
        GLabel_674.place(x=520,y=90,width=70,height=25)

        GLineEdit_906=tk.Entry(root)
        GLineEdit_906["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_906["font"] = ft
        GLineEdit_906["fg"] = "#333333"
        GLineEdit_906["justify"] = "center"
        GLineEdit_906["text"] = "genre"
        GLineEdit_906.place(x=520,y=120,width=70,height=25)

    def GButton_812_command(self):
        print("command")


    def GButton_749_command(self):
        print("command")


    def GButton_743_command(self):
        print("command")


    def GButton_643_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
