FROM python:3-slim-bullseye

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install --yes --no-install-recommends \
    wkhtmltopdf=0.12.6-1
RUN pip install grip bs4

RUN mkdir -p /data
WORKDIR /data

COPY ./mdtohtml.py /mdtohtml.py
COPY ./mdtopdf.sh /mdtopdf.sh
RUN chmod +x /mdtopdf.sh

ENTRYPOINT ["/mdtopdf.sh"]