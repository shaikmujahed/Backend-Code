# importing CursorFromConnectionFromPool class from database file
from database import CursorFromConnectionFromPool

# creating User class
class User:
    def __init__(self,id,email,first_name,last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

     # creating representation and formatting the output
    def __repr__(self):
        return "<User {},{},{}>".format(self.email,self.first_name,self.last_name,self.id)

    #saving data to database
    def save_to_db(self):
            with CursorFromConnectionFromPool() as cursor:
                cursor.execute("INSERT INTO users(email,first_name,last_name) VALUES(%s,%s,%s)",
                               (self.email,self.first_name,self.last_name))

        
       #loading data from database
    @classmethod
    def load_from_db_by_email(cls,email):
               with CursorFromConnectionFromPool () as cursor:
                     cursor.execute("SELECT * FROM users WHERE email = %s",(email,))
                     user_data = cursor.fetchone()
                     return cls(email=user_data[1],first_name=user_data[2],last_name=user_data[3],id=user_data[0])










