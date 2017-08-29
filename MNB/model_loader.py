from sklearn.externals import joblib
import numpy as np

filename = 'finalized_model2.sav'
loaded_model = joblib.load(filename)
vectorizer = joblib.load('vectorizer2.pk')

my_test = ["VR's mind tricks can teleport you into a Pixar-like world where your role and smart characters suck you deeper into the story.",
           "Nuclear radiation rearranges the electrons in insulators such as brick, glass and porcelain.",
           "He'll sell you solar rooftop tiles to generate electricity, a giant battery to store all that energy and an electric car to suck it up.",
           "Giroud scored 16 goals last season, but started only 11 Premier League matches with manager Arsene Wenger preferring to deploy Alexis Sanchez in a central striking role.",
           "A bidding war is set to break out as Cristiano Ronaldo's Bernabeu exit beckons.",
           "Instead, there could be two periods of 30 minutes with the clock stopped whenever the ball goes out of play.",
           "If you've been watching any of the hottest TV properties this season, you might have noticed that bludgeoning is kind of the new black.",
           "Adele Fans Unite for Tribute Performances of Her Songs After She Cancels Concerts",
           "A fortnight ago, fashion's glitterati were saluting the enduring legacy of Alexandra Shulman at Vogue.",
           "Founded in Malaysia in 2012, it offers private car, motorbike, taxi, and carpooling services and holds 95% market share of third-party taxi hailing in the region, operating nearly 3 million daily rides.",
           "The company suffered a year-on-year decrease in operating profits of 2.19 trillion won ($1.93 billion) in the third quarter of the 2016 fiscal year.",
           "Carillion's shares plunged after the company announced that results would be below expectations, and that CEO Richard Howson was stepping down.",
           "U.S. issues travel advisory for India amid fears of Islamic State attacks",
           "Kaine on Thursday voted to give Mattis a waiver that will allow him to bypass the requirement that Defense secretaries be out of uniform for at least seven years.",
           "Leaders are expected to brief rank-and-file Republican senators Tuesday during their weekly lunch on revisions they have made to the legislation."
           ]



# my_pred = loaded_model.predict(vectorizer.transform(my_test))
# print my_pred

sentence = """"Some said they had also been contacted by people claiming to be other stars like Ryan Reynolds, Ryan Gosling and Hugh Jackman - but the vast majority said they had quickly sniffed out the deception."""
pred = loaded_model.predict_proba(vectorizer.transform([sentence]))[0]

# print(pred)
# # print(pred.index(max(pred)))
# print(np.argmax(pred))

for prob in pred:
    print(prob)
# while True:
#     print "Enter a sentence:",
#     sentence = raw_input()
#     print(loaded_model.predict_proba(vectorizer.transform([sentence])))