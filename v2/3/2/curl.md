```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/add_user?username=username&user_info=userinfo' \
  -H 'accept: application/json' \
  -d ''

# or

curl -X 'POST' \
  'http://127.0.0.1:8000/add_user?username=user%20name&user_info=user%20info' \
  -H 'accept: application/json' \
  -d ''
```

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/users' \
  -H 'accept: application/json' | jq
```