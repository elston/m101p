M101P
========================

Docker environment for course of https://university.mongodb.com/courses/M101P/about

Technology
----------------
- docker
- python 3.6
- mongodb 3.5


Another
-------
- https://visionfortech.blogspot.ru/2017/01/solution-week-1-introduction-m101p-MongoDB-for-Developer.html (JANUARY 22, 2017)
- https://da8y01.github.io/gh-blog/2016/12/11/m101p-mongodb-for-developers.html    


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


HW4-1
--------------------------------------------------------------------

```
{
    "_id" : ObjectId("50906d7fa3c412bb040eb577"),
    "student_id" : 0,
    "type" : "exam",
    "score" : 54.6535436362647
}
```
```
db.grades.createIndex({"score":1,"type":1})
> db.grades.getIndexes()
[
    {
        "v" : 2,
        "key" : {
            "_id" : 1
        },
        "name" : "_id_",
        "ns" : "students.grades"
    },
    {
        "v" : 2,
        "key" : {
            "score" : 1,
            "type" : 1
        },
        "name" : "score_1_type_1",
        "ns" : "students.grades"
    }
]
db.grades.find({'type':"exam"}).explain("executionStats")
db.grades.find({}).sort({type:1}).explain("executionStats")
db.grades.find({'type':"exam"}).sort({"score":1}).explain("executionStats")
db.grades.find({score:{$gt:50}}).sort({"type":1}).explain("executionStats")
``


sku
price
description
category, brand
reviews.author


- db.products.find( { 'brand' : "GE" } )
+ db.products.find( { 'brand' : "GE" } ).sort( { price : 1 } )
+ db.products.find( { $and : [ { price : { $gt : 30 } }, { price : { $lt : 50 } } ] } ).sort( { brand : 1 } )
- db.products.find( { brand : 'GE' } ).sort( { category : 1, brand : -1 } )



HW4-2
--------------------------------------------------------------------
db.tweets.explain("executionStats").find( { "user.followers_count" : { $gt : 1000 } } ).limit(10).skip(5000).sort( { created_at : 1 } )


HW4-3
--------------------------------------------------------------------

use blog
db.posts.drop()

mongoimport  --host storage -u adminmaster -p passmaster --authenticationDatabase admin --drop -d blog -c posts posts.json

mongo storage:27017/admin -u adminmaster -p passmaster



date

```
db.posts.createIndex({date:-1})
db.posts.getIndexes()

db.posts.createIndex({date:1})

db.posts.find({},{"_id":1}).sort({date:-1}).limit(10)
db.posts.find({},{"_id":1}).sort({date:-1}).limit(10).explain("executionStats")
````


db.posts.find({tags:"wrist"},{tags:1}).limit(2)

db.posts.createIndex({tags:1})
db.posts.createIndex({tags:1,date:-1})
db.posts.getIndexes()

db.posts.find({tags:"wrist"},{tags:1}).explain("executionStats")


db.posts.createIndex({permalink:1})

HW4-4
--------------------------------------------------------------------
19776550
The 'timeLockedMicros' field indicates how many microseconds this operation spent holding a particular lock

    "lockStats": {
        "timeLockedMicros": {
            "r": 19776550,
            "w": 0
        },
        "timeAcquiringMicros": {
            "r": 4134067,
            "w": 5
        }
    },


10000000
    "nscanned": 10000000,


5580001
    "lockStats": {
        "timeLockedMicros": {
            "r": 10428354,
            "w": 0
        },
        "timeAcquiringMicros": {
            "r": 5580001,
            "w": 3
        }
    },


latency of the longest running operation to the collection
15820
    "millis": 15820,

2350
    "responseLength": 2350,




HW5-4
--------------------------------------------------------------------

```
mongoimport  --host storage -u adminmaster -p passmaster --authenticationDatabase admin --drop -d test -c zips zips.json
```

```
mongo storage:27017/admin -u adminmaster -p passmaster
```

```
db.zips.count()
```

```
db.zips.aggregate({
    $project:{
        first_char: {
            $substr : ["$city",0,1]
        }
    }
},{    
    $group:{
        _id:"$first_char", 
        "count": {
            $sum:1
        }
    }
})
```

```
db.zips.find()
```

```
db.myObject.aggregate({
    $project : {
        new_time_stamp : {$substr : ["$time_stamp",0, 10]}
    }
},{
    $group:{
        _id:"$new_time_stamp", 
        "count": {$sum:1}
    }
});
```



```
db.zips.aggregate({
    $project:{
        first_char: {
            $substr : ["$city",0,1]
        }
    }
}).find({
    first_char:{$in:['B', 'D', 'O', 'G', 'N', 'M']}
})
```


```
db.zips.aggregate({
    $project:{
        first_char: {
            $filter:{
                input: '$first_char',
                as: 'city_first_char',
                cond:{
                    $in : ['$$city_first_char.', ['AGAWAM','sdfasd']]
                }
            }
        }
    }
})
```



```
db.zips.aggregate({
    $project:{
        first_char: {
            $substr : ["$city",0,1]
        }
    }
},{
    $match: { 
        first_char :{$in:['B','D','O','G','N','M']}
    }    
})
```

```
db.zips.aggregate({
    $project:{
        first_char: {
            $substr : ["$city",0,1]
        }
    }
},{
    $match: { 
        first_char :{$in:['B','D']}
    }    
})
```


```
db.zips.aggregate({ 
    $project: { 
        _id: 0, 
        city: 1, 
        pop: 1 
    } 
},{ 
    $match: { 
        city: /^(B|D|O|G|N|M).*/ 
    } 
},{ 
    $group: { 
        _id: null, 
        pop: { 
            $sum: "$pop" 
        } 
    } 
},{ 
    $sort: { 
        city: 1
    } 
})
```