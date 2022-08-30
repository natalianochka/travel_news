import streamlit as st
import newspaper
import numpy as np
import pandas as pd

skift = newspaper.build('https://skift.com/news/', memoize_articles=True)

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])


st.title('Travel News')
search_choice = st.sidebar.radio('', options=['Source', 'Keyword'])

if search_choice == 'Source':
    category = st.sidebar.selectbox('Source:', options=['Skift', 
                                                          'Travel Weekly', 
                                                          'Business Travel News', 
                                                          'Business Insider', 
                                                          'Hopper', 
                                                          'PhocusWire',
                                                          'Hospitality Net'], index=2)
    
    st.write(f'{category} - {skift.description}')
    st.write(f'Recent articles from {category}:')
    st.line_chart(chart_data)    
    
elif search_choice == 'Keyword':
    search_keyword = st.sidebar.text_input('Enter Search Keyword')

    if not search_keyword:
        st.write('Please enter a search keyword')
    else:
        st.write(f'Recent articles about {search_keyword}:')