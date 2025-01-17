from stats import Statistics


def main():
    stats = Statistics(init_numbers=[12, 37, 6])

    while True:
        newNumber = input('Add number to the set ("exit" to exit): ')
        if newNumber != 'exit':
            stats.addNumber(int(newNumber))
        else:
            break

    stats.displayNumbers()
    stats.pStats()
    

if __name__ == '__main__':
    main()
