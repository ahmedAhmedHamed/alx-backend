import  redis, { createClient } from 'redis';
const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
  main();
});

async function main() {
  client.hset("HolbertonSchools", "Portland", 50, redis.print);
  client.hset("HolbertonSchools", "Seattle", 80, redis.print);
  client.hset("HolbertonSchools", "New York", 20, redis.print);
  client.hset("HolbertonSchools", "Bogota", 20, redis.print);
  client.hset("HolbertonSchools", "Cali", 40, redis.print);
  client.hset("HolbertonSchools", "Paris", 2, redis.print);
  client.hgetall("HolbertonSchools", function (err, obj) {
    console.dir(obj);
  });
}
