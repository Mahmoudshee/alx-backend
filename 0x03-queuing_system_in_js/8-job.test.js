// 8-job.test.js
import kue from 'kue';
import chai from 'chai';
import createPushNotificationsJobs from './8-job.js';

const { expect } = chai;

// Set up Kue test mode
const queue = kue.createQueue();
queue.testMode.enter();

// Define tests
describe('createPushNotificationsJobs', () => {
  afterEach(() => {
    queue.testMode.clear();
  });

  it('display an error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('invalid', queue)).to.throw('Jobs is not an array');
  });

  it('create two new jobs to the queue', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
      }
    ];

    createPushNotificationsJobs(jobs, queue);

    const jobCount = queue.testMode.jobs.length;
    expect(jobCount).to.equal(jobs.length);
  });
});

// Exit Kue test mode
queue.testMode.exit();

