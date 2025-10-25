# Book Recommender System

A web-based Book Recommender System built using **Python, Flask, Pandas, and Pickle**. This system allows users to explore popular books and get personalized book recommendations based on a selected title.

---

## Table of Contents
- [Features](#features)  
- [Technologies Used](#technologies-used)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Project Structure](#project-structure)  
- [Screenshots](#screenshots)  
- [Future Improvements](#future-improvements)  
- [License](#license)  

---

## Features
- Display **Top 50 popular books** with title, author, rating, and image.  
- **Book recommendation** based on user input (book title).  
- Clean, responsive UI using **Bootstrap**.  
- Handles invalid inputs gracefully.  

---

## Technologies Used
- **Python 3.x** – backend logic  
- **Flask** – web framework  
- **Pandas & NumPy** – data processing  
- **Pickle** – saving/loading preprocessed data  
- **Bootstrap 3** – responsive frontend  

---

## Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/book-recommender.git
cd book-recommender


## Project Structure
book-recommender/
│
├─ app.py                # Flask application
├─ books.pkl             # Book dataset
├─ popular.pkl           # Popular books dataset
├─ pt.pkl                # Pivot table for recommendations
├─ similarity_scores.pkl # Precomputed similarity scores
├─ templates/
│   ├─ index.html        # Homepage template
│   └─ recommend.html    # Recommendation template
├─ static/
│   └─ (optional CSS/images)
├─ requirements.txt      # Project dependencies
└─ README.md             # Project documentation

