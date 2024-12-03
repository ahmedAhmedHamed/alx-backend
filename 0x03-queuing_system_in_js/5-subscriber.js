import { createClient } from 'redis';
const sub = createClient();
sub.on('connect', () => {
  console.log('Redis client connected to the server');
});

sub.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`, err);
});

sub.subscribe("holberton school channel");

sub.on("message", function (channel, message) {
    console.log(message);
    if (message === 'KILL_SERVER') {
        sub.unsubscribe();
        sub.quit();
    }
});
