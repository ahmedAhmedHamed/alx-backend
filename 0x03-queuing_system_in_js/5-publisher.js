import  redis from 'redis';
const pub = redis.createClient();

pub.on('connect', () => {
  console.log('Redis client connected to the server');
});

pub.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`, err);
});

function publishMessage(message, timer) {
  console.log(`About to send ${message}`);
  setTimeout(() => pub.publish('holberton school channel', message), timer);
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
