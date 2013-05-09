import flask
import requests
from pprint import pprint


app = flask.Flask(__name__)
app.config.debug = True


@app.route('/')
def show_image():
    return 'y'


def get_image(search_term):

    params = {
        'v': 1.0,
        'q': search_term
    }
    headers = {
        'Referer': 'testing'
    }
    url = 'https://ajax.googleapis.com/ajax/services/search/images'
    r = requests.get(url, params=params, headers=headers)
    if r.status_code == 200:
        pprint(r.json())

if __name__ == '__main__':
    get_image('eagles')
    #app.run()
