from typing import Union
import requests
import timeit


class APIRequester:
    def __init__(self):
        self.url_prefix = "http://localhost:8000/rfid-epayment-api/"
        self.session = requests.Session()

    def get(self, url: str):
        if url[0] == "/":
            url = url[1:]
        rurl = self.url_prefix + url
        response = self.session.get(url=rurl)
        try:
            if response.status_code == 200:
                json_data = response.json()
                return json_data["api_response"]
            return []
        except requests.exceptions.JSONDecodeError as e:
            print(e)
            return []

    def post(self, url: str, payload: Union[list, dict]):
        if url[0] == "/":
            url = url[1:]
        rurl = self.url_prefix + url
        response = self.session.post(url=rurl, json=payload)
        try:
            if response.status_code == 200:
                json_data = response.json()
                return json_data["api_response"]
            return []
        except requests.exceptions.JSONDecodeError as e:
            print(e)
            return []


if __name__ == "__main__":
    dts = []
    test_times = 50

    # Avg exec time:
    #   requests.get()           -> 2    s
    #   requests.Session().get() -> 0.04 s
    requester = APIRequester()

    for i in range(test_times):
        t0 = timeit.default_timer()
        ret = requester.get("card/")
        if ret:
            print(f"{i} success")
        t1 = timeit.default_timer()
        dts.append(t1 - t0)

    avg_time = sum(dts) / len(dts)
    print(f"Test {len(dts)} times, avg time is {avg_time}s")
    print(dts)
