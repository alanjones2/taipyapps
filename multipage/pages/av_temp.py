from taipy.gui import Gui 
import taipy.gui.builder as tgb
import pandas as pd
import plotly.express as px

year = 2023

def plot_chart(df, year=year):
    fig = px.bar(df, x="Month", y=str(year), title=f"Average World Temperatures in {year}")
    fig.update_yaxes(range=[10,20])
    return fig

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
                        #width= 500, height = 500,
                        projection='equirectangular', 
                        title='World CO2 Emissions',
                        #template = 'plotly_dark',
                        color_continuous_scale=px.colors.sequential.Reds
                        )
    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        )
    return fig


df = pd.read_csv("data/monthly-average-surface-temperatures-by-year-world.csv") 
fig = plot_choro("2020")

def on_slider(state, var, val):    
    state.fig = plot_choro(val)

with tgb.Page() as page:

    tgb.html( 'h1', "World temperature averages since 1950", style="color:red")
    tgb.text(value="#### Use the slider to select a year", mode='md')
    tgb.slider(value="{year}",min=1950, max=2024, on_change=on_slider)
    tgb.chart(figure="{fig}")

    with tgb.layout(columns="1 0"):
        with tgb.part():
            tgb.text(value="#### Use the slider to select a year", mode='md')
            tgb.slider(value="{year}",min=1950, max=2024, on_change=on_slider)
            tgb.chart(figure="{fig}")
        with tgb.part():
            tgb.text(value="#### World temperature data", mode='md')
            tgb.table("{df}")

#Gui(page=page).run()
