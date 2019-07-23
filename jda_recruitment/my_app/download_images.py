#!/usr/bin/env python
"""Download images from remote location and stores it in local disk.

Args:
    text-file: plain-text file containing URLs, one per line.

Author:
    Manish Jaiswal (mjaiswal1905@gmail.com)
"""

import argparse
import logging
import os
import sys
import requests


class DownloadImages:

    def __init__(self, filepath):
        self.filepath = filepath

    def read_file(self):
        """Fetch a list of URLs from a plaintext file and pass it to _download method.
        """
        if not os.path.isfile(self.filepath):
            logging.error("File path {} does not exist. Exiting...".format(os.path.abspath(self.filepath)))
            sys.exit(1)

        with open(self.filepath, 'r') as _fh:
            logging.info("Start reading file: {}".format(os.path.abspath(self.filepath)))
            for _line in _fh.readlines():
                _url = _line.rstrip()
                logging.debug("URL: {}".format(_url))
                _location = self._download(_url)
                logging.info("Image location on disk: {}".format(os.path.abspath(_location)))

            logging.info("Finished reading file")

    @staticmethod
    def _download(_url):
        """Download the image from given url and store in local disk.

        Args:
            _url: URL of a image(.jpg)

        Returns:
            disk location of stored image
        """
        _response = requests.get(_url, stream=True)

        try:
            _file = os.path.basename(_url)

            with open(_file, 'wb') as _image:
                for _chunk in _response.iter_content(chunk_size=1024*1024):
                    if _chunk:
                        _image.write(_chunk)
            _response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            logging.error(err)
            sys.exit(1)

        return _file


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download images from remote location and stores it in local disk.')
    parser.add_argument(dest='text_file', help='plain-text file containing URLs, one per line.')
    parser.add_argument('--debug', dest='logLevel', action='store_const', const='DEBUG', default='INFO',
                        help='enable DEBUG logging level')
    args = parser.parse_args()
    text_file = args.text_file

    logging.basicConfig(level=args.logLevel,
                        format='%(asctime)s - %(module)s - %(levelname)s - %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='my_app.log',
                        filemode='a')

    images = DownloadImages(text_file)
    images.read_file()
