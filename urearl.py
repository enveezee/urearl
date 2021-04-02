#!/usr/bin/env python3
#
# * urearl.py - U R EARL - UNCLE R. EARL 
#
#               URL Now Can /Likely/ Extract Returns 
#               Easily Abstracting Regular Libraries
#           nvz < http://github.com/enveezee/urearl >
#
# ? DEFAULT settings, possibly import these from env or config?
DEFAULT_USER_AGENT='Mozilla/5.0'
DEFAULT_URL_REGEX=None

# Standard (Regular) Library imports.
from html.parser import HTMLParser
from json import loads
from urllib.error import HTTPError
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from re import match

# Static globals method names, if you don't want to use string literals.
D = DOWNLOAD = 'DOWNLOAD'
H = HTML = 'HTML'
J = JSON = 'JSON'
P = PARSE = 'PARSE'
R = REQUEST = 'REQUEST'
T = TRIM = 'TRIM'
V = VALIDATE = 'VALIDATE'

class UREarl():
    '''UNCLE R. EARL class object.
    
    This class extracts returnable information from URLs using standard library
    methods with batteries included.

    UREarl(url=None, method=None, headers=None)

    Methods: DOWNLOAD, HTML, JSON, PARSE, REQUEST, TRIM, VALIDATE
    '''
    def __init__(self, url=None, method=None, headers=None):
        # If instantiated with a URL, then set the URL for this instance.
        if url:
            self.url(url)
            # If instantiated with a method, call the method(s).
            if method:
                func = getattr(self, method.casefold())
                func()


    def download(self):
        '''Download a file from URL.'''
        response = self.request(self.url)
        # ! NOT IMPLEMENTED YET
        # TODO: detect filename, open and write file.. etc


    def html(self):
        '''Extract information from HTML.'''
        response = self.request(self.url)
        return htmlParser(response)



    def json(self):
        '''Parse JSON response from URL.'''
        response = self.request(self.url)
        if self.headers['Content-Type'] == 'application/json':
            try:
                jsonDict = loads(response)

            except JSONDecodeError as e:
                print('JSON decoding failed!')
                return e

            return jsonDict
        
        else:
            print('The content is not JSON')
            return None


    def parse(self, *args):
        '''Parse URL into its comoponent parts.
        
        If arguments are supplied, only those parts will be returned as a list.

        Without arguments a ParseResult object will be returned.
        '''
        url = urlparse(self.url)
        if args:
            # Return requested parts.
            output = []
            for arg in args:
                output.append(getattr(url, arg))
            return output
        # Return ParseResult.
        return url


    def request(self, headers=self.HEADERS):
        '''Form a request with optional headers for this url and attept to open
        returning a response.
        '''
        request = Request(self.url)
        if headers:
            # Supplied headers.
            for header in headers:
                request.add_header(header, headears[header])
        else:
            # Default headers.
            request.add_header('User-Agent', DEFAULT_USER_AGENT)

        try:
            response = urlopen(request)
        except HTTPError as e:
            # e.code, HTTP Error code.
            #   404
            # e.msg, HTTP Error message.
            #   Not Found
            # e.hdr, HTTP Response headers.
            #   Content-Type: text/html; charset=UTF-8
            #   Referrer-Policy: no-referrer
            #   Content-Length: 1567
            #   Date: Thu, 01 Apr 2021 04:31:31 GMT
            #   Connection: close
            # e.fp, pointer to the http.client.HTTPResponse object.
            self.code = e.code
            self.headers = e.hdr
            self.msg = e.msg
            self.response = e.fp
            return e

        self.code = response.status
        self.headers = dict(response.getheaders())
        self.response = response

        if not self.url == response.url:
            self.redirect = True

        if read:
            return response.read()
        else:
            return response


    def trim(self):
        '''Remove query strings from URL.'''
        if '?' in self.url: # ? Too simplistic?
            self.url = ''.join(self.url.split('?')[0])
        return self.url


    def url(self, url):
        '''Set or change the URL for this instance.'''
        self.url = url


    def validate(self):
        '''Check that URL is properly formed.'''
        # ! NOT IMPLEMENTED YET
        # TODO: check url against a regular expression, possibly encode it.
        pass


class htmlParser(HTMLParser):
    '''A simple standard library HTML parser for extracting information.'''
    def __init__(self, html):
        super().__init__()
        document = htmlDoc()


    def handle_starttag(self, tag, attrs):
        tag = htmlTag(tag, attrs)


    def handle_endtag(self, tag):
        pass


    def handle_data(self, data):
        pass


class htmlDoc():
    def __init__(self, url)
        pass


class htmlTag():
    def __init__(self, tag, parent):
        self.attrs = {}
        self.children = []
        self.data = []
        self.open = True
        self.parent = parent
        self.sibling = []
        self.tag = tag


    def close(self):
        self.open = False


    def insert(self, data):
        self.data.append(data)


    def relate(self, tag, relation):
        self.sibling.append(sibling)


if __name__ == '__main__':
    # TODO: Parse commandline and handle URL
    pass
