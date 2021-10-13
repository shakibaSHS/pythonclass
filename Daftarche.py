############################################
########## part0 : creation ################
############################################

# import sqlite3
# conn = sqlite3.connect('Daftarche.db')
# cursor = conn.cursor()
# query = "create table my_notebook(first_name,last_name,home_office,number,favorite_tag);"
# cursor.execute(query)
# conn.commit()

##############################################
########## part1 : initiation ################
##############################################
#
# import sqlite3
# conn = sqlite3.connect('Daftarche.db')
# cursor = conn.cursor()
# first_names = ['ali', 'hamed', 'saeid']
# last_names = ['alii', 'hamedi', 'saeidi']
# type_numbers = ['work', 'home', 'other']
# numbers = [912111111, 912333333, 9111111]
# favorite_tag = ['yes', 'no', 'no']
# # #
# for f_name, l_name, types, number, f_tag in zip(first_names,last_names, type_numbers, numbers,favorite_tag):
#     query2 = f"insert into my_notebook values ('{f_name}','{l_name}', '{types}', '{number}', '{f_tag}')"
#     cursor.execute(query2)
# conn.commit()

##############################################################
########### part 2 : user command ############################
##############################################################

first_input = input(str('Welcome to your Contact Book!!!\n\n\
                      to Search in contact please type ==> S \n\
                      to save a New contact please type  ==> N \n\
                      to Delete a contact please type  ==> D \n\
                      to Edit a contact please type ==> E \n\
                      input your command (S/N/D/E) = '))
temp = 0

while temp == 0:

    if first_input == 's' or first_input == 'n' or first_input == 'd' or first_input == 'e'\
     or first_input == 'S' or first_input == 'N' or first_input == 'D' or first_input == 'E':
        temp += 1
        start_point = first_input

    else:
        first_input = input('Please insert a correct letter!!\n\n\
                to Search in contact please type ==> S \n\
                to save a New contact please type  ==> N \n\
                to Delete a contact please type  ==> D \n\
                to Edit a contact please type  ==> D \n\
                please input your command (S/N/D/E) = ')



#########################
####### Save part #######
#########################


if start_point == 'n' or start_point == 'N':

    import sqlite3
    conn = sqlite3.connect('Daftarche.db')

    temp_n = 0

    while temp_n == 0:

        f_name = input('Please input first name \n\
                first name = ')
        l_name = input('Please input last name \n\
                last name = ')
        number = input('Please input the number without zero (hint: 911xxxxxxx \n\
                number = ')
        h_w = input('home or work or other ?\n\
                   (Home=> H/Work=>W)=')
        tag = input('is it favorite contact?\n\
                   (Yes=>Y/No=>N)=')

        cursor = conn.cursor()
        query2 = f"insert into my_notebook values ('{f_name}','{l_name}', '{h_w}', '{number}', '{tag}')"
        cursor.execute(query2)
        conn.commit()

        new_other_contact = input('the contact has been saved \n\
            Do you want to save an other contact?\n\
            (Yes=>Y/No=>N) (y/n)= ')

        if new_other_contact == 'N' or new_other_contact == 'n':
            temp_n += 1


###########################
##### delete part #########
###########################

if start_point == 'D' or start_point == 'd':

    temp_d = 0
    import sqlite3
    conn1 = sqlite3.connect('Daftarche.db')

    while temp_d == 0:

        # f_name = input('Please input first name \n\
        #         first name = ')
        l_name = input('Please input last name \n\
                last name = ')

        query3_1 = f"select * from my_notebook where last_name='{l_name}';"
        cursor = conn1.cursor()
        cursor.execute(query3_1)
        rows3_1 = cursor.fetchall()
        #conn.commit()
        kk3_1 = len(rows3_1)

        if kk3_1 > 0:

            query3 = f"delete from my_notebook where last_name='{l_name}';"

            import sqlite3
            conn = sqlite3.connect('Daftarche.db')
            cursor = conn.cursor()
            cursor.execute(query3)
            conn.commit()
            print(f'{kk3_1} contacts found and deleted!\n')

            del_other_contact = input('\n\
                Do you want to delete an other contact?\n\
                YES==>Y , NO==> N : (y/n)= ')

            if del_other_contact == 'N' or del_other_contact == 'n':
                temp_d += 1

        else:

            del_other_contact = input('The result not found!!!  \n\
                Do you want try again?\n\
                YES==>Y , NO==> N : (y/n)= ')

            # temp_d += 1

            if del_other_contact == 'N' or del_other_contact == 'n':
                temp_d += 1
                # conn.close()


###########################
##### search part #########
###########################

