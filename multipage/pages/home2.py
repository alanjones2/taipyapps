from taipy import Gui
from taipy.gui import navigate
import taipy.gui.builder as tgb

def on_button_press(state, id):
    page = "home"
    if id == "CO2": page = "CO2_Sources" 
    if id == "temp": page = "Average_World_Temperatures"
    print(id,page)
    navigate(state, to=page)

with tgb.Page() as page:
    tgb.text( value = "## World Temperatures and CO2 Emissions", mode = 'md', class_name="color-secondary")
    tgb.text( value = "#### Explore the graphs using the navigation bar above, or the buttons below.", 
             mode = 'md')
    with tgb.layout(columns="1 1"):
        with tgb.part():
            tgb.text("![](images/co2emissionspagesmall.png)", mode='md') 
            with tgb.layout("2 1"):
                with tgb.part():
                    tgb.text("__Select the Co2 Emissions page here:__", mode='md')
                with tgb.part():
                    tgb.button("CO2", id="CO2",  on_action=on_button_press)
        with tgb.part():
            tgb.text("![](images/worldtemppagesmall.png)", mode='md') 
            with tgb.layout("2 1"):
                with tgb.part():
                    tgb.text("__Select the world temperatures page here:__", mode='md')
                with tgb.part():
                    tgb.button("Temperatures", id="temp", on_action=on_button_press)
