class RealService:
    def request(self):
        return "Real service response"


class ServiceProxy:
    def __init__(self):
        self._service = None

    def request(self):
        if self._service is None:
            self._service = RealService()
        return self._service.request()
