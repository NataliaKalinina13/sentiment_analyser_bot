import telebot
import string
import fasttext
from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel


class SentimentAnalyzerBot:
    def __init__(self, api_token, model_path):
        self.tokenizer = RegexTokenizer()
        self.model = FastTextSocialNetworkModel(tokenizer=self.tokenizer)
        self.API_token = api_token
        self.res_dict = {
            'negative': 'негативное',
            'positive': 'позитивное',
            'neutral': 'нейтральное',
            'speech': 'является обиходным выражением'
        }
        self.bot = telebot.TeleBot(self.API_token)
        fasttext.FastText.eprint = lambda x: None
        FastTextSocialNetworkModel.MODEL_PATH = model_path

        @self.bot.message_handler(commands=['start'])
        def start(message):
            '''output a greeting after /start'''
            message_with_user_name = f'Привет, <b>{message.from_user.first_name}</b>. Я бот для анализа настроения твоего сообщения. Отправь мне любой текст'
            self.bot.send_message(message.chat.id, message_with_user_name, parse_mode='html')

        @self.bot.message_handler()
        def analyze_message(message):
            '''call the preprocessing function and conduct a sentiment-analysis'''
            preprocessed_message = self.preprocess_message(message)

            message_tokens = self.tokenizer.split(preprocessed_message)
            results = self.model.predict([str(message_tokens)])

            result_dict = dict()

            for result in results:
                for key in result:
                    if key not in result_dict:
                        result_dict[key] = 0
                    result_dict[key] += result[key]

            largest = max(result_dict, key=result_dict.get)
            response = 'Ваше сообщение ' + self.res_dict[largest]

            self.bot.reply_to(message, response)

    def preprocess_message(self, message):
        '''Lowercase text and remove punctuation'''
        low_message = message.text.lower()
        clean_punct_mess = low_message.translate(str.maketrans("", "", string.punctuation))
        return clean_punct_mess

    def run(self):
        self.bot.polling(none_stop=True)


if __name__ == '__main__':
    API_token = 'token_text'
    model_path = 'model_path'
    bot = SentimentAnalyzerBot(API_token, model_path)
    bot.run()

