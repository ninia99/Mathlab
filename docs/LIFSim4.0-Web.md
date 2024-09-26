# This is a web application for project of LIFSim4.0
## It does have four pages: Home, About, Source, Contact
## There are two hidden pages: Download, Demo. Models of these pages are commented out

- Home - There are some posts, which includes essential information about project. It does have detail page.
- About - This page in backend has summernote implementation, admin can insert any kind of scientific report with links, images, etc. 
- Source - This page has same structure, like about has.
- Contact - This page is for user, if anybody has any question, that person can contact admin directly via message container.


## Installation
### Prerequisites
- Django==5.0.4
- django-summernote==0.8.20.0
- numpy==1.26.4
- pandas==2.2.2
- pillow==10.3.0
- psycopg2-binary==2.9.9
- uwsgi

### Set up

1. clone the repository:
     ```bash
   https://github.com/ninia99/Mathlab.git 
    ```
    ``` bash
   cd mathlab
    ```
    ``` bash
   python3 -m venv env
   source env/bin/activate
    ```
    ``` bash
   pip install -r requirements.txt 
   ``` 
    ``` bash
   python manage.py migrate
    ```
  
# Server 

   