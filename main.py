import wget
import os

BASE_URL = "https://update.code.visualstudio.com/commit:"
LAST_URL = "/server-linux-x64/stable"


def download_vscode_bin(commit_id):
    dirs = [".vscode-server", '.vscode-server/bin', f".vscode-server/bin/{commit_id}"]

    for dir in dirs:
        if not os.path.exists(dir):
            os.mkdir(dir)

    url = BASE_URL + commit_id + LAST_URL
    path = f".vscode-server/{commit_id}/bin/"
    file_name = "vscode-server.tar.gz"
    wget.download(url=url, out=path + file_name)


download_vscode_bin("64bbfbf67ada9953918d72e1df2f4d8e537d340e")
