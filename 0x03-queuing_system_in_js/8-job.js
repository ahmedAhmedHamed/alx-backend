function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) { throw new Error('Jobs is not an array'); }
  jobs.forEach(function (jobData) {
    const job = queue.create('push_notification_code_3', jobData).save();
    job.on('complete', function() {
      console.log(`Notification job ${job.id} completed`);
    }).on('failed', function(error){
      console.log(`Notification job JOB_ID failed: ${error}`);
    }).on('enqueue', function(){
      console.log(`Notification job created: ${job.id}`);
    }).on('progress', (progress) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
      });
    });
}

module.exports = createPushNotificationsJobs;
