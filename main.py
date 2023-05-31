import tkinter as tk
import tkinter.font as tkFont
from controller import *

# Setting variable name for class
f_controller = controller()


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.title("Film Flix")
        width=613
        height=570
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)
        

        # the container is where we'll stack a bunch of frames on top of each other, then the one we want visible will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (menu_scrn, query_scrn, add_scrn, amend_scrn):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("menu_scrn")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class menu_scrn(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        Title=tk.Label(self)
        ft = tkFont.Font(family='Times',size=48)
        Title["font"] = ft
        Title["fg"] = "#333333"
        Title["justify"] = "center"
        Title["text"] = "Film Flix"
        Title.place(x=0,y=30,width=614,height=53)
        
        Search_menu_btn=tk.Button(self)
        Search_menu_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=14)
        Search_menu_btn["font"] = ft
        Search_menu_btn["fg"] = "#000000"
        Search_menu_btn["justify"] = "center"
        Search_menu_btn["text"] = "Search Film Flix"
        Search_menu_btn.place(x=220,y=150,width=150,height=30)
        Search_menu_btn["command"] = lambda: controller.show_frame("query_scrn")
        
        Add_menu_btn=tk.Button(self)
        Add_menu_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=14)
        Add_menu_btn["font"] = ft
        Add_menu_btn["fg"] = "#000000"
        Add_menu_btn["justify"] = "center"
        Add_menu_btn["text"] = "Add a new film"
        Add_menu_btn.place(x=220,y=200,width=150,height=30)
        Add_menu_btn["command"] = lambda: controller.show_frame("add_scrn")
        
        Quit_btn=tk.Button(self)
        Quit_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=14)
        Quit_btn["font"] = ft
        Quit_btn["fg"] = "#000000"
        Quit_btn["justify"] = "center"
        Quit_btn["text"] = "Quit"
        Quit_btn.place(x=220,y=250,width=150,height=30)
        Quit_btn["command"] = lambda: quit()
        


