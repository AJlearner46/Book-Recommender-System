import streamlit as st
import pickle
import numpy as np

popular_df = pickle.load(open('popular.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))


st.title('Book  Recommender System')

user_input = st.selectbox('Select A Book :-', list(popular_df['Book-Title'].values))

if st.button('Show Recommendation'):
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted((enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

    st.write("Recommended Books:")

    columns = st.columns(4)

    for i, (book_index, score) in enumerate(similar_items):
        
        temp_df = books[books['Book-Title'] == pt.index[book_index]]


        if not temp_df.empty:
            book_title = temp_df['Book-Title'].values[0]
            book_author = temp_df['Book-Author'].values[0]
            book_image = temp_df['Image-URL-M'].values[0]
            
            with columns[i % 4]:  # Distribute books evenly across the four columns
                st.image(book_image, use_column_width=True)
                st.write(f"Title: {book_title}")
                st.write(f"Author: {book_author}")
                st.write(f"Score: {round(score, 2)}")
                         
    


st.sidebar.write("--> About this App : ")
st.sidebar.write("This app recommends books based on the book you select from the sidebar. It uses a similarity matrix to find books with similar content and recommends them to you.")