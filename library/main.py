from flask import Flask
app = Flask(__name__, static_folder='./templates/img_svg_video_icon')
from flask import render_template




@app.route("/")
def index():
    return render_template('index.html')

@app.route("/account")
def account():
    return render_template('account.html')

@app.route("/search")
def search():
    return render_template('search.html')


@app.route("/lending")
def lending():
    return render_template('lending.html')

@app.route("/return")
def areturn():
    return render_template('return.html')

@app.route("/new-book")
def new_book():
    return render_template('new-book.html')


@app.route("/keyword_update")
def keyword_update():
    return render_template('keyword_update.html')

@app.route("/inventory")
def inventory():
    return render_template('inventory.html')

@app.route("/info")
def ainfo():
    return render_template('info.html')

if __name__ == '__main__':
    app.run()
