# Słownik z tłumaczeniami
translations = {
    'computer': 'komputer',
    'mouse': 'myszka',
    'keyboard': 'klawiatura',
    'printer': 'drukarka'
}

# Pętla umożliwiająca wielokrotne sprawdzanie tłumaczeń
while True:
    print("=== English to Polish Translator ===")
    word = input("Enter an English word (or type 'exit' to quit): ").strip().lower()
    
    if word == 'exit':
        print("Exiting the translator. Goodbye!")
        break
    
    # Sprawdzanie, czy słowo istnieje w słowniku
    translation = translations.get(word)
    
    if translation:
        print(f"The Polish translation of '{word}' is '{translation}'.")
    else:
        print(f"Sorry, the translation for '{word}' is not available.")
