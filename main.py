import tkinter as tk
import tkinter.font as tkFont
from fn_controller import *
from tkinter import ttk

# Setting variable name for class
f_controller = fn_controller()

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.title("Film Flix")
        width=613
        height=620
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)
        

        # the container is where the frames are stacked on top of each other, then the one we want visible will be raised above the others
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

    def get_page(self, classname):
        '''Returns an instance of a page given it's class name as a string'''
        for page in self.frames.values():
            if str(page.__class__.__name__) == classname:
                return page
        return None

class menu_scrn(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        menu_Title=tk.Label(self)
        ft = tkFont.Font(family='Times',size=48)
        menu_Title["font"] = ft
        menu_Title["fg"] = "#333333"
        menu_Title["justify"] = "center"
        menu_Title["text"] = "Film Flix"
        menu_Title.place(x=0,y=30,width=614,height=53)
        
        menu_Search_btn=tk.Button(self)
        menu_Search_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=14)
        menu_Search_btn["font"] = ft
        menu_Search_btn["fg"] = "#000000"
        menu_Search_btn["justify"] = "center"
        menu_Search_btn["text"] = "Search Film Flix"
        menu_Search_btn.place(x=220,y=150,width=150,height=30)
        menu_Search_btn["command"] = lambda: controller.show_frame("query_scrn")
        
        menu_Add_btn=tk.Button(self)
        menu_Add_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=14)
        menu_Add_btn["font"] = ft
        menu_Add_btn["fg"] = "#000000"
        menu_Add_btn["justify"] = "center"
        menu_Add_btn["text"] = "Add a new film"
        menu_Add_btn.place(x=220,y=200,width=150,height=30)
        menu_Add_btn["command"] = lambda: controller.show_frame("add_scrn")
        
        menu_Quit_btn=tk.Button(self)
        menu_Quit_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=14)
        menu_Quit_btn["font"] = ft
        menu_Quit_btn["fg"] = "#000000"
        menu_Quit_btn["justify"] = "center"
        menu_Quit_btn["text"] = "Quit"
        menu_Quit_btn.place(x=220,y=250,width=150,height=30)
        menu_Quit_btn["command"] = lambda: quit()
        


