
import os
import numpy as np
from datetime import datetime, date, timedelta
import fda.constants as constants


class Bond(object):

    def init(self, coupon_rate: float, issue_date: str, maturity_date : str, face_value: float = 100.0, coupon_frequency: int = constants.SEMI_ANNUALY):

        self.face_value = face_value
        self.coupon_rate = coupon_rate
        self.issue_date = datetime.strptime(issue_date, constants.DEFAULT_DATE_TIME).date()
        self.maturity_date = datetime.strptime(maturity_date, constants.DEFAULT_DATE_TIME).date()
        self.coupon_frequency = coupon_frequency

        if issue_date >= maturity_date:
            raise Exception("")

    def future_value(self, **kwrgs):
        periods = kwrgs.get('periods', self.coupon_frequency)
        fv = self.face_value * (1 + self.coupon_rate ) ** periods
        return fv

    def repr(self):
        return f"face_value: {self.face_value}; coupon_rate: {self.coupon_rate}; {self.issue_date}; issue_date: {self.issue_date}; maturity_date: {self.maturity_date}; coupon_frequency: {self,coupon_frequency}"


