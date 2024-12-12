# test_converters.py

from converters import m_to_cm, cm_to_m, cm_to_inches, feet_and_inches_to_cm

if __name__ == "__main__":
    print("Testowanie funkcji konwersji:")
    
    # Testy funkcji
    print(f"2 metry to {m_to_cm(2)} cm")
    print(f"532 cm to {cm_to_m(532)} metry/a")
    print(f"100 cm to {cm_to_inches(100):.2f} cale")
    print(f"5 stóp i 3 cale to {feet_and_inches_to_cm(5, 3):.2f} cm")
