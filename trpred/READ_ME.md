# trp.red
For use with Turing trp.red project

run_daily.py
* To be run daily to collect both submissions and comments added over the past day.
* Functions run from this file are in daily.py

run_once_submissions.py
* Run to scrape all submissions of r/TheRedPill
* Calls function `crawl_subreddit()` from all.py

run_once_comments.py
* Run to scrape two years of comments of r/TheRedPill
* Calls function `crawl_comments()` from all.py

all.py
* Contains functions `get_pages()`, `crawl_subreddit()`, `crawl_comments()`

daily.py
* Contains functions `get_pages()` (diff vs. one in all.py -- change name?), `get_dailysubmissions()`, `get_dailycomments()`
