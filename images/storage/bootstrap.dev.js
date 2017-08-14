db.createUser({
    user: "usermaster",
    pwd: "passmaster",
    roles: [{ 
        role: "dbOwner", 
        db: "roaming" 
    }]
},{
    w: "majority",
    wtimeout: 5000
});

db.createCollection("test");

// // ..
// db.createUser({ 
//     user: 'adminmaster', 
//     pwd: 'passmaster', 
//     roles: [{ 
//         role: "userAdminAnyDatabase", 
//         db: "admin" 
//     }]
// });

// ..
// db.createUser({ 
//     user: 'usermaster',
//     pwd: 'passmaster',
//     roles: [{
//         role: "dbAdminAnyDatabase",
//         db: "admin"
//     }]
// });

// db.createCollection("test");