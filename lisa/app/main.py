from time import sleep
import re
from utils import *


def process_data(quotes):
    """
    Process every quote after it's fetched from the API
    :param quotes:list Quotes that are being processed
    :return:None
    """
    columns = ['character', 'quote']
    for quote in quotes:
        row = [quote[col] for col in columns]
        if save_quote(row, quote['character']):
            # add words to counter only if the quote wasn't processed yet
            count_words(quote['quote'], quote['character'])
        save_image(quote['image'], quote['character'])


def count_words(text, character):
    """
    Count words for the current quote and aggregate them per character
    :param text:string Quote
    :param character:string Character's name
    :return:None
    """
    counter = load_word_counter(character)
    words = list(filter(None, re.split(r"[.,;?!\n\t\s\"]+", text.lower())))
    for word in words:
        counter[word] = counter.get(word, 0) + 1
    save_word_counter(counter, character)


def save_image(url, character):
    """
    Save image for a character
    :param url:string URL pointing to the image
    :param character:string Character's name
    :return:None
    """
    file_path = get_image_path(url, character)
    download_file(url, file_path)


def start_app(sleep_time, limit):
    """
    Starts the application
    :param sleep_time:int sleep time between requests
    :param limit:int number of requests that will be sent
    :return:None
    """
    api_url = 'https://thesimpsonsquoteapi.glitch.me/quotes'
    n = 0
    while n < limit:
        n += 1
        resp = get_api_data(api_url)
        if resp[0] == 200:
            process_data(json.loads(resp[1]))
        sleep(sleep_time)


if __name__ == '__main__':
    start_app(int(os.getenv('SLEEP_TIME', 30)), int(os.getenv('REQ_LIMIT', 999999999999999999999999)))

