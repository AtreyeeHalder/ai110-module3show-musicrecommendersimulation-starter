"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


DIVIDER = "─" * 52

def print_recommendations(recommendations: list) -> None:
    print(f"\n{'Top Recommendations':^52}")
    print(DIVIDER)
    for rank, (song, score, reasons) in enumerate(recommendations, start=1):
        print(f"  #{rank}  {song['title']}")
        print(f"       Artist : {song['artist']}")
        print(f"       Score  : {score:.2f}")
        print(f"       Why    :")
        for reason in reasons:
            print(f"                • {reason}")
        print()
    print(DIVIDER)


# Standard profiles
HIGH_ENERGY_POP = {
    "favorite_genre": "pop",
    "favorite_mood": "happy",
    "target_energy": 0.9,
    "likes_acoustic": False,
}

CHILL_LOFI = {
    "favorite_genre": "lofi",
    "favorite_mood": "calm",
    "target_energy": 0.2,
    "likes_acoustic": True,
}

DEEP_INTENSE_ROCK = {
    "favorite_genre": "rock",
    "favorite_mood": "angry",
    "target_energy": 0.85,
    "likes_acoustic": False,
}

# Adversarial / edge-case profiles
# Conflicting signals: high energy but sad mood.
# Exposes that mood and energy are scored independently —
# an upbeat song may outscore a genuinely sad one.
CONFLICTING_ENERGY_MOOD = {
    "favorite_genre": "pop",
    "favorite_mood": "sad",
    "target_energy": 0.9,
    "likes_acoustic": False,
}

# Genre that likely doesn't exist in the catalog.
# Top-5 are decided purely by mood + energy — effectively noise.
NO_MATCH_GENRE = {
    "favorite_genre": "k-pop",
    "favorite_mood": "happy",
    "target_energy": 0.5,
    "likes_acoustic": False,
}

# target_energy=0.5 minimises energy variance across all songs,
# making genre+mood the only real differentiators and exposing
# how near-ties are broken.
NEUTRAL_ENERGY = {
    "favorite_genre": "rock",
    "favorite_mood": "angry",
    "target_energy": 0.5,
    "likes_acoustic": False,
}

# EDM songs almost never have acousticness >= 0.5, so
# likes_acoustic=True silently contributes 0 pts every time.
ACOUSTIC_MISMATCH = {
    "favorite_genre": "edm",
    "favorite_mood": "energetic",
    "target_energy": 0.95,
    "likes_acoustic": True,
}

# Targets the theoretical max score (5.5 pts).
# Checks whether tie-breaking is stable across runs.
PERFECT_SCORE_BAIT = {
    "favorite_genre": "pop",
    "favorite_mood": "happy",
    "target_energy": 1.0,
    "likes_acoustic": True,
}


def main() -> None:
    songs = load_songs("data/songs.csv")

    profiles = [
        # Standard
        ("High-Energy Pop",          HIGH_ENERGY_POP),
        ("Chill Lofi",               CHILL_LOFI),
        ("Deep Intense Rock",        DEEP_INTENSE_ROCK),
        # Adversarial
        ("[ADV] Conflicting Energy+Mood", CONFLICTING_ENERGY_MOOD),
        ("[ADV] Impossible Genre",        NO_MATCH_GENRE),
        ("[ADV] Neutral Energy (0.5)",    NEUTRAL_ENERGY),
        ("[ADV] Acoustic+EDM Mismatch",   ACOUSTIC_MISMATCH),
        ("[ADV] Perfect-Score Bait",      PERFECT_SCORE_BAIT),
    ]

    for label, user_prefs in profiles:
        print(f"\n{'=' * 52}")
        print(f"  Profile: {label}")
        print(f"{'=' * 52}")
        recommendations = recommend_songs(user_prefs, songs, k=5)
        print_recommendations(recommendations)


if __name__ == "__main__":
    main()
