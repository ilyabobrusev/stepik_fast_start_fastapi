```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/items/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "qwe",
  "description": "qweqwe",
  "price": 0,
  "tax": 0
}'
```
