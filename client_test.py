import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    self.assertEqual(getDataPoint(quotes[0]), ('ABC', 120.48, 121.2, 120.84))
    self.assertEqual(getDataPoint(quotes[1]), ('DEF', 117.87, 121.68, 119.78))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    self.assertEqual(getDataPoint(quotes[0]), ('ABC', 120.48, 119.2, 119.84))
    self.assertEqual(getDataPoint(quotes[1]), ('DEF', 117.87, 121.68, 119.78))


  """ ------------ Add more unit tests ------------ """
  def test_getRatio(self):
     price_a = 100.50
     price_b = 121.30
     expected = price_a / price_b

     self.assertEqual(getRatio(price_a, price_b), expected)

  def test_getRatio_divideByZero(self):
     price_c = 87.80
     price_d = 0

     self.assertEqual(getRatio(price_c, price_d), None)
     





if __name__ == '__main__':
    unittest.main()
