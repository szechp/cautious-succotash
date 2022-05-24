import unittest
import points_calculator
import pandas as pd

class TestPointsCalculator(unittest.TestCase):
    def test_calculate_age(self):
        """test: compare result of calculate_age with the known age
        """
        result = points_calculator.calculate_age("1963-01-19")
        self.assertEqual(result, 59)

    def test_prepare_df(self):
        """test: compare the rows of a pre defined df with the one returned by
        the function.
        """
        data = {"Donation ID":[151722], "Date of birth":["1970-11-06"], "Annual amount":[180.01], "Fundraiser ID": [12229], "Points": 4.5, "Age": 51}
        expected_df = pd.DataFrame(data)
        test_df=pd.read_csv("test_donations.csv", sep = ";")
        points_calculator.prepare_df(test_df)
        points_calculator.calculate_points(test_df)
        self.assertEqual(list(test_df.columns), list(expected_df.columns))

    def test_calculate_points(self):
        """test: compare result of calculate_points to pre calculated points
        """
        test_df=pd.read_csv("test_donations.csv", sep = ";")
        points_calculator.prepare_df(test_df)
        points_calculator.calculate_points(test_df)
        self.assertEqual(test_df.loc[1, "Points"], 0.5)
        self.assertEqual(test_df.loc[2, "Points"], 2)
        #usw.

    def test_sum_points(self):
        """test: compare sum of points in test_donations.csv
        """
        test_df=pd.read_csv("test_donations.csv", sep = ";")
        points_calculator.prepare_df(test_df)
        points_calculator.calculate_points(test_df)
        df_sum_points = points_calculator.sum_points(test_df)
        self.assertEqual(df_sum_points.loc[0, "Sum of points"], 5.5)
        self.assertEqual(df_sum_points.loc[1, "Sum of points"], 2.0)
        self.assertEqual(df_sum_points.loc[2, "Sum of points"], 5.0)


if __name__ == "__main__":
    unittest.main()
