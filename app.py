import streamlit
import pandas

songs = pandas.read_csv("songs.csv")

songsDataFrame = pandas.DataFrame(songs)
del songsDataFrame['Lyrics']
songsDataFrame.sort_values(by='Popularity', inplace=True)

streamlit.title("Music Data Set")
streamlit.table(songsDataFrame)