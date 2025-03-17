import requests


def get_ip_info(ip):
    url = f"http://ip-api.com/json/{ip}?fields=66846719"
    response = requests.get(url)
    return response.json()


if __name__ == "__main__":
    ip = input("Enter IP address: ")
    data = get_ip_info(ip)

    for key, value in data.items():
        print(f"{key}: {value}")