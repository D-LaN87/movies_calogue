from flask import Flask, render_template
import requests

app = Flask(__name__)

API_KEY = 'a604030dc8dd3bb1ae4ff45da168fd94'
API_URL = f'https://api.themoviedb.org/3/movie/popular?api_key=a604030dc8dd3bb1ae4ff45da168fd94&language=pl-PL'

@app.route('/')
def homepage():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        print("Status odpowiedzi:", response.status_code)
        print("Pełna odpowiedź JSON:", response.json())

        movies = response.json().get('results', [])
    except Exception as e:
        print(f"Błąd pobierania filmów: {e}")
        movies = []

    print("Lista filmów:", movies)
    return render_template("homepage.html", movies=movies)

if __name__ == '__main__':
    app.run(debug=True)