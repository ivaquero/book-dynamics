#import "@local/qooklet:0.1.0": *
#show: qooklet.with(
  title: "混沌控制",
  author: "Yāng Xīnbīn",
  footer-cap: "Yāng Xīnbīn",
  header-cap: "动力系统入门",
  lang: "zh",
)

= 自我复制
<自我复制>

== Kleene 递归定理
<kleene-递归定理>

在可计算性理论中，Kleene 递归定理（Kleene’s recursion theorems）是关于可计算函数应用于自身描述的一对基本结果。该定理由 Stephen Cole Kleene（1909～1994）于 1938 年首次证明，并出现在他 1952 年出版的《元数学导论》（Introduction to Metamathematics）一书中。递归定理可应用于构造可计算函数上的某些运算的定点、生成奎因（quine），以及通过递归定义构造函数。

#theorem(title: "第一递归定理")[
  若$F$和$G$是自然数上的偏函数，记号$F ≃ G$表示，对于每个$n$，$F(n)$和$G(n)$都被定义且等价，否则$F(n)$和$G(n)$均是未定义的。
]

#theorem(title: "第二递归定理")[
  对于任何偏递归函数$Q (x, y)$，存在一个索引$p$，使得$ϕ_p ≃ λ y⋅Q (p, y)$。
]

== 奎因
<奎因>

奎因是一种计算机程序，它不需要任何输入，只产生一份自己的源码副本作为唯一的输出。这类程序在可计算性理论和计算机科学文献中的标准术语是”自复制程序”。

奎因是执行环境的一个固定点，当执行环境被看作是将程序转化为其输出的函数时，奎因就是执行环境的一个固定点。在任何图灵完整的程序设计语言中都可能出现奎因，这是 Kleene 递归定理的直接结果。

"奎因"（Quine）这个名字是 Douglas Richard Hofstadter（1945～）在他的科普书《Gödel, Escher, Bach: An Eternal Golden Braid》中提出的，以纪念哲学家 Willard Van Orman Quine（1908～2000），他对间接自指法进行了广泛的研究，特别是对以下的悖论产生的表达方式，被称为奎因悖论（Quine’s paradox）：

`"Yields falsehood when preceded by its quotation" yields falsehood when preceded by its quotation.`

#let quine = read("python/ch14_quine.py")
#raw(quine, lang: "python", block: true)
