import kue from 'kue';

// Create an array of job data
const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  // ... add more job data here
];

// Create a Kue queue
const queue = kue.createQueue();

// Function to send notifications
const sendNotification = (phoneNumber, message) => {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};

// Set up queue process for push_notification_code_2 jobs
queue.process('push_notification_code_2', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);

  // Simulate progress
  let progress = 0;
  const progressInterval = setInterval(() => {
    progress += 10;
    job.progress(progress, 100);
    if (progress >= 100) {
      clearInterval(progressInterval);
      done();
    }
  }, 1000);
});

// Loop through the array and create jobs
for (const jobData of jobs) {
  const job = queue.create('push_notification_code_2', jobData);
  job.save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    }
  });

  job
    .on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    })
    .on('failed', (err) => {
      console.log(`Notification job ${job.id} failed: ${err}`);
    })
    .on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
}

console.log('Job creator is running...');

