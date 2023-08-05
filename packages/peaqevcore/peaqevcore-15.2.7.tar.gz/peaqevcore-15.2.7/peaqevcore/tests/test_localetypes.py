from datetime import datetime, date, time
import pytest
from ..models.locale.enums.querytype import QueryType
from ..services.locale.querytypes.const import QUERYTYPE_AVERAGEOFTHREEDAYS, QUERYTYPE_AVERAGEOFTHREEHOURS, QUERYTYPE_SOLLENTUNA
from ..services.locale.querytypes.querytypes import QUERYTYPES
from ..services.locale.countries.sweden import SE_SHE_AB, SE_Bjerke_Energi, SE_Gothenburg, SE_Kristinehamn, SE_Skovde, SE_Sollentuna, SE_Ellevio,SE_JBF
from ..services.locale.countries.belgium import VregBelgium
from ..services.locale.countries.default import NoPeak

def test_SE_Bjerke_Energi():
    p = SE_Bjerke_Energi
    assert p.free_charge(p, mockdt=datetime.combine(date(2005, 7, 14), time(22, 30))) is True
    assert p.free_charge(p, mockdt=datetime.combine(date(2005, 7, 14), time(15,00))) is False
    del(p)

def test_generic_querytype_avg_threedays():
    pt = QUERYTYPES[QueryType.AverageOfThreeDays]
    pt.reset()
    pt.try_update(new_val=1.2, timestamp=datetime.combine(date(2022, 7, 14), time(20, 30)))
    pt.try_update(new_val=2, timestamp=datetime.combine(date(2022, 7, 14), time(21, 30)))
    to_state_machine = pt.peaks.export_peaks
    pt.peaks.set_init_dict(dict_data=to_state_machine, dt=datetime.combine(date(2022, 7, 14), time(23, 30)))
    pt.try_update(new_val=0.6, timestamp=datetime.combine(date(2022, 7, 15), time(21, 30)))
    assert len(pt.peaks.p) == 2
    assert pt._charged_peak_value == 1.3

def test_generic_querytype_avg_threedays2():
    pg = QUERYTYPES[QueryType.AverageOfThreeDays]
    pg.reset()
    pg.try_update(new_val=1.2, timestamp=datetime.combine(date(2022, 7, 14), time(20, 30)))
    pg.try_update(new_val=2, timestamp=datetime.combine(date(2022, 7, 14), time(21, 30)))
    assert len(pg.peaks.p) == 1
    assert pg._charged_peak_value == 2

def test_generic_querytype_avg_threedays3():
    to_state_machine = {'m': 7, 'p': {'14h21': 2}}
    p1 = QUERYTYPES[QueryType.AverageOfThreeDays]
    p1.reset()
    p1.try_update(new_val=1, timestamp=datetime.combine(date(2022, 7, 15), time(21, 30)))
    p1.peaks.set_init_dict(to_state_machine, datetime.combine(date(2022, 7, 15), time(21, 30)))
    assert len(p1.peaks.p) == 2
    assert p1.charged_peak == 1.5
    assert p1.observed_peak == 1
    p1.try_update(new_val=2, timestamp=datetime.combine(date(2022, 7, 15), time(22, 30)))
    assert len(p1.peaks.p) == 2
    assert p1.charged_peak == 2
    assert p1.observed_peak == 2

def test_faulty_number_in_import():
    to_state_machine = {'m': 7, 'p': {'14h21': 2, '11h22': 1.49, '12h9': 1.93, '12h14': 0.73}}
    p1 = QUERYTYPES[QueryType.AverageOfThreeDays]
    p1.reset()
    p1.try_update(new_val=1, timestamp=datetime.combine(date(2022, 7, 15), time(21, 30)))
    p1.peaks.set_init_dict(to_state_machine, datetime.combine(date(2022, 7, 15), time(21, 30)))
    assert len(p1.peaks.p) == 3
    assert p1.charged_peak == 1.81
    assert p1.observed_peak == 1.49
    p1.try_update(new_val=1.5, timestamp=datetime.combine(date(2022, 7, 15), time(22, 30)))
    assert len(p1.peaks.p) == 3
    assert p1.charged_peak == 1.81
    assert p1.observed_peak == 1.5
    
def test_overridden_number_in_import():
    to_state_machine = {'m': 7, 'p': {'11h22': 1.49, '12h9': 1.93, '13h16': 0.86}}
    p1 = QUERYTYPES[QueryType.AverageOfThreeDays]
    p1.reset()
    p1.try_update(new_val=0.22, timestamp=datetime.combine(date(2022, 7, 13), time(21, 30)))
    p1.peaks.set_init_dict(to_state_machine, datetime.combine(date(2022, 7, 13), time(21, 30)))
    assert p1.charged_peak == 1.43

