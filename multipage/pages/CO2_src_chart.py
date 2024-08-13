from taipy import Gui
import taipy.gui.builder as tgb
import pandas as pd
import plotly.express as px



def plot_chart2(df, y="Total"):
    fig = px.bar(df, x="Year", y=y)
    return fig

def on_select(state, var, val):
    #print(var,val)
    state.fig2 = plot_chart2(df2, y=val)

df2 = pd.read_csv("data/co2-emissions-by-category.csv") 
src = "Total"
fig2 = plot_chart2(df2)

with tgb.Page() as page:
    tgb.text( value = "### CO2 Emissions by source since the mid-19th Century", mode = 'md', class_name="color-secondary")
    tgb.selector(label="Select a CO2 Source", 
                    value="{src}", 
                    lov="Total;Coal;Oil;Gas;Cement", 
                    dropdown=True, 
                    on_change=on_select)
    tgb.chart(figure="{fig2}")