class query_scrn(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        Title=tk.Label(self)
        ft = tkFont.Font(family='Times',size=48)
        Title["font"] = ft
        Title["fg"] = "#333333"
        Title["justify"] = "center"
        Title["text"] = "Film Flix"
        Title.place(x=0,y=30,width=614,height=53)
        
        Id_label=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        Id_label["font"] = ft
        Id_label["fg"] = "#333333"
        Id_label["justify"] = "center"
        Id_label["text"] = "ID"
        Id_label.place(x=20,y=90,width=70,height=25)

        Id_entry=tk.Entry(self)
        Id_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        Id_entry["font"] = ft
        Id_entry["fg"] = "#333333"
        Id_entry["justify"] = "center"
        Id_entry["text"] = "ID"
        Id_entry.place(x=20,y=120,width=70,height=25)

        Title_label=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        Title_label["font"] = ft
        Title_label["fg"] = "#333333"
        Title_label["justify"] = "center"
        Title_label["text"] = "Title"
        Title_label.place(x=120,y=90,width=70,height=25)

        Title_entry=tk.Entry(self)
        Title_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        Title_entry["font"] = ft
        Title_entry["fg"] = "#333333"
        Title_entry["justify"] = "center"
        Title_entry["text"] = "Title"
        Title_entry.place(x=120,y=120,width=70,height=25)

        Rel_yr_label=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        Rel_yr_label["font"] = ft
        Rel_yr_label["fg"] = "#333333"
        Rel_yr_label["justify"] = "center"
        Rel_yr_label["text"] = "Release year"
        Rel_yr_label.place(x=220,y=90,width=77,height=30)

        Rel_yr_entry=tk.Entry(self)
        Rel_yr_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        Rel_yr_entry["font"] = ft
        Rel_yr_entry["fg"] = "#333333"
        Rel_yr_entry["justify"] = "center"
        Rel_yr_entry["text"] = "release_year"
        Rel_yr_entry.place(x=220,y=120,width=70,height=25)

        Rating_label=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        Rating_label["font"] = ft
        Rating_label["fg"] = "#333333"
        Rating_label["justify"] = "center"
        Rating_label["text"] = "Rating"
        Rating_label.place(x=320,y=90,width=70,height=25)

        Rating_entry=tk.Entry(self)
        Rating_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        Rating_entry["font"] = ft
        Rating_entry["fg"] = "#333333"
        Rating_entry["justify"] = "center"
        Rating_entry["text"] = "rating"
        Rating_entry.place(x=320,y=120,width=70,height=25)

        Duration_label=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        Duration_label["font"] = ft
        Duration_label["fg"] = "#333333"
        Duration_label["justify"] = "center"
        Duration_label["text"] = "Duration"
        Duration_label.place(x=420,y=90,width=70,height=25)

        Duration_entry=tk.Entry(self)
        Duration_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        Duration_entry["font"] = ft
        Duration_entry["fg"] = "#333333"
        Duration_entry["justify"] = "center"
        Duration_entry["text"] = "duration"
        Duration_entry.place(x=420,y=120,width=70,height=25)

        Genre_label=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        Genre_label["font"] = ft
        Genre_label["fg"] = "#333333"
        Genre_label["justify"] = "center"
        Genre_label["text"] = "Genre"
        Genre_label.place(x=520,y=90,width=70,height=25)

        Genre_entry=tk.Entry(self)
        Genre_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        Genre_entry["font"] = ft
        Genre_entry["fg"] = "#333333"
        Genre_entry["justify"] = "center"
        Genre_entry["text"] = "genre"
        Genre_entry.place(x=520,y=120,width=70,height=25)

        Search_btn=tk.Button(self)
        Search_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=14)
        Search_btn["font"] = ft
        Search_btn["fg"] = "#000000"
        Search_btn["justify"] = "center"
        Search_btn["text"] = "Search"
        Search_btn.place(x=230,y=160,width=150,height=30)
        Search_btn["command"] = lambda:self.Search_btn_command()
        
        Results=tk.Entry(self)
        Results["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        Results["font"] = ft
        Results["fg"] = "#333333"
        Results["justify"] = "center"
        Results["text"] = "Entry"
        Results.place(x=10,y=200,width=591,height=261)
        
        Delete_btn=tk.Button(self)
        Delete_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=14)
        Delete_btn["font"] = ft
        Delete_btn["fg"] = "#000000"
        Delete_btn["justify"] = "center"
        Delete_btn["text"] = "Delete"
        Delete_btn.place(x=130,y=470,width=150,height=30)
        Delete_btn["command"] = self.Delete_btn_command

        Amend_btn=tk.Button(self)
        Amend_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=14)
        Amend_btn["font"] = ft
        Amend_btn["fg"] = "#000000"
        Amend_btn["justify"] = "center"
        Amend_btn["text"] = "Amend details"
        Amend_btn.place(x=330,y=470,width=150,height=30)
        Amend_btn["command"] = lambda: controller.show_frame ("amend_scrn")

        Back_btn=tk.Button(self)
        Back_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=14)
        Back_btn["font"] = ft
        Back_btn["fg"] = "#000000"
        Back_btn["justify"] = "center"
        Back_btn["text"] = "Back"
        Back_btn.place(x=220,y=520,width=150,height=30)
        Back_btn["command"] = lambda: controller.show_frame ("menu_scrn")
        
    def Delete_btn_command(self):
        print("command")

    def Search_btn_command(self):
        print("command")
        
        


