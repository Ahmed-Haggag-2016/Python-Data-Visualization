# Python-Data-Visualization
A Python Rebo for Data Visualization
----
Objective
This is a Python evaluation focused on data visualization and storytelling: given a type of plot (dashboard, Sankey diagram, etc.), your task is to recreate a similar visual that tells the same story using a dummy dataset and Python scripts for data generation and visualization. You will also write an input prompt that would naturally produce the visual you created.


Labeling Steps
1. Find and Analyze the Dashboard/Graph
The data row begins with searching the web for a reference image of a business-related dashboard or graph that matches the chart description you are given. For example, you may search for something such as “dashboard for business software”.

When you find a reference image, you will need to obtain the direct URL to the image itself. You can do this by right-clicking on the image and selecting “Copy Image Address”.

Carefully inspect your reference image. Your objective is to creatively expand on this reference image, capturing the core features while developing datasets and visualizations that reflect real-world situations.


2. Generate a Prompt
Write a simple user-style question or instruction that the reference image would answer. This prompt frames the data story and helps guide your synthetic data generation:


The prompt should not be very specific and can be open-ended.
The prompt should not specify a lot of formatting requirements.
The prompt must be natural and practical, reflecting the kind of questions a user might realistically ask in a real-world scenario.

Prompt Examples
Below are some examples of good prompts along with the story and visuals related to them. These are for inspiration only and you should not directly use them:



Prompt Topic
Story & Visuals




“Show how global electric-vehicle (EV) adoption has evolved since 2015 and predict the next five years.”
• Multi-line time-series of unit sales by region
• Stacked area of battery chemistries
• Sankey of supply-chain flows
• Heat-map of EV market-share by country




“Analyze hospital network capacity vs. infectious-disease outbreaks during winter seasons.”
• Dual-axis line (ICU beds vs. cases)
• Correlation heat-map of symptoms & test positivity
• Box-whisker of LOS by diagnosis group




“Contrast same-day vs. two-day e-commerce delivery performance during holiday peaks.”
• Violin plot of delivery times
• Pareto of top delay causes
• Time-series forecast of warehouse backlog




“Track sustainable-aviation-fuel (SAF) usage across the airline industry and project carbon savings.”
• Waterfall of CO₂ reductions
• Treemap of SAF feedstocks
• Monte Carlo projection of carbon offset targets




“Visualise smart-city energy flows between residential, commercial, and EV charging nodes.”
• Chord diagram of kWh transfers
• Area chart of renewables vs. grid demand
• Animated map of substation loads by hour




“Evaluate multi-modal public-transport punctuality and rider sentiment in megacities.”
• Box-plot of lateness by mode (bus, metro, rail)
• Word-cloud & sentiment drill-down
• Gantt of headways over 24 h




“Benchmark fintech fraud-detection algorithms across geographies and transaction types.”
• ROC curves for each model
• Confusion-matrix heat-maps
• KPI bullet charts for latency & cost




“Map food-delivery fleet efficiency vs. weather impacts in dense urban zones.”
• Scatter of drop-offs vs. travel km
• Histogram of idle minutes per driver
• Isochrone map overlaying rainfall intensity




“Identify semiconductor-fab yield losses and correlate with equipment maintenance logs.”
• Stacked bar of defect classes
• Control chart of daily yields
• Network graph of tool dependencies




“Forecast coastal-city real-estate risk under sea-level-rise scenarios to 2100.”
• Scenario fan-chart of property values
• Choropleth of flood exposure zones
• Animated slider of shoreline retreat





3. Generate Data To Tell the Business Story
Write a data creation script within the scripts folder (../scripts/data_gen.py) that:

Uses only pandas and numpy.
Generates at least two datasets (as DataFrames or Numpy arrays) into the data folder, such as (../data/sales_data.csv and ../data/local_sales_data.csv)
Tells a similar story based on your reference image, reflects real-world situations, and contains enough detail to fully recreate the image.


4. Recreate the Visualization
Write a visualization script within the scripts folder (../scripts/viz.py) that:

Uses only pandas, numpy, and plotly (library is known as dash)
You can use the pip install dash command to install Plotly Dash.
Reads the generated files from your data creation script.
Generates one HTML file of an interactive dashboard into the outputs folder (../outputs/golden_image.html) using Plotly's HTML export method.
Works and can be interacted with properly.
Contains visuals that adhere to the following style guidelines:
Typography: titles MUST be bold, and properly formatted legends and labels.
Layout: Well-organized legend placement, appropriate spacing.
Legends: If a legend is present, ensure it is clearly displayed and boxed, if appropriate.
Color Palette: Use a professional and aesthetically pleasing color scheme. The color palette should complement the data and enhance readability.
Overall Quality: The final result should be polished and suitable for a business presentation or publication.


6. Upload Files
This step is very important to save your work.

Download this .zip file https://drive.google.com/file/d/18zhtNttttE3J6QPeIlGfXDmCuhPQOx_V/view?usp=sharing
Open the file and enter the password, which is scatter.
Place the upload.py script into the root directory of your project.
Install the required libraries with pip install google-cloud-storage google-auth
Run the script and follow the instructions that it provides within your terminal.

Please confirm that all files in your 'data', 'outputs', and 'scripts' folders are correct. Once uploaded, you will NOT be able to update or replace them.




Folder Structure Overview
<data_row_id>/
├── data/
│   ├── sample.npy
│   ├── dataframe2.csv
│   └── dataframe.csv          # Generated .csv and/or npy files
│
├── scripts/
│   ├── data_gen.py            # Data generation script
│   └── viz.py                 # Visualization script
│
├── outputs/
│   └── dashboard.html         # Interactive html generated using viz.py
├── upload.py 	             # Script to upload your work

Once uploaded, submit all the paths in the appropriate sections in the Labelbox editor.
Best Practices
Refer to this section for examples of the charts that you may encounter.

While searching for a reference image, here are some examples of charts you should be pursuing versus not:

✅Positive examples
❌Negative examples

A full example is available here.

