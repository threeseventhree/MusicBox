import urequests # type: ignore

class APIHandler:
    def __init__(self, host):
        self.host = host

    def get(self, address: str):
        response = urequests.get(self.host + address)
        responseData = response.json()
        response.close()
        return responseData

    def post(self, address: str, data=None):
        response = urequests.post(self.host + address, json=data)
        responseData = response.json()
        response.close()
        return responseData
