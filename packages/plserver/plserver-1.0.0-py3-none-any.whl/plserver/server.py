# examples/server_simple.py
from .file_handler import *
from .websocket_handler import path
from aiohttp import web
from datetime import datetime
import signal
import sys
import webbrowser


response_header = {"Cache-Control":"no-cache, no-store, must-revalidate", "Pragma":"no-cache", "Expires":"0"}
# Http Handler.
async def handle(request):
    # Http Request path.
    name = request.match_info.get('name', "Anonymous")
    # Check if the path is a file.
    time = str(datetime.now())[:-7]
    method = request.method
    text = '[{time}] --- {method} --- {path}'.format(time=time, method=method, path=name)
    if "." in name:
        content, code, file_type = path(name)
        file_type = file_type[0]
        text += '" {}'.format(code)
        print(text)
        return web.Response(text=content, status=code, content_type=file_type, headers=response_header)
    else:
        return web.Response(text = '<html>', content_type="text/html", status=code)

# Websocket Handler
async def wshandle(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    name = request.match_info.get('name', "Anonymous")
    source = "/" + name
    print(source)
    files = file_extractor(source)
    iis = initial_sizes1(files)

    # Listen to each message sent
    async for msg in ws:
        if source_file_Handler(iis, files) == 1:
            data = "reload"
        else:
            data = "keep"
        if msg.type == web.WSMsgType.text:
            await ws.send_str("{}".format(data))
        elif msg.type == web.WSMsgType.binary:
            await ws.send_bytes(msg.data)
        elif msg.type == web.WSMsgType.close:
            break

    return ws


def signal_handler(sig, frame):
    print("======== Stoping Current Live Server ========")
    sys.exit(1)

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}/ws', wshandle),
                web.get('/{name}', handle)])

def Serve(*port):
    if port:
        port = port[0]
        pass
    else:
        port = 2000
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:/Program Files/Google/Chrome/Application/chrome.exe"))
    webbrowser.get('chrome').open("http://localhost:" + str(port) + "/index.html") 
    signal.signal(signal.SIGINT, signal_handler)
    web.run_app(app, port=port, )
    

