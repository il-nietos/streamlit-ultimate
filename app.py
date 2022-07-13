import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px 
from PIL import Image
import pandas as pd
import streamlit as st



# --------------------------------------------------#
# Extras: 

# navigation bar: https://www.youtube.com/watch?v=hEPoto5xp3k&ab_channel=CodingIsFun
# nav bar: https://github.com/Sven-Bo/streamlit-navigation-menu


# --------------------------------------------------#
# Data for clustering

# Players
players = pd.read_csv('data/cluster_players.csv')
players.dropna(inplace=True)
df = pd.read_csv('data/EDA_data.csv')
# Teams
# teams = pd.read_csv('cluster_teams.csv')
# teams.dropna(inplace=True)

# --------------------------------------------------#

# Banner
image = Image.open('static/images/frisbee3.png')
new_image = image.resize((1700, 600))
st.image(new_image)

# --------------------------------------------------#

# Title
st.title('Team and player analytics for frisbee lovers')
#st.write('Exploring the American Ultimate Disc League (AUDL) data')

# --------------------------------------------------#
## DROP Files 

def my_widget(key):
    st.subheader('Team analysis')
    return st.button(key + 'performing teams')

# This works in the main area
my_expander = st.expander("Expand", expanded=True)
with my_expander:
    clicked = my_widget("Best ")

url3 = "https://www.ultianalytics.com/getting-started.html"

#{st.write("[UltiAnalytics app](%s)" % url3)}
st.file_uploader('Upload an UltiAnalytics csv file', type=['csv'], help='Upload the UltiAnalytics App to get started with data collection')



# --------------------------------------------------#
# Plots in main page

def my_widget(key):
    st.subheader('AUDL team analysis')
    return st.button(key + 'performing teams')

# This works in the main area
my_expander = st.expander("Expand", expanded=True)
with my_expander:
    clicked = my_widget("Best ")

# And within an expander
my_expander = st.expander("Expand", expanded=True)
with my_expander:
    clicked = my_widget("Worst ")

# AND in st.sidebar!
#with st.sidebar:
 #   clicked = my_widget("Worst")

# --------------------------------------------------#
# Scatterplot

# TEAM analysis
team_options = df['team'].unique().tolist()

# Filter data based on user selection
team =st.selectbox['What team do you want to analyse', team_options, 0]

df = df[df['team'] == team]

#fig = px.scatter(df, x="te", y="score", color="team", size="score", hover_data=["team", "score"])

fig.update_layout(width=800)
st.write(fig)


# RANK analysis
rank_options = df['rank'].unique().tolist()

# Filter data based on user selection
rank =st.selectbox['What level', rank_options, 0]
df = df[df['rank'] == rank]

fig = px.scatter(df, x="rank", y="score", color="team", size="score", hover_data=["team", "score"])

fig.update_layout(width=800)
st.write(fig)

# --------------------------------------------------#
## DROP TEAM DATA 




# --------------------------------------------------#
# SIDEBAR

#Adding a sidebar to the app
st.sidebar.title("Explore players!") 


# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Cluster",
        ("Players", "Teams")
    )


# LINKS
with st.sidebar:
    url = "https://github.com/il-nietos"
    st.write("[Check out the source code](%s)" % url)



with st.sidebar:
    url2 = "https://wudl.ca/ultimate-terminology"
    st.write("[Check out Ultimate terminology](%s)" % url2)


# --------------------------------------------------#

st.subheader('Star players')
