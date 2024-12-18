// Connect to the database
db = db.getSiblingDB('mydb');

// Function to generate random user data
function generateRandomUser(i) {
    const cities = ['New York', 'London', 'Paris', 'Tokyo', 'Sydney'];
    const interests = ['Sports', 'Reading', 'Music', 'Travel', 'Cooking'];
    
    return {
        userId: "user" + i,
        name: "User " + i,
        age: Math.floor(Math.random() * 50) + 20,
        email: "user" + i + "@example.com",
        city: cities[Math.floor(Math.random() * cities.length)],
        interests: interests.slice(0, Math.floor(Math.random() * 3) + 1),
        createdAt: new Date(),
        score: Math.floor(Math.random() * 100)
    };
}

// Enable sharding for database and collection
sh.enableSharding("mydb");
db.users.drop();  // Clear existing data if any
db.createCollection("users");
sh.shardCollection("mydb.users", { "userId": "hashed" });

// Insert 1000 users
print("Starting data insertion...");
for(let i = 1; i <= 1000; i++) {
    db.users.insertOne(generateRandomUser(i));
    if(i % 100 === 0) {
        print(`Inserted ${i} documents`);
    }
}
print("Data insertion complete.");

// Print shard distribution
print("\nShard distribution:");
sh.status();