def test_SE_Gothenburg():
    p = SE_Gothenburg
    assert p.free_charge(p) is False
    p.query_model.try_update(new_val=1.2, timestamp=datetime.combine(date(2022, 7, 14), time(22, 30)))
    p.query_model.try_update(new_val=1, timestamp=datetime.combine(date(2022, 7, 16), time(22, 30)))
    p.query_model.try_update(new_val=1.5, timestamp=datetime.combine(date(2022, 7, 17), time(22, 30)))
    p.query_model.try_update(new_val=1.7, timestamp=datetime.combine(date(2022, 7, 17), time(22, 30)))
    p.query_model.try_update(new_val=1.5, timestamp=datetime.combine(date(2022, 7, 19), time(22, 30)))
    assert p.query_model.observed_peak > 0
    del(p)

def test_generic_querytype_avg_threehour2s():
    p = SE_Sollentuna
    p.query_model.try_update(new_val=1.2, timestamp=datetime.combine(date(2022, 7, 14), time(22, 30)))
    p.query_model.try_update(new_val=1, timestamp=datetime.combine(date(2022, 7, 16), time(22, 30)))
    p.query_model.try_update(new_val=1.5, timestamp=datetime.combine(date(2022, 7, 17), time(22, 30)))
    p.query_model.try_update(new_val=1.7, timestamp=datetime.combine(date(2022, 7, 17), time(22, 30)))
    p.query_model.try_update(new_val=1.5, timestamp=datetime.combine(date(2022, 7, 19), time(22, 30)))
    assert p.query_model.observed_peak == 0
    d1 = date(2022, 7, 14)
    t = time(22, 30)
    dt1 = datetime.combine(d1, t)
    p.query_model.try_update(new_val=1.2, timestamp=dt1)
    d2 = date(2022, 7, 16)
    dt2 = datetime.combine(d2, t)
    p.query_model.try_update(new_val=1, timestamp=dt2)
    d3 = date(2022, 7, 17)
    dt3 = datetime.combine(d3, t)
    p.query_model.try_update(new_val=1.5, timestamp=dt3)
    d3 = date(2022, 7, 17)
    dt3 = datetime.combine(d3, t)
    p.query_model.try_update(new_val=1.7, timestamp=dt3)
    d4 = date(2022, 7, 19)
    dt4 = datetime.combine(d4, t)
    p.query_model.try_update(new_val=1.5, timestamp=dt4)
    
# def test_SE_Kristinehamn():
#     p = SE_Kristinehamn
#     p.query_model.try_update(new_val=0.5, timestamp=datetime.combine(date(2023, 6, 14), time(20, 30)))
#     assert p.query_model.charged_peak == 0.5
#     p.query_model.try_update(new_val=1.2, timestamp=datetime.combine(date(2023, 2, 14), time(16, 30)))
#     assert p.query_model.charged_peak == 1.2

def test_peak_new_month():
    p = SE_Gothenburg
    p.query_model.try_update(new_val=1.2, timestamp=datetime.combine(date(2022, 6, 2), time(22, 30)))
    p.query_model.try_update(new_val=1, timestamp=datetime.combine(date(2022, 6, 16), time(22, 30)))
    p.query_model.try_update(new_val=1.5, timestamp=datetime.combine(date(2022, 6, 17), time(20, 30)))
    p.query_model.try_update(new_val=1.7, timestamp=datetime.combine(date(2022, 6, 17), time(22, 30)))
    p.query_model.try_update(new_val=1.5, timestamp=datetime.combine(date(2022, 6, 19), time(22, 30)))
    assert len(p.query_model.peaks.p) == 3
    assert p.query_model.observed_peak == 1.2
    p.query_model.try_update(new_val=0.03, timestamp=datetime.combine(date(2022, 7, 1), time(0, 0)))
    assert len(p.query_model.peaks.p) == 1
    assert p.query_model.observed_peak == 0.03
    
def test_peak_new_hour():
    p = SE_Gothenburg
    p.query_model.try_update(new_val=1.2, timestamp=datetime.combine(date(2022, 6, 1), time(1, 30)))
    assert p.query_model.peaks.p == {(1, 1): 1.2}
    p.query_model.try_update(new_val=1, timestamp=datetime.combine(date(2022, 6, 1), time(6, 30)))
    assert p.query_model.peaks.p == {(1, 1): 1.2}
    p.query_model.try_update(new_val=1.5, timestamp=datetime.combine(date(2022, 6, 1), time(9, 30)))
    assert p.query_model.peaks.p == {(1, 9): 1.5}

