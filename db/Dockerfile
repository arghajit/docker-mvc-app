FROM library/postgres


# ADD ./init.sql /docker-entrypoint-initdb.d
RUN service postgresql start
# ADD ./docker-entrypoint-initdb.d/run.sh /docker-entrypoint-initdb.d
# ADD ./postgres/data/postgresql.auto.conf /var/lib/postgresql/data
# ADD init.sql /docker-entrypoint-initdb.d
# RUN su -c "rm -rf /usr/local/var/postgres && initdb /usr/local/var/postgres -E utf8"
RUN ls /docker-entrypoint-initdb.d
# entrypoint['/docker-entrypoint-initdb.d/run.sh']
CMD ["postgres"]
