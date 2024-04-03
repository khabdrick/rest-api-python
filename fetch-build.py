import os
from dotenv import load_dotenv
import json
import requests

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
username = os.getenv("LT_USERNAME")
access_key = os.getenv("LT_ACCESS_KEY")

def get_lambdatest_all_builds():
    url = "https://%s:%s@api.lambdatest.com/automation/api/v1/sessions" % (username, access_token)
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)

    # Check if request was successful (status code 200)
    if response.status_code == 200:
        # Extract builds data from response
        builds_data = response.json()
        return builds_data

    else:
        print("Failed to fetch builds. Status code:", response.status_code)
        print("Error Message:", response.text)
        return None

def filter_builds_by_date_range(builds_data, start_date, end_date):
    filtered_builds = []
    for build in builds_data["data"]:
        create_timestamp = build["create_timestamp"]
        if start_date <= create_timestamp <= end_date:
            filtered_builds.append(build)
    return filtered_builds

# Define your desired start and end dates
start_date = "2024-01-01"
end_date = "2024-02-01"

# Fetch all builds
builds = get_lambdatest_all_builds()

# Filter builds by date range
filtered_builds = filter_builds_by_date_range(builds, start_date, end_date)
filtered_builds = json.dumps(filtered_builds, indent=4)
print("Filtered Builds:")
print(filtered_builds)

