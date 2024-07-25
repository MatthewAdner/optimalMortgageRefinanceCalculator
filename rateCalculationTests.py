import unittest
from rateCalculation import calculate_lambda

class TestRateCalculation(unittest.TestCase):

    def test_calculate_lambda(self):
        # Example values based on the context and formula
        mu = 0.1  
        tau = 25
       
        i0 = 0.06
        pi = 0.03  

        expected_result = .147
        result = calculate_lambda(mu, i0, tau, pi)
        
        self.assertEqual(result, expected_result, f"Expected {expected_result}, but got {result}")

    # def test_calculate_lambda_with_different_values(self):
    #     mu = 0.1
    #     p = 0.10#?
    #     m = 5
    #     i0 = 0.06
    #     pi = 0.03

    #     expected_result = mu + ((p/m) - i0) + pi
    #     expected_result = .147
    #     result = calculate_lambda(mu, p, m, i0, pi)
        
    #     self.assertEqual(result, expected_result, f"Expected {expected_result}, but got {result}")

if __name__ == '__main__':
    unittest.main(verbosity=2)
