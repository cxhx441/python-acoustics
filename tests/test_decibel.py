from acoustics.decibel import *

class Testdbsum:
    def test_double(self):
        assert (abs(dbsum([10.0, 10.0]) - 13.0103) < 1e-5)

    def test_ten_times(self):
        assert (dbsum([10.0]*10) == 20)

    def test_random_positive(self):
        assert (abs(dbsum([92, 67, 39, 30, 13, 43, 89, 83, 26, 4]) - 94.12257) < 1e-5)

    def test_random_negative(self):
        assert (abs(dbsum([-91, -75, -89, -13, -31, -83, -36, -30, -74, -10]) - -8.17687) < 1e-5)

    def test_random_pos_neg(self):
        assert (abs(dbsum([1, -8, -50, 17, -18, -40, 53, 53, -48, -6]) - 56.01086) < 1e-5)


class Testdbmean:
    def test_two_same(self):
        assert (dbmean([10.0, 10.0]) == 10.0)

    def test_ten_times(self):
        assert (dbmean([10.0]*10) == 10.0)

    def test_random_positive(self):
        assert (abs(dbmean([92, 67, 39, 30, 13, 43, 89, 83, 26, 4]) - 84.12257) < 1e-5)

    def test_random_negative(self):
        assert (abs(dbmean([-91, -75, -89, -13, -31, -83, -36, -30, -74, -10]) - -18.17687) < 1e-5)

    def test_random_pos_neg(self):
        assert (abs(dbmean([1, -8, -50, 17, -18, -40, 53, 53, -48, -6]) - 46.01086) < 1e-5)


class Testdbadd:
    def test_two_same(self):
        assert (abs(dbadd(10.0, 10.0) - 13.0103) < 1e-5)

    def test_no_effect_positive(self):
        assert (abs(dbadd(100.0, 24.0) - 100.0) < 1e-5)

    def test_no_effect_negative(self):
        assert (abs(dbadd(100.0, -24.0) - 100.0) < 1e-5)


class Testdbsub:
    def test_two_same(self):
        assert (abs(dbsub(13.0103, 10) - 10.0) < 1e-5)

    def test_no_effect_positive(self):
        assert (abs(dbsub(100.0, 24.0) - 100.0) < 1e-5)

    def test_no_effect_negative(self):
        assert (abs(dbsub(100.0, -24.0) - 100.0) < 1e-5)


class Testdbmul:
    def test_two_same(self):
        assert (abs(dbmul(10.0, 2) - 13.0103) < 1e-5)

    def test_ten_times(self):
        assert (abs(dbmul(100.0, 10) - 110) < 1e-5)

    def test_twenty_times(self):
        assert (abs(dbmul(100.0, 20) - 113.0103) < 1e-5)


class testdbdiv:
    def test_two_same(self):
        assert (abs(dbdiv(13.0103, 2) - 10.0) < 1e-5)

    def test_by_ten(self):
        assert (abs(dbdiv(100.0, 10) - 90) < 1e-5)

    def test_by_twenty(self):
        assert (abs(dbdiv(100.0, 20) - 86.98970) < 1e-5)
