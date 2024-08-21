from taipy.gui import Gui

page1 = "## This is page 1"
page2 = "## This is page 2"

pages = {
    "page1": page1,
    "page2": page2,
}

Gui(pages=pages).run(dark_mode=False)