class query_scrn(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        query_Title=tk.Label(self)
        ft = tkFont.Font(family='Times',size=48)
        query_Title["font"] = ft
        query_Title["fg"] = "#333333"
        query_Title["justify"] = "center"
        query_Title["text"] = "Film Flix"
        query_Title.place(x=0,y=30,width=614,height=53)
        
        query_Id_label=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        query_Id_label["font"] = ft
        query_Id_label["fg"] = "#333333"
        query_Id_label["justify"] = "center"
        query_Id_label["text"] = "ID"
        query_Id_label.place(x=20,y=90,width=70,height=25)

        query_Id_entry=tk.Entry(self)
        query_Id_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        query_Id_entry["font"] = ft
        query_Id_entry["fg"] = "#333333"
        query_Id_entry["justify"] = "center"
        query_Id_entry["text"] = ""
        query_Id_entry.place(x=20,y=120,width=70,height=25)

        query_Title_label=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        query_Title_label["font"] = ft
        query_Title_label["fg"] = "#333333"
        query_Title_label["justify"] = "center"
        query_Title_label["text"] = "Title"
        query_Title_label.place(x=120,y=90,width=70,height=25)

        query_Title_entry=tk.Entry(self)
        query_Title_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        query_Title_entry["font"] = ft
        query_Title_entry["fg"] = "#333333"
        query_Title_entry["justify"] = "center"
        query_Title_entry["text"] = ""
        query_Title_entry.place(x=120,y=120,width=70,height=25)

        query_Rel_yr_label=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        query_Rel_yr_label["font"] = ft
        query_Rel_yr_label["fg"] = "#333333"
        query_Rel_yr_label["justify"] = "center"
        query_Rel_yr_label["text"] = "Release year"
        query_Rel_yr_label.place(x=220,y=90,width=77,height=30)

        query_Rel_yr_entry=tk.Entry(self)
        query_Rel_yr_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        query_Rel_yr_entry["font"] = ft
        query_Rel_yr_entry["fg"] = "#333333"
        query_Rel_yr_entry["justify"] = "center"
        query_Rel_yr_entry["text"] = ""
        query_Rel_yr_entry.place(x=220,y=120,width=70,height=25)

        query_Rating_label=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        query_Rating_label["font"] = ft
        query_Rating_label["fg"] = "#333333"
        query_Rating_label["justify"] = "center"
        query_Rating_label["text"] = "Rating"
        query_Rating_label.place(x=320,y=90,width=70,height=25)

        query_Rating_entry=tk.Entry(self)
        query_Rating_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        query_Rating_entry["font"] = ft
        query_Rating_entry["fg"] = "#333333"
        query_Rating_entry["justify"] = "center"
        query_Rating_entry["text"] = ""
        query_Rating_entry.place(x=320,y=120,width=70,height=25)

        query_Duration_label=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        query_Duration_label["font"] = ft
        query_Duration_label["fg"] = "#333333"
        query_Duration_label["justify"] = "center"
        query_Duration_label["text"] = "Duration"
        query_Duration_label.place(x=420,y=90,width=70,height=25)

        query_Duration_entry=tk.Entry(self)
        query_Duration_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        query_Duration_entry["font"] = ft
        query_Duration_entry["fg"] = "#333333"
        query_Duration_entry["justify"] = "center"
        query_Duration_entry["text"] = ""
        query_Duration_entry.place(x=420,y=120,width=70,height=25)

        query_Genre_label=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        query_Genre_label["font"] = ft
        query_Genre_label["fg"] = "#333333"
        query_Genre_label["justify"] = "center"
        query_Genre_label["text"] = "Genre"
        query_Genre_label.place(x=520,y=90,width=70,height=25)

        query_Genre_entry=tk.Entry(self)
        query_Genre_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        query_Genre_entry["font"] = ft
        query_Genre_entry["fg"] = "#333333"
        query_Genre_entry["justify"] = "center"
        query_Genre_entry["text"] = ""
        query_Genre_entry.place(x=520,y=120,width=70,height=25)

        query_Search_btn=tk.Button(self)
        query_Search_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=14)
        query_Search_btn["font"] = ft
        query_Search_btn["fg"] = "#000000"
        query_Search_btn["justify"] = "center"
        query_Search_btn["text"] = "Search"
        query_Search_btn.place(x=230,y=160,width=150,height=30)
        query_Search_btn["command"] = lambda:self.query_Search_btn_command(query_Id_entry.get(), query_Title_entry.get(),  query_Rel_yr_entry.get(), query_Rating_entry.get(), query_Duration_entry.get(), query_Genre_entry.get(), query_Results, query_Message)
        
        query_Results=ttk.Treeview(self, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings', height=8)
        # Results["borderwidth"] = "1px"
        # ft = tkFont.Font(family='Times',size=10)
        # Results["font"] = ft
        # Results["fg"] = "#333333"
        # Results["justify"] = "center"
        # Results["text"] = "Entry"
        query_Results.place(x=10,y=200,width=590,height=261)
        query_Results.column("# 1", anchor="center", minwidth=0, width=50)
        query_Results.heading("# 1", text="Film ID")
        query_Results.column("# 2", anchor="center", minwidth=0, width=235)
        query_Results.heading("# 2", text="Title")
        query_Results.column("# 3", anchor="center", minwidth=0, width=90)
        query_Results.heading("# 3", text="Release year")
        query_Results.column("# 4", anchor="center", minwidth=0, width=60)
        query_Results.heading("# 4", text="Rating")
        query_Results.column("# 5", anchor="center", minwidth=0, width=60)
        query_Results.heading("# 5", text="Duration")
        query_Results.column("# 6", anchor="center", minwidth=0, width=93)
        query_Results.heading("# 6", text="Genre")
        
        query_Message=tk.Label(self)
        ft = tkFont.Font(family='Times',size=14)
        query_Message["font"] = ft
        query_Message["fg"] = "#cc0000"
        query_Message["justify"] = "center"
        query_Message["text"] = ""
        query_Message.place(x=0,y=470,width=613,height=30)
                
        query_Delete_btn=tk.Button(self)
        query_Delete_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=14)
        query_Delete_btn["font"] = ft
        query_Delete_btn["fg"] = "#000000"
        query_Delete_btn["justify"] = "center"
        query_Delete_btn["text"] = "Delete"
        query_Delete_btn.place(x=130,y=520,width=150,height=30)
        query_Delete_btn["command"] = lambda: self.query_Delete_btn_command(query_Id_entry.get(), query_Title_entry.get(),  query_Rel_yr_entry.get(), query_Rating_entry.get(), query_Duration_entry.get(), query_Genre_entry.get(), query_Results, query_Message)

        query_Amend_btn=tk.Button(self)
        query_Amend_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=14)
        query_Amend_btn["font"] = ft
        query_Amend_btn["fg"] = "#000000"
        query_Amend_btn["justify"] = "center"
        query_Amend_btn["text"] = "Amend details"
        query_Amend_btn.place(x=330,y=520,width=150,height=30)
        query_Amend_btn["command"] = lambda: self.query_Amend_btn_command(controller, query_Results, query_Message)

        query_Back_btn=tk.Button(self)
        query_Back_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=14)
        query_Back_btn["font"] = ft
        query_Back_btn["fg"] = "#000000"
        query_Back_btn["justify"] = "center"
        query_Back_btn["text"] = "Back"
        query_Back_btn.place(x=220,y=570,width=150,height=30)
        query_Back_btn["command"] = lambda: self.query_Back_btn_command(controller, query_Id_entry, query_Title_entry,  query_Rel_yr_entry, query_Rating_entry, query_Duration_entry, query_Genre_entry)
    
    def query_Amend_btn_command(self, controller, p_Results, message):
        # Get selected item to Edit
        selected_item = p_Results.focus()
        # Data validation to ensure a film is selected
        if selected_item == "":
            message["fg"] = "#cc0000"
            message["text"] = "Please select a film to amend"
            message.after(3000,lambda: f_controller.remove_message(message))
        else:
            selected_item = p_Results.item(selected_item)
            selected_item = selected_item["values"]
            
            amend_page = self.controller.get_page("amend_scrn")
            amend_page.amend_Results.delete(*amend_page.amend_Results.get_children())
            amend_page.amend_Results.insert('', 'end', text="1", values=selected_item)

            controller.show_frame ("amend_scrn")
        
    def query_Delete_btn_command(self, p_film_id, p_title, p_year_released, p_rating, p_duration, p_genre, p_results, message):
        # Get selected item to Delete
        deleted_item = p_results.focus()
        # Data validation to ensure a film is selected
        if deleted_item == "":
            message["fg"] = "#cc0000"
            message["text"] = "Please select a film to delete"
            message.after(3000,lambda: f_controller.remove_message(message))
        else:
            deleted_item = p_results.item(deleted_item)
            deleted_item = deleted_item["values"]
            f_controller.delete(deleted_item, message)
            p_results.delete(*p_results.get_children())
            f_controller.query(p_film_id, p_title, p_year_released, p_rating, p_duration, p_genre, p_results)

    def query_Search_btn_command(self, p_film_id, p_title, p_year_released, p_rating, p_duration, p_genre, p_Results, message):
        p_Results.delete(*p_Results.get_children())
        f_controller.query(p_film_id, p_title, p_year_released, p_rating, p_duration, p_genre, p_Results, message)

    def query_Back_btn_command(self, controller, p2_film_id, p2_title, p2_year_released, p2_rating, p2_duration, p2_genre):
        boxes = [p2_film_id, p2_title, p2_year_released, p2_rating, p2_duration, p2_genre]
        for i in boxes:
            i.delete(0, tk.END)
        controller.show_frame ("menu_scrn")


