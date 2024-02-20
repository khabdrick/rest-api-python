import os
from dotenv import load_dotenv
import json
import aiohttp
import asyncio

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
username = os.getenv("USERNAME_LT")
access_token = os.getenv("ACCESS_TOKEN")

async def test_get_lambdatest_all_builds():
    url = f"https://{username}:{access_token}@api.lambdatest.com/automation/api/v1/builds"
    headers = {"accept": "application/json"}
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                builds_data = await response.json()
                
                return builds_data
            else:
                print("Failed to fetch builds. Status code:", response.status)
                print("Error Message:", await response.text())
                return None

def filter_builds_by_date_range(builds_data, start_date, end_date):
    filtered_builds = []
    for build in builds_data["data"]:
        create_timestamp = build["create_timestamp"]
        if start_date <= create_timestamp <= end_date:
            filtered_builds.append(build)
    return filtered_builds

async def main():
    # Define your desired start and end dates
    start_date = "2024-01-01"
    end_date = "2024-02-01"

    # Fetch all builds asynchronously
    builds = await test_get_lambdatest_all_builds()

    # Filter builds by date range
    filtered_builds = filter_builds_by_date_range(builds, start_date, end_date)
    formatted_filtered_builds = json.dumps(filtered_builds, indent=4)
    print("Filtered Builds:")
    print(formatted_filtered_builds)

# Run the asyncio event loop
asyncio.run(main())
