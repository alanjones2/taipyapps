from taipy.gui import Gui 
import taipy.gui.builder as tgb
import pandas as pd
import plotly.express as px

# set a default plotly template
template="plotly_white"

year = 2023
ddvalue = "text"


def plot_chart(df, year=year):
    fig = px.bar(df, x="Month", y=str(year), template=template, title=f"Average World Temperatures in {year}")
    fig.update_yaxes(range=[10,20])
    return fig

def plot_chart2(df, y="Total"):
    fig = px.bar(df, x="Year", y=y, template=template)
    return fig


df = pd.read_csv("monthly-average-surface-temperatures-by-year-world.csv") 
fig = plot_chart(df)

df2 = pd.read_csv("co2-emissions-by-category.csv") 
# Nah...
col_list = list(df2.columns)
emission_total = col_list[0]
dd_list = ';'.join(col_list[0:-1])
emissions_pc = col_list[-1]
fig2 = plot_chart2(df2)




def on_slider(state, var, val):    
    state.fig = plot_chart(df, val)



with tgb.Page() as page:

    tgb.html( 'h1', "World temperature averages since 1950", style="color:red")
    with tgb.layout(columns="1 1"):
        with tgb.part():
            tgb.text(value="#### Use the slider to select a year", mode='md')
            tgb.slider(value="{year}",min=1950, max=2024, on_change=on_slider)
            tgb.chart(figure="{fig}")
        with tgb.part():
            tgb.text(value="#### World temperature data", mode='md')
            tgb.table("{df}")


