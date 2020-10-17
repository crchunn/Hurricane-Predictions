
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<webpage.html>/')
def render_static(page_name):
    return render_template('%s.html' % page_name)</string:page_name>

if __name__ == '__main__':
    app.run()
