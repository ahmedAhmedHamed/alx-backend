import express from 'express';
import { createClient } from 'redis';
import util from "util";

const client = createClient();
const getAsync = util.promisify(client.get).bind(client);
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

function getItemById(id) {
  return listProducts.find(product => product.id === id) || null;
}

app.listen(PORT);

app.get('/list_products', (req, res)=>{
  res.json(listProducts);
});

app.get('/list_products/:itemId', (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (product) {
    res.json(product);
  } else {
    res.json({ status: 'Product not found' });
  }
});
