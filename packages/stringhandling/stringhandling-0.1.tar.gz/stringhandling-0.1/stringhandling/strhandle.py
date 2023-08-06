
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