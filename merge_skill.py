#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""重建 SKILL.md：核心部分保留，附录由 知识库/*.md 自动生成。
用法: python3 merge_skill.py（在仓库根目录运行）"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
core = (HERE / "SKILL.md").read_text(encoding="utf-8")
import re
core = re.split(r"^#{1,2} 附：依力老师知识库（全文，随本skill挂载）", core, flags=re.M)[0].rstrip() + "\n"

parts = ["\n---\n\n## 附：依力老师知识库（全文，随本skill挂载）\n\n> 以下知识库原文随本skill挂载。讲授相关话题时直接使用其中的真实观点与方法论。\n"]
for f in sorted((HERE / "知识库").glob("*.md")):
    parts.append(f.read_text(encoding="utf-8"))
    parts.append("\n")
combined = core + "\n" + "\n".join(parts)
(HERE / "SKILL.md").write_text(combined, encoding="utf-8")
print(f"SKILL.md 重建完成：{len(combined)} 字符")
