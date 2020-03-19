# README
This is a very simple scraper that takes three parameters: 
1. `SCRAPE_URL`: the scraping target
2. `REGEX`: a python favor regular expression for matching the scraped content
3. `OUTPUT_FILE`: the filepath to which the result should be written  

## Setup
`pip3 install -r requirements.txt`

## Build 
`$ docker build -t simple-scraper-regex .`

## RUN
`$ docker run --env-file ./sample.env -v /Users/billykong/workspace/github.com/billykong/scraper-regex/results:/results simple-scraper-regex:latest`

With sample.env:
```
SCRAPE_URL=https://www.bing.com/covid/data
REGEX=\{[^\{]*hong[^\}]*\}
OUTPUT_FILE=/results/output-container.txt
```

You can also run it in a terminal:
`$ python scraper.py 'https://www.bing.com/covid/data' '\{[^\{]*hong[^\}]*\}' ./output.txt`

## TODO
- [ ] Add unit tests
- [ ] Setup GitHub Action to push Docker image to DockerHub upon push to master
