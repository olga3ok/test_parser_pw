import requests
from bs4 import BeautifulSoup
import os


def get_html():
    url = 'https://pw.mail.ru/server_status.php'
    r = requests.get(url)
    return r.text

def get_status_of_server(html):
    soup = BeautifulSoup(html, 'lxml')
    t = soup.find('li', class_='even_server_status').find_all('span')
    server_status = str(t).split('=')[1][1:16]
    return server_status

def send_message(message):
    title = 'Статус сервера Саргас:'
    os.system('notify-send "{}" "{}"'.format(title, message))

def main():
    rate = get_status_of_server(get_html())
    message = ''
    if rate == 'server_status_1':
        message = 'Онлайн'
    else:
        message = 'Оффлайн'
    send_message(message)



if __name__ == '__main__':
    main()
