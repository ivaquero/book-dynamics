#import "@preview/qooklet:0.7.2": *
#import "@preview/touying-quick:0.5.0": *
#import "@preview/physica:0.9.8": *
#import "@preview/rexllent:0.4.1": xlsx-parser
#import "@preview/subpar:0.2.2": grid as sgrid
#import "@preview/typed-smiles:0.13.0": ce

#let info = toml("info.toml").global
#let slide = toml("info.toml").slide

// —— 章末参考文献 ——
// 全书的文献库仍是 dynam.bib 一个文件，但每章章末只排本章真正引用过的条目。
// 做法：从该章源文件里提取 @key（与 bib 键取交集，故 @标签、@preview 之类不会误收），
// 再把这些键对应的原始条目拼成一段临时书目交给 bibliography。
// 这样新增引用无需另行登记，也不会把全书文献堆在某一章后面。
// 注意：Typst 的文献编号是全书连续计数（[1]…[n]），不按章重排。

#let bib-entries = {
  let d = (:)
  for chunk in str(read("dynam.bib", encoding: none)).split(regex("(?m)^@")) {
    if chunk.trim() == "" { continue }
    let entry = "@" + chunk
    let m = entry.match(regex("^@[a-zA-Z]+\\{([^,]+),"))
    if m != none { d.insert(m.captures.at(0), entry.trim()) }
  }
  d
}

#let chapterbib(src) = {
  let keys = ()
  // 路径解析以本文件（lib/）为基准，故前置 ../ 回到仓库根。
  for m in str(read("../" + src, encoding: none)).matches(regex("@[A-Za-z][A-Za-z0-9_:-]*")) {
    let k = m.text.slice(1)
    if k in bib-entries and not keys.contains(k) { keys.push(k) }
  }
  if keys.len() == 0 { return }
  bibliography(
    bytes(keys.map(k => bib-entries.at(k)).join("\n\n")),
    style: "future-science",
  )
}

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

// —— 章内独立编号：例 / 定理 / 定义 / 推论 ——
// 章号由 dynamics.typ 的 chapter 包装写入 counter-chapter-local，各计数器每章重置。
// 定理与推论共用一套编号（LaTeX 惯例），定义另立一套。

#let counter-chapter-local = counter("chapter-local")
#let counter-example = counter("example-local")
#let counter-theorem-local = counter("theorem-local")
#let counter-definition-local = counter("definition-local")

// 章内编号的公共渲染：粗体标签 + 编号 + 正文。块内统一顶格，避免与正文缩进规则冲突。
#let numbered-block(label, counter, title: none, body) = {
  counter.step()
  block(
    above: 1.1em,
    below: 1.1em,
    width: 100%,
    {
      set par(first-line-indent: 0em)
      context {
        let c = counter-chapter-local.get().first()
        let n = counter.get().first()
        let head = if title == none {
          text(weight: "bold")[#label #c.#n.]
        } else {
          text(weight: "bold")[#label #c.#n（#title）.]
        }
        [#head #body]
      }
    },
  )
}

// 兼容两种调用形式：#theorem[正文] 与 #theorem(ctext("名称"))[正文]。
#let numbered-env(label, counter, args) = {
  let pos = args.pos()
  let title = args.named().at("title", default: none)
  if title == none and pos.len() >= 2 { title = pos.at(0) }
  numbered-block(label, counter, pos.last(), title: title)
}

#let example(..args) = numbered-env("例", counter-example, args)

#let theorem(..args) = numbered-env("定理", counter-theorem-local, args)

#let corollary(..args) = numbered-env("推论", counter-theorem-local, args)

#let definition(..args) = numbered-env("定义", counter-definition-local, args)

