
This is documentation for the Housing Visualization project, aimed to help realtors/possible homeowners understand housing prices. Instead of having to manually parse thousands of homes from redfin, this program automatically scrapes the website, downloads the data, and visualizes it in an easy to understand format.

## Why is this important?
+ Helps clear up complicated housing data
+ Condenses 10K rows of data into 6 easy to understand visuals
+ Explores how web scraping can be used in conjunction with data science/processing

## Who should use this?
+ Users who want to explore different visuals
+ Realtors who want to better understand housing in the RDU area
+ Programmers who want to learn more about data visualization or web scraping
  
# Sample Output

## From redfin.py
![Image of redfin](https://github.com/kingan1/Housing-data-Visualization/blob/master/redfins.png)

## From image.py
![Image of redfin](https://github.com/kingan1/Housing-data-Visualization/blob/master/image.png)

# Getting Started
To be able to run the program, a few libraries need to be installed beforehand.

## Library installations

### Install [Python](https://www.python.org/downloads/release/python-367)
Python is the underlying language of this program. To be able to run anything, Python must be installed.
1. Follow the link above.
2. Navigate to the link that says `Python 3.6.7`
3. Select `download`
4. Open a terminal
5. Run
  `$ python version`
6. The output should be 
   `Python 3.6.7`
   
As long as the version is above 3.6, the program will function correctly

### Install [XMing](https://sourceforge.net/projects/xming/files/Xming/6.9.0.31/Xming-6-9-0-31-setup.exe/download)
XMing is used as a "whiteboard" for our visualizations.
1. Navigate to the link above
2. Wait for 5 seconds for the download to begin.
3. Open the executable
4. Complete the setup wizard

### Install [Selenium](https://selenium-python.readthedocs.io/installation.html)
Selenium is used to scrape websites, where we get our housing data from.
1. Navigate to the link above
2. Open a terminal
    + If pip is not installed on your computer, it can be installed from [here](https://pip.pypa.io/en/stable/installing)
3. Run the pip command found in Section 1.2
4. Navigate to section 1.3
5. Download the Firefox link

To confirm Selenium was downloaded correctly, follow these steps
1. Open a terminal
2. Type: `python`
3. Type: `from selenium import webdriver`

If this command executes with no errors, Selenium has been installed correctly!

### Install Pandas
Pandas is used to hold large amounts of datas in an efficient and easy to use format.

Before installing Pandas, ensure you have pip installed

1. Open a terminal
2. Type this command: `pip install pandas`
3. Hit ENTER
4. To ensure pandas is installed correctly, type this command `python`
5. Hit ENTER
6. Type this command `import pandas`
7. Hit ENTER

If Pandas is installed correctly, there will be no error messages

### Install Matplotlib
Matplotlib is used to plot the data. Think of XMing as the whiteboard, and Matplotlib as the marker.

1. Open a terminal
2. Type this command: `python -m pip install -U pip`
3. Hit ENTER
4. Type this command: `python -m pip install -U matplotlib`
5. To ensure Matplotlib is installed correctly, type this command `python`
6. Hit ENTER
7. Type this command `import matplotlib`
8. Hit ENTER

If Matplotlib is installed correctly, there will be no error messages


# Running the program

## How to run the program

### Download the source code
1. Navigate to this [link](https://github.com/kingan1/Housing-data-Visualization)
2. Clone/Download the repository

### Run redfin.py

Prerequisites: All libraries have been installed

1. Open a terminal
2. Navigate to where you downloaded the repository
3. Type this command: `python redfin.py`
4. Hit ENTER

The output should be: `done`
 + redfin.py creates a web crawler, and opens Redfins page for the RDU area.
 + The program then expands the area, clearing all filters as well.
 + The program then downloads the .csv file, renaming it to `file.csv`
 + At the end of running redfin.py, you will have a new file in your folder titled file.csv

### Run image.py

Prerequisites: redfin.py has been executed and you have a file.csv file in your folder

1. Open a terminal
2. Navigate to where you downloaded the repository
3. Type this command: `python image.py`
4. Hit ENTER

Multiple windows should open, all with different visualizations.
  + image.py takes in `file.csv` from the previous step, and creates several visualizations
  + These visualizations help you understand what the data represents, and explores different types of visuals
  
# FAQ

If you encounter any issues with installation or running the program, linked below are frequently asked questions
+ [FAQ for Selenium](https://www.seleniumhq.org/support/)
+ [FAQ for Xming](http://www.straightrunning.com/XmingNotes/trouble.php)

# Want to contribute?
+ [Issue tracker](https://github.com/kingan1/Housing-data-Visualization/issues)
+ [Source code](https://github.com/kingan1/Housing-data-Visualization)

# License
This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/)
