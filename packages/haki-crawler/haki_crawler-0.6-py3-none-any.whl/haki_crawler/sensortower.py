from datetime import date, timedelta
from datetime import date
import requests
import json


def app_info(cookie, app_id='com.lemon.lvoverseas', country='US', auth_token='your_auth_token'):
    """
    This function retrieves data about a specified app from the Sensor Tower API.

    Args:
    - app_id (str): The ID of the app to retrieve data for.
    - cookie (str): The value of the 'session' cookie needed to authenticate the request.
    - country (str): The two-letter code for the country to retrieve data for. Defaults to 'US'.
    - auth_token (str): The authentication token for the Sensor Tower API. Defaults to 'your_auth_token'.

    Returns:
    - response (requests.Response): A response object containing the data retrieved from the API.
    """

    session = cookie['session']
    device_id = cookie['device_id']

    # Create the headers needed for the request
    headers = {
        'Cookie': f'session={session}; device_id={device_id}'
    }

    # Set the parameters for the request
    params = {
        'country': country,
        'auth_token': auth_token,
        'app_ids': app_id
    }

    # Set the URL for the request
    url = "https://api.sensortower.com/v1/android/apps"

    # Send the request to the API and return the response
    response = requests.request("GET", url, headers=headers, params=params)
    return response.json()


def app_info_minified(
        cookie,
        app_id='com.lemon.lvoverseas',
        country='US',
        auth_token='your_auth_token'
):
    """
    This function retrieves data about a specified app from the Sensor Tower API but minified

    Args:
    - app_id (str): The ID of the app to retrieve data for.
    - cookie (str): The value of the 'session' cookie needed to authenticate the request.
    - country (str): The two-letter code for the country to retrieve data for. Defaults to 'US'.
    - auth_token (str): The authentication token for the Sensor Tower API. Defaults to 'your_auth_token'.

    Returns:
    - response (requests.Response): A response object containing the data retrieved from the API.
    """

    session = cookie['session']
    device_id = cookie['device_id']

    # Create the headers needed for the request
    headers = {
        'Cookie': f'session={session}; device_id={device_id}'
    }

    # Set the parameters for the request
    params = {
        'country': country,
        'auth_token': auth_token,
        'app_ids': app_id
    }

    # Set the URL for the request
    url = "https://app.sensortower.com/api/android/apps/{}".format(app_id)
    # Send the request to the API and return the response
    response = requests.request("GET", url, headers=headers, params=params)
    return response.json()


def retention(cookie, app_id='com.lemon.lvoverseas', country='US', auth_token='your_auth_token'):
    """
    This function retrieves retention data for a specified app from the Sensor Tower API.

    Args:
    - cookie (dict): A dictionary containing 'session' and 'device_id' values needed to authenticate the request.
    - app_id (str): The ID of the app to retrieve retention data for. Defaults to 'com.lemon.lvoverseas'.
    - country (str): The two-letter code for the country to retrieve data for. Defaults to 'US'.
    - auth_token (str): The authentication token for the Sensor Tower API. Defaults to 'your_auth_token'.

    Returns:
    - response (requests.Response): A response object containing the data retrieved from the API.
    """

    session = cookie['session']
    device_id = cookie['device_id']

    # Create the headers needed for the request
    headers = {
        'Cookie': f'session={session}; device_id={device_id}'
    }

    # Set the parameters for the request
    params = {
        'country': country,
        'auth_token': auth_token,
        'app_ids': app_id,
        'date_granularity': "all_time",
        'start_date': date.today().strftime('%Y-%m-%d')
    }

    # Set the URL for the request
    url = "https://api.sensortower.com/v1/android/usage/retention"

    # Send the request to the API and return the response
    response = requests.request("GET", url, headers=headers, params=params)
    return response.json()


def usages(
    cookie,
    app_id='com.lemon.lvoverseas',
    usage_type='demographics',
    time_range=90,
    country='US',
    auth_token='your_auth_token'
):
    """
    This function retrieves usage data for a specified app from the Sensor Tower API.

    Args:
    - cookie (dict): A dictionary containing 'session' and 'device_id' values needed to authenticate the request.
    - app_id (str): The ID of the app to retrieve usage data for.
    - usage_type (str): The type of usage data to retrieve. Accepted values: 'session_count', 'session_duration', 'time_spent', 'demographics'.
    - time_range (int): The number of days to retrieve data for. Defaults to 90.

    Returns:
    - response (requests.Response): A response object containing the data retrieved from the API.
    """

    today = date.today()
    prior_date = today - timedelta(days=time_range)

    session = cookie['session']
    device_id = cookie['device_id']

    # Create the headers needed for the request
    headers = {
        'Cookie': f'session={session}; device_id={device_id}'
    }

    # Set the parameters for the request
    params = {
        'country': country,
        'auth_token': auth_token,
        'app_ids': app_id,
        'date_granularity': "all_time",
        "start_date": today.strftime('%Y-%m-%d'),
        "end_date": prior_date.strftime('%Y-%m-%d'),
    }

    # Set the URL for the request
    url = f"https://api.sensortower.com/v1/android/usage/{usage_type}"

    # Send the request to the API and return the response
    response = requests.request("GET", url, headers=headers, params=params)
    return response.json()


def advanced_search(cookie, custom_filter_id, term, limit=250, country='US', auth_token='your_auth_token'):
    """
    This function performs an advanced search on the Sensor Tower website.

    Args:
    - cookie (str): The value of the 'session' cookie needed to authenticate the request.
    - custom_filter_id (str): The ID of the custom filter to use for the search.
    - term (str): The search term to use for the search.
    - limit (int): The maximum number of results to return. Defaults to 250.

    Returns:
    - response (requests.Response): A response object containing the data retrieved from the search.
    """

    # Extract session and device_id from the cookie
    session = cookie['session']
    device_id = cookie['device_id']

    # Set the URL and parameters for the request
    url = "https://app.sensortower.com/advanced_search"
    params = {
        'country': country,
        'auth_token': auth_token,
        'device_type': 'android',
        'entity_type': 'app',
        'os': 'android',
        'search_fields[]': ['name', 'short_description'],
        'custom_fields_filter_id': custom_filter_id,
        'term': term,
        'limit': limit
    }

    # Set the headers for the request
    headers = {
        'Cookie': f'session={session}; device_id={device_id}'
    }

    # Send the request to the Sensor Tower website and return the response
    response = requests.request("GET", url, headers=headers, params=params)
    return response.json()


if __name__ == "__main__":
    # cookie = requests.get('http://localhost:3000/sensortower')
    # cookie = cookie.json()

    cookie = {
        "session": "2e8e2b1cfd6d791d55b235e53066f7a3",
        "device_id": "446def50-8494-487a-ab39-d8d965f014d2",
    }

    result = advanced_search(
        cookie=cookie, custom_filter_id="643bd16ee1714cfff1654c97", term="voice changer")
    print(json.dumps(result, indent=2))

