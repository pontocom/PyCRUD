import mariadb
from prettytable import PrettyTable

conn_params = {
    "user": "",
    "password": "",
    "host": "localhost",
    "database": "crud"
}


def create_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    name = input("Enter name: ")
    address = input("Enter address: ")

    connection = mariadb.connect(**conn_params)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO utilizador (username, password, nome, morada) VALUES (?,?,?,?)", (username, password, name, address))
    cursor.close()
    connection.commit()
    connection.close()


def read_users():
    table = PrettyTable()
    table.field_names = ["Uid", "Username", "Password", "Name", "Address"]
    table.align["Uid"] = "c"
    table.align["Username"] = "l"
    table.align["Password"] = "l"
    table.align["Name"] = "l"
    table.align["Address"] = "l"

    connection = mariadb.connect(**conn_params)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM utilizador")
    rows = cursor.fetchall()
    for row in rows:
        table.add_row(row)

    print(table)
    cursor.close()
    connection.close()


def update_user():
    uid = input("Select user to update: ")
    connection = mariadb.connect(**conn_params)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM utilizador WHERE uid=?", (uid,))
    row = cursor.fetchone()
    print(row)
    username = row[1]
    password = row[2]
    name = row[3]
    address = row[4]
    u_username = input("New username [left blank if no change] ")
    if u_username == '':
        u_username = username
    u_password = input("New password [left blank if no change] ")
    if u_password == '':
        u_password = password
    u_name = input("New name [left blank if no change] ")
    if u_name == '':
        u_name = name
    u_address = input("New address [left blank if no change] ")
    if u_address == '':
        u_address = address
    cursor.execute("UPDATE utilizador SET username = ?, password = ?, nome = ?, morada = ? WHERE uid = ? ", (u_username, u_password, u_name, u_address, uid))
    cursor.close()
    connection.commit()
    connection.close()


def delete_user():
    uid = input("User id to delete: ")
    connection = mariadb.connect(**conn_params)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM utilizador WHERE uid=?", (uid,))
    cursor.close()
    connection.commit()
    connection.close()


def print_menu():
    print("-------------------")
    print("|     M e n u     |")
    print("-------------------")
    print("[1] Create new User")
    print("[2] Read all users")
    print("[3] Update user")
    print("[4] Delete user")
    print("[0] Exit")


if __name__ == "__main__":
    while True:
        print_menu()
        option = input("Enter option -> ")

        if option == '1':
            create_user()
        elif option == '2':
            read_users()
        elif option == '3':
            read_users()
            update_user()
        elif option == '4':
            read_users()
            delete_user()
        elif option == '0':
            break
        else:
            print("Wrong option selected!!!")
