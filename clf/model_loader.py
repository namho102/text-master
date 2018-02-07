from sklearn.externals import joblib

loaded_model = joblib.load('model_dump/finalized_model.sav')
vectorizer = joblib.load('model_dump/vectorizer.pk')

sentence = """"Some said they had also been contacted by people claiming to be other stars like Ryan Reynolds, Ryan Gosling and Hugh Jackman - but the vast majority said they had quickly sniffed out the deception."""
pred = loaded_model.predict(vectorizer.transform([sentence]))

print(pred[0])
