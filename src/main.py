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


def main() -> None:
    songs = load_songs("data/songs.csv")

    # Starter example profile
    user_prefs = {"favorite_genre": "pop", "favorite_mood": "happy", "target_energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)
    print_recommendations(recommendations)


if __name__ == "__main__":
    main()
