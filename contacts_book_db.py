from pwinput import pwinput
from mysql.connector import connect, Error


class Contacts:
    global contacts
    
    def __init__(self):
        self.txt = "This object manipulates contacts."

    def __str__(self):
        return self.txt
    

    def create_db(self, db_name, host):
        create_db_query = "CREATE DATABASE %s" %(db_name)

        try:
            with connect(
                host = host,
                user = input("Enter username: "),
                password = pwinput("Enter password: ")
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(create_db_query)
        
        except Error as e:
            print(e)


    def create_tb(self, db_name, tb_name, host):
        create_tb_query = """
        CREATE TABLE %s (
        name VARCHAR(250),
        mobile_phone VARCHAR(11),
        PRIMARY KEY(mobile_phone)
        );
        """ %(tb_name)
    
        try:
            with connect(
                host = host,
                user = input("Enter username: "),
                password = pwinput("Enter password: "),
                database = db_name
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(create_tb_query)
                    connection.commit()
        
        except Error as e:
            print(e)

    def display_db(self, db_name, host):
        display_db_query = "SHOW TABLES FROM %s" %(db_name)

        try:
            with connect(
                host = host,
                user = input("Enter username: "),
                password = pwinput("Enter password: "),
                database = db_name
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(display_db_query)
                    result = cursor.fetchall()
                    for row in result:
                        print(row)
        
        except Error as e:
            print(e)


    def display_tb(self, db_name, tb_name, host):
        display_tb_query = "SHOW COLUMNS FROM %s" %(tb_name)

        try:
            with connect(
                host = host,
                user = input("Enter username: "),
                password = pwinput("Enter password: "),
                database = f"{db_name}"
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(display_tb_query)
                    result = cursor.fetchall()
                    for row in result:
                        print(row)
        
        except Error as e:
            print(e)
    

    def add(self, db_name, tb_name, host):
        ins_num = int(input("How many contacts do you wish to add: "))

        try:
            with connect(
                host = host,
                user = input("Enter username: "),
                password = pwinput("Enter password: "),
                database = db_name
            ) as connection:
                with connection.cursor() as cursor:
                    insert_tb_query = f"INSERT INTO `{tb_name}` (name, mobile_phone) VALUES(%s, %s);"
                    if (ins_num == 1):
                        ins_name = input("Enter the name of the contact: ")
                        ins_phone = input("Enter the phone number: ")
                        ins_tpl = (ins_name, ins_phone)
                        cursor.execute(insert_tb_query, ins_tpl)

                    elif (ins_num > 1):
                        ins_name = input("Enter the names of the contact as comma seperated values: ")
                        ins_phone = input("Enter the phone numbers as comma seperated values: ")
                        ins_name_lst = ins_name.split(",")
                        ins_phone_lst = ins_phone.split(",")

                        for i in range(ins_num):
                            each_ins_name = ins_name_lst[i]
                            each_ins_phone = ins_phone_lst[i]
                            ins_tpl = (each_ins_name, each_ins_phone)
                            cursor.execute(insert_tb_query, ins_tpl)
                    connection.commit()
        
        except Error as e:
            print(e)
             

    def edit(self, db_name, tb_name, host):
        edit_name = input("Enter the name of the contact you wish to edit: ")
        try:
            with connect(
                host = host,
                user = input("Enter username: "),
                password = pwinput("Enter password: "),
                database = db_name
            ) as connection:
                with connection.cursor() as cursor:
                    new_name = input("Enter the new name of the contact, enter 'q' to skip: ")
                    new_phone = input("Enter the new phone number of the contact, enter 'q' to skip: ")

                    if (new_name != 'q') and (new_phone != 'q'):
                        edit_tb_query = f"""
                            UPDATE `{tb_name}`
                            SET name = %s, mobile_phone = %s
                            WHERE name = '{edit_name}';
                            """
                        edit_tpl = (new_name, new_phone)
                        cursor.execute(edit_tb_query, edit_tpl)
                    elif (new_name == 'q') and (new_phone != 'q'):
                        edit_tb_query = f"""
                            UPDATE `{tb_name}`
                            SET mobile_phone = '%s'
                            WHERE name = '{edit_name}';
                            """ %(new_phone)
                        cursor.execute(edit_tb_query)
                    elif (new_name != 'q') and (new_phone == 'q'):
                        edit_tb_query = f"""
                            UPDATE `{tb_name}`
                            SET name = '%s'
                            WHERE name = '{edit_name}';
                            """ %(new_name)
                        cursor.execute(edit_tb_query)
                    connection.commit()

        except Error as e:
            print(e)


    def select(self, db_name, tb_name, host):
        select_name = input("Enter the name of the contact: ")
        select_query = f"""
            SELECT * FROM `{tb_name}`
            WHERE name = '%s';
            """ %(select_name)
        try:
            with connect(
                host = host,
                user = input("Enter username: "),
                password = pwinput("Enter password: "),
                database = db_name
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    for row in result:
                        print(row)

        except Error as e:
            print(e)


    def delete(self, db_name, tb_name, host):
        del_num = int(input("How many contacts do you wish to delete: "))
        try:
            with connect(
                host = host,
                user = input("Enter username: "),
                password = pwinput("Enter password: "),
                database = db_name
            ) as connection:
                with connection.cursor() as cursor:
                    if (del_num == 1):
                        del_name = input("Enter the name of the contact: ")
                        delete_tb_query = f"""
                        DELETE FROM `{tb_name}`
                        WHERE name = '%s';""" %(del_name)
                        cursor.execute(delete_tb_query)

                    elif (del_num > 1):
                        del_name = input("Enter the names of the contact as comma seperated values: ")
                        del_name_lst = del_name.split(",")

                        for i in range(del_num):
                            each_del_name = del_name_lst[i]
                            delete_tb_query = f"""
                            DELETE FROM `{tb_name}`
                            WHERE name = '%s';""" %(each_del_name)
                            cursor.execute(delete_tb_query)
                    connection.commit()
        
        except Error as e:
            print(e)