# multilingual sentiment analysis with visualization


## How the app works
* The app would take input in english language and output the sentiment of the sentence. Sentiment analysis is done in unsupervised wordlist based manner.
* there is also a summarization route which would summarize the bunch of text in a concise way. The summarizer is created using gensim library.
* for security, encryption of password using saltings and hashing techniques takes place before storing to firebase (database).
* The application is developed using Flask framework
* There is a section where user can enter their mobile app name. I've used google play store scraper to scrape and store the reviewof the app the user entered in playstore. Then bar chart and pie chart of sentiment is shown to the user. Mongodb is used to store the scrapped reviews. The plots are rendered using plotly and Flask.
* Twitter api was used to scrape trending tweets for the country id the user enters.

