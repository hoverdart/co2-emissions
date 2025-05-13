import pandas as pd
import plotly.express as px
import preswald
##Quick note; SQL Filtering was annoying to type and didn't work too great, so I manually filtered the code instead. 
##Another quick note; the cursor is misaligned on this IDE, and it made typing this code very troublesome. Copy-pasting worked wonders.

## Data and Filtering
df = pd.read_csv("data/co2Emissions.csv")
df_recent = df[df["Year"] >= 2010]

## Create scatter plot: Year vs Emissions (highlighting countries)
fig = px.scatter( df_recent,  x="Year",y="Annual CO₂ emissions",color="Entity",title="CO₂ Emissions by Country Since 2010 (Metric Tonnes)",labels={"Annual CO₂ emissions": "CO₂ Emissions (metric tons)", "Entity": "Country"},)
fig.update_layout(template="plotly_white")

## Preswald stuffsies
preswald.text("# 🌍 Annual CO2 Emissions Data Visualization")
preswald.text("This dashboard shows annual CO₂ emissions, measured in metric tons, from 2010 onward for all countries.")
preswald.plotly(fig)
preswald.text("Clearly, emissions trends are slowly rising. **Not Good.**")
preswald.text("To examine this issue further, let's look at the emissions for the major polluting countries, and see how they've evolved.")

## Displaying the Major Countries
countries = ["China", "United States", "India", "Germany", "Brazil", "United Kingdom", "France"]
df_major = df[df["Entity"].isin(countries)]
fig = px.line(df_major,x="Year",y="Annual CO₂ emissions", color="Entity",title="Annual CO₂ Emissions (1750–2023) for Major Countries",labels={"Annual CO₂ emissions": "CO₂ Emissions (metric tons)", "Entity": "Country"},)
fig.update_layout(template="plotly_white")
preswald.text("## Annual CO₂ Emissions for the Major Countries (1750–2023)")
preswald.plotly(fig)
preswald.text("As shown in the graph, **China's emissions have been on the rise, while most countries are slowly tapering off.**")

##Full Table
preswald.text("Finally, let's examine a table of emissions data for **all countries.**")
preswald.text("## Emissions Data for All Countries")
preswald.table(df_recent)

##Cool Call to Action
preswald.text("## So, what can we do?")

preswald.text("""
The data is clear: while global emissions remain high, **change is possible**.

Here are a few ways countries, companies, and individuals can take action:

-  **Accelerate the shift to clean energy** (solar, wind, hydro, and even nuclear)
-  **Invest in energy efficiency**, from smart homes to greener supply chains
-  **Adopt carbon pricing and regulation** to hold major polluters accountable
-  **Support reforestation and conservation efforts** to naturally absorb CO₂
-  **Change individual habits**: fly less, eat local, waste less

Ultimately, addressing climate change starts with data, but ends with **decisive global and local action** :)
""")

preswald.text("### Thanks for exploring this CO₂ dashboard! Hire me please!")
preswald.text("_Built with 💻 Python, 📊 Plotly, and ⚡ Preswald_")

