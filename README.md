# 🎵 Music Recommender Simulation

## Project Summary

This project builds a simple music recommender that reads songs from a CSV file, compares them to a user’s taste profile, and ranks them based on genre, mood, energy, and acoustic preference. The system uses a weighted scoring approach to generate recommendations and explain why each song was selected. It also includes a small command-line simulation so the recommendations can be viewed clearly for different example users.

---

## How The System Works

Collaborative filtering and content based filtering are two types of approaches that recommendation systems use to help predict which items a user will like based on patters in data. This system used a simple content-based approach:

  - It looks at the features of each song
  - Compares features to the user's preferences
  - Gives each song a scored based on how well it matches
  - Ranks songs and recommends the best ones

Features of the Song objects:

  - id
  - title
  - artist
  - genre
  - mood
  - energy
  - tempo_bpm
  - valence
  - danceability
  - acousticness

Features of the UserProfile objects:

  - favorite_genre
  - favorite_mood
  - target_energy
  - likes_acoustic

Songs are chosen by comparing each song's features to the user's preferences, giving each song a score, and then ranking the songs from highest score to lowest. The songs with the best match are recommended first.
---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
User Profile
-----------
Favorite genre: pop
Favorite mood: happy
Target energy: 0.80
Likes acoustic: False

Loaded songs from CSV:

- Sunrise City by Neon Echo | genre=pop | mood=happy | energy=0.82
- Midnight Coding by LoRoom | genre=lofi | mood=chill | energy=0.42
- Storm Runner by Voltline | genre=rock | mood=intense | energy=0.91
- Library Rain by Paper Lanterns | genre=lofi | mood=chill | energy=0.35
- Gym Hero by Max Pulse | genre=pop | mood=intense | energy=0.93
- Spacewalk Thoughts by Orbit Bloom | genre=ambient | mood=chill | energy=0.28
- Coffee Shop Stories by Slow Stereo | genre=jazz | mood=relaxed | energy=0.37
- Night Drive Loop by Neon Echo | genre=synthwave | mood=moody | energy=0.75
- Focus Flow by LoRoom | genre=lofi | mood=focused | energy=0.40
- Rooftop Lights by Indigo Parade | genre=indie pop | mood=happy | energy=0.76
- Golden Hour Drive by Marina Vale | genre=indie folk | mood=nostalgic | energy=0.58
- Electric Skyline by Nova Pulse | genre=electronic | mood=upbeat | energy=0.84
- Blackout Harbor by Iron Harbor | genre=metal | mood=dark | energy=0.95
- Soft Horizon by Willow Reed | genre=folk | mood=calm | energy=0.31
- Velvet Streets by The Blue Hour | genre=blues | mood=melancholy | energy=0.49
- Sunset Parade by Carina & Co | genre=reggae | mood=laid-back | energy=0.54
- Neon Dreamscape by Pixel Harbor | genre=synthpop | mood=dreamy | energy=0.70
- Winter Window by The Cedar Choir | genre=classical | mood=peaceful | energy=0.22

Top recommendations:

- Sunrise City by Neon Echo | Score: 5.00 | Why: Genre matched the user's favorite genre. Mood matched the user's favorite mood. Energy was within the user's preferred range.
- Gym Hero by Max Pulse | Score: 3.50 | Why: Genre matched the user's favorite genre. Mood did not match the user's favorite mood. Energy was within the user's preferred range.
- Rooftop Lights by Indigo Parade | Score: 3.00 | Why: Genre did not match the user's favorite genre. Mood matched the user's favorite mood. Energy was within the user's preferred range.
- Storm Runner by Voltline | Score: 1.50 | Why: Genre did not match the user's favorite genre. Mood did not match the user's favorite mood. Energy was within the user's preferred range.
- Night Drive Loop by Neon Echo | Score: 1.50 | Why: Genre did not match the user's favorite genre. Mood did not match the user's favorite mood. Energy was within the user's preferred range.

```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

After doubling the importance of energy and halving the importance of genre, most of the recommendation stayed consistent with an exception of a swap in positions in two of the user profiles. This could indicate that the recommender is not very sensitive to those particular features, or that the songs already had very similar values across the affected attributes. Songs with a certain genre might have similar numbers in energy, meaning the scores would still stay consistent. 

---

## Limitations and Risks

The experiments show that the recommender is not as senstive to the weighing choices, which can be a positive sign that the top recommendations are robust. However, consistency may also indicate that the system is still using a simple scoring approach, as it does not capture a majority of the attributes that exist like tempo_bpm, valence, danceability, acousticness, etc. The library is also relatively small, which limits how well the system can generalize to a much wider catalogue of songs. Finally, the system could also be too narrow or predictable with the recommendations, as at times, songs can have overlapping attributes, such as a rock song not always being high energy, but rather low instead.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

This project showed me that recommender systems turn simple data into predictions by assigning scores to different features and ranking items from best match to worst match. I also learned that even a small rule-based system can reflect bias, because it may favor certain genres, moods, or energy levels more than others and therefore make some users feel underrepresented. The AI coding assistant in VSCode was very useful in helping create ideas and explain concepts that could have been difficult to understand at first. It was very exciting to build and learn how a small scale recommendation system works for music, as it's an area I would like to work on in the future with the help of machine learning and artificial intelligence.



