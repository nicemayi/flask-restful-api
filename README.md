# flask-restful-api

## Notes:
1. `virtualenv virtualenv`

2. `pip install -r requirements.txt`

3. Setup local mysql for testing purpose (under /flask-restful-api dir, requirement mysql client installed):
```
docker run --name mysql -v <YOUR_DIR>/flask-restful-api/mysql_db:/var/lib/mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=<YOUR_ROOT_PASSWORD> -d mysql

mysql -u root --password=<YOUR_ROOT_PASSWORD> -h 127.0.0.1
```

4. Setup local redis for testing purpose (under /flask-restful-api dir, requirement redis client installed)
```
docker run --name redis -p 6379:6379 -v <YOUR_DIR>/flask-restful-api/redis_db:/data -d redis

redis-cli
```

## Questions:
1. Why not define app in entry?