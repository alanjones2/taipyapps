

### CO2 Emissions Visualization App

This Python application is designed to visualize global CO2 emissions data using an interactive web-based interface. It leverages the Taipy GUI framework to create a dynamic and responsive app that displays CO2 emissions across different countries and years through a choropleth map and accompanying data tables.

#### Key Features:

1. **Global CO2 Emissions Data Loading and Preprocessing**:
   - The application reads CO2 emissions data from a CSV file (`co2_total.csv`).
   - It filters and processes the data to prepare it for visualization.
   - The data includes annual CO2 emissions for various countries from 1950 to 2021.

2. **Interactive Choropleth Map**:
   - The core visualization is a choropleth map that displays CO2 emissions for each country in a selected year.
   - The map is colored based on CO2 emissions, with a color scale ranging from the minimum to the maximum emissions value in the dataset.
   - Users can interact with the map to see detailed emissions data for each country by hovering over the map.

3. **Year Selection Slider**:
   - A slider allows users to select the year for which they want to view the CO2 emissions data.
   - The map and data table update dynamically based on the selected year.

4. **Country Selection**:
   - Users can select multiple countries from a dropdown menu to view detailed emissions data for those countries.
   - The data table updates to display emissions data for the selected countries in the selected year.

5. **Global Emissions Summary**:
   - The app provides a summary of total global CO2 emissions for the selected year.
   - This summary is displayed alongside the map and data table.

6. **Responsive Layout**:
   - The app layout is divided into columns: the left column displays the choropleth map and year selection slider, while the right column displays the global emissions summary and country-specific data table.
   - The layout is designed to be responsive, ensuring a good user experience across different devices and screen sizes.

7. **Acknowledgment and Data Source**:
   - The app includes a footer that acknowledges the data source, Our World in Data, and provides a link to the original dataset.

#### How It Works:

1. **Data Initialization**:
   - The app initializes by loading the CO2 emissions data and setting up global variables for the emissions column, year range, and default selected countries.

2. **Plotting Function**:
   - The `plot_choro` function creates a choropleth map for a given year using Plotly Express. It configures the map with appropriate settings and returns the figure object.

3. **Data Update Function**:
   - The `update_data` function updates the working data and choropleth map based on the selected year and countries. It is triggered whenever the user changes the year or the selected countries.

4. **GUI Definition**:
   - The app's GUI is defined using the Taipy GUI builder. It includes text elements, a slider for year selection, a choropleth chart, a country selector, and a data table.
   - The GUI layout and elements are specified within a `Page` context, which defines the structure and content of the app.

5. **Running the App**:
   - The app is executed by creating a `Gui` object with

the defined page and calling its `run` method to start the interactive interface.

### Code Overview

Here is an overview of the main sections and functionalities of the code:

#### Data Loading and Initialization
- **Global CO2 Emissions Data**: The data is read from a CSV file, and unnecessary columns are dropped.
- **Global Variables**: Variables for the emissions column, year range, default year, and default selected countries are initialized.

```python
df_all_countries = pd.read_csv('co2_total.csv')
df_all_countries = df_all_countries.drop(columns=['Unnamed: 0'])
df_world = df_all_countries[df_all_countries['Entity']=='World']

col = 'Annual CO₂ emissions'
max = df_all_countries[col].max()
min = df_all_countries[col].min()
ymax = 2021
ymin = 1950

year = ymax

all_countries = list(df_all_countries['Entity'].unique())
countries = ['France', 'United Kingdom']
df_working_list = df_all_countries[
    (df_all_countries['Year'] == year) &
    (df_all_countries['Entity'].isin(countries))
]
```

#### Plotting Function
- **Choropleth Map**: The `plot_choro` function generates a choropleth map for a specified year using Plotly Express. The map settings include location codes, color scales, and layout adjustments.

```python
def plot_choro(year):
    fig = px.choropleth(df_all_countries[df_all_countries['Year'] == year], 
                        locations="Code",
                        color=col,
                        hover_name="Entity",
                        range_color=(min, max),
                        scope='world',
                        projection='equirectangular',
                        title='World CO2 Emissions',
                        color_continuous_scale=px.colors.sequential.Reds)
    fig.update_layout(margin={'r': 50, 't': 0, 'b': 0, 'l': 0})
    return fig

fig = plot_choro(ymax)
```

#### Data Update Function
- **Update Mechanism**: The `update_data` function updates the working list of data and the choropleth map based on user selections. It is triggered by changes in the year or country selection.

```python
def update_data(state):
    state.df_working_list = state.df_all_countries[
        (state.df_all_countries['Year'] == state.year) &
        (state.df_all_countries['Entity'].isin(state.countries))
    ]
    state.fig = plot_choro(state.year)
```

#### GUI Definition
- **Page Layout**: The GUI is structured using the Taipy GUI builder. It includes a header, choropleth map, year slider, country selector, and data table.

```python
with tgb.Page() as page:
    tgb.text("# World CO2 Emissions from {ymin} to {ymax}", mode='md')
    tgb.text("---", mode='md')

    with tgb.layout(columns="2 1"):
        with tgb.part():
            with tgb.layout(columns="2 1"):
                tgb.text(value="#### Use the slider to select a year", mode='md')
                tgb.text("### {year}", mode='md')
            tgb.slider(value="{year}", min=ymin, max=ymax, on_change=update_data)
            tgb.chart(figure="{fig}")

        with tgb.part():
            tgb.text("#### Total global emissions for {year}:", mode='md')
            tgb.text("##### {int(df_world[df_world['Year'] == year]['Annual CO₂ emissions'].iloc[0])} tonnes", mode='md')
            tgb.text("---", mode='

'md')
            tgb.text(value="#### World temperature data", mode='md')
            tgb.selector(value="{countries}", lov="{all_countries}", multiple=True, dropdown=True, width=1000, on_change=update_data)
            tgb.table("{df_working_list}")

    tgb.text("Global CO2 Emission Data from {ymin} to {ymax}. Data derived, with thanks, from [Our World in Data](https://ourworldindata.org/)", mode='md')
```

#### Running the App
- **Execution**: The app is run by creating a `Gui` object with the defined page and calling its `run` method.

```python
Gui(page=page).run()
```

### Usage
- **Interactive Elements**: Users can interact with the slider to select different years and use the dropdown to select different countries. The map and data table will update dynamically based on these selections.
- **Data Visualization**: The choropleth map visually represents the CO2 emissions of each country for the selected year, and the data table provides detailed emissions data for the selected countries.

### Summary
This app provides a comprehensive and interactive way to visualize global CO2 emissions data. Users can explore how emissions have changed over time and compare emissions between different countries. The app is built to be user-friendly, leveraging the capabilities of the Taipy GUI framework and Plotly for dynamic data visualization.