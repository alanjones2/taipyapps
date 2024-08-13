from taipy import Gui
import taipy.gui.builder as tgb
import pandas as pd
import plotly.express as px



def plot_chart2(df, y="Total"):
    fig = px.line(df, x="Year", y=y)
    return fig

def on_select(state, var, val):
    #print(var,val)
    state.fig2 = plot_chart2(df2, y=val)

df2 = pd.read_csv("data/co2-emissions-by-category.csv") 
src = "Total"
fig2 = plot_chart2(df2)

with tgb.Page() as page:
    
    with tgb.layout(columns="2 1"):
        with tgb.part():
            tgb.text( value="# CO2 Emissions", mode='md',class_name="color-secondary")
            tgb.selector(label="Select a CO2 Source", 
                         value="{src}", 
                         lov="Total;Coal;Oil;Gas;Cement", 
                         dropdown=True, 
                         on_change=on_select)
            tgb.chart(figure="{fig2}")
        with tgb.part():
            pass
    tgb.table("{df2}")

#Gui(page=page).run()