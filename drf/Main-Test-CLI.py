import requests
import argparse

def test_api(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the response has an error status code

        print("API Test Successful")
        print("Response:")
        print(response.text)

    except requests.exceptions.RequestException as e:
        print("API Test Failed:", e)

def main():
    parser = argparse.ArgumentParser(description="Command-line tool to test APIs")
    parser.add_argument("url", type=str, help="URL of the API to test")

    args = parser.parse_args()
    test_api(args.url)

if __name__ == "__main__":
    main()
