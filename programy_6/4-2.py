import queue

# Tworzy kolejkę plików do drukowania
files_to_print = queue.Queue()

while True:
    print('1. Add file to print')
    print('2. Print file')
    print('0. Quit')
    menu = input('Select an option: ')
    
    if menu == '1':
        # Dodawanie pliku do kolejki
        file_name = input('Enter file name to print: ')
        files_to_print.put(file_name)
        print(f'File "{file_name}" has been added to the print queue.')

    elif menu == '2':
        # Drukowanie pliku z kolejki
        if not files_to_print.empty():
            file_to_print = files_to_print.get()
            print(f'File "{file_to_print}" is currently being printed. Please wait!')
        else:
            print('The print queue is empty. No files to print.')

    elif menu == '0':
        # Wyjście z programu
        print('Exiting the program.')
        break

    else:
        print('Invalid option. Please select a valid menu option.')
