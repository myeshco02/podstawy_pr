def f(detector):
    people_in_room = 0
    for action in detector:
        if action == "+":
            people_in_room += 1
        elif action == "-":
            people_in_room -= 1
        
        # Jeśli kiedykolwiek w pokoju będzie co najmniej 3 osoby, zwracamy True
        if people_in_room >= 3:
            return True
    
    # Jeśli nigdy nie było co najmniej 3 osób, zwracamy False
    return False

print(f("+-+++-+---"))  # wynik: True
print(f("+-+-+-+-"))    # wynik: False
print(f("+-++-+--"))     # wynik: False
print(f("+-++-++-+---")) # wynik: True
