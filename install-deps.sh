#!/bin/sh -e

. ../simple_travel.env

sudo apt-get update
sudo apt-get -y install mariadb-server libmysqlclient-dev python-dev python-pip

# echo <<EOF | sudo mysql -p
# create user simple_travel identified by \'$DB_PASS\''
# create database simple_travel;
# use simple_travel;
# grant ALL on simple_travel.* to 'simple_travel';
# grant ALL on test_simple_travel.* to 'simple_travel';
# EOF

sudo pip install -r requirements.txt

./manage.py test
