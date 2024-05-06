import random

Global_array = []
Array = []
history_theme = []

class Search:

    def __init__(self, input_word, database, theme):
        self.input_word = input_word
        self.database = database
        self.theme = theme

    def open_file(self, database):
        global Array
        with open(self.database, 'r', encoding="utf-8") as files:
            Array = files.read().splitlines()

    def check_word(self, input_word):
        global Array
        if input_word.title() in Array:
            Array.remove(input_word.title())
            return True
        else:
            return False    
        
    def check_true(self, input_word):
        global Global_array
        global Array
       
        if input_word in Global_array:
            return 'Введіть інше слово, це слово вже було використано'

        check = self.check_word (input_word)

        if check:
            x = -1
            last_letter = input_word[x].lower()
            matching_words = [word for word in Array if word.lower().startswith(last_letter)]
            
            if not matching_words:
                x = -2
                last_letter = input_word[x].lower()
                matching_words = [word for word in Array if word.lower().startswith(last_letter)]
                ret = random.choice(matching_words)
                while ret in Global_array:
                    x -= 1
                    if x < -len(input_word):
                        break
                    last_letter = input_word[x].lower()
                    matching_words = [word for word in Array if word.lower().startswith(last_letter)]
                    ret = random.choice(matching_words)

                Global_array.append(input_word.title())
                Global_array.append(ret)
                Array.remove(ret)
                return ret
            else:
                ret = random.choice(matching_words)

                while ret in Global_array:
                    x -= 1
                    if x < -len(input_word):
                        break
                    last_letter = input_word[x].lower()
                    matching_words = [word for word in Array if word.lower().startswith(last_letter)]
                    ret = random.choice(matching_words)

                Global_array.append(input_word.title())
                Global_array.append(ret)
                Array.remove(ret)
                return ret
        else:
            return 'Слово правильно введене ?' + '\n' + 'Натисніть команду:' + '\n' + '/notfound'


    def Search(self):
        self.open_file(self.database)
        global Global_array
        global Array
        global history_theme

        if len(history_theme) > 0:
            if history_theme[-1] != self.theme:
                Global_array = []
                
        if len(Global_array) > 0:
            x = len(Global_array[-1]) - 1
            last_word = Global_array[-1]
            first_letter = self.input_word[0]

            while x >= 0:
                if first_letter.title() == last_word[x].title():
                    break
                else:
                    x -= 1
            if x < 0:
                return 'Літери з якої починається ваше слово не має в минулому слові! Введіть інше:'
        
        if len(history_theme) > 1:
            if self.theme == history_theme[-2]:
                history_theme.append(self.theme)
                return self.check_true(self.input_word) 
            else:
                return self.check_true(self.input_word) 
        else:
            history_theme.append(self.theme)
            return self.check_true(self.input_word)
        
    def Recording(self, input_word, database):
        with open(database, 'a', encoding="utf-8") as file:
            file.write('\n' + input_word.title())