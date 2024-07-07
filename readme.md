Week 6 homework assignment


--- pokeapi.py ---

Problem Statement:
You are tasked with creating a Python application that interfaces with a public API, fetches data, and processes it. This application should provide insights into how different web architectures work and demonstrate your ability to set up a Python environment, make API requests, and handle JSON data.


        Task #1
        --------------------------------------------
        * Using "pokeapi.co/api" I used a get request to fetch data for the pokemon snorlax. Looped through his data to find specific keys "name" & "abilities". Instead of printing the entire dictionary for Snorlax's abilities I looped through that dictionary and displayed the name of each ability ONLY (otherwise screen would've looked very messy)
  
        Task #2
        --------------------------------------------
        * Created a function that takes an array of pokemon names. Loops through the data for each pokemon and pulls out their names, abilities & weight



--- digital_cosmos.py ---

Problem Statement:
Imagine you are a developer tasked with creating a feature for a web application that provides users with insightful information about various space objects. Your application will fetch data from a publicly available space API, process this data, and display it in a user-friendly format.
        

        Task #1
        --------------------------------------------
        * Using "https://api.le-systeme-solaire.net/rest/bodies/" I created 2 functions. Function #1 "fetch_planet_data" I used a get request to fetch data for planets and returned the json response 
        * Next I created the function "planet_info" which calls the "fetch_planet_data" function and stores it as a variable. I used the variable to pull out all planets where "isPlanet == True", their "name"s, "mass" and "sideralObrit"s

        Task #2
        --------------------------------------------
        * Created the function "fetch_heaviest_planet" by calling the "fetch_planet_data" function and using the returned data to loop through each planetg wherfe "isPlanet == True". Then stored each planet's mass value into an empty array "planet_mass". After appending each value to the new array, I used the python lis max() function to find the highest value in the planet_mass array. Using the results from the max() while inside of the same loop, I created an if statement to return the name of the planet with the highest mass.

        