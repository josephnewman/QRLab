from flask import Flask, render_template, request, flash, url_for
import os
import qr

app = Flask(__name__)
app.secret_key = os.urandom(12)

@app.route('/', methods=['GET', 'POST'])
def home():
    qr_img_bytes = None
    request_info = None
    if request.method == 'POST' and all(x in request.form for x in ['qrdata', 'colour', 'bg_colour']):
        request_info = {
            'qr_data': request.form['qrdata'],
            'colour': request.form['colour'] if request.form['colour'] != '' else 'black', 
            'bg_colour': request.form['bg_colour'] if request.form['bg_colour'] != '' else 'white'
        }
        try:
            qr_img_bytes = qr.make_qr(
                data = request_info['qr_data'],
                colour=request_info['colour'],
                bg_colour=request_info['bg_colour']
            )
        except:
            flash('An unexpected error occurred. Please try again.')

    return render_template('index.html', qr_img_bytes = qr_img_bytes, request_info = request_info)


if __name__ == '__main__':
    app.run(
        debug = True,
    )