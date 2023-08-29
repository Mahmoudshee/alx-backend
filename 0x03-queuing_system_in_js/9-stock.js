import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const app = express();
const port = 1245;

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

app.use(express.json());

const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 }
];

async function reserveStockById(itemId, stock) {
  await setAsync(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const reservedStock = await getAsync(`item.${itemId}`);
  return parseInt(reservedStock, 10) || 0;
}

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = listProducts.find(item => item.itemId === itemId);

  if (!product) {
    res.json({ status: 'Product not found' });
  } else {
    const currentReservedStock = await getCurrentReservedStockById(itemId);
    const currentQuantity = product.initialAvailableQuantity - currentReservedStock;
    res.json({ ...product, currentQuantity });
  }
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = listProducts.find(item => item.itemId === itemId);

  if (!product) {
    res.json({ status: 'Product not found' });
  } else {
    const currentReservedStock = await getCurrentReservedStockById(itemId);
    const remainingStock = product.initialAvailableQuantity - currentReservedStock;

    if (remainingStock <= 0) {
      res.json({ status: 'Not enough stock available', itemId });
    } else {
      await reserveStockById(itemId, currentReservedStock + 1);
      res.json({ status: 'Reservation confirmed', itemId });
    }
  }
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

