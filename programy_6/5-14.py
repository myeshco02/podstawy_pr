from collections import deque

class CustomerServiceQueue:
    def __init__(self):
        self.queue = deque()  # Tworzymy pustą kolejkę
        self.ticket_number = 1  # Numer biletu startowego

    def add_client(self):
        # Dodanie nowego klienta do kolejki
        print(f"Klient z biletem nr {self.ticket_number} dodany do kolejki.")
        self.queue.append(self.ticket_number)
        self.ticket_number += 1

    def serve_client(self):
        # Obsługa klienta z początku kolejki
        if self.queue:
            current_client = self.queue.popleft()
            print(f"Obsługiwany jest klient z biletem nr {current_client}.")
        else:
            print("Brak klientów w kolejce do obsłużenia.")

    def display_queue(self):
        # Wyświetlanie stanu kolejki
        if self.queue:
            print("Aktualna kolejka:", list(self.queue))
        else:
            print("Kolejka jest pusta.")

def main():
    service_queue = CustomerServiceQueue()

    while True:
        print("\nMenu:")
        print("1. Dodaj klienta do kolejki")
        print("2. Obsłuż następnego klienta")
        print("3. Wyświetl aktualną kolejkę")
        print("4. Zakończ")
        
        choice = input("Wybierz opcję: ").strip()

        if choice == "1":
            service_queue.add_client()
        elif choice == "2":
            service_queue.serve_client()
        elif choice == "3":
            service_queue.display_queue()
        elif choice == "4":
            print("Dziękujemy za skorzystanie z systemu!")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    main()
