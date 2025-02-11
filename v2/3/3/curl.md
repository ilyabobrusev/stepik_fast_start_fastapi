```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/add_user' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "qwe",
  "user_info": "qweqwe"
}'

curl -X 'GET' \
  'http://127.0.0.1:8000/users' \
  -H 'accept: application/json' | jq
```
