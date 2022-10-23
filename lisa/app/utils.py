import requests
import json
import os
import csv
from urllib.parse import unquote


def init_folder(name):
    """
    Initialise a character's folder and quote file if they have not been created yet
    """
    columns = ['character', 'quote']
    if not os.path.isdir(name):
        os.mkdir(name)
    with open(f'{name}/quotes.csv', 'w+') as fp:
        csv.writer(fp, delimiter=';').writerow(columns)


def get_image_path(url, character):
    """
    Resolves path and file name to save a character's image
    :param url:string URL pointing to the image file
    :param character:string Character's name
    :return:string Full path to the image file
    """
    url = unquote(url)
    file_name = url.rsplit('/', 1)[1].rsplit('?', 1)[0]
    return f"{character}/{file_name}"


def get_quotes_path(character):
    """
    Returns the path to the file where the quotes of a character
    need to be saved
    :param character:string Name of the character
    :return:string path to the quotes file
    """
    file_path = f'{character}/quotes.csv'
    if not os.path.isfile(file_path):
        init_folder(character)
    return file_path


def download_file(url, file_path):
    """
    Download and save a file if it has not been downloaded yet
    :param url:string URL to the file being downloaded
    :param file_path:string Path where the file needs to be saved
    :return:None
    """
    if os.path.isfile(file_path):
        return

    resp = requests.get(url, allow_redirects=True)
    if resp.status_code == 200:
        open(file_path, 'wb').write(resp.content)


def save_quote(row, character):
    """
    Saves a quote to its corresponding CSV file. Duplicates are skipped.
    :param row:list Quote data
    :param character:string Character's name
    :return:bool True when the quote is new, False if it was already in the file
    """
    file_path = get_quotes_path(character)
    # Fetch all rows to check if the current row has been already processed.
    # This might not be efficient for high volume & velocity, but for
    # the scope of this problem it's not a big deal.
    with open(file_path, 'r') as fp:
        reader = csv.reader(fp, delimiter=';')
        rows = list(reader)

    if row in rows:
        return False
    else:
        # Append row only if it's not in the file
        with open(file_path, 'a') as fp:
            csv.writer(fp, delimiter=';').writerow(row)
        return True


def get_api_data(url):
    """
    Send GET request to the API URL
    :param url:string URL
    :return:tuple containing the response's status code and body
    """
    resp = requests.get(url)
    return resp.status_code, resp.text


def load_word_counter(character):
    """
    Load word counter for a character
    :param character:string Character's name
    :return:dict The word counter for this character
    """
    file_path = f"{character}/counter.json"
    return load_counter_file(file_path)


def load_counter_file(file_path):
    """
    Reads and parses to JSON a word counter file
    :param file_path:string Path to the file
    :return:dict The word counter if the file exists. Otherwise, returns an empty dict.
    """
    if os.path.isfile(file_path):
        with open(file_path) as fp:
            raw_str = fp.read()
            return json.loads(raw_str.replace('\n', ''))
    else:
        return {}


def save_word_counter(counter, character):
    """
    Dumps the word counter to a file
    :param counter:dict A word counter dictionary
    :param character:string Character's name to whom the word counter belongs to.
    :return:None
    """
    file_path = f"{character}/counter.json"
    with open(file_path, 'w+') as fp:
        return json.dump(counter, fp)
