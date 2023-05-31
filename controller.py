from sqlite import *

connector = sql_handling("filmflix.db")

class controller():
    def __init__(self) -> None:
        pass
    
    def add_film(self, p_film_id, p_title, p_year_released, p_rating, p_duration, p_genre):
        # Data verification here
        connector.sql_execute(f"INSERT INTO tblFilms (filmID, title, yearReleased, rating, duration, genre) VALUES ({p_film_id}, {p_title}, {p_year_released}, {p_rating}, {p_duration}, {p_genre});")
