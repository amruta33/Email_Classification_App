
## Email Spam Classification using NLP and ML Techniques

<div style="text-align: center; background: #ff8c00; font-family: 'Montserrat', sans-serif; color: white; padding: 15px; font-size: 30px; font-weight: bold; line-height: 1; border-radius: 20px 20px 0 0; margin-bottom: 20px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);">🚀 SMS Spam Classification: Detecting Unwanted Messages 🚀</div>  

Overview

The objective of this project is to build a classifier that can differentiate between spam and non-spam emails using Natural Language Processing (NLP) techniques and Machine Learning (ML) algorithms. The dataset consists of email messages labeled as either "ham" (non-spam) or "spam". Through the utilization of NLP methods and ML algorithms, we aim to develop a model capable of accurately classifying incoming emails as either spam or non-spam, thereby assisting in the identification and filtering of unwanted or potentially harmful messages.


Key Insights:
Imbalanced Dataset: The dataset exhibits an imbalance, with a higher proportion of spam emails.
Higher Word Counts: Spam emails tend to have higher word counts compared to non-spam emails,
as observed during Exploratory Data Analysis (EDA).

NLP Techniques Utilized:
Text Preprocessing:
Convert text to lowercase.
Tokenization: Split text into individual words.
Removal of stopwords and punctuation.
Stemming: Reduce words to their root form.

TF-IDF Vectorization:
Term Frequency-Inverse Document Frequency considers the importance of terms in the entire dataset.
  1. Term Frequency (TF): This measures how frequently a term appears in a document. It is calculated by dividing the number of occurrences of a term in a document by the total number of terms in the document.
  2. Inverse Document Frequency (IDF): This measures the rarity of a term across the entire dataset. It is calculated by taking the logarithm of the ratio of the total number of documents to the number of      documents containing the term.
This is advantageous for text classification tasks, especially with an imbalanced dataset.

ML Algorithms Employed:
Multinomial Naive Bayes (MNB):

Initially explored for its suitability in text classification tasks.
Support Vector Machine (SVM):

Demonstrated high accuracy in classifying emails.
K-Nearest Neighbors (KNN):

Achieved decent accuracy but lower precision compared to MNB and SVM.

Random Forest:

Yielded high accuracy and precision.

Ultimate Selection:
Multinomial Naive Bayes (MNB):
Chosen ultimately for its effectiveness in text classification tasks, particularly when combined with TF-IDF vectorization.
Random Forest  Accuracy: 97.69%


Further Enhancements:
Precision over Accuracy: Due to the dataset's imbalance, emphasis was placed on 
precision over accuracy in model evaluation.

TF-IDF vs Bag-of-Words: TF-IDF was chosen over Bag-of-Words due to its ability to a
ssign higher weights to rare terms, making it more suitable for imbalanced datasets.

Conclusion:
This project showcases the efficacy of Natural Language Processing (NLP) techniques when coupled with Machine Learning (ML) algorithms for the classification of spam emails. With a focus on precision, the classifier prioritizes accurately identifying spam emails while minimizing false positives. Leveraging the Multinomial Naive Bayes algorithm, the classifier demonstrates reliable performance. Through meticulous feature selection and model training, the classifier achieves a high level of accuracy in distinguishing spam from legitimate emails, thereby enhancing email security and user experience.


