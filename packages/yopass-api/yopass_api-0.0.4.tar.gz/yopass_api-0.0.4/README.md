# yopass_api

This is a module to work with a (the) [Yopass](https://github.com/jhaals/yopass) backend created by [Johan Haals](https://github.com/jhaals).
This module will allow you to use Python and Yopass in automation projects.

## Installing

```py
pip install yopass_api
```

## Basic Example

This is a basic example of store secret, get link and fetch secret:

```py
from yopass_api import Yopass

yopass = Yopass(api="http://your.yopass.backend:1024")
secret_password = yopass.generate_passphrase(length=5)
secret_id = yopass.store(
    message="test",
    password=secret_password,
    expiration="1w",
    one_time=False,
)
secret_url = yopass.secret_url(secret_id=secret_id, password=secret_password)
print(secret_url)
message = yopass.fetch(secret_id=secret_id, password=secret_password)
print(message)

```
