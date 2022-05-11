from datetime import datetime
from time import strftime
import pytz

Spain_timezone = pytz.timezone("Europe/Madrid")
Spain_date = datetime.now(Spain_timezone)
print("Spain: ", Spain_date.strftime("%d/%m/%Y", "%H:%M:%S"))

Mexico_timezone = pytz.timezone("America/MExico_City")
Mexico_date = datetime.now(Mexico_timezone)
print("Cuidad de México: ", Mexico_date.strftime("%d/%m/%Y", "%H:%M:%S"))

Arizona_timezone = pytz.timezone("US/Arizona")
Arizona_date = datetime.now(Arizona_timezone)
print("Arizona: ", Arizona_date.strftime("%m/%d/%Y", "%H:%M:%S"))