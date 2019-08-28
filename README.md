# Project 05 : Use the Open Food Fact datas from its API REST.

This program offers you the possibility to discover healthier aliments by user the Open Food Fact API REST service (https://world.openfoodfacts.org/).

It has been coded with Python3, the database system used is MySQL. The graphical interface has been done with the Tkinter library.

## Operation

On start, the program will ask you to login or regsiter to use the service. Once your done with the registration, and as soon as you will be
"logged in", a new page will be displayed with 9 categories of aliments. 

Select a category by entering its reference number and valid your choice.

A list of 20 aliments concerned by your category choice is displayed. Choose one of them and valid your choice by entering its number.

The program returns you an aliment from the selected category. This aliment has at least, the same or a better nutriscore evaluation witch
may be a good alternative.

You may choose to save this aliment in your records or make another search.

To see your records, go to the category page and click on the dedicated button.


#### Database configuration:

To use this porgramm, you need to have Python3 and MySQL installed. Once done, you need to configure the database. 

Open MySQL console and enter the following commands:

Creat a database called "foodappdb"

```
CREATE DATABASE foodappd;
```

Creat a user:

```
CREATE USER 'user_foodapp'@'localhost' IDENTIFIED BY 'p@ssword';
```

Define privileges for this user:

```
GRANT SELECT, INSERT ON foodappdb.* TO 'user_foodapp'@'localhost';
```


#### Install the program:

For the program installation, open your terminal and enter the following commands:

1) Download the files:

```
git clone https://github.com/athd33/P5-Tk.git
```

2) Create and activate a virtual environement:

```
virtualenv -p python3 env

source env/bin/activate
```

3) Install dependencies:

```
pip install -r requirements.txt

```

4) Start the program:

```
python3 main.py
```



