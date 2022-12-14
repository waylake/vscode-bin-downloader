import wget
import os
from pathlib import Path

BASE_URL = "https://update.code.visualstudio.com/commit:"
LAST_URL = "/server-linux-x64/stable"

commit_id = '64bbfbf67ada9953918d72e1df2f4d8e537d340e'

dirs = [".vscode-server", '.vscode-server/bin']
# home_dir = str(Path.home())
home_dir = os.getcwd()

for dir_ in dirs:
    if not os.path.exists(home_dir + "/" + dir_):
        os.mkdir(home_dir + "/" + dir_)


def rename_folder(old, new):
    os.rename(old, new)


def un_tar(file):
    os.system(f"tar -xzf {file} -C {home_dir}/.vscode-server/bin/{commit_id}")


def download_vscode_bin(id_):
    url = BASE_URL + id_ + LAST_URL
    wget.download(url, out=home_dir + "/.vscode-server/bin/" + id_ + ".tar.gz")



if __name__ == "__main__":
    download_vscode_bin(commit_id)
    un_tar(home_dir + f'/.vscode-server/bin/vscode-server-{commit_id}.tar.gz')