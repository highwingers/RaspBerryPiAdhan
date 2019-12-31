from lib.PrayerPy import PrayerData

data = PrayerData("20 squirrel ln levittown ny 11756", "RaspberryPi",-5)
times = data.getTimes()
print(times["fajr"])
print(times["zuhr"])
print(times["asr"])
print(times["maghrib"])
print(times["isha"])