from flask import Flask, render_template
import rarbgapi
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

client = rarbgapi.RarbgAPI()
client.search(search_string="Rick and Morty")



app = Flask(__name__)
app.config['SECRET_KEY'] = 'tpb_clone'
for torrent in client.list():
    print(torrent)

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

class SearchForm(FlaskForm):
    search_item = StringField("Pirate Search", validators=[DataRequired()])
    submit = SubmitField


if __name__ == '__main__':
    app.run()