class add_scrn(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        add_Title=tk.Label(self)
        ft = tkFont.Font(family='Times',size=48)
        add_Title["font"] = ft
        add_Title["fg"] = "#333333"
        add_Title["justify"] = "center"
        add_Title["text"] = "Film Flix"
        add_Title.place(x=0,y=30,width=614,height=53)
                
        add_Id_label=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        add_Id_label["font"] = ft
        add_Id_label["fg"] = "#333333"
        add_Id_label["justify"] = "left"
        add_Id_label["text"] = "ID"
        add_Id_label.place(x=230,y=100,width=70,height=25)

        add_Id_entry=tk.Entry(self)
        add_Id_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        add_Id_entry["font"] = ft
        add_Id_entry["fg"] = "#333333"
        add_Id_entry["justify"] = "center"
        add_Id_entry["text"] = ""
        add_Id_entry.place(x=320,y=100,width=70,height=25)

        add_Title_label=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        add_Title_label["font"] = ft
        add_Title_label["fg"] = "#333333"
        add_Title_label["justify"] = "left"
        add_Title_label["text"] = "Title"
        add_Title_label.place(x=230,y=140,width=70,height=25)

        add_Title_entry=tk.Entry(self)
        add_Title_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        add_Title_entry["font"] = ft
        add_Title_entry["fg"] = "#333333"
        add_Title_entry["justify"] = "center"
        add_Title_entry["text"] = ""
        add_Title_entry.place(x=320,y=140,width=70,height=25)

        add_Rel_yr_label=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        add_Rel_yr_label["font"] = ft
        add_Rel_yr_label["fg"] = "#333333"
        add_Rel_yr_label["justify"] = "left"
        add_Rel_yr_label["text"] = "Release year"
        add_Rel_yr_label.place(x=230,y=180,width=77,height=30)

        add_Rel_yr_entry=tk.Entry(self)
        add_Rel_yr_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        add_Rel_yr_entry["font"] = ft
        add_Rel_yr_entry["fg"] = "#333333"
        add_Rel_yr_entry["justify"] = "center"
        add_Rel_yr_entry["text"] = ""
        add_Rel_yr_entry.place(x=320,y=180,width=70,height=25)

        add_Rating_label=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        add_Rating_label["font"] = ft
        add_Rating_label["fg"] = "#333333"
        add_Rating_label["justify"] = "left"
        add_Rating_label["text"] = "Rating"
        add_Rating_label.place(x=230,y=220,width=70,height=25)

        add_Rating_entry=tk.Entry(self)
        add_Rating_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        add_Rating_entry["font"] = ft
        add_Rating_entry["fg"] = "#333333"
        add_Rating_entry["justify"] = "center"
        add_Rating_entry["text"] = ""
        add_Rating_entry.place(x=320,y=220,width=70,height=25)

        add_Duration_label=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        add_Duration_label["font"] = ft
        add_Duration_label["fg"] = "#333333"
        add_Duration_label["justify"] = "left"
        add_Duration_label["text"] = "Duration"
        add_Duration_label.place(x=230,y=260,width=70,height=25)

        add_Duration_entry=tk.Entry(self)
        add_Duration_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        add_Duration_entry["font"] = ft
        add_Duration_entry["fg"] = "#333333"
        add_Duration_entry["justify"] = "center"
        add_Duration_entry["text"] = ""
        add_Duration_entry.place(x=320,y=260,width=70,height=25)

        add_Genre_label=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        add_Genre_label["font"] = ft
        add_Genre_label["fg"] = "#333333"
        add_Genre_label["justify"] = "left"
        add_Genre_label["text"] = "Genre"
        add_Genre_label.place(x=230,y=300,width=70,height=25)

        add_Genre_entry=tk.Entry(self)
        add_Genre_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        add_Genre_entry["font"] = ft
        add_Genre_entry["fg"] = "#333333"
        add_Genre_entry["justify"] = "center"
        add_Genre_entry["text"] = ""
        add_Genre_entry.place(x=320,y=300,width=70,height=25)
        
        add_Message=tk.Label(self)
        ft = tkFont.Font(family='Times',size=14)
        add_Message["font"] = ft
        add_Message["fg"] = "#00cc22"
        add_Message["justify"] = "center"
        add_Message["text"] = ""
        add_Message.place(x=0,y=350,width=613,height=30)
                
        add_Add_btn=tk.Button(self)
        add_Add_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=14)
        add_Add_btn["font"] = ft
        add_Add_btn["fg"] = "#000000"
        add_Add_btn["justify"] = "center"
        add_Add_btn["text"] = "Add film"
        add_Add_btn.place(x=230,y=400,width=150,height=30)
        add_Add_btn["command"] = lambda: self.add_Add_btn_command(add_Id_entry.get(), add_Title_entry.get(), add_Rel_yr_entry.get(), add_Rating_entry.get(), add_Duration_entry.get(), add_Genre_entry.get(), add_Id_entry, add_Title_entry, add_Rel_yr_entry, add_Rating_entry, add_Duration_entry, add_Genre_entry, add_Message)

        add_Back_btn=tk.Button(self)
        add_Back_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=14)
        add_Back_btn["font"] = ft
        add_Back_btn["fg"] = "#000000"
        add_Back_btn["justify"] = "center"
        add_Back_btn["text"] = "Back"
        add_Back_btn.place(x=230,y=450,width=150,height=30)
        add_Back_btn["command"] = lambda: self.add_Back_btn_command(controller, add_Id_entry, add_Title_entry, add_Rel_yr_entry, add_Rating_entry, add_Duration_entry, add_Genre_entry)
        
    def add_Add_btn_command(self, p_film_id, p_title, p_year_released, p_rating, p_duration, p_genre, p2_film_id, p2_title, p2_year_released, p2_rating, p2_duration, p2_genre, message):
        f_controller.add_film(p_film_id, p_title, p_year_released, p_rating, p_duration, p_genre, message, p2_film_id, p2_title, p2_year_released, p2_rating, p2_duration, p2_genre)
            
    def add_Back_btn_command(self, controller, p2_film_id, p2_title, p2_year_released, p2_rating, p2_duration, p2_genre):
        boxes = [p2_film_id, p2_title, p2_year_released, p2_rating, p2_duration, p2_genre]
        for i in boxes:
            i.delete(0, tk.END)
        controller.show_frame ("menu_scrn")


