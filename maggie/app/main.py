import requests
import json
import csv
import os
from time import sleep


def init_files():
    """
    Initialise quote files if they have not been created
    """
    columns = ['character', 'quote']
    for folder in ['homer', 'lisa', 'general']:
        file_path = f'{folder}/quotes.csv'
        with open(file_path, 'w+') as fp:
            csv.writer(fp, delimiter=';').writerow(columns)


def get_api_data(url):
    """
    Send GET request to the API URL
    :param url:string URL
    :return:tuple containing the response's status code and body
    """
    resp = requests.get(url)
    return resp.status_code, resp.text


def get_file_path(character):
    """
    Returns the path to the file where the quotes of a character
    need to be saved
    :param character:string Name of the character
    :return:string path to the quotes file
    """
    folder = ''
    if character.lower().find('homer') >= 0:
        folder += 'homer'
    elif character.lower().find('lisa') >= 0:
        folder += 'lisa'
    else:
        folder += 'general'
    return f"{folder}/quotes.csv"


def save_quote(quotes):
    """
    Saves a list of quotes to their corresponding CSV file
    :param quotes:list of quotes
    :return:None
    """
    columns = ['character', 'quote']
    for quote in quotes:
        file_path = get_file_path(quote['character'])
        row = [quote[col] for col in columns]
        with open(file_path, 'a') as fp:
            csv.writer(fp, delimiter=';').writerow(row)


def start_app(sleep_time, limit):
    """
    Starts the application
    :param sleep_time:int sleep time between requests
    :param limit:int number of requests that will be sent
    :return:
    """
    api_url = 'https://thesimpsonsquoteapi.glitch.me/quotes'
    init_files()
    n = 0
    while n < limit:
        n += 1
        resp = get_api_data(api_url)
        if resp[0] == 200:
            save_quote(json.loads(resp[1]))
        sleep(sleep_time)


if __name__ == '__main__':
    start_app(int(os.getenv('SLEEP_TIME', 1)), int(os.getenv('REQ_LIMIT', 999999999999999999999999)))
