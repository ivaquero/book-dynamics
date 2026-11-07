#import "lib/lib.typ": *

#cover(info)
#contents(depth: 1, info: info)

#include "00-前言.typ"

// 图的章内编号：章号 + 本章图序。
#let chapter-figure-numbering(n) = context {
  let c = counter-chapter-local.get().first()
  numbering(d => str(c) + "." + str(d), n)
}

#let chapter(filename) = {
  let m = filename.match(regex("^([0-9]+)"))
  if m != none { counter-chapter-local.update(int(m.text)) }
  // 各计数器每章归零，使编号形如 公式 (3.7)、图 3.2、定理 3.1。
  counter-example.update(0)
  counter-theorem-local.update(0)
  counter-definition-local.update(0)
  counter(math.equation).update(0)
  counter(figure.where(kind: image)).update(0)
  set figure(numbering: chapter-figure-numbering)
  include filename
  counter(heading).update(0)
}

#chapter("01-平面系统.typ")
#chapter("02-种群与极限环.typ")
#chapter("03-哈密顿系统I.typ")
#chapter("04-哈密顿系统II.typ")
#chapter("05-分岔理论.typ")
#chapter("06-局部分岔.typ")
#chapter("07-极限环数.typ")
#chapter("08-连续型混沌.typ")
#chapter("09-线性离散.typ")
#chapter("10-离散型混沌.typ")
#chapter("11-复数型混沌.typ")
#chapter("12-延迟效应.typ")
#chapter("13-二元振荡器.typ")
#chapter("14-混沌控制.typ")
#chapter("15-非线性系统.typ")
#chapter("16-系统仿真.typ")
#chapter("A-常微分方程.typ")
#chapter("B-微积分技术.typ")
#chapter("C-自指与可计算性.typ")
