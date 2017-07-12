

import os
from datetime import datetime
stat = os.stat('normal.log')
str1 = datetime.fromtimestamp(stat.st_atime)
str2 = datetime.date(str1)


