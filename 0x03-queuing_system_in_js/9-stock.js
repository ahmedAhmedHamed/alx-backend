import express from 'express';
import redis, { createClient } from 'redis';
import util from "util";

const client = createClient();
const getAsync = util.promisify(client.get).bind(client);
const setAsync = util.promisify(client.set).bind(client);
const app = express();
const PORT = 1245;

const listProducts = [
  {
    id: 1,
    name: 'Suitcase 250',
    price: 50,
    stock: 4
  },
  {
    id: 2,
    name: 'Suitcase 450',
    price: 100,
    stock: 10
  },
  {
    id: 3,
    name: 'Suitcase 650',
    price: 350,
    stock: 2
  },
  {
    id: 4,
    name: 'Suitcase 1050',
    price: 550,
    stock: 5
  },
]

function reformat(input) {
  const output = {}
  output['itemId'] = input['id'];
  output['itemName'] = input['name'];
  output['price'] = input['price'];
  output['initialAvailableQuantity'] = input['stock'];
  return output;
}

function getItemById(id) {
  return listProducts.find(product => product.id === id) || null;
}

function reserveStockById(itemId, stock) {
  return setAsync(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  return await getAsync(itemId) || 0;
}

app.listen(PORT);

app.get('/list_products', (req, res)=>{
  const ret = [];
  listProducts.forEach((product) => {
    ret.push(reformat(product));
  });
  res.json(ret);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const item = getItemById(itemId);
  const reserved = await getCurrentReservedStockById(itemId) || 0;
  let ret = {"status":"Product not found"};
  if (item) {
    ret = reformat(item);
    ret.currentQuantity = item.stock - reserved;
  }
  res.json(ret);
});
