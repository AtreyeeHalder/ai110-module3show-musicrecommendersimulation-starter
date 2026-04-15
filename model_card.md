# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

A limitation of this system is that catalog skew systematically disadvantages low-energy listeners. Of the 17 songs in the dataset, 9 have an energy level above 0.7, while only 5 fall below 0.4. Thus, high-energy genres like rock, pop, metal, and EDM are more represented in the data than calm genres like ambient, classical, and folk. Because the energy similarity score rewards closeness to the user's target, a low-energy listener (for example, a user who prefers ambient or sleep music near energy 0.1) has far fewer songs that can score well on energy, and the songs that do appear near their target are also spread across unrelated genres and moods. During testing, the "Chill Lofi" profile consistently surfaced acoustic songs from non-lofi genres in its top 5 simply because they happened to sit near the right energy value, not because they were stylistically close. This means the system quietly delivers worse recommendations to users with quieter tastes, not because of a flaw in the scoring formula itself, but because the data it scores against was never balanced to represent them fairly.

---

## 7. Evaluation  


Eight profiles were tested: three standard (High-Energy Pop, Chill Lofi, Deep Intense Rock) and five adversarial (Conflicting Energy+Mood, Impossible Genre, Neutral Energy, Acoustic+EDM Mismatch, Perfect-Score Bait). For each run, the goal was to check whether the top-ranked song felt like something a real listener would actually want, and whether the score reasons honestly explained the result. Some results I found interesting are:

High-Energy Pop vs. Chill Lofi: These two profiles are at opposite energy extremes and the results reflected that; uptempo pop at the top of one, quiet lofi at the top of the other. However, I found it surprising that Chill Lofi never matched on mood once. The user preference said "calm" but every lofi song in the catalog is labeled "chill." The system treated those as a complete mismatch even though they mean nearly the same thing to a real person.

Conflicting Energy+Mood vs. High-Energy Pop: Swapping mood from "happy" to "sad" reshuffled the top results, but the system still returned energetic, upbeat songs because no pop songs with a sad mood exist in the dataset. The mood signal never fired at all. The system had no way to say that there are no matches for the user's preferences and just quietly returned the wrong thing.

Impossible Genre vs. Neutral Energy: Both disable one major signal. Impossible Genre (k-pop) means the genre bonus never fires. Neutral Energy (target 0.5) means energy scores bunch together and barely separate songs. In both cases the middle rankings felt arbitrary. Small coincidences in the data determined third versus fifth place.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
