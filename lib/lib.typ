#import "@preview/qooklet:0.7.2": *
#import "@preview/touying-quick:0.5.0": *
#import "@preview/physica:0.9.8": *
#import "@preview/rexllent:0.4.1": xlsx-parser
#import "@preview/subpar:0.2.2": grid as sgrid
#import "@preview/typed-smiles:0.13.0": ce

#let info = toml("info.toml").global
#let slide = toml("info.toml").slide

#let bib = bibliography("dynam.bib", style: "future-science")

// —— 可复用辅助：图溯源、章末配套代码 ——

// 图/示例的“生成脚本”溯源注（放在 figure 之后）。
#let genby(path) = text(size: 0.75em, fill: gray)[生成脚本：#path]

// 章末“配套代码”清单：一条调用列出该章所有脚本（路径相对于仓库根目录）。
#let companion(..paths) = grid(
  columns: 1,
  rows: paths.len(),
  row-gutter: 3pt,
  inset: 0pt,
  ..paths.map(p => [#raw(p, block: false)]),
)
