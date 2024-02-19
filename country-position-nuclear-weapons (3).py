import pandas as pd
import plotly.express as px

# Load your dataset
uploaded_file = r"c:\Users\Chaymae\Downloads\country-position-nuclear-weapons.csv"
df = pd.read_csv(uploaded_file)

# Create the choropleth map
fig = px.choropleth(df, 
                    locations='Entity', 
                    locationmode='country names', 
                    color='Nuclear weapons status',
                    hover_name='Entity', 
                    title='Nuclear Weapons Status by Entity',
                    animation_frame='Year',
                    color_continuous_scale='Blues')

# Update layout
fig.update_layout(geo=dict(showcountries=True, countrycolor="Black"))

# Show the map
fig.show()
