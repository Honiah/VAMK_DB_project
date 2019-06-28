# VAMK_DB_project

Django + Apache2 tutorial

https://mikesmithers.wordpress.com/2017/02/21/configuring-django-with-apache-on-a-raspberry-pi/

+

pip install djangorestframework
pip install mysqlclient
pip install django-cors-headers

activate apache2-mpm-worker

sudo a2dismod mpm_event
sudo a2enmod mpm_worker
sudo service apache2 restart