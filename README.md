# Pika Assignment

## Features

+ Python
+ FastAPI
+ Postgres
+ celery
+ RabbitMQ
+ Pytest
+ Docker
+ Sentry for monitoring the app
+ Celery flower for monitoring the Celery tasks
+ Alembic for Database Migrations
+ pre-commit hooks

## 1. Clone the repository
```shell
git clone git@github.com:MbxrAteeq/pika-test.git
```

## Docker Setup
Create a `.env` file and set database url's
```shell
cp .env-sample .env
```
Build Docker Images
```shell
sudo docker-compose build
```
Start Docker Services
```shell
sudo docker-compose up -d
```
Run alembic migrations
```shell
sudo docker-compose run app alembic upgrade head
```

## Non Docker environment setup
### 2. Virtual environment
Create and activate virtual environment:
```shell
cd pika-assignment
python3 -m venv env
source env/bin/activate
```

### 3. Create a `.env` file
```shell
cp .env-sample .env
```
Note: set .env values according to your local configurations.

### 4. Database migration
Note: If you are running the app with PostgreSQL, you will probably need to
create the databases as well:
```shell
createdb --host=localhost -U postgres -O postgres -E utf8 -T template0 pika
createdb --host=localhost -U postgres -O postgres -E utf8 -T template0 pika_test
```

### 5. Install the required modules:
```shell
bash ./setup.sh
```

### 6. Start the Application

```shell
bash run.sh
```

### 7. Run celery worker
```shell
celery -A celery_service.celery worker --loglevel=info
```

### 8. Run celery flower
```shell
celery -A celery_service.celery flower
```

The server will start listens on port 8000 on address [http://127.0.1:8000](http://127.0.0.1:8000).
Find swagger docs at [http://127.0.1:8000/docs/swagger](http://127.0.0.1:8000/docs/swagger).
Find flower dashboard at [http://127.0.1:5555](http://127.0.0.1:5555).

### 9. Tests
To run test, run the following command
```shell
pytest -vv -s
```
