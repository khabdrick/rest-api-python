## What is this Repository about?
This repo contains example code of fetching test data from Lmbdatest API. The file `fetch-build.py` contains code for fetching test data from Lambdatest API from a certain date range.`fetch-build-async.py` shows how you can fetch data from an API synchronously using aiohttp.

## Running the code 
If you already have Python installed you only need to install dotenv which we will use to get the environment variables.

```bash
pip install python-dotenv
```
After installations create the environment variables in `.env` file and populate with you LambdaTest details.
```
# .env
USERNAME_LT=your_username
ACCESS_TOKEN=your_access_key
```
