M101P
========================

Docker environment for course of https://university.mongodb.com/courses/M101P/about

Technology
----------------
- docker
- python
- mongodb


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
mongo admin --host storage -u adminmaster -p passmaster
```


Connect to mongo contaner
--------------------------------------------------------------------

```
docker exec -it m101p_storage_1 /bin/sh
```