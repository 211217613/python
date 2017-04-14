import requests

BASE_URL_V0 = 'https://hacker-news.firebaseio.com/v0/item/' 
BASE_URL_V1 = 'https://hacker-news.firebaseio.com/v1/item/' 

def main():
    get = requests.get(BASE_URL_V1 + str(13301832))
    if get.status_code is not 200:
        print("Something went wrong")
    # print(get.json())
    get.json().keys
    # for keys, values in get.json():
        # print(get.json().keys, get.json().values)
if __name__ == '__main__':
    main()