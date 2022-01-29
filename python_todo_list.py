import sqlite3

# functionality
class DatabaseManage(object):
    def __init__(self):
        global dbConnection
        try:
            dbConnection = sqlite3.connect("todos.db")
            with dbConnection:
                cursor = dbConnection.cursor()
                cursor.execute("CREATE TABLE IF NOT EXISTS todo(Id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, status TEXT, is_private BOOLEAN NOT NULL DEFAULT 1)") 
        except Exception:
            print("Unable to create a database.")
    
    def insert_data(self, data):
        try:
            with dbConnection:
                cursor =  dbConnection.cursor()
                cursor.execute("INSERT INTO todo(name, description, status, is_private) VALUES (?,?,?,?)", data)
                return True
        except Exception:
            print("Unable to insert data in the database.")
            return False
    
    def fetch_data(self):
        try:
            with dbConnection:
                cursor = dbConnection.cursor()
                cursor.execute("SELECT * FROM todo")
                return cursor.fetchall()
        except Exception:
            print("Unable to fetch data from the database.")
            return False
    
    def delete_data(self, id):
        try:
            with dbConnection:
                cursor = dbConnection.cursor()
                sql = "DELETE FROM todo WHERE id = ?"
                cursor.execute(sql, [id])
                return True
        except Exception:
            print("Unable to delete data from the database.")
            return False
                

# TODO: interface

def main():
    print("\n:: TODO MANAGEMENT APPLICATION :: \n")
    print("*"*40)
    print("\n")

    db = DatabaseManage()
    
    print("\n:: COMMANDS :: \n")
    print("*"*40)
    print('\nPress 1. Insert a new todo\n')
    print('Press 2. Show all todos\n')
    print('Press 3. Delete a todo\n')
    
    choice = input("\n Enter a choice: ")
    
    if choice == "1":
        name = input("\n Enter todo name: ")
        description = input("\n Enter todo description: ")
        status = input("\n Enter todo status: ")
        private = input("\n Is this todo private (0/1): ")
        
        if db.insert_data([name, description, status, private]):
            print("\n Todo was inserted successfully.")
        else:
            print("Error! todo insertion failed.")
        
    elif choice == "2":
        print("\n:: TODO List ::")
        print("*"*40)
        
        for index, todo in enumerate(db.fetch_data()):
            print("\n TODO ID : " + str(todo[0]))
            print("\n TODO Name : " + str(todo[1]))
            print("\n TODO Description : " + str(todo[2]))
            print("\n TODO Status : " + str(todo[3]))
            private = "Yes" if (todo[4] == 1) else "No"
            print("\n Is Private : " + private)
            print("\n")
            print("*"*40)
            
    elif choice == "3":
        todo_id = input("Enter the todo id you want to delete: ")
        
        if db.delete_data(todo_id):
            print("Todo was deleted successfully.")
        else:
            print("Error! todo deletion failed.")
            
    else:
        print("\n Wrong operation.")
        
if __name__ == "__main__":
    main()