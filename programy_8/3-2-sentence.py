sentence = 'I completely agree with you'


def main():
    result = list(map(lambda word: len(word), sentence.split()))
    print(f'Text: {sentence}')
    print(f'Number of letters in words: {result}')


if __name__ == '__main__':
    main()
