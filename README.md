# 🔭 Tech News 2026 Recommender

A premium, high-contrast news discovery platform. It uses **Machine Learning (TF-IDF & Cosine Similarity)** to curate personalized news feeds based on user search patterns.

## ✨ Features
- **Hyper-Personalized:** Content-based filtering engine.
- **2026 Tech Stack:** Streamlit, Scikit-Learn, and Custom Glassmorphism CSS.
- **User-Centric UI:** Minimalist centered search with real-time similarity scoring.

## 🛠️ How it Works
1. **Vectorization:** Converts news summaries into mathematical vectors using TF-IDF.
2. **Similarity:** Calculates the Cosine distance between articles to find matches.
3. **UI:** A modern, high-contrast dark mode built for quick scanning.

## 🧠 Technical Deep Dive (FAQ)

### 1. How is the recommendation engine built?
The app uses a **Content-Based Filtering** approach. 
- **Vectorization:** I used `TfidfVectorizer` to transform text into numerical feature vectors. Unlike simple word counting, TF-IDF penalizes common words (like "the" or "is") and highlights unique tech terms (like "Quantum" or "Neural").
- **Mathematical Similarity:** I implemented **Cosine Similarity** to measure the angle between two vectors. A smaller angle (closer to 1.0) indicates that the articles are contextually similar.

### 2. Why use TF-IDF instead of simple word counts?
In tech news, words like "AI" or "Technology" appear everywhere. Simple counting would make every article look similar. **TF-IDF** ensures that specific keywords—like "Solid-state battery"—carry more weight, leading to much more accurate recommendations.

### 3. How does the UI handle "Glassmorphism"?
The high-end visual style is achieved through custom CSS injection in Streamlit. 
- **Backdrop-filter:** Used `blur(10px)` to create the frosted glass effect.
- **Transparency:** Used `rgba` color values to allow the animated gradient background to peek through the cards.
- **Responsiveness:** The layout is designed to scale from desktop monitors to mobile screens seamlessly.

### 4. What was the biggest technical challenge?
**Dependency Resolution:** Deploying on Python 3.13 required careful management of the `Altair` and `Streamlit` versions to ensure the visualization libraries were compatible with the latest Python interpreter.

## 🚀 Live Demo

https://vignesh-tech-pulse.streamlit.app/
