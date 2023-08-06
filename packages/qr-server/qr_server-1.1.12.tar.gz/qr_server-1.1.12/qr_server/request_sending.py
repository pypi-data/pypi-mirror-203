from dataclasses import dataclass
import requests
import json

@dataclass
class QRAddress:
    host: str
    port: str

    def get_full_url(self, url):
        return f'{self.host}:{self.port}/{url}'


class QRRequest:
    def __init__(self, json_data=None, params=None, headers=None, form=None):
        self.__json_data = json_data
        self.__params = params
        self.__headers = headers
        self.__form = form

    def get_json_data(self): return self.__json_data

    def get_params(self): return self.__params

    def get_headers(self): return self.__headers

    def get_form(self): return dict(self.__form) if self.__form is not None else dict()

    params = property(get_params)
    json_data = property(get_json_data)
    headers = property(get_headers)

    def get_args(self) -> dict:
        args = {
            'json': self.get_json_data(),
            'params': self.get_params(),
            'headers': self.get_headers(),
            'data': self.get_form(),
        }
        for a in 'json', 'params', 'data':
            if len(args[a]) == 0:
                args.pop(a)
        if args['headers'].get('CONTENT_TYPE') is not None:
            # clear content type in case if 'data' (form) field is present - it needs boundaries which are better to be recalculated
            args['headers'] = dict(args['headers'])
            args['headers'].pop('Content-Type')
        return args


@dataclass
class QRResponse:
    ok: bool
    status_code: int
    reason: str
    content: bytes

    def get_json(self):
        return json.loads(self.content)


def send_request(address: QRAddress, url: str, method='GET', request: QRRequest = None):
    if request is None:
        request = QRRequest(None, None, None)

    resp = requests.request(method, address.get_full_url(url), **request.get_args())

    return QRResponse(resp.ok, resp.status_code, resp.reason, resp.content)