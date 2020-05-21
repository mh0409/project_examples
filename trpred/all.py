# Load modules
import pandas as pd
import requests
import json
import csv
import time
import datetime as dt
from psaw import PushshiftAPI # https://github.com/dmarx/psaw

## Submissions
def get_pages(subreddit: str, last_posttime = None):
    """Crawl a page of results from a given subreddit.
    :param subreddit: The subreddit to crawl.
    :param last_page: The last downloaded page.
    :return: A page of results.
    """

    url = "https://api.pushshift.io/reddit/search/submission"

    queries = {"subreddit": subreddit,\
               "size": 500,\
               "sort": "desc",\
               "sort_type": "created_utc"}

    # Called to "scroll down" page based on before
    if last_posttime is not None:
        queries["before"] = last_posttime

    results = requests.get(url, queries)

    if not results.ok:
        # something wrong happened
        raise Exception("Server returned status code {}".format(results.status_code))
    return results.json()["data"]


def crawl_subreddit(subreddit, max_submissions = 200000):
    """Crawl submissions from a subreddit.
    :param subreddit: The subreddit to crawl.
    :param max_submissions: The maximum number of submissions to download.
    :return: A list of submissions."""

    all_submissions = [] # empty list to hold all submissions
    last_posttime = None  # will become an empty list when reached the last page

    while len(all_submissions) < max_submissions:
        current_submissions = get_pages(subreddit, last_posttime)
        if len(current_submissions) == 0:
            break
        last_posttime = current_submissions[-1]["created_utc"]
        all_submissions += current_submissions

        #time.sleep(3)

        if len(all_submissions) % 10000 == 0: # to track progress for big pulls
            print(len(all_submissions))
    return all_submissions[:max_submissions]

## Comments
def crawl_comments(subreddit, before = None, after = None, max_comments = None):
    """Crawl comments from a subreddit
    :param subreddit: The subreddit to crawl.
    :param max_submissions: The max number of comments to download.
    :return: a data frame of comments"""

    # api = PushshiftAPI()
    #
    # if before is None and after is None:
    #     gen = api.search_comments(subreddit = subreddit)
    # else:
    #     gen = api.search_comments(subreddit = subreddit,
    #                              before = before,
    #                              after = after)
    #
    # comments = []

    today = dt.datetime.utcnow().date()
    filename_csv = "data/raw/comments/" + "allcomments-asof-" + str(today) + ".csv"  # create filename

    counter = 0

    for c in gen:
        comments.append(c)
        counter += 1

        if counter % 10000 == 0:
            df = pd.DataFrame([obj.d_ for obj in comments])
            df.to_csv(filename_csv, index = False, mode = "a") ## doing csv first since cant append to json

            print(counter)

            comments = [] # empty comments container to avoid memory issues

        if len(comments) % 10000 == 0:
            print(len(comments))

         # Omit this to not limit to max_comments
        if max_comments is not None:
            if counter >= max_comments:
                 break

    # Convert to json
    filename_json = "data/raw/comments/" + "allcomments-asof-" + str(today) + ".json"  # create filename

    json_data = [json.dumps(d) for d in csv.DictReader(open(filename_csv))]
    # Save as json


    with open(filename_json, 'w', encoding='utf-8') as f: # write file
        json.dump(json_data, f, ensure_ascii = False, indent=4)

    # Below code only used if the `if len(comments)` lines above not commented out
    #if False: # False flag - to be changed to True if we want to get rest of the results
    #    for c in gen:
    #        comments.append(c)


    # Create pandas data frame to return
    #df = pd.DataFrame([obj.d_ for obj in comments])

    return # empty return -- file saved
