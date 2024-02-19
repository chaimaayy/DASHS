import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

st.set_page_config(page_title = 'Dashboard', 
    layout='wide',
    page_icon='💹')



import streamlit as st

# Apply external CSS style
with open('C:\\Users\\User\\Downloads\\style (1).css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# Add your Streamlit app content below...
st.markdown('<h3 style="color: green; font-size: 40px;">Dashboard</h3>', unsafe_allow_html=True)

# Divide layout into 3 columns
col1, col2, col3 = st.columns(3)

# Display metrics with bigger text for the title
col1.metric("**Dépenses mondiales pour les armes nucléaires**", "82.9 Bn USD", "USD")
col2.metric("**Nombre d'armes nucléaires dans le monde**", "12500 Armes", "unités")
col3.metric("**Nombre de tests nucléaires dans le monde depuis 1945**", "2056 Tests", "tests")



st.sidebar.header('Dashboard `description`')
st.sidebar.header('Nuclear Weapons')
st.sidebar.header('Few countries possess nuclear weapons, but some have large arsenals')
st.sidebar.write('Estimated nuclear warhead inventories, 2023')
st.sidebar.header('A lof of countries have given up obtaining nuclear weapons')
st.sidebar.write('Nuclear weapons proliferation')
st.sidebar.header('The number of nuclear weapons has declined substantially since the end of the Cold War')
st.sidebar.write('Estimated nuclear warhead stockpiles')
st.sidebar.header('Nuclear weapons tests have almost stopped')
st.sidebar.write('Number of nuclear weapons tests, 1945 to 2022')
st.sidebar.header('Many countries want to limit or abolish nuclear weapons')
st.sidebar.write('Number of countries that approve of nuclear weapons treaties')
st.sidebar.write('Country position on the Nuclear Non-Proliferation Treaty, 2023')






c1, c_space1, c2, c_space2, c3 = st.columns((2, 0.5, 2, 0.5, 2))

# Nuclear Weapons by Year
with c1:
    colors = ['#164863', '#427D9D', '#9BBEC8', '#DDF2FD']
    years = ['1940', '1950', '1960', '1970', '1980', '1990', '2000', '2010', '2020', '2021', '2022', '2023']
    countries_considering = [3, 7, 6, 9, 5, 2, 1, 1, 1, 1, 1, 1]
    countries_pursuing = [0, 1, 3, 2, 6, 5, 3, 1, 1, 1, 1, 1]
    countries_possessing = [0, 2, 4, 6, 7, 9, 8, 9, 9, 9, 9, 9]

    trace1 = go.Bar(x=years, y=countries_considering, name='Countries Considering', marker=dict(color=colors[0]))
    trace2 = go.Bar(x=years, y=countries_pursuing, name='Countries Pursuing', marker=dict(color=colors[1]))
    trace3 = go.Bar(x=years, y=countries_possessing, name='Countries Possessing', marker=dict(color=colors[2]))

    layout = go.Layout(
        title='Nuclear Weapons by Year',
        xaxis=dict(title='Year'),
        yaxis=dict(title='Number of Countries'),
        barmode='group',
        title_font=dict(color="burlywood",size=24)
    )

    fig = go.Figure([trace1, trace2, trace3], layout=layout)
    st.plotly_chart(fig)

#Nuclear Warheads Distribution by Entity
with c2:
    # Sample data for the map
    data = {
        'Entity': ['China', 'France', 'India', 'Israel', 'North Korea', 'Pakistan', 'Russia', 'United Kingdom', 'United States'],
        'Code': ['CHN', 'FRA', 'IND', 'ISR', 'PRK', 'PAK', 'RUS', 'GBR', 'USA'],
        'Year': [2023] * 9,
        'Deployed_Strategic': [0, 280, 0, 0, 0, 0, 1674, 120, 1670],
        'Deployed_NonStrategic': [0, 0, 0, 0, 0, 0, 0, 0, 100],
        'Nondeployed_Reserve': [410, 10, 164, 90, 30, 170, 2815, 105, 1938],
        'Retired': [0, 0, 0, 0, 0, 0, 1400, 0, 1536]
    }

    df = pd.DataFrame(data)
    df = df.sort_values(by='Deployed_Strategic', ascending=True)

    fig_map = go.Figure()

    colors = ['#164863', '#427D9D', '#9BBEC8', '#DDF2FD']

    for i, category in enumerate(['Deployed_Strategic', 'Deployed_NonStrategic', 'Nondeployed_Reserve', 'Retired']):
        fig_map.add_trace(go.Bar(
            x=df[category],
            y=df['Entity'],
            name=category,
            orientation='h',
            text=df[category],
            hoverinfo='text',
            marker=dict(color=colors[i])
        ))
    fig_map.update_layout(
        barmode='stack',
        yaxis=dict(title='Entity'),
        xaxis=dict(title='Number of Warheads'),
        title='Nuclear Warheads Distribution by Entity',
        title_font=dict(color="burlywood",size=24)
    )
    st.plotly_chart(fig_map)

#nuclear-warhead-stockpiles-lines
with c3:
    # Sample data for the line chart
    df_line_chart = pd.read_csv("C:\\Users\\User\\Downloads\\nuclear-warhead-stockpiles-lines.csv")

# Line chart
    fig_line_chart = px.line(df_line_chart, x='Year', y='Number of nuclear warheads', color='Entity', title='Number of Nuclear Warheads Over Time')
    fig_line_chart.update_layout(xaxis=dict(rangeslider=dict(visible=True)), xaxis_title='Year', yaxis_title='Number of Nuclear Warheads',
                                  title_font=dict(color="burlywood",size=24))
    st.plotly_chart(fig_line_chart)






c4, c5, c6 = st.columns((3, 3, 3))
#country-position-nuclear-weapons
with c4:

    uploaded_file = "C:\\Users\\User\\Downloads\\country-position-nuclear-weapons (1).csv"
    df = pd.read_csv(uploaded_file)


    def render_choropleth_map(df):
        fig = px.choropleth(df, 
                            locations='Entity', 
                            locationmode='country names', 
                            color='Nuclear weapons status',
                            hover_name='Entity', 
                            title='Nuclear Weapons Status by Entity',
                            animation_frame='Year',
                            color_continuous_scale='Blues')

   
        fig.update_layout(geo=dict(showcountries=True, countrycolor="Black"), title_font=dict(color="burlywood",size=24))

    
        st.plotly_chart(fig, use_container_width=True)  # Utilize c4 size


    def main():
    
        render_choropleth_map(df)

    if __name__ == '__main__':
        main()




#number-of-nuclear-weapons-tests
with c5:

    csv_file_path = 'C:\\Users\\User\\Downloads\\number-of-nuclear-weapons-tests (1)1.csv'
    df = pd.read_csv(csv_file_path)

    df = df[['Entity', 'Year', 'Number of nuclear weapons tests']]

    country_codes = {
        'China': 'CHN',
        'France': 'FRA',
        'India': 'IND',
        'North Korea': 'PRK',
        'Pakistan': 'PAK',
        'Russia': 'RUS',
        'United Kingdom': 'GBR',
        'United States': 'USA'
}
    df['Country Code'] = df['Entity'].map(country_codes)
    grouped = df.groupby(['Country Code', 'Year']).sum().unstack(level=0)
    traces = []
    colors = ['blue', 'deepskyblue', 'darkcyan', 'dodgerblue', 'purple', 'darkslategray', 'mediumslateblue', 'cadetblue']  # USA is red

    for country, color in zip(grouped.columns.get_level_values(1), colors):
        trace = go.Bar(x=grouped.index, y=grouped['Number of nuclear weapons tests'][country], name=country, marker_color=color)
        traces.append(trace)
    fig = go.Figure(data=traces)
    fig.update_layout(
        barmode='stack',
        xaxis=dict(title='Year', tickvals=grouped.index[::5], ticktext=grouped.index[::5]),
        yaxis=dict(title='Number of Nuclear Weapons Tests'),
        title='Nuclear Weapons Tests by Country (1945-2022)',
        title_font=dict(color="burlywood",size=24),
        legend_title='Country'
)
    st.plotly_chart(fig, use_container_width=True)  # Utilize c5 size




with c6:
    blue_palette = ['#0000FF', '#1E90FF', '#4682B4', '#87CEEB', '#87CEFA', '#00BFFF', '#87CEEB']
    df = pd.read_csv('C:\\Users\\User\\Downloads\\approve 1 (3).csv')
    columns_of_interest = ['Year', 
                           ' Comprehensive Nuclear-Test-Ban Treaty', 
                           ' Nuclear Non-Proliferation Treaty',
                           'Prohibition of Nuclear Weapons',
                           'Partial Test Ban Treaty']
    df = df[columns_of_interest]
    df.set_index('Year', inplace=True)
    df_melted = df.melt(ignore_index=False).reset_index()
    fig = px.line(df_melted, x='Year', y='value', color='variable',
                title='Historical Trend of Number of Countries with Status on Nuclear Treaties',
                labels={'value': 'Number of Countries', 'variable': 'Treaty', 'Year': 'Year'},
                color_discrete_sequence=blue_palette)
    fig.update_layout(xaxis_title='Year', 
                      yaxis_title='Number of Countries', 
                      legend_title="Treaties",
                      legend=dict(
                          orientation="v",
                          yanchor="top",
                          y=0.99,
                          xanchor="left",
                          x=1.02,
                          font=dict(size=8)  # Adjust legend font size
                      ),
                      font=dict(
                          family="Arial",
                          size=12,
                          color="black"
                      ),
                      plot_bgcolor='rgba(0,0,0,0)',
                      xaxis=dict(showgrid=True),
                      yaxis=dict(showgrid=True),
                      width=600,  
                      height=450, 
                      title=dict(
                        text="Historical Trend of Number of Countries with Status on Nuclear Treaties",
                        font=dict(size=24, color="burlywood")
                     )                
                )
    st.plotly_chart(fig)
