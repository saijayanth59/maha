import datetime
from dataclasses import dataclass, field

@dataclass
class DailyData:
    """
    Represents a single day's Open, High, Low, Close (OHLC) price data.
    """
    date: datetime.date
    open: float
    high: float
    low: float
    close: float