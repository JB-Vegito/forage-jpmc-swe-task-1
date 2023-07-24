import unittest
from client3 import getDataPoint
from client3 import getRatio


class ClientTest(unittest.TestCase):

  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """


  """ ------------ Add more unit tests ------------ """

  def test_getRatio_basic_case(self):
    result = getRatio(10, 2)
    self.assertEqual(result, 5.0)

  def test_getRatio_invalid_data(self):
    with self.assertRaises(TypeError):
      result = getRatio("string", 4)

  def test_getRatio_zero_division(self):
    with self.assertRaises(ZeroDivisionError):
      result = getRatio(10, 0)

  def test_getRatio_float_case(self):
    result = getRatio(7.5, 2.5)
    self.assertEqual(result, 2.5)

  def test_getRatio_negative_case(self):
    result = getRatio(-6, 3)
    self.assertEqual(result, -2.0)

  def test_getRatio_large_number_case(self):
    result = getRatio(1000000, 500000)
    self.assertEqual(result, 2.0)

if __name__ == '__main__':
    unittest.main()
