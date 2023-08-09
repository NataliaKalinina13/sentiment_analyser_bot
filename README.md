Sometimes it can be really useful to understand which messages have negative or positive coloring. Especially if we’re talking about chat moderation. Instead of calling an admin (house chats are a sore topic!), it’s more convenient to enable automation of cleaning messages with a negative component, for example, insults or obscene language. So, this bot can be used for this aim.

Since I decided to work with the Russian language, the choice fell on the Dostoevsky python library. This model was trained on RuSentiment dataset and achieves up to ~0.71 F1 score.

So, lemmatization and stop-word removing depend on the specifics of your task. I decided not to use these two aspects. Moreover, Dostoevsky provides a model for sentiment-analysis that can work with raw texts. It means that you can transfer texts directly to the library without steps mentioned above.

However, lemmatization and stop-word removing can increase accuracy. If your task requires an accurate sentiment-analysis and you are dealing with a large amount of texts, in this case you should lemmatize and delete stop words before transferring texts to the Dostoevsky library. 

The Dostoevsky classifies the text into 5 classes:
- negative;
- positive;
- neutral;
- speech act (formal greetings, thank-you and congratulatory posts);
- the "skip" class is for unclear cases.

In this project I’m interested only in negative, positive and neutral classes. Also remember that Dostoevsky doesn’t consider emojis as a component of tonality.

Let’s have a look at the algorithm of sentiment-analyzer implemented as a telegram-bot.
<img width="239" alt="image" src="https://github.com/NataliaKalinina13/sentiment_analyser_bot/assets/85068191/281b8c5c-cc0e-4754-9816-6e738ac3bd50">


And this is the result! Soon I’ll improve it and test new models, but now that’s it))
<img width="599" alt="image" src="https://github.com/NataliaKalinina13/sentiment_analyser_bot/assets/85068191/b4b5fe3a-72a1-4e77-946b-25a0f437e31f">



Don't forget to install requirements and download model weights for sentiment analysis (https://storage.b-labs.pro/models/fasttext-social-network-model.bin)

FastTextSocialNetworkModel.MODEL_PATH = '/<some_folders>/fasttext-social-network-model.bin' model = FastTextSocialNetworkModel(tokenizer=tokenizer)

