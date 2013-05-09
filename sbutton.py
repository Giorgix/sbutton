from flask import Flask, render_template
import google_img_search


#configuration
DEBUG = True
SECRET_KEY = 'development key'


#create application
app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def show_images():
    img_href = google_img_search.myUrl[0]['unescapedUrl']
    return render_template('show_images.html', img_href=img_href)


if __name__ == '__main__':
    app.run(host='192.168.1.13')
