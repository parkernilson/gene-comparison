import os

from flask import Flask, request, flash, redirect, send_from_directory, url_for, render_template
import matplotlib.pylab as plt

from .functions import apply_style_transfer, save_image
from .functions.parse_post_images import parse_post_images

# initialize flask app
app = Flask(__name__)

# Configure app
RESULTS_FOLDER = '/results'
app.config['RESULTS_FOLDER'] = RESULTS_FOLDER
app.config['SECRET_KEY'] = "b879ab3$$lskjb"


@app.route('/', methods=['GET'])
def home():
    """ Display the home page template """
    return render_template('style-transfer.html')


@app.route('/style-transfer', methods=['POST'])
def style_transfer():
    """ Perform style transfer on given content and style images """

    # check to see that the images given in the post request are valid
    try:
        content_image_file, style_image_file = parse_post_images(request)
    except error:
        # if the given images are not valid, flash an error and redirect to home
        flash(error)
        return redirect('/')

    # perform style transfer on them using style_transfer method
    stylized_image = apply_style_transfer(content_image_file, style_image_file)

    # save the resulting image to a static image directory
    result_filename = save_image(stylized_image, app)

    # redirect user to the resulting image
    return redirect(url_for('results', filename=result_filename))


@app.route('/results/<filename>')
def results(filename):
    """ Perform static file serving for the stylized result images """
    return send_from_directory(app.config["RESULTS_FOLDER"], filename)


@app.after_request
def dont_cache_dev_files(r):
    """ If in development environment, tell browser not to cache files """
    if os.environ["ENV"] == "development":
        r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        r.headers["Pragma"] = "no-cache"
        r.headers["Expires"] = "0"
        r.headers['Cache-Control'] = 'public, max-age=0'
    return r


if __name__ == "__main__":
    app.run(host="0.0.0.0")