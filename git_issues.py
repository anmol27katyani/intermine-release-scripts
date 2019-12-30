#!/usr/bin/env python
from __future__ import print_function
import requests


ISSUES = {}
API_URL = 'https://api.github.com/'
URL1 = API_URL+'repos/intermine/intermine/issues?direction=asc&state=all&milestone=48&per_page=1000'
# For improving the code quality
RESPONSE = requests.get(URL1)

ISSUES = RESPONSE.json()
for issue in ISSUES:
    if 'pull_request' not in issue:
        print("#" + str(ISSUES['number']) + " - " + str(ISSUES['title']))


print("\n --------------------- \n")

MILESTONES = {}

RESPONSE = requests.get('https://api.github.com/repos/intermine/intermine/milestones')

MILESTONES = RESPONSE.json()
for milestone in MILESTONES:
    print("#" + str(MILESTONES['number']) + " - " + str(MILESTONES['title']))


# https://developer.github.com/v3/issues/