class amend_scrn(tk.Frame):

    amend_Results = ""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        amend_Title=tk.Label(self)
        ft = tkFont.Font(family='Times',size=48)
        amend_Title["font"] = ft
        amend_Title["fg"] = "#333333"
        amend_Title["justify"] = "center"
        amend_Title["text"] = "Film Flix"
        amend_Title.place(x=0,y=30,width=614,height=53)
                
        self.amend_Results=ttk.Treeview(self, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings', height=8)
        # Results["borderwidth"] = "1px"
        # ft = tkFont.Font(family='Times',size=10)
        # Results["font"] = ft
        # Results["fg"] = "#333333"
        # Results["justify"] = "center"
        # Results["text"] = "Entry"
        self.amend_Results.place(x=10,y=120,width=591,height=50)
        self.amend_Results.column("# 1", anchor="center", minwidth=0, width=50)
        self.amend_Results.heading("# 1", text="Film ID")
        self.amend_Results.column("# 2", anchor="center", minwidth=0, width=235)
        self.amend_Results.heading("# 2", text="Title")
        self.amend_Results.column("# 3", anchor="center", minwidth=0, width=90)
        self.amend_Results.heading("# 3", text="Release year")
        self.amend_Results.column("# 4", anchor="center", minwidth=0, width=60)
        self.amend_Results.heading("# 4", text="Rating")
        self.amend_Results.column("# 5", anchor="center", minwidth=0, width=60)
        self.amend_Results.heading("# 5", text="Duration")
        self.amend_Results.column("# 6", anchor="center", minwidth=0, width=94)
        self.amend_Results.heading("# 6", text="Genre")

        amend_Id_label=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        amend_Id_label["font"] = ft
        amend_Id_label["fg"] = "#333333"
        amend_Id_label["justify"] = "center"
        amend_Id_label["text"] = "ID"
        amend_Id_label.place(x=20,y=180,width=70,height=25)

        amend_Id_entry=tk.Entry(self)
        amend_Id_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        amend_Id_entry["font"] = ft
        amend_Id_entry["fg"] = "#333333"
        amend_Id_entry["justify"] = "center"
        amend_Id_entry["text"] = ""
        amend_Id_entry.place(x=20,y=210,width=70,height=25)

        amend_Title_label=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        amend_Title_label["font"] = ft
        amend_Title_label["fg"] = "#333333"
        amend_Title_label["justify"] = "center"
        amend_Title_label["text"] = "Title"
        amend_Title_label.place(x=120,y=180,width=70,height=25)

        amend_Title_entry=tk.Entry(self)
        amend_Title_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        amend_Title_entry["font"] = ft
        amend_Title_entry["fg"] = "#333333"
        amend_Title_entry["justify"] = "center"
        amend_Title_entry["text"] = ""
        amend_Title_entry.place(x=120,y=210,width=70,height=25)

        amend_Rel_yr_label=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        amend_Rel_yr_label["font"] = ft
        amend_Rel_yr_label["fg"] = "#333333"
        amend_Rel_yr_label["justify"] = "center"
        amend_Rel_yr_label["text"] = "Release year"
        amend_Rel_yr_label.place(x=220,y=180,width=77,height=30)

        amend_Rel_yr_entry=tk.Entry(self)
        amend_Rel_yr_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        amend_Rel_yr_entry["font"] = ft
        amend_Rel_yr_entry["fg"] = "#333333"
        amend_Rel_yr_entry["justify"] = "center"
        amend_Rel_yr_entry["text"] = ""
        amend_Rel_yr_entry.place(x=220,y=210,width=70,height=25)

        amend_Rating_label=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        amend_Rating_label["font"] = ft
        amend_Rating_label["fg"] = "#333333"
        amend_Rating_label["justify"] = "center"
        amend_Rating_label["text"] = "Rating"
        amend_Rating_label.place(x=320,y=180,width=70,height=25)

        amend_Rating_entry=tk.Entry(self)
        amend_Rating_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        amend_Rating_entry["font"] = ft
        amend_Rating_entry["fg"] = "#333333"
        amend_Rating_entry["justify"] = "center"
        amend_Rating_entry["text"] = ""
        amend_Rating_entry.place(x=320,y=210,width=70,height=25)

        amend_Duration_label=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        amend_Duration_label["font"] = ft
        amend_Duration_label["fg"] = "#333333"
        amend_Duration_label["justify"] = "center"
        amend_Duration_label["text"] = "Duration"
        amend_Duration_label.place(x=420,y=180,width=70,height=25)

        amend_Duration_entry=tk.Entry(self)
        amend_Duration_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        amend_Duration_entry["font"] = ft
        amend_Duration_entry["fg"] = "#333333"
        amend_Duration_entry["justify"] = "center"
        amend_Duration_entry["text"] = ""
        amend_Duration_entry.place(x=420,y=210,width=70,height=25)

        amend_Genre_label=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        amend_Genre_label["font"] = ft
        amend_Genre_label["fg"] = "#333333"
        amend_Genre_label["justify"] = "center"
        amend_Genre_label["text"] = "Genre"
        amend_Genre_label.place(x=520,y=180,width=70,height=25)

        amend_Genre_entry=tk.Entry(self)
        amend_Genre_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        amend_Genre_entry["font"] = ft
        amend_Genre_entry["fg"] = "#333333"
        amend_Genre_entry["justify"] = "center"
        amend_Genre_entry["text"] = ""
        amend_Genre_entry.place(x=520,y=210,width=70,height=25)
        
        amend_Message=tk.Label(self)
        ft = tkFont.Font(family='Times',size=14)
        amend_Message["font"] = ft
        amend_Message["fg"] = "#00cc22"
        amend_Message["justify"] = "center"
        amend_Message["text"] = ""
        amend_Message.place(x=0,y=250,width=613,height=30)
                
        amend_Amend_btn=tk.Button(self)
        amend_Amend_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=14)
        amend_Amend_btn["font"] = ft
        amend_Amend_btn["fg"] = "#000000"
        amend_Amend_btn["justify"] = "center"
        amend_Amend_btn["text"] = "Amend details"
        amend_Amend_btn.place(x=230,y=300,width=150,height=30)
        amend_Amend_btn["command"] = lambda: self.amend_Amend_btn_command(amend_Id_entry.get(), amend_Title_entry.get(), amend_Rel_yr_entry.get(), amend_Rating_entry.get(), amend_Duration_entry.get(), amend_Genre_entry.get(), self.amend_Results, amend_Message)

        amend_Back_btn=tk.Button(self)
        amend_Back_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=14)
        amend_Back_btn["font"] = ft
        amend_Back_btn["fg"] = "#000000"
        amend_Back_btn["justify"] = "center"
        amend_Back_btn["text"] = "Back"
        amend_Back_btn.place(x=230,y=350,width=150,height=30)
        amend_Back_btn["command"] = lambda: self.amend_Back_btn_command(controller, amend_Id_entry, amend_Title_entry, amend_Rel_yr_entry, amend_Rating_entry, amend_Duration_entry, amend_Genre_entry)
                
    def amend_Amend_btn_command(self, p_Id, p_Title, p_Rel_yr, p_Rating, p_Duration, p_Genre, Results, message):
        f_controller.change(p_Id, p_Title, p_Rel_yr, p_Rating, p_Duration, p_Genre, Results, message)
    
    def amend_Back_btn_command(self, controller, p2_film_id, p2_title, p2_year_released, p2_rating, p2_duration, p2_genre):
        boxes = [p2_film_id, p2_title, p2_year_released, p2_rating, p2_duration, p2_genre]
        for i in boxes:
            i.delete(0, tk.END)
        controller.show_frame ("menu_scrn")

                    

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()