"""
CO2 Emissions Visualization
This Python application is designed to visualize global CO2 emissions data using 
an interactive web-based interface. It leverages the Taipy GUI framework to 
create a dynamic and responsive app that displays CO2 emissions across different 
countries and years through a choropleth map and accompanying data tables.

Copyright Alan Jones, 2024
MIT license - attribution appreciated

"""
from taipy.gui import Gui 
import taipy.gui.builder as tgb
import pandas as pd
import plotly.express as px

# Define the global (state) data 

df_all_countries = pd.read_csv('co2_total.csv')
df_all_countries = df_all_countries.drop(columns=['Unnamed: 0'])
df_world = pd.read_csv('co2_total_world.csv')
df_world = df_world.drop(columns=['Unnamed: 0'])

col = 'Annual CO₂ emissions'            # the column that contains the emissions data
max = df_all_countries[col].max()       # maximum emissions value for color range
min = df_all_countries[col].min()       # minimum emissions value for color range
ymax = 2021 #df_total["Year"].max()     # first year
ymin = 1950 #df_total["Year"].min()     # last year

year = ymax                             # default year

# create a list of all countries
all_countries = list(df_all_countries['Entity'].unique())
countries = ['France','United Kingdom'] # set a default list - could be empty

# the working list is the dataframe for the countries currently selected by
# the selected year and the selected list of countries
df_working_list = df_all_countries[
    (df_all_countries['Year']==year)&               
    (df_all_countries['Entity'].isin(countries))
    ]

def plot_choro(year):
    """
    Function to draw a choropleth map for the given year.

    Parameters:
    year (int): The year for which to draw the choropleth.

    Returns:
    fig: Plotly figure object for the choropleth map.
    """
    fig = px.choropleth(df_all_countries[df_all_countries['Year']==year], 
                        locations="Code",       # The ISO code for the Entity (country)
                        color=col,              # color is set by this column
                        hover_name="Entity",    # hover name is the name of the Entity (country)
                        range_color=(min,max),  # the range of values as set above
                        scope= 'world',         # a world map - the default
                        projection='equirectangular', 
                        title='World CO2 Emissions',
                        #template = 'plotly_dark',
                        color_continuous_scale=px.colors.sequential.Reds,
                        )
    fig.update_layout(margin={'r':50, 't':0, 'b':0, 'l':0})  # adjust the figure size
    return fig

def update_data(state):
    """
    Function to update the working list and plot the choropleth when a new year or new country is selected.

    Parameters:
    state (object): The state object containing the application's current state from which we can 
                    find the currently selected year, country list and dataframe
    """
    state.df_working_list = state.df_all_countries[
        (state.df_all_countries['Year']==state.year)&
        (state.df_all_countries['Entity'].isin(state.countries))
        ]
    state.fig = plot_choro(state.year)

# Create the choropleth for the default year
fig = plot_choro(ymax)

# Define the page
with tgb.Page() as page:
    # Header
    tgb.text( "# World CO2 Emissions from {ymin} to {ymax}", mode='md')
    tgb.text("---", mode='md')

    # Left column contains the choropleth and the right one the data
    with tgb.layout(columns="2 1"):
        # choropleth and slider to select year
        with tgb.part():
            with tgb.layout(columns="2 1"):
                tgb.text(value="#### Use the slider to select a year", mode='md')
                tgb.text("### {year}", mode='md')
            tgb.slider(value="{year}",min=ymin, max=ymax, on_change=update_data)
            tgb.chart(figure="{fig}")
        # A header with the global emissions per year and the data for the selected country/year
        with tgb.part():
            # header
            tgb.text("#### Total global emissions for {year}:", mode='md')
            tgb.text("##### {int(df_world[df_world['Year']==year]['Annual CO₂ emissions'].iloc[0])} tonnes", mode='md')            
            tgb.text("---", mode='md')
            # data
            tgb.text(value="#### World temperature data", mode='md')
            tgb.selector(value="{countries}", lov="{all_countries}", multiple=True,dropdown=True, width=1000 ,on_change=update_data)            
            tgb.table("{df_working_list}")

    # footer with acknowledgement
    tgb.text("Global CO2 Emission Data from {ymin} to {ymax}. Data derived, with thanks, from  [Our World in Data](https://ourworldindata.org/)", mode='md')

#Run the app
Gui(page=page).run()
