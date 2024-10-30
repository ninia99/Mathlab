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
### when someone make changes on local it has to be pushed first of all on local side and afterward, it has to be pulled
### on the server side. second step is to make migration if something is changed in the code (Mathlab/mathlab/pages/models.py)
### this migration happens first in local and after on server. Do not forget if model is changed, it has to be migrated and after push.
### on the server this changing has to be pulled. it is also important to restart systemctl
### and be sure that it is active and running. In order to start server, use this command: bash /src/lifsim/deployment/uwsgi_start.sh &
### passwords are stored in keepassXC on local.


``` bash
   ssh root@195.201.114.12
   ``` 


``` bash
   cd ..   
   ```

### There is a directory of the Project
``` bash
   cd /src/
   ```

### activate environment 
``` bash
   source  lifsim_env/bin/activate
   ```

### If there are some changing in code
``` bash
   git pull
   python manage.py migrate
   
   ```

``` bash
   systemctl status lifsim.uwsgi.service 
   systemctl start lifsim.uwsgi.service 
   ```

``` bash
    bash /src/lifsim/deployment/uwsgi_start.sh &
   ```

# Use Admin Panel 

### https://lifsim.empi-rf.de/admin/
### insert user and password there.
### if admin wants to change posts in about, there is summernote for that, you can give even position to the posts
### Contact page is static
### Logos is dynamical, it means admin can upload logos from admin panel, but if you need to see that logo on live, there is command collectstatics <----(try this if you do not see changing), it has to be run on server
### posts page has description, title, image, short_text, category, admin can manually  upload info from there.
### sources and abouts pages, they do have same structure.
### Titles: there admin can change title, sub_title and image of background of web-site.
