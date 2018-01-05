FROM spectreteam/python_mcr:r2016b

COPY download_redist.py download_redist.py

COPY extract_redist.py extract_redist.py

RUN python download_redist.py &&\
    python extract_redist.py &&\
    rm msi-redist.zip &&\
    chmod --recursive 777 /msi-redist &&\
    cd /msi-redist &&\
    python setup.py install &&\
    cd / &&\
    rm -r msi-redist &&\
    rm download_redist.py &&\
    rm extract_redist.py
