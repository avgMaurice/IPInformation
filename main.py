import requests


def get_ip_info(ip):
    """
    Retrieves detailed information about an IP address by making a request
    to the IP-API service. The returned data includes details such as
    location, ISP, and other metadata provided by the API.

    :param ip: The IP address to retrieve information for. Must be a valid
        string representation of an IPv4 or IPv6 address.
    :type ip: str
    :return: A dictionary containing the JSON response from the IP-API
        service. This includes keys such as 'status', 'country', 'region',
        and more metadata about the specified IP address.
    :rtype: dict
    :raises requests.exceptions.RequestException: If the HTTP request
        fails during communication with the API.
    """
    url = f"http://ip-api.com/json/{ip}?fields=66846719"
    response = requests.get(url)
    return response.json()


if __name__ == "__main__":
    ip = input("Enter IP address: ")
    data = get_ip_info(ip)

    for key, value in data.items():
        print(f"{key}: {value}")