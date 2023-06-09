# AFRICAN STUDENTS IN AMERICA

## Description
This project retrieve data from the API of <https://developer.schooldigger.com/> to get the top 5 of states in the USA that have the most percentage of enrolled African in High School. For this project, it just takes the 20 first school of every state, so its result may be different of the reality.

## Steps to execution
### Clone this repository
- go to the path to the desired directory of this project : 

    `cd path/to/the/directory`
- clone the current repository:

     `git clone git@github.com:alfa-nomena/school.git`

### Create virtual enviromnent
- Change the directory to the school folder : 

    `cd school`


- Create a new virtual environment, so this project won't break any other projects and to ensure that it will work perfectly. Note that this code work in python>=3.9. That's why creating a new virtual environment is important: 

    `python -m venv school_env`
- Activate the virtual environment just created : 
    - For Windows : 
    
        `.\school_env\Scripts\activate`

    - For Unix based OS : 
    
        `source school_env\bin\activate`

### Install all requirements
This project has some requirements used to improve user experience and have a more readable code : 

`python -m pip install -r requirements.txt`

### Execute the *client.py* file
After all these steps, the current project should work perfectly. You can just execute this like this:
`python client.py`

### Get the results in the excel file
The name of the result file is called file in the .env file. By default, this file is named Results, but you can change it in the .env by changing the FILE variable.
The Excel file contains as many sheets as the API provides data, plus one sheet that contains a global result for all years. For example, if the API provides data for 2020 to 2023, there will be five sheets in the Excel file for 2020 to 2023 and for the global result