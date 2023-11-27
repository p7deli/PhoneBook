from sqlite3 import connect


class Database:
    def __init__(self, database_name):
        self.database_name = database_name
        self.db = None

    def connect_db(self):
        self.db = connect(self.database_name)

    def create_table(self):
        cursor = self.db.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS phonebook (
            Id_ INTEGER PRIMARY KEY AUTOINCREMENT,
            First_Name TEXT,
            Last_Name TEXT,
            Phone_Number TEXT,
            Address TEXT
            )
        """)

    def close_db(self):
        self.db.close()

    def check_user(self, firstname, lastname):
        cursor = self.db.cursor()
        cursor.execute("""
            SELECT * FROM phonebook WHERE First_Name=? AND Last_Name=?
        """, (firstname, lastname))
        table_info = cursor.fetchall()
        if len(table_info) == 0:
            return True
        return False

    def create_user(self, firstname, lastname, phone_number, address):
        if self.check_user(firstname, lastname):
            cursor = self.db.cursor()
            cursor.execute(f"""
                INSERT INTO phonebook (First_Name, Last_Name, Phone_Number, Address)
                VALUES (?, ?, ?, ?)
            """, (firstname, lastname, phone_number, address))
            self.db.commit()
            return True
        return False

    def edit(self, id, firstname, lastname, phone_number, address):
        cursor = self.db.cursor()
        cursor.execute(f"UPDATE phonebook SET First_Name = '{firstname}', Last_Name = '{lastname}', Phone_Number = '{phone_number}', Address = '{address}' WHERE id_ = {id}")
        self.db.commit()
        return True

    def delete(self, Id_):
        cursor = self.db.cursor()
        cursor.execute(f"DELETE FROM phonebook WHERE id_ = {Id_}")
        self.db.commit()
        return True

    def show_users(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM phonebook")
        return cursor

    def search(self, name, family, number):
        cursor = self.db.cursor()
        if name != "" and family == "" and number == "":
            cursor.execute(f"SELECT * FROM phonebook WHERE First_Name = '{name}'")
            return cursor
        elif name == "" and family != "" and number == "":
            cursor.execute(f"SELECT * FROM phonebook WHERE Last_Name = '{family}'")
            return cursor
        elif name == "" and family == "" and number != "":
            cursor.execute(f"SELECT * FROM phonebook WHERE Phone_Number = '{number}'")
            return cursor
        elif name != "" and family != "" and number != "":
            cursor.execute(f"SELECT * FROM phonebook WHERE First_Name = '{name}' AND Last_Name = '{family}' AND Phone_Number = '{number}'")
            return cursor
        elif name != "" and family != "" and number == "":
            cursor.execute(f"SELECT * FROM phonebook WHERE First_Name = '{name}' AND Last_Name = '{family}'")
            return cursor
        elif name != "" and family == "" and number != "":
            cursor.execute(f"SELECT * FROM phonebook WHERE First_Name = '{name}' AND Phone_Number = '{number}'")
            return cursor
        elif name == "" and family != "" and number != "":
            cursor.execute(f"SELECT * FROM phonebook WHERE Last_Name = '{family}' AND Phone_Number = '{number}'")
            return cursor
        else:
            return False
