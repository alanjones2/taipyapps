from taipy.gui import Gui
from pages.home import page as homepage
from pages.CO2_src_chart import page as co2page
from pages.av_temp_map import page as temppage

root_md = """
<|navbar|>
<|content|>  
_Made with Taipy_    
"""

pages = {
    "/": root_md,
    "home": homepage,
    "CO2_Sources": co2page,
    "Average_World_Temperatures":temppage,
}

Gui(pages=pages).run(dark_mode=True)