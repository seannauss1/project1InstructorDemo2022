import sys

import requests
import secrets


def get_top_250_data()->list[dict]:
    api_query = f"https://imdb-api.com/en/API/Top250TVs/{secrets.secret_key}"
    response = requests.get(api_query)
    if response.status_code != 200: # if we don't get an ok response we have trouble
        print(f"Failed to get data, response code:{response.status_code} and error message: {response.reason} ")
        sys.exit(-1)
    # jsonresponse is a kinda useless dictionary, but the items element has what we need
    jsonresponse = response.json()
    show_list = jsonresponse["items"]
    return show_list


def report_results(top_show_data:list[dict]):
    with open("Output.txt", mode='a') as outputFile:  # open the output file for appending
        for show in top_show_data:
            print(show, file=outputFile)  # write each data item to file
            print("\n", file=outputFile)
            print("===================================================================", file=outputFile)


def main():
    top_show_data = get_top_250_data()
    report_results(top_show_data)


if __name__ == '__main__':
    main()
