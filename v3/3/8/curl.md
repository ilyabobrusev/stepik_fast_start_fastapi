```bash
curl -s -X 'GET' \
  'http://127.0.0.1:8000/headers' \
  -H 'accept: application/json' \
  -H 'User-Agent: curl' \
  -H 'Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3' \
  | jq
```
