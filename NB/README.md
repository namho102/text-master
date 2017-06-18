# Naive-Bayes-Classifier-for-Document-Classification

This project classifies research articles. Raw training data is present in text format in MLDocs folder. 
To run the classifier:
 	1. Run pre_processing.py to pre process training data:
		bash$ python pre_processing.py
	2. Run log.py to classify the articles. on running log.py prompts the user to enter the number of articles to be classified and then
	   the path of each of the research articles is to be given. The classifier classifies each of the articles and outputs the result.
		bash$ python log.py


Currently the classifier has a vocabualary of 1000 words and the accuracy was found to be 84%.

