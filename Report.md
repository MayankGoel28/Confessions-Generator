# IIIT Confessions Generator using Recurrent Neural Network

## Dataset
We scraped ~21k Confessions from Facebook pages of various US Colleges, using a Selenium Bot. This was done in reference to this project on mental health. This process took time due to the anti-bot features of Facebook which we circumvented using timeouts and random behaviour. This data had to be majorly cleaned as it was not in the UTF-8 Encoding standard we were basing our model on. Thus, we used Pandas to read the csv and encode it in UTF-8, and then only use ASCII characters from the data left. We ran multiple regular expressions on this model for cleaning, and getting read of residual encoding errors, urls and so on. Further on, to avoid dealing with the complex challenge of code-mixing, we used a modified version of the NLTK English Language Wordlist, adding text-speech to properly illustrate college languge, and then created a Non-English Rate, and removed all sentences with N-E rate above 30%. This was chosen as several words like “sooooo” or such were detected as N-E, and we wished to preserve them. This brought our dataset down to 13k sentences. This data was stored as quoted strings due to errors from automatic delimiters in CSV renderers such as Libre.
  The data obtained was US-based data, and to convert it to a iiit-based data we identified patterns withing the confessions and used regex to translate them so as to cater to iiit students.

## The Neural Network && The Database Generation

We have used a LSTM model with embeddings to capture character level dependencies.
  The embeddings layer converts the words into 256 dimensional tensors, which are then fed into the LSTM layer. The LSTM layer takes into account all the previous characters it has seen till now. The speciality of the LSTM cell is that it is able to capture long ranged dependencies as well, as is seen in the case of gender inflections. The short term dependencies helps it get the spellings correct. At the end, we put the returned sequences into a Dense layer, which now predicts the character to be output next.
  After the model has been trained for sufficient number of epochs, we start our database generation.

## Website
