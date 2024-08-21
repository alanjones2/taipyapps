from taipy.gui import Gui

root = """
<|navbar|>  
<|content|>
_This is a footer_
"""

page1 = "## This is page 1"
page2 = "## This is page 2"

pages = {
    "/": root,
    "page1": page1,
    "page2": page2,
}

Gui(pages=pages).run(dark_mode=False)