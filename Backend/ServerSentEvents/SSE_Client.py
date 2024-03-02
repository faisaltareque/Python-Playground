from sseclient import SSEClient

messages = SSEClient('http://0.0.0.0:8000/events')

for msg in messages:
    if msg.event == 'close':
        break
    else:
        print(msg.data)

