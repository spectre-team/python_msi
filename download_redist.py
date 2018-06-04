import urllib.request

# hack for python 3.4 ssl
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

remote_path = 'https://github.com/spectre-team/matlab-legacy/releases/download/legacy-v4.0.6/python-linux64.zip'
local_path = 'msi-redist.zip'

urllib.request.urlretrieve(remote_path, local_path)
