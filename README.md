# 🎬 Movie Recommendation System

A content-based movie recommendation system that suggests similar movies based on a movie you like — built with the TMDB 5000 Movies dataset, scikit-learn, and deployed as an interactive Streamlit web app.

Try it out: pick a movie from the dropdown, hit "Get Recommendations," and get 5 similar movies instantly.

---
# [try it yourself](http://machine-learning-movie-recommender-system.streamlit.app)
---

## 📌 Overview

This project recommends movies using **content-based filtering**. Instead of relying on user ratings or collaborative behavior, it analyzes each movie's *content* — its overview, genres, keywords, cast, and director — and recommends movies that are most similar in that content space.

The pipeline:
1. Clean and merge the TMDB movies and credits datasets
2. Extract and engineer a combined "tags" feature per movie (overview + genres + keywords + cast + crew)
3. Vectorize tags using a Bag-of-Words model
4. Compute pairwise **cosine similarity** between all movie vectors
5. Serve recommendations through a Streamlit UI

---

## ✨ Features

- 🔍 Search and select from thousands of movies
- 🎯 Get top 5 similar movie recommendations based on content similarity
- ⚡ Fast, cached data loading for smooth performance
- 🎨 Clean, custom-styled dark UI built with Streamlit

---

## 🗂️ Project Structure

```
movie-recommender-system/
├── movie-recommender-system.ipynb # Data preprocessing, feature engineering & model building
├── app.py # Streamlit web application
├── movies_dict.pkl # Preprocessed movie data (generated from notebook)
├── similarity.pkl # Precomputed cosine similarity matrix (generated from notebook)
├── tmdb_5000_movies.csv # Raw dataset (movies)
├── tmdb_5000_credits.csv # Raw dataset (credits)
└── README.md
```

---

## 🧠 How It Works

### 1. Data Preprocessing
- Merges `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv` on `title`
- Selects relevant columns: `movie_id`, `genres`, `keywords`, `title`, `overview`, `cast`, `crew`
- Drops missing/null values

### 2. Feature Engineering
- Converts stringified JSON columns (`genres`, `keywords`, `cast`, `crew`) into clean Python lists
- Keeps only the **top 3 cast members** and the **director** from the crew
- Splits `overview` into a list of words
- Removes spaces within multi-word names (e.g., `"Sam Worthington"` → `"SamWorthington"`) so they're treated as single tokens
- Combines `overview + genres + keywords + cast + crew` into a single `tags` column

### 3. Text Processing
- Converts tags to lowercase
- Applies **stemming** using NLTK's `PorterStemmer` to normalize words (e.g., `loving` → `love`)

### 4. Vectorization & Similarity
- Uses **`CountVectorizer`** (Bag-of-Words, top 5000 features, English stopwords removed) to convert each movie's tags into a vector
- Computes a **cosine similarity matrix** across all movie vectors

### 5. Recommendation Logic
Given a movie title, the system:
- Finds its index and similarity scores against all other movies
- Sorts by similarity score (descending)
- Returns the **top 5 most similar movies** (excluding the movie itself)

### 6. Deployment
- Preprocessed data (`new_df`) and the similarity matrix are serialized with `pickle` into `movies_dict.pkl` and `similarity.pkl`
- `app.py` loads these artifacts and serves recommendations through a Streamlit interface

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| Data Processing | Pandas, NumPy |
| NLP / ML | scikit-learn (`CountVectorizer`, `cosine_similarity`), NLTK (`PorterStemmer`) |
| Web App | Streamlit |
| Serialization | Pickle |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- The TMDB 5000 dataset ([`tmdb_5000_movies.csv`](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) and `tmdb_5000_credits.csv`)

### Installation

```bash
git clone https://github.com/dhyeysavalia01/movie-recommender-system.git
cd movie-recommender-system
```

### 1. Generate the model files
Run all cells in `movie-recommender-system.ipynb` to preprocess the data and generate `movies_dict.pkl` and `similarity.pkl`.

> These `.pkl` files are required by `app.py` but are not included in the repo (large file size) — generate them locally or download from the repo's Releases if provided.

### 2. Run the app

```bash
streamlit run app.py
```

Then open the local URL shown in your terminal (typically `http://localhost:8501`).

---

## 📦 requirements.txt

```
streamlit
pandas
numpy
scikit-learn
nltk
```

---

## 📊 Dataset

This project uses the **TMDB 5000 Movie Dataset**, containing metadata for ~5000 movies including overview, genres, keywords, cast, and crew information.

- [TMDB 5000 Movie Dataset on Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

---
