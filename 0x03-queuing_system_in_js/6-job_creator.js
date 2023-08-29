import kue from 'kue';

// Create a Kue queue
const queue = kue.createQueue();

// Create a job data object
const jobData = {
  phoneNumber: '1234567890',
  message: 'This is a test push notification.',
};

// Create a job and add it to the queue
const job = queue.create('push_notification_code', jobData);

// Event handler for job creation success
job.on('enqueue', () => {
  console.log(`Notification job created: ${job.id}`);
  process.exit(0); // Terminate the script after job creation
});

// Event handler for job completion
job.on('complete', () => {
  console.log('Notification job completed');
});

// Event handler for job failure
job.on('failed', () => {
  console.log('Notification job failed');
});

// Save the job to the queue
job.save();

