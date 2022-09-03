# Virtual Library
This is a web based system which allows user to share their books and earn profits as well as rent books to read great and rare books in low cost. The system also have book reviews, comments, and many more to guide users to best books and best book sharers.

## Requirements (software)
Python 3.8+

## Installation 
- Create a Virtual Environment and Activate it.
- Clone the project using following command (git should be installed)
```
git clone https://github.com/maahad767/virtual-library.git
```
- Install the project dependencies by running following command
```
pip install -r requirements.txt
```
- Run the following commands to create database tables(SQLite will be automatically generated, to use anything else, change database info in settings.py)
```
python manage.py migrate
```
## How to Run the Project
- Run the following command
```
python manage.py runserver 
```
- Now, visit http://127.0.0.1:8000/ to access the website.

## Testing
To run the tests, run the following command
```
python manage.py test
```
