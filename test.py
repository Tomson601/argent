data =  b'POST /weather HTTP/1.1\r\nContent-Type: application/json\r\nUser-Agent: PostmanRuntime/7.29.2\r\nAccept: */*\r\nPostman-Token: 936a07f8-0729-47ca-b394-6c29669ce03f\r\nHost: 192.168.1.77:90\r\nAccept-Encoding: gzip, deflate, br\r\nConnection: keep-alive\r\nContent-Length: 52\r\n\r\n{\n    "temperature": 36.6,\n    "humidtitidi": 45.0\n}' 


import json

def __extract_payload(request):
    request_lines = request.split(b'\r\n')
    payload_start_index = request_lines.index(b'') + 1
    payload = b'\r\n'.join(request_lines[payload_start_index:])
    return json.loads(payload.decode('utf-8'))

payload=__extract_payload(data)

print(payload)