import redis from 'redis';
import { promisify } from 'util';

// Create a Redis client
const client = redis.createClient();

// Event handler for successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event handler for connection error
client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

// Promisify the get and hgetall functions
const getAsync = promisify(client.get).bind(client);
const hgetallAsync = promisify(client.hgetall).bind(client);

// Function to set a new school value
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Function to display the value of a school using async/await
async function displaySchoolValue(schoolName) {
  const value = await getAsync(schoolName);
  console.log(value);
}

// Function to create and display a hash
function createAndDisplayHash() {
  const hashKey = 'HolbertonSchools';
  const hashData = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
  };

  // Store hash values
  Object.entries(hashData).forEach(([key, value]) => {
    client.hset(hashKey, key, value, redis.print);
  });

  // Display hash values using hgetall
  hgetallAsync(hashKey).then((result) => {
    console.log(result);
  });
}

// Call the functions
async function main() {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
  createAndDisplayHash();
}

main();

