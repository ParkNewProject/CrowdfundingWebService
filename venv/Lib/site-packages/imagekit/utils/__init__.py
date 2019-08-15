from __future__ import absolute_import

from .contants import constants as ct

from os import path
from hashlib import sha1
import hmac
import sys

PY3 = (sys.version_info[0] == 3)

if PY3:
    import http.client as httplib
    NotConnected = httplib.NotConnected
    import urllib.request as urllib2
    import urllib.error
    HTTPError = urllib.error.HTTPError
    from io import StringIO, BytesIO
    from urllib.parse import urlencode, unquote, urlparse, parse_qs, quote_plus
    to_bytes = lambda s: s.encode('utf8')
    to_bytearray = lambda s: bytearray(s, 'utf8')
    to_string = lambda b: b.decode('utf8')
    string_types = str

else:
    import httplib
    from httplib import NotConnected
    from io import BytesIO
    import StringIO
    import urllib2
    HTTPError = urllib2.HTTPError
    from urllib import urlencode, unquote, quote_plus
    from urlparse import urlparse, parse_qs
    to_bytes = str
    to_bytearray = str
    to_string = str
    string_types = (str, unicode)


__all__ = ['getHost', 'get_protocol', 'get_image_upload_url', 'calculate_signature', 'get_inifinite_expiry']


class Error(Exception): pass
class NotFound(Error): pass
class NotAllowed(Error): pass
class AlreadyExists(Error): pass
class RateLimited(Error): pass
class BadRequest(Error): pass
class GeneralError(Error): pass
class AuthorizationRequired(Error): pass

EXCEPTION_CODES = {
    400: BadRequest,
    401: AuthorizationRequired,
    403: NotAllowed,
    404: NotFound,
    409: AlreadyExists,
    420: RateLimited
}


def get_host(imagekitid, use_subdomain=None):
    if not use_subdomain:
        return ct["COMMON_GET_SUBDOMAIN"] + ct["BASE_GET"]
    else:
        return imagekitid + ct["BASE_GET"]


def get_protocol(use_secure):
    if use_secure:
        return ct["HTTPS_PROTOCOL"]
    else:
        return ct["HTTP_PROTOCOL"]


def get_image_upload_url(imagekitid):
    return path.join(ct["BASE_UPLOAD"], ct["UPLOAD_URL"], imagekitid)


def _sort_key_func(item):
    # print(item)
    pairs = []
    for k, v in item:
        # print(k,v)
        pairs.append((k, v))
    return sorted(pairs)


class Custom(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return '{}'.format(self.value)


def calculate_signature(options):
    _message = ['filename=' + options["filename"], 'timestamp=' + str(options["timestamp"]),
                'apiKey=' + options["api_key"]]

    # Sample sorted value
    # apiKey=2qiLpcAeOVWm/Hpzs28jfEofSl0=&filename=gate.jpg&timestamp=1483354819
    _message = sorted(_message)

    _str = "&".join(str(v) for v in _message)
    # print(_str, options["api_secret"])
    hashed = hmac.new(to_bytes(options["api_secret"]), to_bytes(_str), sha1)
    hex_dig = hashed.hexdigest()
    # print(hex_dig)
    return hex_dig


def get_inifinite_expiry():
    return ct["INFINITE_EXPIRY_TIME"]