if start_point == 'S' or start_point == 's':

    import sqlite3
    conn = sqlite3.connect('Daftarche.db')

    temp_s = 0

    while temp_s == 0:

        way_to_search = input('search by name or phone number? \n\
                Name==> N or phone==> P  = ')

        if way_to_search == 'N':

            # f_name = input('Please input first name \n\
            #         first name = ')
            l_name = input('Please input last name \n\
                    last name = ')
            temp_s += 1

            query4 = f"select * from my_notebook where last_name='{l_name}';"

        elif way_to_search == 'P':

            p_number = input('Please input phone number \n\
                      phone number = ')
            temp_s += 1

            query4 = f"select * from my_notebook where number='{p_number}';"

        else:
            wrong_input = input('Please input correct letter to search! \n')

    cursor = conn.cursor()
    cursor.execute(query4)
    rows = cursor.fetchall()

    kk = len(rows)

    if kk > 0:

        for row in rows:
            fname = row[0]
            lname = row[1]
            number = row[3]
            print('The result is a follows:')
            print(f" ** first name : {fname}\n ** last name : {lname} \n ** phone number : {number}")
    else:

        print('The result not found!\n :')

    conn.commit()


###########################
##### edit part #########
###########################

if start_point == 'E' or start_point == 'e':

    import sqlite3
    conn = sqlite3.connect('Daftarche.db')

    temp_e = 0

    while temp_e == 0:

        edit_to_search = input('search by name or phone number? \n\
                Name==> N or phone==> P  = ')

        if edit_to_search == 'N':

            # f_name = input('Please input first name \n\
            #         first name = ')
            l_name = input('Please input last name \n\
                    last name = ')
            temp_e += 1

            query4 = f"select * from my_notebook where last_name='{l_name}';"

        elif edit_to_search == 'P':

            p_number = input('Please input phone number \n\
                      phone number = ')
            temp_e += 1

            query4 = f"select * from my_notebook where number='{p_number}';"

        else:
            wrong_input = input('Please input correct letter to search! \n')

    cursor = conn.cursor()
    cursor.execute(query4)
    rows = cursor.fetchall()

    kk = len(rows)

    if kk > 0:

        for row in rows:
            fname = row[0]
            lname = row[1]
            home = row[2]
            favorite = row[4]
            number = row[3]
            print('The result is a follows:')

            print(f" ** 1-first name : {fname}\n ** 2-last name : {lname} \n ** 3-phone number : {number} \n\
    ** 4-home or office : {home}\n ** 5-favorite contact? : {favorite}")

        edit_tag = input('what do you want to edit? \n\
                insert 1 to 5 : ')

        if edit_tag == '1':

            edit_item = input('edit first name: \n\
                    insert  new first name : ')

            query6 = f"delete from my_notebook where last_name='{lname}';"
            cursor.execute(query6)
            conn.commit()

            query_E = f"insert into my_notebook values ('{edit_item}','{lname}', '{home}', '{number}', '{favorite}')"
            cursor.execute(query_E)
            conn.commit()
            print('The contact has been modified.')

        elif edit_tag == '2':

            edit_item = input('edit last name: \n\
                insert  new last name : ')

            query6 = f"delete from my_notebook where last_name='{lname}';"
            cursor.execute(query6)
            conn.commit()
            query_E = f"insert into my_notebook values ('{fname}','{edit_item}', '{home}', '{number}', '{favorite}')"
            cursor.execute(query_E)
            conn.commit()
            print('The contact has been modified.')

        elif edit_tag == '3':

            edit_item = input('edit number: \n\
                insert  new number : ')

            query6 = f"delete from my_notebook where last_name='{lname}';"
            cursor.execute(query6)
            conn.commit()
            query_E = f"insert into my_notebook values ('{fname}','{lname}', '{home}', '{edit_item}', '{favorite}')"
            cursor.execute(query_E)
            conn.commit()
            print('The contact has been modified.')

        elif edit_tag == '4':

            edit_item = input('edit home office tag: \n\
                        insert  new tag (home /office) : ')

            query6 = f"delete from my_notebook where last_name='{lname}';"
            cursor.execute(query6)
            conn.commit()
            query_E = f"insert into my_notebook values ('{fname}','{lname}', '{edit_item}', '{number}', '{favorite}')"
            cursor.execute(query_E)
            conn.commit()
            print('The contact has been modified.')

        elif edit_tag == '5':

            edit_item = input('edit favorite tag: \n\
                        is it  favorite tag? (Y /N) : ')
            query6 = f"delete from my_notebook where last_name='{lname}';"
            cursor.execute(query6)
            conn.commit()
            query_E = f"insert into my_notebook values ('{fname}','{lname}', '{home}', '{number}', '{edit_item}')"
            cursor.execute(query_E)
            conn.commit()
            print('The contact has been modified.')











