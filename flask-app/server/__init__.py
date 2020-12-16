import os

from flask import Flask, request, flash, redirect, send_from_directory, url_for, render_template
import matplotlib.pylab as plt

from .src import apply_style_transfer, save_image

# initialize flask app
app = Flask(__name__)

RESULTS_FOLDER = '/results'
ALLOWED_EXTENSIONS = ['jpg', 'jpeg', 'png']

app.config['RESULTS_FOLDER'] = RESULTS_FOLDER
app.config['SECRET_KEY'] = "b879ab3$$lskjb"

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def home():
    return render_template('style-transfer.html')

@app.route('/style-transfer', methods=['POST'])
def style_transfer():
    """ Perform style transfer on given content and style images """

    # get the content and style images from the post request, and validate them
    if 'content_image' not in request.files or 'style_image' not in request.files:
        flash('Content image or style image were not present in the request.')
        return redirect('/')
    content_image_file = request.files['content_image']
    style_image_file = request.files['style_image']
    if content_image_file.filename == '' or style_image_file.filename == '':
        flash('A file was not selected for either the content image or the style image')
        return redirect('/')
    if content_image_file and allowed_file(content_image_file.filename) \
        and style_image_file and allowed_file(style_image_file.filename):

            # perform style transfer on them using style_transfer method
            stylized_image = apply_style_transfer(content_image_file, style_image_file)

            # save the resulting image to a static image directory
            result_filename = save_image(stylized_image, app)

            # redirect user to the resulting image
            return redirect(url_for('results', filename=result_filename))
    return '''
    <!doctype html>
    <h1>Something went wrong...</h1>
    '''

@app.route('/results/<filename>')
def results(filename):
    """ Perform static file serving for the stylized result images """
    return send_from_directory(app.config["RESULTS_FOLDER"], filename)

@app.after_request
def add_header(r):
    """
    If in development environment, tell browser not to cache files
    """
    if os.environ["ENV"] == "development":
        r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        r.headers["Pragma"] = "no-cache"
        r.headers["Expires"] = "0"
        r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == "__main__":
    app.run(host="0.0.0.0")