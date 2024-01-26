OpenSpace Organizer - Seat Allocation 

Created on 26th Jan 2024

By Mahak Behl

Description

This project randomly assigns people to a seat on a table in the openspace. Every time the project run it assign different people to the table. By default it runs for an Openspace which has 6 Tables and 4 Seats per table. But there is an option to change the setup of openspace when you execute the project.
The project gives to details of how many seats are present in the openspace, how many people are expected to come to openspace, how many seats are left vacant.
If the number of people expected to come to openspace is more than number of seats it also gives the feasibility to add more tables to the openspace.(As a user you can decide if you want to add a new table and provide seats to everyone or you want to have limited tables in the openspace and some people might not have a seat assigned)
Output of Seat allotment is displayed in the output screen always. It is also possible to save the output to a text file (if you wish to).

Setup

To access this project on your local files, you can clone it using these steps

Open your terminal
Use this command to clone $ git clone https://github.com/MahakBehl/openspace-organizer/tree/master
This will clone the repositoty into your local folder
Run main.py in visual studio


Behaviour Driven Development

Openspace Specifications :
    Openspace Default Size: 
            Tables = 6
            Seats per Table = 4
    NOTE : Default value can be changed in config.json

    Input : Y/y if you want to change the specification(Tables or seats) of the Opensapce. N/n if you want to go by default.


Names of People expected in the opensapce:
    Colleagues.txt file has the names of all the expected participants.
    Location of the file is in config.json file and can be modified from it.


Output:
    All the tables with there seats details and person assigned to it will be displayed on the screen.
    Output can be stored in file. Y/y if you want to save output as file, then enter the name of file you want to store it to.(Note: make sure to enter .txt file otherwise the results will not be stored in file)



Technologies Used:
Python
Git

Contact Details
mahakbehl@gmail.com