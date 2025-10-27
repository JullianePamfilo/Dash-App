CS 340 Project Two: Grazioso Salvare Dashboard
Author: Julliane Pamfilo – CS 340 Project Two
Date: October 2025

Project Summary

The project was designed for a rescue training organization called Grazioso Salvare, which helps find dogs that may be suitable for highly trained search and rescue teams. The dashboard is intended for use by individuals who want to visualize, filter, and analyze data about available animals in the Austin Animal Center. The web-based tool provides an intuitive interface to the underlying MongoDB database by leveraging CRUD operations written in Python.

Required Functionality

All required specifications were met in the development of the dashboard and is evident in the comparison to the CS 340 Project Two rubric. They include:

• CRUD interaction with the database from within the dashboard using a custom Python module aac_crud.py
• Interactive controls (dropdown, slider, and reset button) to allow filtering of the data
• Interactive data table with real-time shelter data that meets the filters of the dashboard
• Dynamic visualizations using a bar chart (Top Breeds) and a geolocation map (Dash Leaflet)
• Use of the Grazioso Salvare logo and a unique project identifier

Tools and Technologies Used

• Python 3 – Primary programming language used for the logic, CRUD operations, and dashboard implementation.
• MongoDB – NoSQL database selected for the use case because of its schema-less and scalable data storage, as well as support for efficient queries.
• Dash and Plotly – Used for interactive visualizations and front-end layout within Jupyter
• Dash Leaflet – For mapping and geolocation visualization of animal locations.
• Pandas – Used for data manipulation and transformation as a connector between the MongoDB database and the dashboard.
• JupyterDash – Provides a way for the dashboard to be run interactively inside Jupyter Notebook.

Why MongoDB and Dash Were Used

Contents 
1. Why MongoDB and Dash Were Used 
2. Steps to Reproduce the Project 
3. Challenges and How They Were Overcome 
4. Screenshots Demonstrating Functionality 
5. Conclusion 

Why MongoDB and Dash Were Used 

MongoDB’s document-oriented structure was selected to easily store and query unstructured animal data, such as breeds, outcomes, and location. Dash was used to create an interactive web application directly within Python, without the need for front-end technologies like HTML, CSS, and JavaScript. MongoDB and Dash together make an ideal client-server model for efficient data access and visualization.

Steps to Reproduce the Project 
1. Open the Codio environment and navigate to the CS 340 project workspace.
2. Import the dataset using the mongoimport command in the terminal:
mongoimport –db aac –collection animals –type=csv –headerline –file code_files/datasets/aac_shelter_outcomes.csv
3. Confirm that the user aacuser exists with authentication enabled in the aac database.
4. Run the aac_crud.py module to ensure it can connect to MongoDB.
5. Open the ProjectTwoDashboard.ipynb file and run the notebook to run the dashboard.
6. Interact with the two filters (Rescue Type and Max Age) and observe how both the charts and map dynamically update based on selection.
7. Confirm all required states (Water Rescue, Mountain/Wilderness, Disaster/Tracking, Reset) are functional.

Challenges and How They Were Overcome 

Some of the challenges encountered and their resolutions included:
• MongoDB Authentication Error: The system was initially producing an ‘Authentication failed.’ error. This was fixed by ensuring the correct credentials (aacuser/ SNHU1234) and setting auth_source to aac.
• PNG Logo Does Not Render: The Grazioso Salvare logo png did not initially render. This was due to an incorrect relative file path. Fix involved confirming the working directory of the notebook and updating the image path.
• Data Filtering and Visualization Not Synced: Some rescue types were returning no records. This was resolved by validating breed queries in the CRUD module and gracefully handling empty DataFrames in the dashboard.

Conclusion 

This project integrates a full MongoDB back end with an interactive and dynamic Dash front end. The dashboard gives Grazioso Salvare an effective tool for exploring their animal data and surfacing potential candidates for rescue. The dashboard meets all CS 340 Project Two requirements and has provided good hands-on experience in database management, Python, and data visualization concepts.

** Module Eight Journal **
What are some steps you take when writing clean, readable, and reusable code?

To ensure readability and maintainability, I wrote CRUD code in reusable functions with clear, consistent naming. This modularity lets others (and my future self) easily change individual steps. For instance, by isolating filtering logic, another developer could swap in a new filter without touching the database calls. Exception handling and consistent output format also make this component robust and easy to extend in other ways. My reuse of this CRUD Python module for Project One to quickly connect to my dashboard in Project Two illustrates its flexibility!

What computational thinking strategies do you use? 

To start this project, I mapped out Grazioso Salvare’s full data needs then divided them into smaller chunks: database access, filtering logic, and visual interface. This project had a greater focus on developing a realistic and usable interface than my previous courses. For my future database-focused projects, I will continue to plan, build, test, and iterate on data-driven solutions until they achieve the user’s goal.

How does the work you do as a computer scientist impact the world?

Computer scientists help turn data into information. In this project, I developed a tool that enables Grazioso Salvare to find rescue animals most in need of homes as quickly as possible. By improving their operational efficiency, the tool directly contributes to their primary goal of protecting animals and has a positive social impact. Projects like this illustrate the power of computing to support problem solving and decision-making.
