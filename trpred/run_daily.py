import os
import daily
import datetime as dt
import json
import pandas as pd


# Calculate time window
today = dt.datetime.utcnow().date()
yesterday = today - dt.timedelta(days = 1) # will count/collect posts after 00:00 on this date

# Get Submissions
submissions = daily.get_dailysubmissions("TheRedPill")

# Save data as .json
os.chdir("/Users/mariajoseherrera/Documents/Admin/yahb/Turing_Institute/trpred/data/raw/submissions")# change wd
filename = "dailysubmissions-" + str(yesterday) + ".json" # create filename

with open(filename, 'w', encoding='utf-8') as f: # write file
    json.dump(submissions, f, ensure_ascii = False, indent=4)


# Pull past day's comments (output: pandas df)
comments = daily.get_dailycomments("TheRedPill", today, yesterday)

# Save data as .json
os.chdir("/Users/mariajoseherrera/Documents/Admin/yahb/Turing_Institute/trpred/data/raw/comments")# change wd
filename = "dailycomments-" + str(yesterday) + ".json" # create filename

comments.to_json(filename)
