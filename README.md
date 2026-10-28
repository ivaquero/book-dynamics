# 动力系统笔记资料

本仓库文本主要翻译摘抄自 Springer 教材 [Dynamical Systems with Applications using Python](https://link.springer.com/book/10.1007/978-3-319-78145-7)，该书是入门系统动力学的经典教材。

笔记原采用 Markdown 格式，但因该格式输出的 PDF 不够稳定，且样式单一，后转向现代文本工具 [Typst](https://github.com/typst/typst)（相信大家会喜欢上 Typst 这个软件）。

现公开分享供对动力学感兴趣的朋友参考及共同讨论。

> 书中配套 Python 代码经过重新命名和整理，方便查阅。

## 配套代码

`python/` 下的脚本按章节命名（`chXX_*.py`），跨章共享的模型、积分器与绘图实现集中在 `python/dynamics/` 子包。

依赖：numpy、scipy、matplotlib、sympy（由 conda/micromamba 环境承载）。

从仓库根目录运行单个脚本：

```bash
python -m python.ch01_critical
```

