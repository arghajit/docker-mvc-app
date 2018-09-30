#!/bin/bash

psql -U postgres -c "CREATE USER admin with password 'admin'"
psql -U postgres -c "ALTER role admin SET client_encoding to 'utf8'"
psql -U postgres -c "CREATE DATABASE service2"
psql -U postgres -c "grant all privileges on DATABASE service2 to admin"

