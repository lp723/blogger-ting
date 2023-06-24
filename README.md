Usage:


generate certs:
```
openssl req -new -x509 -nodes -out cert.pem -keyout key.pem
```

AND THEEEEN:

```
python manage.py runsslserver --cert ./certs/cert.pem --key ./certs/key.pe
```

or

```
python manage.py runsslserver 0.0.0.0:8000 --cert ./certs/cert.pem --key ./certs/key.pem
```