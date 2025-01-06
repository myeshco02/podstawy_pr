def evaluate_rpn():
    stack = []

    while True:
        user_input = input("Wprowadź liczbę, operator (+, -, *, /) lub '=' aby zakończyć: ").strip()

        if user_input == '=':
            if len(stack) == 1:
                print("Wynik:", stack.pop())
            else:
                print("Błąd: nieprawidłowe wyrażenie.")
            break
        elif user_input in ('+', '-', '*', '/'):
            if len(stack) < 2:
                print("Błąd: za mało elementów na stosie do wykonania operacji.")
                continue
            b = stack.pop()
            a = stack.pop()
            if user_input == '+':
                result = a + b
            elif user_input == '-':
                result = a - b
            elif user_input == '*':
                result = a * b
            elif user_input == '/':
                if b == 0:
                    print("Błąd: dzielenie przez zero.")
                    stack.append(a)
                    stack.append(b)
                    continue
                result = a / b
            stack.append(result)
            print("Stos po operacji:", stack)
        else:
            try:
                number = float(user_input)
                stack.append(number)
                print("Stos po dodaniu liczby:", stack)
            except ValueError:
                print("Błąd: nieprawidłowe dane wejściowe.")

if __name__ == "__main__":
    evaluate_rpn()
