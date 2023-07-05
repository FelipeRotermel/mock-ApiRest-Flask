import secrets
from typing import Any, List, Dict

from flask import Flask, Response, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

movies: List[Dict[str, Any]] = [
    {"id": 1, "title": "The Godfather", "year": 1972, "genre": "Crime", "poster": "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg"},
    {"id": 2, "title": "The Shawshank Redemption", "year": 1994, "genre": "Drama", "poster": "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg"},
    {"id": 3, "title": "Schindler's List", "year": 1993, "genre": "Biography", "poster": "https://upload.wikimedia.org/wikipedia/en/3/38/Schindler%27s_List_movie.jpg"},
    {"id": 4, "title": "Raging Bull", "year": 1980, "genre": "Biography", "poster": "https://upload.wikimedia.org/wikipedia/en/5/5f/Raging_Bull_poster.jpg"},
    {"id": 5, "title": "Casablanca", "year": 1942, "genre": "Romance", "poster": "https://upload.wikimedia.org/wikipedia/commons/b/b3/CasablancaPoster-Gold.jpg"},
    {"id": 6, "title": "Call of Gruty", "year": 2021, "genre": "Comedy", "poster": "https://static.wikia.nocookie.net/unmario/images/6/68/DfVsX7yWAAIhcje.jpg/revision/latest?cb=20180708224427"},
]


@app.route("/auth", methods=["POST"])
def auth() -> Response:
    """
    Perform authentication
    """
    data: Any = request.get_json()
    if (
        {"username", "password"}.issubset(data)
        and data["username"] == "admin"
        and data["password"] == "admin"
    ):
        access_token: str = secrets.token_urlsafe()
        refresh_token: str = secrets.token_urlsafe()
        print(access_token)
        return jsonify(
            {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "status": "success",
            }
        )
    return jsonify({"status": "login failed"}), 401


@app.route("/movies", methods=["GET"])
def get_movies() -> Response:
    """
    Get all movies
    """
    return jsonify(movies)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=19004)
