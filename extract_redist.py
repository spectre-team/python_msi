import zipfile

with zipfile.ZipFile('msi-redist.zip') as mcr_installer:
    mcr_installer.extractall('/msi-redist')
