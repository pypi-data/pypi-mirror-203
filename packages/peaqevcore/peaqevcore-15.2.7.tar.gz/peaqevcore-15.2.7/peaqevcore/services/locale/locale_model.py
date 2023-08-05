from dataclasses import dataclass, field
from datetime import datetime
from ...models.locale.enums.querytype import QueryType
from ...models.locale.enums.time_periods import TimePeriods
from ..locale.time_pattern import TimePattern
from ...models.locale.price.locale_price import LocalePrice
from .querytypes.querytypes import LocaleQuery


@dataclass(frozen=True)
class Locale_Type:
    observed_peak: QueryType
    charged_peak: QueryType
    query_model: LocaleQuery
    price: LocalePrice = None
    free_charge_pattern: TimePattern = None
    peak_cycle: TimePeriods = TimePeriods.Hourly
    is_quarterly: bool = field(init=False, repr=False)
    

    def free_charge(self, mockdt: datetime=datetime.min) -> bool:
        if self.free_charge_pattern is None:
            return False
        now = datetime.now() if mockdt is datetime.min else mockdt
        return self.free_charge_pattern.valid(now)

    def is_quarterly(self) -> bool:
        return self.peak_cycle == TimePeriods.QuarterHourly
