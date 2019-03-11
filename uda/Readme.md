# Log-Analysis

## About
This is a project under Udacity's Nanodegree Full Stack Web Developer-I. Here, you'll work with data that could have come from a real-world web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths. The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report.

## To Run

**Prerequisite Softwares :**
-   Python
-   Vagrant
-   VirtualBox (Ubuntu-Linux)
 **Installation Process**

1. Install Vagrant And VirtualBox on your system
2. Git Bash 
3. Unzip the file after downloading data. The file inside is newsdata.sql.

**Running the program**

Launch Git shell and redirect to the required directory by running  `vagrant up`, you can then log in with `vagrant ssh`. 

**Set the Database :**

1. To load the data, use the command  `psql -d news -f newsdata.sql`  to connect a database and run the necessary SQL statements.
2. We used a command i.e psql -d news to connect database.


**To execute the program, run `python ./newsdata.py` from the command line.**
