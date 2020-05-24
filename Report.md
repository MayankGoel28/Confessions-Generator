# IIIT Confessions Generator using Recurrent Neural Network

## Dataset

We scraped ~21k Confessions from Facebook pages of various US Colleges, using a Selenium Bot. This was done in reference to this project on mental health. This process took time due to the anti-bot features of Facebook which we circumvented using timeouts and random behaviour. This data had to be majorly cleaned as it was not in the UTF-8 Encoding standard we were basing our model on. Thus, we used Pandas to read the csv and encode it in UTF-8, and then only use ASCII characters from the data left. We ran multiple regular expressions on this model for cleaning, and getting read of residual encoding errors, urls and so on. Further on, to avoid dealing with the complex challenge of code-mixing, we used a modified version of the NLTK English Language Wordlist, adding text-speech to properly illustrate college languge, and then created a Non-English Rate, and removed all sentences with N-E rate above 30%. This was chosen as several words like “sooooo” or such were detected as N-E, and we wished to preserve them. This brought our dataset down to 13k sentences. This data was stored as quoted strings due to errors from automatic delimiters in CSV renderers such as Libre.

## The Neural Network

## Website
