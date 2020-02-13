from datetime import date

from adhan import adhan
from adhan.methods import ISNA,KARACHI, ASR_STANDARD

params = {}
params.update(KARACHI)
params.update(ASR_STANDARD)

adhan_times = adhan(
    day=date.today(),
    location=(31.5656079,74.3141775),
    parameters=params,
    timezone_offset=-5,
)

print(date.today())
print(adhan_times)
