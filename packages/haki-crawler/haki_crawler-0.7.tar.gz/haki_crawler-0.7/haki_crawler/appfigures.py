import requests
import time


def product_id(cookie, app_id='com.airhorn.funny.prank.sounds'):
    """
    This function retrieves app information using Appfigures API, given a cookie and an optional app_id.

    :param cookie: Dictionary containing '_af_session' and '_af_user_token' keys
    :param app_id: The app identifier, defaults to 'com.airhorn.funny.prank.sounds'
    :return: JSON response containing app information
    """
    url = "https://appfigures.com/api/appbase/products?fields=product_id%2Cname%2Cstorefronts%2Cdeveloper%2Cactive&count=25&page=1"
    payload = f'q=%5B%22and%22%2Cnull%2C%5B%22and%22%2C%5B%22or%22%2C%5B%22match%22%2C%22name%22%2C%22{app_id}%22%2C%5B%22operator%22%2C%22and%22%5D%2C%5B%22mode%22%2C%22fuzzy%22%5D%5D%2C%5B%22match%22%2C%22developer%22%2C%22{app_id}%22%2C%5B%22operator%22%2C%22and%22%5D%2C%5B%22mode%22%2C%22phrase%22%5D%5D%2C%5B%22match%22%2C%22sku%22%2C%22{app_id}%22%5D%2C%5B%22match%22%2C%22stores_id%22%2C%22{app_id}%22%5D%5D%2C%5B%22and%22%2C%5B%22match%22%2C%22type%22%2C%5B%22or%22%2C%22app%22%2C%22bundle%22%5D%5D%2C%5B%22match%22%2C%22storefronts%22%2C%5B%22or%22%2C%22google_play%22%5D%5D%5D%5D%5D'

    _af_session = cookie['_af_session']
    x_st = cookie['x_st']

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': f'_af_session={_af_session}; G_ENABLED_IDPS=google',
        'X-Requested-With': 'XMLHttpRequest',
        'X-ST': x_st,
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()


def app_keywords(cookie, product_id):
    """
    This function retrieves app keywords using Appfigures ASO API, given a cookie and a product_id.

    :param cookie: Dictionary containing '_af_session' and '_af_user_token' keys
    :param product_id: The product identifier obtained from the Appfigures API
    :return: JSON response containing app keywords
    """
    url = f"https://appfigures.com/api/aso/products-snapshot?group_by=keyword%2Cproduct&products={product_id}&countries=US&device=handheld&page=1&"
    _af_session = cookie['_af_session']
    x_st = cookie['x_st']

    payload = {}
    headers = {
        'Cookie': f'_af_session={_af_session}; G_ENABLED_IDPS=google',
        'X-Requested-With': 'XMLHttpRequest',
        'X-ST': x_st,
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()


def keyword_rank(cookie, keyword):
    """
    This function retrieves keyword ranking using Appfigures ASO API, given a cookie and a keyword.

    :param cookie: Dictionary containing '_af_session' and '_af_user_token' keys
    :param keyword: The keyword for which the ranking is to be retrieved
    :return: JSON response containing keyword ranking
    """
    url = f"https://appfigures.com/api/aso-ranks?term={keyword}&country=US&storefront=google_play&page=&device=handheld&count=15"

    _af_session = cookie['_af_session']
    x_st = cookie['x_st']

    headers = {
        'Cookie': f'_af_session={_af_session}; G_ENABLED_IDPS=google',
        'X-Requested-With': 'XMLHttpRequest',
        'X-ST': x_st,
    }

    # Keep sending requests until status is not 'running'
    i = 0
    while i < 15*60:
        print("calling api for '{}'..".format(keyword))
        response = requests.get(url, headers=headers)
        response_data = response.json()

        status = response_data['metadata']['keyword']['status']
        print("status: {}".format(status))
        if status != 'running':
            return response_data

        i = i + 1
        time.sleep(1)
    return response_data


def keyword_rank_fast(cookie, keyword):
    """
    This function retrieves keyword ranking using Appfigures ASO API, given a cookie and a keyword, but faster.

    :param cookie: Dictionary containing '_af_session' and '_af_user_token' keys
    :param keyword: The keyword for which the ranking is to be retrieved
    :return: JSON response containing keyword ranking
    """
    url = f"https://appfigures.com/api/aso-ranks?term={keyword}&country=US&storefront=google_play&page=&device=handheld&count=15"

    _af_session = cookie['_af_session']
    x_st = cookie['x_st']

    headers = {
        'Cookie': f'_af_session={_af_session}; G_ENABLED_IDPS=google',
        'X-Requested-With': 'XMLHttpRequest',
        'X-ST': x_st,
    }

    # Keep sending requests until status is not 'running'
    response = requests.get(url, headers=headers)
    response_data = response.json()
    return response_data
