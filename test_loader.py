import unittest
from loader import *
import pandas as pd


class TestLoader(unittest.TestCase):
    def test_valid_locations(self):
        geo_locator = get_geolocator()

        expected_locations = [
            {
                "location": "Museum of Modern Art",
                "latitude": 40.7618552,
                "longitude": -73.9782438,
                "type": "Museum",
            },
            {
                "location": "USS Alabama Battleship Memorial Park",
                "latitude": 30.684373,
                "longitude": -88.015316,
                "type": "Park",
            },
        ]

        for expected in expected_locations:
            result = fetch_location_data(geo_locator, expected["location"])

            self.assertIsNotNone(result)

            self.assertAlmostEqual(
                result["latitude"],
                expected["latitude"],
                delta=0.01,
            )
            self.assertAlmostEqual(
                result["longitude"],
                expected["longitude"],
                delta=0.01,
            )
            self.assertEqual(
                result["type"].lower(),
                expected["type"].lower(),
            )
    
    def test_invalid_location(self):
        geolocator = get_geolocator()

        result = build_geo_dataframe(
            geolocator,
            ["asdfqwer1234"],
        )

        self.assertEqual(
            result.loc[0, "location"],
            "asdfqwer1234",
        )
        self.assertTrue(pd.isna(result.loc[0, "latitude"]))
        self.assertTrue(pd.isna(result.loc[0, "longitude"]))
        self.assertTrue(pd.isna(result.loc[0, "type"]))


if __name__ == "__main__":
    unittest.main()
