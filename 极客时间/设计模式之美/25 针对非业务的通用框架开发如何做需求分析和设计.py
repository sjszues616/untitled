class RequestInterceptor():
    pass


class RequestHeadersInterceptor(RequestInterceptor):
    def apply(self, template):
        template.header("appId", "...")
        template.header("version", "...")
        template.header("timestamp", "...")
        template.header("token", "...")
        template.header("idempotent-token", "...")
        template.header("sequence-id", "...")


class CustomizedLogger():
    pass


class ErrorDecoder(object):
    pass


class Response:
    pass


class ResponseErrorDecoder(ErrorDecoder):
    def decode(self, methodKey: str, respone: Response):
        pass
