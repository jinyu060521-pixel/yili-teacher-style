#!/bin/bash
cd "$(dirname "$0")"
python3 rebuild.py
echo ""
echo "更新完成。index.html 已包含最新下载文件。"
read -n 1 -s -p "按任意键关闭..."
