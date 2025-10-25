from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load pickles
books = pickle.load(open('books.pkl', 'rb'))  # full books dataset
popular_df = pickle.load(open('popular.pkl', 'rb'))  # popular books dataset
pt = pickle.load(open('pt.pkl', 'rb'))  # pivot table for recommendations
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))

# Merge popular_df with books to get author and image info
popular_books = popular_df.merge(books, on='Book-Title')

@app.route('/')
def index():
    # Prepare data to send to template
    books_data = zip(
        popular_books['Book-Title'],
        popular_books['Book-Author'],
        popular_books['Image-URL-M'],
        popular_books['num_ratings'],
        popular_books['avg_ratings']
    )
    return render_template('index.html', books=books_data)


@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')


@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input')

    # Check if the input exists in pt index
    if user_input not in pt.index:
        return render_template('recommend.html', message="Book not found. Please check spelling.")

    # Find similar books
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:6]

    data = []
    for i in similar_items:
        temp_df = books[books['Book-Title'] == pt.index[i[0]]].drop_duplicates('Book-Title')
        item = [
            temp_df['Book-Title'].values[0],
            temp_df['Book-Author'].values[0],
            temp_df['Image-URL-M'].values[0]
        ]
        data.append(item)

    return render_template('recommend.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
