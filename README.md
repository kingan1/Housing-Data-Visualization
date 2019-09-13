# Housing Data Visualization
This is documentation for the Housing Visualization project, a beginners introduction to web scraping and data visualization. 

[Web scraping](https://en.wikipedia.org/wiki/Web_scraping) can take on many forms, but at its minimum is defined as navigating websites by using a "robot" (browser controlled by a program) to extract large amounts of information from web pages.

Instead of having to manually parse thousands of homes from [Redfin](https://www.redfin.com/), this program automatically scrapes the website, downloads the data, and visualizes it in an easy to understand format.

## Why is this important?
+ Helps clear up complicated housing data
+ Condenses 10K rows of data into 6 easy to understand visuals
+ Explores how web scraping can be used in conjunction with data science/processing

## Who should use this?
+ Users who want to explore different visuals
+ Beginners to web scraping or data visualization who want to see how to scrape and visualize data
+ Python developers who want to explore new libraries and see how they are effectively used
  
# [Sample Output](#sample-output)

## From redfin.py
This picture is a screenshot of the output file, `file.csv`. This Python file scrapes Redfin.com, and downloads information about housing into a .csv file for later use. `redfin.py` transforms the process of having to manually copy data from each page into an automated process that takes under 30 seconds.

The .csv file lists the Sale Type, Property Type, Address, City, and State. There are plenty of more attributes of each home, but these are just the first few.

![Image of redfin](/redfins.png)

## From image.py
This image is an example visual from `image.py`. `image.py` takes in the file created in `redfin.py` and processes the data. It then creates 6 visuals exploring such data.

This image is an summarization of homes by latitude and longitude, where each dot represents one house. Another dimension is added, adding a color gradient for the cost of each home. This produces a map that displays both the spread of homes and average cost per region.
![Image of redfin](/image.png)

# <span style="color:black">[Getting Started](#getting-started)</span>,
To be able to run the program, a few libraries need to be installed beforehand.

## Library installations

### <a href = "#install-python"><font color = "black"> Install Python</font></a>
Python is the underlying language of this program. To be able to run anything, Python must be installed.
1. Follow this [link](https://www.python.org/downloads/release/python-367).
2. Navigate to the link that says `Python 3.6.7`
3. Select `download`
4. Open a terminal
5. Type
  `python --version`
6. Hit ENTER
7. The output should be 
   `Python 3.6.7`
   
![Image of Python](/pythonversion.png)   
As long as the version is above 3.6, the program will function correctly

### [Install XMing](#install-xming)
XMing is used as a "whiteboard" for our visualizations.
1. Navigate to this [link](https://sourceforge.net/projects/xming/files/Xming/6.9.0.31/Xming-6-9-0-31-setup.exe/download)
2. Wait for 5 seconds for the download to begin.
3. Open the executable
4. Complete the setup wizard

To confirm XMing was downloaded correctly, follow these steps:
1. Search for "XMing" on your computer
2. Click on the XMing Executable
3. Verify the XMing symbol is present on the lower right hand side of your screen
![Image of XMing](/xming.png)


### [Install Selenium](#install-selenium)
Selenium is used to scrape websites, where we get our housing data from.
1. Navigate to this [link](https://selenium-python.readthedocs.io/installation.html)
2. Open a terminal
    + If pip is not installed on your computer, it can be installed [here](https://pip.pypa.io/en/stable/installing)
3. Type this command: `pip install selenium`
4. Hit ENTER
5. Navigate to section 1.3 from the link above
6. Download the Firefox link

To confirm Selenium was downloaded correctly, follow these steps
1. Open a terminal
2. Type: `python`
3. Hit ENTER
4. Type: `from selenium import webdriver`
5. Hit ENTER
6. Verify the command executed with no errors
![Image of Selenium](/selenium.png)

### [Install Pandas](#install-pandas)
Pandas is used to hold large amounts of datas in an efficient and easy to use format.

Before installing Pandas, ensure you have pip installed

1. Open a terminal
2. Type this command: `pip install pandas`
3. Hit ENTER
4. To ensure pandas is installed correctly, type this command `python`
5. Hit ENTER
6. Type this command `import pandas`
7. Hit ENTER
8. Verify the command executed with no errors
![Image of Pandas](/pandas.png)

### [Install Matplotlib](#install-matplotlib)
Matplotlib is used to plot the data. Think of XMing as the whiteboard, and Matplotlib as the marker.

1. Open a terminal
2. Type this command: `python -m pip install -U pip`
3. Hit ENTER
4. Type this command: `python -m pip install -U matplotlib`
5. To ensure Matplotlib is installed correctly, type this command `python`
6. Hit ENTER
7. Type this command `import matplotlib`
8. Hit ENTER
9. Verify the command executed with no errors
![Image of Matplotlib](/matplotlib.png)

# [Running the program](#running-the-program)
Now that we have all of the libraries downloaded, we are able to start gathering and processing data!
## How to run the program

### [Download the source code](#download-source-code)
1. Navigate to this [link](https://github.com/kingan1/Housing-data-Visualization)
2. Clone/Download the repository

### [Run redfin.py](#run-redfin)

1. Open a terminal
2. Navigate to where you downloaded the repository
3. Type this command: `python redfin.py`
4. Hit ENTER

![Image of Redfin Running](/redfinsample.png)

The output should be: `done`
 + `redfin.py` creates a web crawler, initialized to Redfins page for the RDU area.
 + The program then expands the area, clearing all filters as well.
 + The program then downloads a .csv file, renaming it to `file.csv` so it is easier for the next program to find
 + At the end of running `redfin.py`, you will have a new file in your folder titled `file.csv`

### [Run image.py](#run-image)

Prerequisites: `redfin.py` has been executed and you have a `file.csv` file in your folder

1. Open a terminal
2. Navigate to where you downloaded the repository
3. Type this command: `python image.py`
4. Hit ENTER

Multiple windows should open, all with different visualizations.
  + `image.py` takes in `file.csv` from the previous step, and creates several visualizations
  + These visualizations help you understand what the data represents, and explores different types of visuals
  
#### [For detailed information about each visual, click here](/visualInfo.html)
  
# [FAQ](#faq)

If you encounter any issues with installation or running the program, linked below are frequently asked questions
+ [FAQ for Selenium](https://www.seleniumhq.org/support/)
+ [FAQ for Xming](http://www.straightrunning.com/XmingNotes/trouble.php)

# [Want to contribute?](#contribute)
+ [Issue tracker](https://github.com/kingan1/Housing-data-Visualization/issues)
+ [Source code](https://github.com/kingan1/Housing-data-Visualization)

# [License](#license)
This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/)
