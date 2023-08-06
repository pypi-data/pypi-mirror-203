import pprint
import unittest
import random

from src.analyser_hj3415.db import mongo
from src.analyser_hj3415.report import CLIReport

addr = "mongodb://192.168.0.173:27017"
client = mongo.connect_mongo(addr)
all_codes = mongo.Corps.get_all_codes(client)


class ReportTest(unittest.TestCase):
    def setUp(self):
        self.rndcode = random.choice(all_codes)

    def test_CLIReport(self):
        print(CLIReport(client, self.rndcode))
