import logics

input_word = 'Привіт'
database = 'Data\\test.txt'
theme = 'test'

test = logics.Search(input_word, database, theme).Search()
print(test)
