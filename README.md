📚 Book Recommendation System
🧠 Overview

The Book Recommendation System is a machine learning–based web app that recommends books to users based on popularity and content similarity.
It uses collaborative filtering and cosine similarity techniques to suggest relevant books and is deployed as a Flask web application.

🚀 Features

📊 Top Popular Books — Displays a list of the most popular books based on user ratings.

🔍 Personalized Recommendations — Recommends similar books to a given title.

💾 Pickle-based Model Storage — Pre-trained data and similarity models are loaded from .pkl files.

🌐 Interactive Web Interface — Built using Flask and Bootstrap for a clean, user-friendly experience.

🧩 Tech Stack
Category	Technologies
Frontend	HTML, CSS, Bootstrap
Backend	Python (Flask Framework)
ML Libraries	scikit-learn, pandas, numpy
Data Storage	Pickle Files (.pkl)
IDE Used	PyCharm
📂 Project Structure
Book-Recommendation/
│
├── app.py                  # Flask app entry point
├── book_recommender.ipynb  # Jupyter Notebook for model building
├── popular.pkl             # Pickle file for popular books data
├── pt.pkl                  # Pickle file for pivot table
├── books.pkl               # Pickle file for books dataset
├── similarity.pkl          # Pickle file for similarity matrix
├── templates/
│   ├── index.html          # Homepage template
│   ├── recommend.html      # Recommendation result page
│
├── static/
│   ├── style.css           # Custom styles
│
├── requirements.txt        # List of dependencies
└── README.md               # Project documentation

⚙️ Installation and Setup
1. Clone the Repository
git clone https://github.com/yourusername/book-recommender.git
cd book-recommender

2. Create a Virtual Environment
python -m venv venv
venv\Scripts\activate     # for Windows
source venv/bin/activate  # for Mac/Linux

3. Install Dependencies
pip install -r requirements.txt

4. Run the Flask App
python app.py


Then open your browser and go to http://127.0.0.1:5000/

🧪 How It Works

Data Preparation:

The dataset (Books, Users, Ratings) is preprocessed and filtered.

Popular books are selected based on minimum ratings and average score.

Model Building:

A user–item matrix is created using pivot tables.

Cosine similarity measures how closely books are related based on user preferences.

Web Integration:

The model is serialized into .pkl files.

Flask serves user input to generate predictions in real time.

💡 Example

Input:

"Harry Potter and the Sorcerer’s Stone"

Output Recommendations:

Harry Potter and the Chamber of Secrets

The Hobbit

Percy Jackson and the Olympians

Eragon

🧑‍💻 Developed By

Shristi Singh
B.Tech | Data Science & AI Enthusiast
📧 [wellallis057@gmail.com
]
🌐 [LinkedIn https://www.linkedin.com/in/shristisingh1312/]

🏁 Future Improvements

Add user login and personalized dashboard

Include NLP-based sentiment analysis for reviews

Deploy on cloud platforms like Render / Vercel / Hugging Face Spaces
