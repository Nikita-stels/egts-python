"""EGTS_SR_DIG_SENS_DATA"""
from ....egts_types import *


class AbsDigSensData(EGTSRecord):
    """EGTS_SR_DIG_SENS_DATA Class"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(AbsDigSensData, self).__init__(
            # Digital sensor state set outside
            ('dsnl_dsst', DsnlDsst()),
            ('dsnh', Byte()),
            *args, **kwargs
        )

    @property
    def special_inputs(self):
        return {
            'dsn': self._set_dsn
        }

    def _set_dsn(self, value):
        self['dsnl_dsst']['dsnl'] = value % 2**4
        self['dsnh'] = value // 2**4


class DsnlDsst(BitField):
    """EGTS_SR_DIG_SENS_DATA Sensor State Bits and Number Low Bits Field"""
    def __init__(self, *args, **kwargs):
        """
        Overriding constructor with fields
        :param args: additional args
        :param kwargs: parent class kwargs
        """
        super(DsnlDsst, self).__init__(
            ('dsnl', Bits(maxlen=4)),
            ('dsst', Bits(maxlen=4)),
            *args, **kwargs
        )
