M101P
========================

Docker environment for course M101P: MongoDB for Developers (https://university.mongodb.com/courses/M101P/about)

Technology
----------------
- docker
- python 3.6
- mongodb 3.5
  

Getting Started with Docker and Docker Compose for Local Development
--------------------------------------------------------------------

### Install Docker

https://docs.docker.com/installation/

### Install Docker Compose

http://docs.docker.com/compose/install/

### Install the app's

In the project ./book/dev/ (where the `Makefile` file is located), run:

```
make build_all && make bootstrap_all
```


Getting started with mongo command line shell
--------------------------------------------------------------------

```
make shell_mongoshell
```

then write:

```
mongo storage:27017/admin -u adminmaster -p passmaster
```


Connect to mongo contaner
--------------------------------------------------------------------

```
docker exec -it m101p_storage_1 /bin/sh
```

Mongo restore dump
--------------------------------------------------------------------

```
mongorestore --host storage -u adminmaster -p passmaster dump
```


Mongo restore json
--------------------------------------------------------------------

```
mongoimport  --host storage -u adminmaster -p passmaster --authenticationDatabase admin --drop --db students --collection grades grades.json
```

