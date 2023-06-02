from sqlite import *
import time
import tkinter as tk

connector = sql_handling("filmflix.db")

class fn_controller():
    def __init__(self) -> None:
        pass
    
    def add_film(self, p_film_id, p_title, p_year_released, p_rating, p_duration, p_genre, message):
        # Data verification here
        vals = (p_film_id, p_title, p_year_released, p_rating, p_duration, p_genre)
        connector.sql_execute(f"INSERT INTO tblFilms (filmID, title, yearReleased, rating, duration, genre) VALUES (?,?,?,?,?,?);", vals)
        
        message["fg"] = "#00cc22"
        message["text"] = "Film added successfully"
        message.after(3000,lambda: self.remove_message(message))

    def query(self, p_film_id, p_title, p_year_released, p_rating, p_duration, p_genre, p_Results):
        # Data verification here
        
        if p_film_id == "":
            p_film_id = "%"
        else:
            p_film_id = int(p_film_id)
        
        if p_year_released == "":
            p_year_released = "%"
        else:
            p_year_released = int(p_year_released)
            
        if p_duration == "":
            p_duration = "%"
        else:
            p_duration = int(p_duration)
        
        if p_title == "":
            p_title = "%"

        if p_rating == "":
            p_rating = "%"
    
        if p_genre == "":
            p_genre = "%"
        
        vals = (p_film_id, p_title, p_year_released, p_rating, p_duration, p_genre)
        search = connector.sql_execute_query(f"SELECT * FROM tblFilms WHERE filmID LIKE ? AND title LIKE ? AND yearReleased LIKE ? AND rating LIKE ? AND duration LIKE ? AND genre LIKE ?;", vals)
        for i in search:
            p_Results.insert('', 'end', text=str(i[0]), values=(i))

        
    def change(self, p_film_id, p_title, p_year_released, p_rating, p_duration, p_genre, p_results, message):
        # Data verification here
        
        for line in p_results.get_children():
            record = p_results.item(line)["values"][0]
        
        if p_genre != "":
            val6 = (p_genre, int(record))
            connector.sql_execute(f"UPDATE tblFilms SET genre = ? WHERE filmID = ?;", val6)

        if p_duration != "":
            val5 = (int(p_duration), int(record))
            connector.sql_execute(f"UPDATE tblFilms SET duration = ? WHERE filmID = ?;", val5)
            
        if p_rating != "":
            val4 = (p_rating, int(record))
            connector.sql_execute(f"UPDATE tblFilms SET rating = ? WHERE filmID = ?;", val4)
            
        if p_year_released != "":
            val3 = (int(p_year_released), int(record))
            connector.sql_execute(f"UPDATE tblFilms SET yearReleased = ? WHERE filmID = ?;", val3)
            
        if p_title != "":
            val2 = (p_title, int(record))
            connector.sql_execute(f"UPDATE tblFilms SET title = ? WHERE filmID = ?;", val2)
            
        if p_film_id != "":
            val1 = (int(p_film_id), int(record))
            connector.sql_execute(f"UPDATE tblFilms SET filmID = ? WHERE filmID = ?;", val1)
            amended_film = connector.sql_execute_simple_query(f"SELECT * FROM tblFilms WHERE filmID = {int(p_film_id)};")            
        else:
            amended_film = connector.sql_execute_simple_query(f"SELECT * FROM tblFilms WHERE filmID = {int(record)};")
        
        p_results.delete(*p_results.get_children())
        
        for i in amended_film:
            p_results.insert('', 'end', text=str(i[0]), values=(i))
        
        message["fg"] = "#00cc22"
        message["text"] = "Film amended successfully"
        message.after(3000,lambda: self.remove_message(message))

    def remove_message(self, message):
        message["text"] = ""
        
    def delete(self, deleted_item, message):
        val = (int(deleted_item[0]))
        connector.sql_execute_delete(f"DELETE FROM tblFilms WHERE filmID = {val};")
        message["fg"] = "#cc0000"
        message["text"] = "Film deleted successfully"
        message.after(3000,lambda: self.remove_message(message))
