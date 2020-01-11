# Weser [weather]

Weser is just a small server which provides a OpenAPI specification (/docs) and some api endpoints to save data into a Postgres, SQLite or MySQL database.

## Requirements

- [pipenv](https://github.com/pypa/pipenv)

## Installation

```bash
pipenv install
```

## Usage

### Env Variables

DB_URL = Database URI # [See here](https://docs.sqlalchemy.org/en/13/core/engines.html#database-urls)

### Development

```bash
pipenv run dev
```

### Production

```bash
pipenv run prod
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
