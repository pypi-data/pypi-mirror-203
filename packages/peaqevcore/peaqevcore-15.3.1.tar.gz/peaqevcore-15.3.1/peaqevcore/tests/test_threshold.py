from ..services.threshold.thresholdbase import ThresholdBase as t
from ..models.const import CURRENTS_THREEPHASE_1_32, CURRENTS_ONEPHASE_1_16
import pytest

MOVINGAVGS = {
        10: 560,
        11: 560,
        12: 560,
        13: 560,
        14: 560,
        15: 560,
        16: 564,
        17: 568,
        18: 576,
        19: 584,
        20: 594,
        21: 612,
        22: 616,
        23: 616,
        24: 614,
        25: 602
    }
TOTALENERGY = {
    10: 0.34,
    11: 0.36,
    12: 0.39,
    13: 0.41,
    14: 0.45,
    15: 0.5,
    16: 0.53,
    17: 0.56,
    18: 0.58,
    19: 0.63,
    20: 0.68,
    21: 0.7,
    22: 0.74,
    23: 0.76,
    24: 0.8,
    25: 0.84
}


def test__start():
    ret = t._start(50, False)
    assert ret == 83.49

def test__start_caution_non_caution_late():
    ret = t._start(50, False)
    ret2 = t._start(50, True)
    assert ret == ret2

def test__start_caution_non_caution_early():
    ret = t._start(40, False)
    ret2 = t._start(40, True)
    assert ret > ret2

def test__stop():
    ret = t._stop(13, False)
    assert ret == 82.55

def test__stop_caution_non_caution_late():
    ret = t._stop(50, False)
    ret2 = t._stop(50, True)
    assert ret == ret2

def test__stop_caution_non_caution_early():
    ret = t._stop(40, False)
    ret2 = t._stop(40, True)
    assert ret > ret2
    
def test_allowed_current_base():
    ret = t.allowed_current(
        now_min=0,
        moving_avg=1,
        charger_enabled=False,
        charger_done=False,
        currents_dict=CURRENTS_THREEPHASE_1_32,
        total_energy=0,
        peak=1
    )
    assert ret == t.BASECURRENT

def test_allowed_current_1():
    ret = t.allowed_current(
        now_min=10,
        moving_avg=560,
        charger_enabled=True,
        charger_done=False,
        currents_dict=CURRENTS_THREEPHASE_1_32,
        total_energy=0.3,
        peak=10
    )
    assert ret == 16

def test_allowed_current_2():
    ret = t.allowed_current(
        now_min=50,
        moving_avg=560,
        charger_enabled=True,
        charger_done=False,
        currents_dict=CURRENTS_THREEPHASE_1_32,
        total_energy=0.3,
        peak=10
    )
    assert ret == 32


def test__start_quarterly():
    ret = t._start(50, False, True)
    assert ret == 60.62

def test__start_quarterly_caution():
    ret = t._start(50, True, True)
    assert ret == 52.13

def test__stop_quarterly():
    ret = t._start(22, False, True)
    assert ret == 65.29

def test__stop_quarterly_caution():
    ret = t._start(22, True, True)
    assert ret == 58.06


def test_allowed_current_negative_movingavg():
    ret = t.allowed_current(
        now_min=10,
        moving_avg=-560,
        charger_enabled=True,
        charger_done=False,
        currents_dict=CURRENTS_THREEPHASE_1_32,
        total_energy=0.3,
        peak=10
    )
    assert ret == 16

def test_allowed_current_negative_totalenergy():
    ret = t.allowed_current(
        now_min=10,
        moving_avg=560,
        charger_enabled=True,
        charger_done=False,
        currents_dict=CURRENTS_THREEPHASE_1_32,
        total_energy=-0.3,
        peak=10
    )
    assert ret == 16

def test_allowed_current_negative_totalenergy_and_movingavg():
    ret = t.allowed_current(
        now_min=10,
        moving_avg=-1560,
        charger_enabled=True,
        charger_done=False,
        currents_dict=CURRENTS_THREEPHASE_1_32,
        total_energy=-0.3,
        peak=10
    )
    assert ret == 20

def test_allowed_current_fluctuate():
    for i in range(12, 26):    
        ret = t.allowed_current(
            now_min=i,
            moving_avg=MOVINGAVGS.get(i, 0),
            charger_enabled=True,
            charger_done=False,
            currents_dict=CURRENTS_ONEPHASE_1_16,
            total_energy=TOTALENERGY.get(i, 0),
            peak=2.28
        )
        assert ret == 8

@pytest.mark.asyncio
async def test_allowed_current_fluctuate_async():
    for i in range(12, 26):    
        ret = await t.async_allowed_current(
            now_min=i,
            moving_avg=MOVINGAVGS.get(i, 0),
            charger_enabled=True,
            charger_done=False,
            currents_dict=CURRENTS_ONEPHASE_1_16,
            total_energy=TOTALENERGY.get(i, 0),
            peak=2.28
        )
        assert ret == 8