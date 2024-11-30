import requests

visel = {
    "0": r'''
      +---+
          |
          |
          |
          |
          |
    =========
    ''',
    "1": r'''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''',
    "2": r'''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    "3": r'''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    "4": r'''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    "5": r'''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''',
    "6": r'''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''',
    "7": r'''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    '''
}

api_url = 'https://random-word-api.herokuapp.com/word'
response = requests.get(api_url)
word = response.json()[0]
word_2 = "_" * len(word)
error = 0
try:
  while True:
      letter = input('Введите английскую букву: ')
      if error >= 7:
          print("Ты проиграл.")
          break
      elif letter in word:
          index1 = word.index(letter)
          print(visel[str(error)])
          word_2 = word_2[: index1] + letter + word_2[index1 + 1:]
          word = word[: index1] + "_" + word[index1 + 1:]
          print(word_2)
          print('Вы угадали букву')
          print(f"Ошибок: {error}")
      else:
          error += 1
          print(visel[str(error)])
          print(word_2)
          print(f"Ошибок: {error}")
except KeyboardInterrupt:
    None