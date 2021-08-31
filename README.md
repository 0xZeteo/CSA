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
The user interface is written in tkinter, a library that comes with python. Other requirements that need to be installed are included in the requirements.txt file.

IMPORTANT: after cloning the repository, go to the file 'source/db.py' and change the rp variable to include your MySQL root password, otherwise authentication will not work.
PS: because the database is hosted locally, i kept it this way for now, however, this will be changed later on to reflect a more secure way of authentication.
