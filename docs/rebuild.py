#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把4个下载文件内嵌进 index.template.html，生成可独立下载的单文件网站。
用法: python3 rebuild.py  (在官网目录下运行；更新下载文件后运行一次)"""
import base64
from pathlib import Path

HERE = Path(__file__).resolve().parent
MIME = {".skill": "application/zip", ".zip": "application/zip", ".txt": "text/plain"}
FILES = ["yili-style-full.skill", "yili-style-lite.skill", "yili-style-pack.zip", "yili-style-prompt.txt"]

html = (HERE / "index.template.html").read_text(encoding="utf-8")
for name in FILES:
    p = HERE / name
    if not p.exists():
        print(f"缺少 {name}，请先复制到官网目录再运行")
        raise SystemExit(1)
    data = base64.b64encode(p.read_bytes()).decode()
    uri = f"data:{MIME[p.suffix]};base64,{data}"
    html = html.replace(f'href="{name}"', f'href="{uri}"')
    print(f"已内嵌 {name} ({p.stat().st_size//1024}KB)")
(HERE / "index.html").write_text(html, encoding="utf-8")
print(f"完成，index.html 现在 {(HERE/'index.html').stat().st_size//1024}KB，可独立分发")
