import unittest
import points_calculator
import pandas as pd

class TestPointsCalculator(unittest.TestCase):
    def test_calculate_age(self):
        result = points_calculator.calculate_age("1963-01-19")
        self.assertEqual(result, 59)
    def test_prepare_df(self):
        data = {"Donation ID":[151722], "Date of birth":["1970-11-06"], "Annual amount":[180.01], "Fundraiser ID": [12229], "Points": 4.5, "Age": 51}
        expected_df = pd.DataFrame(data)
        pd.testing.assert_frame_equal(df, expected_df)
    def test_calculate_points(self):
        test_df=pd.read_csv("test_donations.csv", sep = ";")
        points_calculator.prepare_df(test_df)
        points_calculator.calculate_points(test_df)
        self.assertEqual(test_df.loc[1, "Points"], 0.5)
        self.assertEqual(test_df.loc[2, "Points"], 4.5)
        #usw.



if __name__ == "__main__":
    unittest.main()