def test_peak_new_hour_multiple():
    p = SE_Gothenburg
    p.query_model.try_update(new_val=1.2, timestamp=datetime.combine(date(2022, 7, 2), time(22, 30)))
    p.query_model.try_update(new_val=1, timestamp=datetime.combine(date(2022, 7, 16), time(22, 30)))
    p.query_model.try_update(new_val=1.5, timestamp=datetime.combine(date(2022, 7, 17), time(20, 30)))
    p.query_model.try_update(new_val=1.7, timestamp=datetime.combine(date(2022, 7, 17), time(22, 30)))
    p.query_model.try_update(new_val=1.5, timestamp=datetime.combine(date(2022, 7, 19), time(22, 30)))
    assert p.query_model.peaks.export_peaks == {'m': 7, 'p': {'2h22': 1.2, '17h22': 1.7, '19h22': 1.5}}
    assert p.query_model.peaks.p == {(2,22): 1.2, (17,22): 1.7, (19,22): 1.5}
    assert p.query_model.peaks.m == 7
    p.query_model.try_update(new_val=2.5, timestamp=datetime.combine(date(2022, 7, 19), time(23, 30)))
    assert p.query_model.peaks.export_peaks == {'m': 7, 'p': {'2h22': 1.2, '17h22': 1.7, '19h23': 2.5}}
    assert p.query_model.peaks.p == {(2,22): 1.2, (17,22): 1.7, (19,23): 2.5}
    
def test_overridden_number_in_import():
    to_state_machine = {'m': 7, 'p': {'1h15': 1.5}}
    p1 = QUERYTYPES[QueryType.AverageOfThreeDays]
    p1.reset()
    p1.try_update(new_val=0.22, timestamp=datetime.combine(date(2022, 7, 2), time(15, 30)))
    p1.peaks.set_init_dict(to_state_machine, datetime.combine(date(2022, 7, 2), time(15, 30)))
    assert len(p1.peaks.p) == 2

def test_quarterly():
    p = SE_Kristinehamn
    assert not p.is_quarterly(p)
    p2 = VregBelgium
    assert p2.is_quarterly(p2)

def test_peak_new_month_2():
    p = SE_Gothenburg
    p.query_model.try_update(new_val=1.2, timestamp=datetime.combine(date(2022, 7, 2), time(22, 30)))
    p.query_model.try_update(new_val=1, timestamp=datetime.combine(date(2022, 7, 16), time(22, 30)))
    p.query_model.try_update(new_val=1.5, timestamp=datetime.combine(date(2022, 7, 17), time(20, 30)))
    p.query_model.try_update(new_val=1.7, timestamp=datetime.combine(date(2022, 7, 17), time(22, 30)))
    p.query_model.try_update(new_val=1.5, timestamp=datetime.combine(date(2022, 7, 19), time(22, 30)))
    assert len(p.query_model.peaks.p) == 3
    assert p.query_model.observed_peak == 1.2
    p.query_model.try_update(new_val=0.03, timestamp=datetime.combine(date(2022, 8, 1), time(22, 30)))
    assert p.query_model.observed_peak == 0.03
    assert len(p.query_model.peaks.p) == 1
    p.query_model.try_update(new_val=0.06, timestamp=datetime.combine(date(2022, 8, 2), time(22, 30)))
    assert len(p.query_model.peaks.p) == 2
    assert p.query_model.charged_peak == 0.04
    assert p.query_model.observed_peak == 0.03

def test_se_ellevio():
    p = SE_Ellevio
    assert p.free_charge(p, mockdt=datetime.now()) is False
    p.query_model.try_update(new_val=1.2, timestamp=datetime.combine(date(2022, 7, 14), time(22, 30)))
    p.query_model.try_update(new_val=1, timestamp=datetime.combine(date(2022, 7, 16), time(22, 30)))
    p.query_model.try_update(new_val=1.5, timestamp=datetime.combine(date(2022, 7, 17), time(22, 30)))
    p.query_model.try_update(new_val=1.7, timestamp=datetime.combine(date(2022, 7, 17), time(22, 30)))
    p.query_model.try_update(new_val=1.5, timestamp=datetime.combine(date(2022, 7, 19), time(22, 30)))
    assert p.query_model.observed_peak > 0
    del(p)

def test_se_jbf():
    p = SE_JBF
    assert p.free_charge(p, mockdt=datetime.combine(date(2023, 2, 14), time(21, 59))) is False
    assert p.free_charge(p, mockdt=datetime.combine(date(2023, 2, 14), time(22, 1))) is True
    assert p.free_charge(p, mockdt=datetime.combine(date(2023, 5, 17), time(12, 0))) is True

    p.query_model.try_update(new_val=1.2, timestamp=datetime.combine(date(2023, 2, 6), time(10, 30)))
    p.query_model.try_update(new_val=1, timestamp=datetime.combine(date(2023, 2, 6), time(11, 30)))
    assert p.query_model.observed_peak == 1
    assert p.query_model.charged_peak == 1.1
    p.query_model.try_update(new_val=2, timestamp=datetime.combine(date(2023, 2, 6), time(12, 30)))
    assert p.query_model.charged_peak == 1.4
    del(p)    

# def test_no_peak():
#     p = NoPeak
#     assert p.free_charge(p, mockdt=datetime.now()) is True
#     p.query_model.try_update(new_val=1.5, timestamp=datetime.combine(date(2023, 7, 19), time(22, 30)))
#     assert p.query_model.charged_peak == 0