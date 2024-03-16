# Movie-Recommendation-System

A movie recommendation system that suggests similar films based on the chosen movie’s genre, title, or some related keywords thereby reducing inconvenience of fetching for one online.
 
The data is converted from text to vectors. Here the vector could be each word present in the tagof the movie. So if a person searches for a movie, they will be recommended the nearest vectors (movies) to that particulr vector. The project was built with the help of Python libraries such as NumPy, Pandas, scikit-learn on Jupyter notebook. The UI was developed using a python framework Streamlit. 
                        
The dataset chosen for the project was collected from kaggle.

Note: get an API key from TMDB site and insert it in the URL provided while declaring response variable under fetch_poster function in main.py. 

link to the dataset: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
