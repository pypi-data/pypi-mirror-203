# File Content Opener.
import os
import sys
from mimetypes import guess_type

# Current Working Directory.
cw_dir = os.getcwd()
# JavaScript Webscoket To be attached to html files.
def websocketJs() -> bytes:
    websocket_file = "\websocket.js"
    #Check for where our webscoket js file is stored
    package_path = os.path.dirname(__file__)
    script_src = package_path + websocket_file
    file = open(script_src, "rb")
    allscript = file.read(1000000)
    script = b'<script type="text/javascript">' + allscript + b'</script>'
    return script

def path(content):
    file_src = cw_dir + '/' + content
    file_type = guess_type(file_src)
    try:
        f = open(file_src, "rb")
    except FileNotFoundError:
        gf = b""
        code = 400
    else:
        gf = f.read(6000000)
        code = 200
    if "html" in content:
        gf = gf.replace(b"</body>", websocketJs() + b'</body>')
    else:
        pass
    if file_type == None:
        file_type= "text/plain"
    else:
        pass
    return gf.decode("utf-8"), code, file_type
