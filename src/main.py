"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

try:
    from .recommender import load_songs, recommend_songs
except ImportError:
    from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    user_prefs = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.8,
        "likes_acoustic": False,
    }

    print("\nUser Profile")
    print("-----------")
    print(f"Favorite genre: {user_prefs['favorite_genre']}")
    print(f"Favorite mood: {user_prefs['favorite_mood']}")
    print(f"Target energy: {user_prefs['target_energy']:.2f}")
    print(f"Likes acoustic: {user_prefs['likes_acoustic']}")
    print()

    print("Loaded songs from CSV:\n")
    for song in songs:
        print(
            f"- {song['title']} by {song['artist']} "
            f"| genre={song['genre']} | mood={song['mood']} | energy={song['energy']:.2f}"
        )

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")
    for song, score, explanation in recommendations:
        print(
            f"- {song['title']} by {song['artist']} | "
            f"Score: {score:.2f} | Why: {explanation}"
        )


if __name__ == "__main__":
    main()
