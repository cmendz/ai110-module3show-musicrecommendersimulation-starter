# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

SoundSense

---

## 2. Intended Use  

This recommender suggests songs for a simple classroom-style music simulation. It assumes the user has a favorite genre, mood, energy level, and sometimes an acoustic preference.

---

## 3. How the Model Works  

The model scores songs by comparing them to a user’s genre, mood, energy, and acoustic preference. Songs that match these traits more closely get higher scores and appear earlier in the recommendations.

---

## 4. Data  

The dataset contains 18 songs with features like genre, mood, energy, tempo, valence, danceability, and acousticness. It is small, so it is useful for a simple demo but not for full-scale personalization.

---

## 5. Strengths  

The system works well for simple profiles, such as users who prefer a certain genre, mood, or energy level. It also gives easy-to-understand explanations for why each song was recommended.

---

## 6. Limitations and Bias 

The model is limited by its small dataset and simple rule-based scoring. It does not consider deeper factors like artist loyalty, lyrics, listening history, or cultural context, so it can overvalue obvious matches and miss more personal taste.

---

## 7. Evaluation  

I evaluated the recommender by testing three distinct user profiles: a pop/happy/high-energy user, a lofi/chill/low-energy user, and a rock/intense/high-energy user. For each profile, I looked for whether the top recommendation matched the user's stated genre, mood, and energy preferences, and whether the explanations made sense. I was especially interested in whether the system could distinguish between calm/friendly songs and more energetic tracks. The results were able to show this, since they were mostly intuitive. Songs with different genres still ranked well when their energy and mood aligned closely with the profile. However, it is noted that this is based on the scoring system as well, and changes to the system could result in variability.

---

## 8. Future Work  

I would add more user features, expand the dataset, and improve the diversity of recommendations. I would also make the explanations more detailed and support more complex taste profiles.

---

## 9. Personal Reflection  

This project showed me that even simple recommender systems can make intuitive suggestions when the rules are clear. I also learned that small design choices, like weighting features differently, can strongly change the results.

## 10. Terminal Output Of All Profiles (EXTRA)

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

User Profile
-----------
Favorite genre: pop
Favorite mood: happy
Target energy: 0.80
Likes acoustic: False

Top recommendations:

- Sunrise City by Neon Echo | Score: 5.00 | Why: Genre matched the user's favorite genre. Mood matched the user's favorite mood. Energy was within the user's preferred range.
- Gym Hero by Max Pulse | Score: 3.50 | Why: Genre matched the user's favorite genre. Mood did not match the user's favorite mood. Energy was within the user's preferred range.
- Rooftop Lights by Indigo Parade | Score: 3.00 | Why: Genre did not match the user's favorite genre. Mood matched the user's favorite mood. Energy was within the user's preferred range.
- Storm Runner by Voltline | Score: 1.50 | Why: Genre did not match the user's favorite genre. Mood did not match the user's favorite mood. Energy was within the user's preferred range.
- Night Drive Loop by Neon Echo | Score: 1.50 | Why: Genre did not match the user's favorite genre. Mood did not match the user's favorite mood. Energy was within the user's preferred range.
----------------------------------------

User Profile
-----------
Favorite genre: lofi
Favorite mood: chill
Target energy: 0.35
Likes acoustic: True

Top recommendations:

- Midnight Coding by LoRoom | Score: 5.80 | Why: Genre matched the user's favorite genre. Mood matched the user's favorite mood. Energy was within the user's preferred range. The song was acoustic, which matched the user's preference.
- Library Rain by Paper Lanterns | Score: 5.80 | Why: Genre matched the user's favorite genre. Mood matched the user's favorite mood. Energy was within the user's preferred range. The song was acoustic, which matched the user's preference.
- Focus Flow by LoRoom | Score: 4.30 | Why: Genre matched the user's favorite genre. Mood did not match the user's favorite mood. Energy was within the user's preferred range. The song was acoustic, which matched the user's preference.
- Spacewalk Thoughts by Orbit Bloom | Score: 3.80 | Why: Genre did not match the user's favorite genre. Mood matched the user's favorite mood. Energy was within the user's preferred range. The song was acoustic, which matched the user's preference.
- Coffee Shop Stories by Slow Stereo | Score: 2.30 | Why: Genre did not match the user's favorite genre. Mood did not match the user's favorite mood. Energy was within the user's preferred range. The song was acoustic, which matched the user's preference.
----------------------------------------

User Profile
-----------
Favorite genre: rock
Favorite mood: intense
Target energy: 0.90
Likes acoustic: False

Top recommendations:

- Storm Runner by Voltline | Score: 5.00 | Why: Genre matched the user's favorite genre. Mood matched the user's favorite mood. Energy was within the user's preferred range.
- Gym Hero by Max Pulse | Score: 3.00 | Why: Genre did not match the user's favorite genre. Mood matched the user's favorite mood. Energy was within the user's preferred range.
- Sunrise City by Neon Echo | Score: 1.50 | Why: Genre did not match the user's favorite genre. Mood did not match the user's favorite mood. Energy was within the user's preferred range.
- Rooftop Lights by Indigo Parade | Score: 1.50 | Why: Genre did not match the user's favorite genre. Mood did not match the user's favorite mood. Energy was within the user's preferred range.
- Electric Skyline by Nova Pulse | Score: 1.50 | Why: Genre did not match the user's favorite genre. Mood did not match the user's favorite mood. Energy was within the user's preferred range.