from crypt import methods
from flask import Flask, render_template, request
import test

app: Flask = Flask(__name__)
song_lists: dict[str, list[str]] ={}

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/about', methods=["GET", "POST"])
def about():
    if request.method == "POST":
        
        global song_lists

        player: str = request.form['player']
        name: str = request.form['name']
        if player not in song_lists.keys():
            song_lists[player] = []
        if name not in song_lists[player]:
            song_lists[player].append(name)
        # if player not in song_lists:
        #     song_lists[player] = name
        # else: 
        #     song_lists[player] += name
    return render_template('about.html')


@app.route("/success")
def success():
    test.main(song_lists)
    return render_template('success.html')




    
if __name__ == '__main__':
    app.run(debug=True)