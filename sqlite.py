import sqlite3 as sql

class sql_handling():
    
    cursor = ""
    my_conn =""
    
    def __init__(self, database):
        #Create the connection object   
        with sql.connect(database) as self.my_conn:
        #printing the connection object   
            print(self.my_conn)  
            self.cursor = self.my_conn.cursor()
    

    def sql_execute(self, query, vals):
        self.cursor.execute(query, vals)
        self.my_conn.commit()
    
    def sql_execute_query(self, query, vals):
        self.cursor.execute(query, vals)
        return self.cursor.fetchall()

    def sql_execute_delete(self, query):
        self.cursor.execute(query)
        self.my_conn.commit()