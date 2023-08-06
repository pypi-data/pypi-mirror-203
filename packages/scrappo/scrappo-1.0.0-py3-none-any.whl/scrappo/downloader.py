import time
import requests

from scrappo.utils.log import show


class Downloader:
    def __init__(self, url, path):
        self.url = url
        self.path = path

    def download_video(self):
        start = time.time()
        try:
            r = requests.get(self.url, stream=True)
            with open(self.path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024 * 1024):
                    f.write(chunk)
        except (requests.exceptions.RequestException, OSError, IOError):
            show('Something wrong happened while opening/downloading the following URL:\n\t' + self.url + '(SKIPPED)')
            return False

        end = time.time()
        show("Timelapse: " + str(((end - start) * 10 ** 3) / 1000 / 60) + " minutes")
        show(self.path + ' successfully downloaded!')

        return True
