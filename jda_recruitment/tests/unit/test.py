#!/usr/bin/env python
"""Test read_file function
"""

import unittest
from unittest.mock import patch, mock_open
import requests_mock

from my_app.download_images import DownloadImages


class TestReadFiles(unittest.TestCase):

    def setUp(self):
        self.file_content_mock = """http://mywebserver.com/images/271947.jpg"""
        self.fake_file_path = 'file/path/mock'
        self.images = DownloadImages(self.fake_file_path)

    @patch('my_app.download_images.os.path.isfile')
    @patch('my_app.download_images.os.path.abspath')
    @patch('my_app.download_images.DownloadImages._download')
    def test_read_file(self, mock_isfile, mock_abspath, mock_download):
        mock_isfile.return_value = True
        mock_abspath.return_value = 'file/path/image'
        mock_download.return_value = 'image'
        with patch('my_app.download_images.open'.format(__name__),
                   new=mock_open(read_data=self.file_content_mock)) as _file:
            self.images.read_file()
            _file.assert_called_once_with(self.fake_file_path, 'r')

    @requests_mock.mock()
    def test_download(self, m):
        m.get(self.file_content_mock)
        self.assertEqual(self.images._download(self.file_content_mock), '271947.jpg')
