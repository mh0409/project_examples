import all
import datetime as dt
import pandas as pd
import os
import json
from dateutil.relativedelta import relativedelta


## Comments

# Get past two years
today = dt.datetime.utcnow().date()
two_yrs_ago = today - relativedelta(years = 2)

all.crawl_comments("TheRedPill", before = today, after = two_yrs_ago)

# Get all comments
# all.crawl_comments('TheRedPill', 1000)

# Save data as .json
#filename = "allcomments-" + str(today) + ".json" # create filename

#df_comments.to_json(filename)
