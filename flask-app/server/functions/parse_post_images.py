ALLOWED_EXTENSIONS = ['jpg', 'jpeg', 'png']

def allowed_file(filename):
    """ True if the given filename represents an allowed file for upload """
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def parse_post_images(request):
    # get the content and style images from the post request, and validate them
    if 'content_image' not in request.files or 'style_image' not in request.files:
        raise 'Content image or style image were not present in the request.'

    content_image_file = request.files['content_image']
    style_image_file = request.files['style_image']

    if content_image_file.filename == '' or style_image_file.filename == '':
        raise 'A file was not selected for either the content image or the style image'

    if content_image_file and allowed_file(content_image_file.filename) \
        and style_image_file and allowed_file(style_image_file.filename):
        return content_image_file, style_image_file
    else:
        raise 'Something went wrong while parsing the given images'