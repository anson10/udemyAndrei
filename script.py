from translate import Translator
translate = Translator(to_lang="ja")
try:
    with open('test.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translate.translate(text)
        with open('test-ja.txt', mode='w') as my_file2:
            my_file2.write(translation)
except FileNotFoundError as e:
    print("Check your path!")