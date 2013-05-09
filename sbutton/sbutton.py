import flask
import requests


app = flask.Flask(__name__)


@app.route('/images')
def show_image():

    image_num = int(flask.request.args.get('image_num', 0))
    image_num += 1

    url = get_image('eagles', image_num)
    return flask.render_template(
        'show_images.html',
        img_href=url,
        image_num=image_num
    )


def get_image(search_term, image_num=0):

    params = {
        'v': 1.0,
        'q': search_term,
        'start': image_num
    }
    headers = {
        'Referer': 'testing'
    }
    url = 'https://ajax.googleapis.com/ajax/services/search/images'
    r = requests.get(url, params=params, headers=headers)

    if r.status_code == 200:
        images_data = r.json()['responseData']
        images = images_data['results']

        image_urls = [image['url'] for image in images]
        return image_urls[0]

if __name__ == '__main__':
    app.run(debug=True)
