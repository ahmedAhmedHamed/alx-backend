import  redis, { createClient } from 'redis';
import util from 'util';

const client = createClient();
const getAsync = util.promisify(client.get).bind(client);

client.on('connect', () => {
  console.log('Redis client connected to the server');
  main();
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`, err);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  getAsync(schoolName).then((reply) => console.log(reply));
}

async function main() {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}
