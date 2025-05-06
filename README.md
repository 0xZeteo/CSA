# cybersecurity-assessment-tool

This tool is based on the National Institute for Standards and Technology (NIST) framework for cybersecurity, and the Federal Financial Institutions Examination Council (FFIEC) cybersecurity assessment tool (links below).

NIST - https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.04162018.pdf

FFIEC - https://www.ffiec.gov/cyberassessmenttool.htm#tool

The main goal of this application is to provide a way for companies to assess their cybersecurity level. After answering all the questions of the framework, the final results are presented under 2 categories:
  - Inherent Risk Profile: reflects the company's inherent risk level with a total of 5 levels (Least, Minimal, Moderate, Significant, Most)
  - Cybersecurity Maturity: reflects the company's current risk maturity, also with 5 levels (Baseline, Evolving, Intermediate, Advanced, Innovative)


Before cloning the repository, make sure you have the following requirements installed:
  - Python 3.9.5 - https://www.python.org/
  - MySQL Server 8.0.26 - https://dev.mysql.com/downloads/mysql/
  - MySQL Connector Python 8.0.26 - https://dev.mysql.com/downloads/connector/python/


This application was developed and tested on Windows 10 Pro version 1903 build 18362.30.
The user interface is written in tkinter, a library that comes with python. Other libraries that need to be installed are included in the 'requirements.txt' file.

N.B. after cloning the repository, go to the file 'source/db.py' and change the rp variable to include your MySQL root password, otherwise authentication will not work (because the database is hosted locally, i kept it this way for now, however, this will be changed later on to reflect a more secure way of authentication).

To get this working on ubuntu (tested on 20.04.3 LTS) go to the file 'source/main.py' and comment the line 'self.iconbitmap(default='resources/cyber.ico')' in the 'Main_App' class. Because ubuntu does not handle .ico files, you have to change this line if you want an icon for the window. 
This will get it working on ubuntu, however, some quality of life improvements are needed:
  - Fonts used are a bit unclear as this was mainly designed for windows
  - Events are handled differently on ubuntu, and while the scollbars present do function when dragged with the mouse, event bindings need to be changed to get the mousewheel working (i.e. look for widget.bind('Mousewheel', do_something) and replace 'Mousewheel' with 'Button-4' and 'Button-5' for ubuntu (different bindings for MacOS)).
