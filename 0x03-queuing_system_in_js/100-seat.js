import express from 'express';
import { createClient } from 'redis';
import util from "util";
import { createQueue } from 'kue';

const client = createClient();
const getAsync = util.promisify(client.get).bind(client);
const setAsync = util.promisify(client.set).bind(client);
const app = express();
const PORT = 1245;
const queue = createQueue();
const reservationEnabled = true;
setAsync('available_seats', 50);

function reserveSeat(number) {
  return setAsync('available_seats', number);
}

function getCurrentAvailableSeats() {
  return getAsync('available_seats');
}

app.listen(PORT);

app.get('/available_seats', async (req, res)=>{
  const numSeats = await getCurrentAvailableSeats();
  res.json({'numberOfAvailableSeats': numSeats.toString()});
});

app.get('/reserve_seat', async (req, res)=>{
  const numSeats = await getCurrentAvailableSeats();
  if (reservationEnabled === false) {
    res.json({"status": "Reservation are blocked"});
  } else {
    const job = queue.create('reserve_seat');
    job.on('complete', function() {
      console.log(`Seat reservation job ${job.id} completed`);
    }).on('failed', function(error){
      console.log(`Seat reservation job JOB_ID failed: ${error.message}`);
    }).on('enqueue', function(){
      console.log(`Notification job created: ${job.id}`);
    }).on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    }).save((err) => {
      if (err) return res.json({ status: 'Reservation failed' });
      return res.json({ status: 'Reservation in process' });
    });

  }
});
