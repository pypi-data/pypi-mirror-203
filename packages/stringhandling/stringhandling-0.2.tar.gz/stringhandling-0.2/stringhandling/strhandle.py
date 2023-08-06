
def get_words_list(sentence):
      wordslst = []
      word = ""
      for Char in sentence:
          if((Char == ' ') and (word != "")):
            wordslst.append(word)
            word = ""
          else:
              if ((Char != ' ') and (Char != '\n') and (Char != '\t')):
                  word = word + Char
      if(word != ""):
        wordslst.append(word)
      return wordslst


def get_char_count(sentence):
    letters_count = {}
    for letter in sentence:
        if(letters_count.get(letter) is not None):
            letters_count[letter] = letters_count[letter] + 1
        else:
            letters_count[letter] = 1
    return letters_count