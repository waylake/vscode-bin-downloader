#!/bin/sh

# This script downloads the latest VSCode binary from the official website

# download the vscode binary file from commit hash
commit_hash=$1
if [ -z "$commit_hash" ]; then
    echo "Please provide the commit hash"
    exit 1
fi

# download the vscode binary file from commit hash
#https://update.code.visualstudio.com/commit:
#/server-linux-x64/stable
wget -O vscode.tar.gz https://update.code.visualstudio.com/commit:$commit_hash/server-linux-x64/stable

# extract the vscode binary file
tar -xvf vscode.tar.gz

# remove the vscode binary file
rm vscode.tar.gz

# rename the vscode binary file
mv vscode-linux-x64 $commit_hash

# move to $HOME/.vscode-server/bin/$commit_hash
mkdir -p $HOME/.vscode-server/bin/$commit_hash
mv $commit_hash $HOME/.vscode-server/bin/$commit_hash