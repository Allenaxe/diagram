#Import

import sys, os
import json

#Initial Value

def Initial(File_name):
    '''
    with open('records.json', 'r') as jfile:
        jdata = json.load(jfile)
    return jdata
    '''
    try:
        with open(File_name, 'r') as fh:
            Balance = int(fh.readline())
            for item in fh.readlines():
                key = item.split()
                record_list[key[0]] = int(key[1])
        return record_list, Balance, File_name
    except FileNotFoundError:
        sys.stderr.write('FileNotFound!\n')
        while True:
            command = input('Create a new file? [Yes/No]: ')
            if command == 'exit':
                sys.exit(0)
            elif command == 'Yes':
                return dict(), int(input('How much money do you have? : ')), File_name
            elif command == 'No':
                return Initial(input('Please reload the file: '))
            else:
                sys.stderr.write('Invaild Command!\n')
    except ValueError and Exception:
        if os.stat(File_name).st_size == 0:
            sys.stderr.write('Empty File\n')
        else:
            sys.stderr.write('Invalid format in records.txt. Deleting the contents.\n')
            with open(File_name, 'w') as fh:
                fh.write('')
        return dict(), int(input('How much money do you have? : ')), File_name 

#Bank Function
def Bank(record_list, Balance):
    while True:
        try:
            data = input('Add an expence or income record with description and amount or exit: ')
            data_input = data.split();
            if data == 'exit':
                break
            data_input = data.split(', ')
            data_input_sequence = [tuple(item.split(' ')) for item in data_input]
            for key, value in data_input_sequence:
                Balance += int(value)
                record_list[key] = value
            print("Append Success.")
        except ValueError:
            sys.stderr.write("Append Failed.\n")
    return record_list, Balance

#Delete Function

def Delete(record_list, Balance):
    print("-------------------")
    print("{:10} | {:>}".format("Item", "Amount"))
    print("-------------------")
    for key in record_list:
        print(f"{key:10} | {record_list[key]:>}")
    print("-------------------")
    try:
        key = input("Please enter items to delete:")
        if key == 'exit':
            return record_list, Balance
        elif record_list.get(key) == None:
            print("Item not found")
            return Delete(record_list, Balance)
        Balance -= int(record_list[key])
        del record_list[key]
        print("Delete Success.")
    except ValueError:
        sys.stderr.write("Delete Failed.\n")
    return Delete(record_list, Balance)

#Search Function

def Search(record_list, Balance):
    search = input("Please enter (Item name/Balance):")
    if search == 'Balance':
        print("Balance = ", Balance)
    else:
        print(record_list.get(search, "Item not found"))

#List Function

def List(record_list, Balance):
    try:
        print("-------------------")
        print("{:10} | {:>}".format("Item", "Amount"))
        print("-------------------")
        for key in record_list:
            print(f"{key:10} | {record_list[key]:>}")
        print("-------------------")
        print(f"Now you have {Balance} dollars")
    except TypeError:
        sys.stderr.write("Invalid Value\n")

def Savefile(record_list, Balance, File_name):
    '''
    try:
        with open('records.json', 'w', encoding = 'utf-8') as jfile:
            json.dump(record_list, jfile, indent = 4)
        print("File Saved")
    except:
        print("File Corruption")
    '''
    fh = open(File_name, 'w')
    fh.write(f'{Balance}')
    fh.write('\n')
    for key in record_list:
        fh.write(f'{key} {record_list[key]}')
        fh.write('\n')
    fh.close()

print("Welcome to Personal Accounting Program!")

#Initial

File_name = input('Please input a load file: ')
record_list, Balance, File_name = Initial(File_name)

#Balance

print(f"Now you have {Balance} dollars")

#Main Function

while True:
    command = input('please enter command(bank/delete/search/list/exit):')

    #Bank Function
    if command == 'exit':
        Savefile(record_list, Balance, File_name)
        break

    elif command == 'bank':
        record_list, Balance = Bank(record_list, Balance)

    #Delete Function

    elif command == 'delete':
        record_list, Balance = Delete(record_list, Balance)

    #Search Function

    elif command == 'search':
        Search(record_list, Balance)
            
    #List Function

    elif command == 'list':
        List(record_list, Balance)

    else:
        sys.stderr.write('Invaild command. Try again!\n')

