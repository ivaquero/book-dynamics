#import "lib/lib.typ": *

#cover(info)
#contents(depth: 1, info: info)

#let chapter(filename) = {
  include filename
  counter(heading).update(0)
}

#chapter("01-平面系统.typ")
#chapter("02-种群与极限环.typ")
#chapter("03-哈密顿系统I.typ")
#chapter("04-分岔理论.typ")
#chapter("05-连续型混沌.typ")
#chapter("06-哈密顿系统II.typ")
#chapter("07-局部分岔.typ")
#chapter("08-极限环数.typ")
#chapter("09-延迟效应.typ")
#chapter("10-线性离散.typ")
#chapter("11-离散型混沌.typ")
#chapter("12-复数型混沌.typ")
#chapter("13-二元振荡器.typ")
#chapter("14-混沌控制.typ")
#chapter("15-非线性系统.typ")
#chapter("16-系统仿真.typ")
// #chapter("A-常微分方程.typ")
// #chapter("B-积分与数值法.typ")

// #bib(main: true)
