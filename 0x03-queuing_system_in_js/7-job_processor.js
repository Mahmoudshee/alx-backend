import kue from 'kue';

// Create an array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Function to send notifications
const sendNotification = (phoneNumber, message, job, done) => {
  job.progress(0, 100); // Track progress of 0%
  if (blacklistedNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // Simulate progress
  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
};

// Create a Kue queue with concurrency 2
const queue = kue.createQueue({ concurrency: 2 });

// Set up queue process for push_notification_code_2 jobs
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});

console.log('Job processor is running...');

