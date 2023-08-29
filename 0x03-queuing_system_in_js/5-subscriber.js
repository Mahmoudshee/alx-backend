import redis from 'redis';

// Create a Redis subscriber client
const subscriber = redis.createClient();

// Event handler for successful connection
subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event handler for connection error
subscriber.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

// Subscribe to the channel
subscriber.subscribe('holberton school channel');

// Event handler for receiving messages
subscriber.on('message', (channel, message) => {
  console.log(`Message received from channel ${channel}: ${message}`);
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe();
    subscriber.quit();
  }
});

