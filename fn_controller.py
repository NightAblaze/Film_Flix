from sqlite import *

connector = sql_handling("filmflix.db")

class fn_controller():
    def __init__(self) -> None:
        pass
    
    def add_film(self, p_film_id, p_title, p_year_released, p_rating, p_duration, p_genre):
        # Data verification here
        vals = (p_film_id, p_title, p_year_released, p_rating, p_duration, p_genre)
        connector.sql_execute(f"INSERT INTO tblFilms (filmID, title, yearReleased, rating, duration, genre) VALUES (?,?,?,?,?,?);", vals)

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

    # def amend(self, selected, p_Results):
    #     Results.insert('', 'end', text="1", values=selected)
        
    def change(self, p_film_id, p_title, p_year_released, p_rating, p_duration, p_genre, p_results):
        # Data verification here
        
        # record = p_results.focus() # May not be needed
        record = p_results.item(record)
        record = record["values"]
        record = record[0]
        print(record)
        
        val1 = (int(p_film_id), int(record))
        val2 = (p_title, int(record))
        val3 = (int(p_year_released), int(record))
        val4 = (p_rating, int(record))
        val5 = (int(p_duration), int(record))
        val6 = (p_genre, int(record))
        
        if p_genre != "":
            connector.sql_execute(f"UPDATE tblFilms SET genre = ? WHERE filmID = ?;", val6)
        if p_duration != "":
            connector.sql_execute(f"UPDATE tblFilms SET duration = ? WHERE filmID = ?;", val5)
        if p_rating != "":
            connector.sql_execute(f"UPDATE tblFilms SET rating = ? WHERE filmID = ?;", val4)
        if p_year_released != "":
            connector.sql_execute(f"UPDATE tblFilms SET yearReleased = ? WHERE filmID = ?;", val3)
        if p_title != "":
            connector.sql_execute(f"UPDATE tblFilms SET title = ? WHERE filmID = ?;", val2)
        if p_film_id != "":
            connector.sql_execute(f"UPDATE tblFilms SET filmID = ? WHERE filmID = ?;", val1)        

    def delete(self, deleted_item):
        val = (int(deleted_item[0]))
        connector.sql_execute_delete(f"DELETE FROM tblFilms WHERE filmID = {val};")
