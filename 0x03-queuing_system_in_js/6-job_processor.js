import kue from 'kue';

// Create a Kue queue
const queue = kue.createQueue();

// Function to send notifications
const sendNotification = (phoneNumber, message) => {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};

// Set up queue process for push_notification_code jobs
queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);
  done();
});

console.log('Job processor is listening...'); // Indicate that the processor is active

