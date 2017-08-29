M101P
========================

Docker environment for course of https://university.mongodb.com/courses/M101P/about

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



HW1-1
--------------------------------------------------------------------

answer 42

HW1-2
--------------------------------------------------------------------

answer 1815

HW1-3
--------------------------------------------------------------------

question http://localhost:8080/hw1/50

answer 53


HW2-1
--------------------------------------------------------------------

```
mongoimport  --host storage -u adminmaster -p passmaster --authenticationDatabase admin --drop --db students --collection grades grades.json
```

```
db.grades.count()
db.grades.aggregate({'$group':{'_id':'$student_id', 'average':{$avg:'$score'}}}, {'$sort':{'average':-1}}, {'$limit':1})
```

```
db.grades.find({score:{$gte:65}}).sort({score:-1})
```

answer 22


HW2-2
--------------------------------------------------------------------

```
db.grades.find({type:"homework"}).count()
db.grades.find({type:"exam"}).count()
db.grades.find({type:"quiz"}).count()
```


```
db.grades.find().sort( { 'score' : -1 } ).skip( 100 ).limit( 1 )
db.grades.find( { }, { 'student_id' : 1, 'type' : 1, 'score' : 1, '_id' : 0 } ).sort( { 'student_id' : 1, 'score' : 1 } ).limit( 5 )
db.grades.aggregate( { '$group' : { '_id' : '$student_id', 'average' : { $avg : '$score' } } }, { '$sort' : { 'average' : -1 } }, { '$limit' : 1 } )

```

answer 54


HW2-3
--------------------------------------------------------------------

answer jkfds5834j98fnm39njf0920f02


HW2-4
--------------------------------------------------------------------

```
db.movieDetails.find({"year":2013,"rated":"PG-13","awards.wins":0},{"title":1,_id:0});
```


HW2-5
--------------------------------------------------------------------

```
db.movieDetails.find({"countries.1":"Sweden"}).count();
```

HW3-1
--------------------------------------------------------------------

```
mongoimport  --host storage -u adminmaster -p passmaster --authenticationDatabase admin --drop --db school --collection students students.json
```

answer: 13


HW3-2
--------------------------------------------------------------------

answer: 89jklfsjrlk209jfks2j2ek


HW3-3
--------------------------------------------------------------------

answer: jk1310vn2lkv0j2kf0jkfs