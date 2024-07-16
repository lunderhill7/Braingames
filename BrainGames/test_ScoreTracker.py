from unittest import TestCase
from ScoreTracker import ScoreTracker
import pytest


class TestScoreTracker(TestCase):

    def test_pull_score(self):
        score100 = ScoreTracker(100)
        assert score100.pullScore()

    def test_calc_score(self):
        scoreDiv400 = ScoreTracker(400)
        assert scoreDiv400.calcScore()

    def test_store_score(self):
        score100 = ScoreTracker(100)
        assert score100.storeScore()
