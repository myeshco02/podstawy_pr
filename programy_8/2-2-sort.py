names = [
   'James',
   'Emily',
   'William',
   'Olivia',
   'Benjamin',
   'Sophia',
   'Henry']


def main():
    print('Sorted list:')
    for name in sorted(names, key=len):
        print(name)
    

if __name__ == '__main__':
    main()
