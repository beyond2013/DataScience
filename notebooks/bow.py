from keras.preprocessing.text import Tokenizer

docs = [
  'the cat sat',
	'the cat sat in the hat',
	' the cat with the hat'
	]

tokenizer = Tokenizer()
tokenizer.fit_on_texts(docs)
print(f'Vocabulary: {list(tokenizer.word_index.keys())}')
vectors = tokenizer.texts_to_matrix(docs, mode='count')
print(vectors)
