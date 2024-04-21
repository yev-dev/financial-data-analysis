from unittest import TestCase

from fda.fic.curve import BootstrapYieldCurve

class TestBootstrapYieldCurve(TestCase):

    def test_yield_curve(self):
        yield_curve = BootstrapYieldCurve()
        yield_curve.add_instrument(100, 0.25, 0., 97.5)
        yield_curve.add_instrument(100, 0.5, 0., 94.9)
        yield_curve.add_instrument(100, 1.0, 0., 90.)
        yield_curve.add_instrument(100, 1.5, 8, 96., 2)
        yield_curve.add_instrument(100, 2., 12, 101.6, 2)

        y = yield_curve.get_zero_rates()
        x = yield_curve.get_maturities()


if __name__ == '__main__':

    tests = TestBootstrapYieldCurve()

    tests.test_yield_curve()

