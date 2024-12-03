import kue from 'kue';
const queue = kue.createQueue();
const jobData = {phoneNumber: '0123', message: '3210'};


const job = queue.create('push_notification_code', jobData).save();

job.on('complete', function() {
  console.log('Notification job completed');
}).on('failed', function(){
  console.log('Notification job failed');
}).on('enqueue', function(){
  console.log(`Notification job created: ${job.id}`);
});
