from taipy.gui import Gui
from pages.home import page as homepage
from pages.CO2_src_chart import page as co2page
from pages.CO2_map import page as CO2countrypage

root_md = """
<|navbar|>
<|content|>  
_Made with Taipy_    
"""

pages = {
    "/": root_md,
    "home": homepage,
    "CO2_Sources": co2page,
    "CO2_by_Country":CO2countrypage,
}

Gui(pages=pages).run(dark_mode=False)