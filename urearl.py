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
from re import match
from urllib.error import HTTPError
from urllib.parse import unquote, urlparse
from urllib.request import Request, urlopen
from time import asctime, gmtime, strftime, time
from sys import argv

class UREarl:
    '''UNCLE R. EARL class object.
    
    This class extracts returnable information from URLs using standard library
    methods with batteries included.

    UREarl(url=None, headers=None)
    '''
    def __init__(self, url, headers=None):
        # Timestamp creation of URL instance.s
        self.ctime = time()

        # Set request headers.
        self._headers = headers

        # Parse out the URL for this instance.
        self._url = urlparse(url)

        # Make the request for this instance.
        self.request()

        # Handle response.
        self.response()


    def __getattribute__(self, name):
        # Track when class object was last accessed.
        if name[2:] != 'time':
            super(URL, self).__setattr__('atime', time())
        return super(URL, self).__getattribute__(name)


    def __setattr__(self, name, value):
        # Track when class object was last modified.
        if name != '_atime':
            super(URL, self).__setattr__('mtime', time())
        super(URL, self).__setattr__(name, value)


    def download(self):
        '''Download a file from URL.'''
        # ! NOT IMPLEMENTED YET
        # TODO: detect filename, open and write file.. etc


    def html(self):
        # ! NOT IMPLEMENTED
        # ? detect if its actually html, or implement other parsers
        pass


    def json(self):
        '''Parse JSON response from URL.'''
        # Try to parse JSON response.
        try:
            jsonDict = loads(self._response.read())

        # Handle errors with parsing
        except JSONDecodeError as e:
            self.error = 'JSON decoding failed!'
            return e

        # Set JSON data.
        self.data = jsonDict


    def request(self):
        '''Form a request with optional headers for this url and attept to open
        returning a response.
        '''
        self._request = Request(self._url.geturl())
        if self._headers:
            # Supplied headers.
            for header in self._headers:
                self._request.add_header(header, self._headers[header])
        else:
            # Default headers.
            self._request.add_header('User-Agent', DEFAULT_USER_AGENT)

        try:
            self._response = urlopen(request)
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
            self.code = e.code      # HTTPError code
            self.error = e.msg      # HTTPError message
            self.headers = e.hdr    # HTTPError headers
            self._response = e.fp   # HTTPResponse object
            return e

        # Set HTTPResponse status code.
        self.code = self._response.status
        # Set error to None, to know we succeeded in making request
        self.error = None
        # Set HTTPResponse headers.
        self.headers = dict(response.getheaders())

        if self._url.geturl() != response.url:
            self.redirect = True


    def response(self):
        if not self.error:
            contentType = self.headers['Content-Type']
            if 'application/json' in contentType:
                self.json()
            elif 'text/html' in contentType:
                # TODO hand off to self.html for further detection
                self.data = htmlParser(self.response.read())
            else:
                self.download()

#! Below here lies fecal code not finished.

class htmlParser(HTMLParser):
    '''A simple standard library HTML parser for extracting information.'''
    def __init__(self, html):
        super().__init__()


    def handle_starttag(self, tag, attrs):
        tag = htmlTag(tag, attrs)


    def handle_endtag(self, tag):
        pass


    def handle_data(self, data):
        pass


class htmlDoc:
    def __init__(self, html)
        pass


class htmlTag:
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
    # ! Braindead commandline implementation
    # TODO write a more robust implementation of commandline usage.
    print(URLEarl(argv[1]).data)
