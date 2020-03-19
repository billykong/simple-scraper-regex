FROM python:3

ADD scraper.py /
ADD requirements.txt /

RUN pip install -r requirements.txt

CMD ["sh", "-c", "python scraper.py $SCRAPE_URL $REGEX $OUTPUT_FILE"]