class add_scrn(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        Title=tk.Label(self)
        ft = tkFont.Font(family='Times',size=48)
        Title["font"] = ft
        Title["fg"] = "#333333"
        Title["justify"] = "center"
        Title["text"] = "Film Flix"
        Title.place(x=0,y=30,width=614,height=53)
                
        Id_label=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        Id_label["font"] = ft
        Id_label["fg"] = "#333333"
        Id_label["justify"] = "left"
        Id_label["text"] = "ID"
        Id_label.place(x=230,y=100,width=70,height=25)

        Id_entry=tk.Entry(self)
        Id_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        Id_entry["font"] = ft
        Id_entry["fg"] = "#333333"
        Id_entry["justify"] = "center"
        Id_entry["text"] = "ID"
        Id_entry.place(x=320,y=100,width=70,height=25)

        Title_label=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        Title_label["font"] = ft
        Title_label["fg"] = "#333333"
        Title_label["justify"] = "left"
        Title_label["text"] = "Title"
        Title_label.place(x=230,y=140,width=70,height=25)

        Title_entry=tk.Entry(self)
        Title_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        Title_entry["font"] = ft
        Title_entry["fg"] = "#333333"
        Title_entry["justify"] = "center"
        Title_entry["text"] = "Title"
        Title_entry.place(x=320,y=140,width=70,height=25)

        Rel_yr_label=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        Rel_yr_label["font"] = ft
        Rel_yr_label["fg"] = "#333333"
        Rel_yr_label["justify"] = "left"
        Rel_yr_label["text"] = "Release year"
        Rel_yr_label.place(x=230,y=180,width=77,height=30)

        Rel_yr_entry=tk.Entry(self)
        Rel_yr_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        Rel_yr_entry["font"] = ft
        Rel_yr_entry["fg"] = "#333333"
        Rel_yr_entry["justify"] = "center"
        Rel_yr_entry["text"] = "release_year"
        Rel_yr_entry.place(x=320,y=180,width=70,height=25)

        Rating_label=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        Rating_label["font"] = ft
        Rating_label["fg"] = "#333333"
        Rating_label["justify"] = "left"
        Rating_label["text"] = "Rating"
        Rating_label.place(x=230,y=220,width=70,height=25)

        Rating_entry=tk.Entry(self)
        Rating_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        Rating_entry["font"] = ft
        Rating_entry["fg"] = "#333333"
        Rating_entry["justify"] = "center"
        Rating_entry["text"] = "rating"
        Rating_entry.place(x=320,y=220,width=70,height=25)

        Duration_label=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        Duration_label["font"] = ft
        Duration_label["fg"] = "#333333"
        Duration_label["justify"] = "left"
        Duration_label["text"] = "Duration"
        Duration_label.place(x=230,y=260,width=70,height=25)

        Duration_entry=tk.Entry(self)
        Duration_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        Duration_entry["font"] = ft
        Duration_entry["fg"] = "#333333"
        Duration_entry["justify"] = "center"
        Duration_entry["text"] = "duration"
        Duration_entry.place(x=320,y=260,width=70,height=25)

        Genre_label=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        Genre_label["font"] = ft
        Genre_label["fg"] = "#333333"
        Genre_label["justify"] = "left"
        Genre_label["text"] = "Genre"
        Genre_label.place(x=230,y=300,width=70,height=25)

        Genre_entry=tk.Entry(self)
        Genre_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        Genre_entry["font"] = ft
        Genre_entry["fg"] = "#333333"
        Genre_entry["justify"] = "center"
        Genre_entry["text"] = "genre"
        Genre_entry.place(x=320,y=300,width=70,height=25)
                
        Add_btn=tk.Button(self)
        Add_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=14)
        Add_btn["font"] = ft
        Add_btn["fg"] = "#000000"
        Add_btn["justify"] = "center"
        Add_btn["text"] = "Add film"
        Add_btn.place(x=220,y=370,width=150,height=30)
        Add_btn["command"] = lambda: self.Add_btn_command(Id_entry.get(), Title_entry.get(), Rel_yr_entry.get(), Rating_entry.get(), Duration_entry.get(), Genre_entry.get())

        Back_btn=tk.Button(self)
        Back_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=14)
        Back_btn["font"] = ft
        Back_btn["fg"] = "#000000"
        Back_btn["justify"] = "center"
        Back_btn["text"] = "Back"
        Back_btn.place(x=220,y=420,width=150,height=30)
        Back_btn["command"] = lambda: controller.show_frame ("menu_scrn")
        
    def Add_btn_command(self, p_film_id, p_title, p_year_released, p_rating, p_duration, p_genre):
        f_controller.add_film(p_film_id, p_title, p_year_released, p_rating, p_duration, p_genre)


