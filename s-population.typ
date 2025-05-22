#import "lib/lib.typ": *
#show: touying-quick.with(
  title: "种群动力学",
  subtitle: "生物建模系列课程第1讲",
  author-size: 20pt,
  lang: "zh",
)

= 背景介绍

== 种群动力学的任务

#block(height: 15em, columns()[
  - 微生物工程需要解决的问题
    - 目标产物的规模生产
    - 目标产物的活性保持
  - 模型预测的挑战
    - 单一菌群的生化特性变化
    - 混合菌群的生态学关系复杂
  - 生物建模的常用技术
    - *种群动力学模型*
    - 生态网络模型

  #figure(image("slides/fermenter.png", width: 100%), caption: none)
])

= 马尔萨斯模型

== 模型提出

1798年，马尔萨斯（Thomas Malthus）在《人口论》中提出：人口按几何级数增长而生活资源只能按算术级数增长，所以不可避免地要导致饥饿、战争和疾病。

#block(height: 15em, columns(gutter: -2em)[
  #h(2em)令时刻$t$时的总种群为$X(t)$，平均生育率为$b$，平均死亡率为$d$，则有

  $ dv(X(t), t) = (b - d) X(t) $

  令净增长率$r = b - d$，则

  $ frac(X^′(t), X(t)) = r $

  积分得

  $ X(t) = X(0) e^(r t) $

  其中，$X(0)$为初始种群

  #figure(image("slides/malthus.png", width: 60%), caption: none)
])

== 模型缺陷

#block(height: 15em, columns()[
  - 马尔萨斯模型的限制因子
    - 净增长率$r$
  - 马尔萨斯模型的缺陷
    - 提出受到时代局限
    - 未考虑种间竞争的影响
  - 导致不切实际的悲观结论

  #figure(image("slides/malthusian.png", width: 80%), caption: none)
])

= 逻辑模型

== 模型提出

逻辑方程（Logistic equation）最初由比利时数学家 Pierre-François Verhulst（1804～1849）于 1838 年提出的，其描述的是，在其他条件相同的情况下，种群的繁殖率与现有种群和可用资源的数量成正比。

对单一种群，设其自然增长率为$r$，令其种内斗争系数为$m$，则有

$ dv(X(t), t) = r X(t) - m X(t)^2 $ <logistic>

分离变量，积分后得

$ X(t) = frac(r X(0), m X(0) + (r - m X(0)) exp(-r t)) $

不难看出

$ lim_(x → ∞) X(t) = r / m = K $

== 模型公式

#block(height: 15em, columns()[

  代入@logistic，则有

  $
    frac(1, X(t)) dv(X(t), t) = r(1 - frac(X(t), K))
  $

  即

  $ dv(X(t), t) = r X(t) (1 - frac(X(t), K)) $

  求解得

  $
    X(t) = (X(0) K e^(r t)) / (K + X(0)(e^(r t) - 1))
  $

  其中，$K$被称为最大环境承载量。

  其简化形式为
  $
    f = frac(K, 1 + A e^(B x))
  $

  #figure(image("slides/logistic.png", width: 80%), caption: none)
])

== 固定点

#block(
  height: 15em,
  columns()[
    通过求导，来判断曲线的变化趋势。在微分方程的语境下，这种点被称为固定点（或平衡点）。

    令导数为0

    $
      0 = r X(t) (1 - frac(X(t), K))
    $

    解得，方程有2个平衡点

    - $X = 0$（不稳定平衡点）
    - $X = K$（稳定平衡点）

    #figure(image("slides/logistic-fixed.png", width: 100%), caption: none),
    #figure(image("slides/fixed-stability.png", width: 90%), caption: none)
  ],
)

= 小结

== 公式

#block(height: 15em, columns()[
  - 马尔萨斯模型
    - 限制因子：$X_0$、$r$
    - 未考虑环境限制
  - 逻辑模型
    - 限制因子：$X_0$、$r$、$K$
    - 考虑了环境限制

  #figure(image("slides/logistic2.png", width: 120%), caption: none)
])

== 下节预告

#block(height: 19em, columns()[
  - Allée 效应
  - 编程实践

  #let code1 = read("python/ch02_eq_logistic.py")
  #code(code1)

  $
    X^′ = r X (1 - frac(X, K))(frac(X, a) - 1)
  $
  \
  #figure(image("slides/allee-fixed.png", width: 100%), caption: none)
])

