import taipy.gui.builder as tgb
import pandas as pd
import plotly.express as px

year_max = 2020
year_min = 1950
year = year_max

# define parameters for map graphic
df_total = pd.read_csv('data/co2_total.csv')
col = 'Annual CO₂ emissions'    # the column that contains the emissions data
max = df_total[col].max()       # maximum emissions value for color range
min = df_total[col].min()       # minimum emissions value for color range

def plot_choro(year):
    fig = px.choropleth(df_total[df_total['Year']==year], 
        locations="Code",       # The ISO code for the Entity (country)
        color=col,              # color is set by this column
        hover_name="Entity",    # hover name is the name of the Entity (country)
        range_color=(min,max),  # the range of values as set above
        scope= 'world',         # a world map - the default
        projection='equirectangular', 
        title=f"CO2 Emissions by country in {year}",
        color_continuous_scale=px.colors.sequential.Reds
        )

    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        )

    return fig

fig = plot_choro(year_max)

def on_slider(state, var, val):    
    state.fig = plot_choro(val)

with tgb.Page() as page:
    tgb.text( value= f"### Country CO2 Emissions from {year_min} to {year_max}", mode='md', class_name="color-secondary")
    tgb.text(value="#### Use the slider to select a year", mode='md')
    tgb.slider(value="{year}", min=year_min, max=year_max, on_change=on_slider)
    tgb.chart(figure="{fig}")