class amend_scrn(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        Title=tk.Label(self)
        ft = tkFont.Font(family='Times',size=48)
        Title["font"] = ft
        Title["fg"] = "#333333"
        Title["justify"] = "center"
        Title["text"] = "Film Flix"
        Title.place(x=0,y=30,width=614,height=53)
        
        Results=tk.Entry(self)
        Results["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        Results["font"] = ft
        Results["fg"] = "#333333"
        Results["justify"] = "center"
        Results["text"] = "Entry"
        Results.place(x=10,y=120,width=591,height=30)
        
        Id_label=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        Id_label["font"] = ft
        Id_label["fg"] = "#333333"
        Id_label["justify"] = "center"
        Id_label["text"] = "ID"
        Id_label.place(x=20,y=160,width=70,height=25)

        Id_entry=tk.Entry(self)
        Id_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        Id_entry["font"] = ft
        Id_entry["fg"] = "#333333"
        Id_entry["justify"] = "center"
        Id_entry["text"] = "ID"
        Id_entry.place(x=20,y=190,width=70,height=25)

        Title_label=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        Title_label["font"] = ft
        Title_label["fg"] = "#333333"
        Title_label["justify"] = "center"
        Title_label["text"] = "Title"
        Title_label.place(x=120,y=160,width=70,height=25)

        Title_entry=tk.Entry(self)
        Title_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        Title_entry["font"] = ft
        Title_entry["fg"] = "#333333"
        Title_entry["justify"] = "center"
        Title_entry["text"] = "Title"
        Title_entry.place(x=120,y=190,width=70,height=25)

        Rel_yr_label=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        Rel_yr_label["font"] = ft
        Rel_yr_label["fg"] = "#333333"
        Rel_yr_label["justify"] = "center"
        Rel_yr_label["text"] = "Release year"
        Rel_yr_label.place(x=220,y=160,width=77,height=30)

        Rel_yr_entry=tk.Entry(self)
        Rel_yr_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        Rel_yr_entry["font"] = ft
        Rel_yr_entry["fg"] = "#333333"
        Rel_yr_entry["justify"] = "center"
        Rel_yr_entry["text"] = "release_year"
        Rel_yr_entry.place(x=220,y=190,width=70,height=25)

        Rating_label=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        Rating_label["font"] = ft
        Rating_label["fg"] = "#333333"
        Rating_label["justify"] = "center"
        Rating_label["text"] = "Rating"
        Rating_label.place(x=320,y=160,width=70,height=25)

        Rating_entry=tk.Entry(self)
        Rating_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        Rating_entry["font"] = ft
        Rating_entry["fg"] = "#333333"
        Rating_entry["justify"] = "center"
        Rating_entry["text"] = "rating"
        Rating_entry.place(x=320,y=190,width=70,height=25)

        Duration_label=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        Duration_label["font"] = ft
        Duration_label["fg"] = "#333333"
        Duration_label["justify"] = "center"
        Duration_label["text"] = "Duration"
        Duration_label.place(x=420,y=160,width=70,height=25)

        Duration_entry=tk.Entry(self)
        Duration_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        Duration_entry["font"] = ft
        Duration_entry["fg"] = "#333333"
        Duration_entry["justify"] = "center"
        Duration_entry["text"] = "duration"
        Duration_entry.place(x=420,y=190,width=70,height=25)

        Genre_label=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        Genre_label["font"] = ft
        Genre_label["fg"] = "#333333"
        Genre_label["justify"] = "center"
        Genre_label["text"] = "Genre"
        Genre_label.place(x=520,y=160,width=70,height=25)

        Genre_entry=tk.Entry(self)
        Genre_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        Genre_entry["font"] = ft
        Genre_entry["fg"] = "#333333"
        Genre_entry["justify"] = "center"
        Genre_entry["text"] = "genre"
        Genre_entry.place(x=520,y=190,width=70,height=25)
                
        Amend_btn=tk.Button(self)
        Amend_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=14)
        Amend_btn["font"] = ft
        Amend_btn["fg"] = "#000000"
        Amend_btn["justify"] = "center"
        Amend_btn["text"] = "Amend details"
        Amend_btn.place(x=220,y=250,width=150,height=30)
        Amend_btn["command"] = self.Amend_btn_command

        Back_btn=tk.Button(self)
        Back_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=14)
        Back_btn["font"] = ft
        Back_btn["fg"] = "#000000"
        Back_btn["justify"] = "center"
        Back_btn["text"] = "Back"
        Back_btn.place(x=220,y=300,width=150,height=30)
        Back_btn["command"] = lambda: controller.show_frame ("menu_scrn")
        
    def Amend_btn_command(self):
        print("command")

                

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()