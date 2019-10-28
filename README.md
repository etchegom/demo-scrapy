# Demo cool [scrapy](https://scrapy.org/) features

- Random user-agent middleware
- Persistence pipeline with PostgreSQL and [SQLAlchemy](https://www.sqlalchemy.org/)
- Check exists in database middleware
- Custom log formatter
- Blacklist middleware
- Extract page metadata with extruct


## Setup locally

- Setup postgres database

```
docker-compose up -d --build
```

- Setup python environment

```
virtualenv -p /usr/bin/python3.7 .venv
source .venv/bin/activate
pip install -r requirements.txt
```

- Run the spider

```
scrapy crawl thomann
```

- Check your items in database using `psql cli` of pgadmin

## Next steps

- Complete scraping in thomaannn spider
- Add [Metabase](https://metabase.com) to the docker stack
- Add a [Scrapyd](https://scrapyd.readthedocs.io/en/stable/) server to the docker stack 