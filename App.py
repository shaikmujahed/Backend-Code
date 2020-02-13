
# importing Database from database file
from database import Database
# importing User() class from user file
from user import User
# connecting to database
Database.initialise(database ='postgres',user='postgres',password='postgre_sql',host='localhost')

# creating a user
my_user = User(None,'microsoft@gmail.com','oracle','oracle')
# saving user to database
my_user.save_to_db()
# loading user from database by email
user_from_db = User.load_from_db_by_email("microsoft@gmail.com")
# printing out user
print(user_from_db)
