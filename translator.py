from translate import Translator
translator= Translator(to_lang="ja")
with open('Test.txt',mode='r') as source_file:
	content = source_file.read()
result = translator.translate(content)
with open('ja.txt',mode='w',encoding='utf-8') as destination_file:
	print(destination_file.write(result))