```bash
curl -s -X 'GET' \
  'http://127.0.0.1:8000/items/' \
  -H 'accept: application/json' \
  -H 'x-token: foo,bar' | jq
```
