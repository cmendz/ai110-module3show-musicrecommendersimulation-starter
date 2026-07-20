import csv
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file into a list of dictionaries."""
    repo_root = Path(__file__).resolve().parent.parent
    path = Path(csv_path)

    if not path.is_absolute():
        path = repo_root / path

    print(f"Loading songs from {path}...")

    songs: List[Dict] = []
    with path.open("r", encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            songs.append(
                {
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": float(row["energy"]),
                    "tempo_bpm": float(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"]),
                }
            )

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a song against a user's taste profile and explain the result."""
    score = 0.0
    reasons: List[str] = []

    favorite_genre = user_prefs.get("favorite_genre")
    favorite_mood = user_prefs.get("favorite_mood")
    target_energy = user_prefs.get("target_energy", 0.0)
    likes_acoustic = user_prefs.get("likes_acoustic", False)

    if song.get("genre") == favorite_genre:
        score += 2.0
        reasons.append("Genre matched the user's favorite genre.")
    else:
        reasons.append("Genre did not match the user's favorite genre.")

    if song.get("mood") == favorite_mood:
        score += 1.5
        reasons.append("Mood matched the user's favorite mood.")
    else:
        reasons.append("Mood did not match the user's favorite mood.")

    energy_difference = abs(song.get("energy", 0.0) - target_energy)
    energy_tolerance = 0.15

    if energy_difference <= energy_tolerance:
        score += 1.5
        reasons.append("Energy was within the user's preferred range.")
    else:
        energy_similarity = max(0.0, 1.0 - (energy_difference / 0.5))
        score += 1.5 * energy_similarity
        reasons.append("Energy was somewhat close to the user's target energy.")

    acousticness = song.get("acousticness", 0.0)
    if likes_acoustic and acousticness >= 0.6:
        score += 0.8
        reasons.append("The song was acoustic, which matched the user's preference.")
    elif likes_acoustic:
        reasons.append("The song was not acoustic enough for the user's preference.")

    return round(score, 2), reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return the top-k songs ranked by weighted relevance to the user's profile."""
    scored_songs: List[Tuple[Dict, float, str]] = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = " ".join(reasons)
        scored_songs.append((song, score, explanation))

    scored_songs.sort(key=lambda item: item[1], reverse=True)
    return scored_songs[:k]
