#import "lib/lib.typ": *
#show: chapter-style.with(
  title: "极限环数",
  info: info,
)

= 极限环的相对配置
<极限环的相对配置>

Poincaré 在 19 世纪 80 年代开始研究平面多项式向量场的孤立周期性循环。但，确定平面内极限环的最大数量和相对配置的一般问题在一个多世纪以来仍然没有解决。1900 年，希尔伯特（David Hilbert）向巴黎的国际数学家大会提交了一份 23 个问题的清单。大部分的问题已经被解决了，或完全解决，或部分解决。但，第十六个问题的第二部分仍未解决。

== Hilbert 数
<Hilbert-数>

考虑二维自治系统

$
  dot(x) = P (x, y)\
  dot(y) = Q (x, y)
$

其中，$P$和$Q$是$x$和$y$的多项式，问题是估计系统的极限环的最大数目和相对位置。当$P$和$Q$为$n$次时，系统可能具有的最大极限循数，Hilbert 数$H_n$由以下公式给出

$ H_n = "sup" {π(P, Q) : ∂P, ∂Q ≤ n} $

其中，$∂$表示次（degree），$π(P, Q)$为系统的极限环数。

#theorem(title: "Dulac 定理")[
  一个给定的多项式系统不可能有无限多的极限环。
]

#tip[
  不幸的是，这并不意味着 Hilbert 数是有限的。
]

在一般多项式系统的情况下，即使考虑局部分岔，结果也比较少。

- 1962 年，Bautin @bautinNumberLimitCycles1952 证明，对于二次系统来说，从一个临界点分岔的 SALC 不会超过 3 个。
- 1965 年，Sibirskii @sibirskiiNumberLimitCycles1965 证明，对于齐次三次系统（无二次项），从一个临界点分岔出的 SALC 不超过 5 个。
- 1980 年，史松龄 @shiConcreteExampleExistence1980 已经得到，对于二次系统，Hilbert 数$H_2 ≥ 4$。
- 1995 年，Christopher 和 Lloyd 证明，$H_n$的增长速度至少与$n^2 log n$一样快。
- 2009 年，李承治等 @liCubicSystemThirteen2009 证明了$H_3 ≥ 13$。

== Poincaré 压实
<Poincaré-压实>

压实法（compactification）是由 Poincaré 在 19 世纪末提出的。通过简单的变换，可将相平面映射到球体上。请注意，该平面可映射到上半球和下半球。这样一来，无穷大处的点就转化为球面赤道上的点。

设：将平面上的一点$(x, y)$映射到球体上半球的一点$(X, Y, Z)$上，如$S^2 = (X, Y, Z) ∈ ℝ^3 ： X^2 + Y^2 + Z^2 = 1$。用$(x, y)$定义$(X, Y, Z)$的方程由下列公式给出

$
  cases(
    delim: "{",
    X = x / sqrt(1 + r^2),
    Y = y / sqrt(1 + r^2),
    Z = 1 / sqrt(1 + r^2)
  )
$

其中，$r^2 = x^2 + y^2$。

#figure(
  image("images/ch08/compactification.png", width: 40%),
  caption: "压实法",
)

变换为极坐标。故，系统转化为

$
  dot(r) &= sum_(i = 0)^n r^i f_(i + 1)(θ)\
  dot(θ) &= sum_(i = 0)^(n-1) r^(i - 1) g_(i + 1)(θ)
$

其中，$f_m$和$g_m$是$cos θ$和$sin θ$的$m$次多项式。

设$ρ = 1 / r$。故，$dot(ρ) = -dot(r) / r^2$，系统转化为

$
  dot(ρ) &= -ρ f_(n+1)(θ) + O (ρ^2)\
  dot(θ) &= g_(n+1)(θ) + O (ρ)
$

#theorem[
  在$ρ = 0$上求解方程$dot(ρ) = dot(θ) = 0$，就可找到无穷大处的临界点，这相当于求解

  $ g_(n+1)(θ) = cos θ Q_n (cos θ, sin θ) - sin θ P_n (cos θ, sin θ) = 0 $

  其中，$P_n$和$Q_n$是$n$次齐次多项式，注意解是由$(θ_i, θ_i + π)$给出的，只要$g_(n+1)(θ) ≠ 0$，就有$n+1$对根，当$g_(n+1)(θ) < 0$时，流向为顺时针，当$g_(n+1)(θ) > 0$时，流向为逆时针。
]

为了确定在无穷大的临界点附近的流动，必须将$X > 0$的半球投射到$X = 1$的平面上，轴线为$y$和$z$，或将$Y > 0$的半球投射到$Y = 1$的平面上，轴线为$x$和$z$。

- 若$n$为奇数，$S^2$上的反点（antinodal point）定性相等。
- 若$n$为偶数，则反点定性相等，但流动方向相反。

#theorem[
  在$y z$平面（$X = ± 1$）上定义的流，除了点$(0, ± 1, 0)$外，与以下定义的流具有质的等价性

  $
    ± dot(y) &= y z^n P (1 / z, y / z) - z^n Q (1 / z, y / z)\
    ± dot(z) &= z^(n+1) P (1 / z, y / z)
  $

  其中，流动方向由$g_(n+1)(θ)$决定。
]

= Liénard 系统
<Liénard-系统>

== Lyapunov 量
<Lyapunov-量>

对 Liénard 方程

$
  dot(x) &= y - F(x)\
  dot(y) &= -g(x)
$

其中，$F(x) = sum_(i=1)^u a_i x^i, g(x) = x + sum_(i = 2)^v b_i x^i$。

系统的前三个 Lyapunov 量为

- $L(0) = -a_1$
- $L(1) = 2 a_2 b_2 - 3 a_3$
- $L(2) = 6 a_2 b_4 - 10 a_2 b_2 b_3 + 20 a_4 b_2 - 15 a_5$

系统等价于

$ dot.double(x) + f(x) dot(x) + g(x) = 0 $
为了使原点的临界点是一个非退化的焦点或中心，需要施加条件$g(0) = 0, g^′(0) > 0$。系统的周期解对应于极限环。

令$∂$表示多项式的度数，令$hat(H)(i, j)$表示全局极限环的最大次数，其中，$i$为$f$的次数，$j$为$g$的次数，系统和主要全局结果如下：

- 1928 年，Liénard 证明，当$∂g = 1$，$f$是连续奇函数，在$x = a$处有唯一根，且$x ≥ a$时单调递增，则有唯一的极限环。
- 1976 年，Cherkas @cherkasConditionsLienardEquation1976 给出了 Liénard 方程有中心的条件。
- 1977 年，Lins，de Melo 和 Pugh @linsLienardEquation2006 证明了$hat(H)(2, 1) = 1$
- 1988 年，Coppel @coppelQuadraticSystemsMost1989 证明了$hat(H)(1, 2) = 1$。
- 1996 年，Dumortier 等 @dumortierMoreLimitCycles2007 证明了$hat(H)(1, 3) = 1$。
- 1997 年，Dumortier 和李承治 @dumortierQuadraticLienardEquations1997 证明了$hat(H)(2, 2) = 1$。
- 2005 年，Jiang，韩茂安等 @jiangLimitCyclesTwo2007 证明了当$f$和$g$是奇数多项式时，$hat(H)(5, 3) = 2$。
- 2017 年，Sun 和黄文韬 @sunBoundingNumberLimit2017 利用多项式代数中的 Chebyshev 准则和正则链理论的工具，证明了类型为$hat(H)(4, 3) = 6$。

== 全局性质
<全局性质>

对系统，定义$X = (P, Q)$为向量场。设一个极限环，$Γ(t) = (x(t), y(t))$，周期为$T$。

#theorem[
  设特征指数（characteristic exponent）
  $ ∫_Γ div(X) dd(t) = ∫_0^⊤(pdv(P, x) + pdv(Q, y)(x(t), y(t))) dd(t) $

  - 若$∫_Γ div(X) dd(t) < 0$，则$Γ$为双曲吸引。
  - 若$∫_Γ div(X) dd(t) > 0$，则$Γ$为双曲排斥。
]

#theorem[
  对 Liénard 方程
  $
    dot(x) &= y - (a_1 x + a_2 x^2 + a_3 x^3)\
    dot(y) &= -x
  $

  若$a_1 a_3 < 0$，则存在一个唯一的双曲极限环。
]

== 大参数 Liénard 系统
<大参数-Liénard-系统>

考虑到参数化的立方 Liénard 方程

$ dot.double(x) + μ f(x) dot(x) + g(x) = 0 $

其中$f(x) = -1 + 3 x^2, g(x) = x$，即为

$
  dot(x) &= μ y - μ F(x)\
  μ dot(y) &= -g(x)
$

其中，$F(x) = ∫_0^x f(s) d s = -x + x^3$，在 Liénard 平面内。Liénard 证明了系统有一个唯一的极限环。包含小参数的系统用 Melnikov 积分进行了考虑。

#figure(
  image("images/ch08/lienard-big-pm.png", width: 50%),
  caption: "Liénard 系统",
)

则，当$μ$很大时，会发生什么？设$μ = 1 / ɛ$，则系统可写成一个等价系统，其形式为

$
  ɛ dot(x) &= y - F(x)\
  dot(y) &= -ɛ g(x)
$

#theorem[
  考虑系统和 Jordan 曲线$J$。当$μ → ∞$，或，$ɛ → 0$时，极限环趋向于分段分析$J$。
]

== 局部性质
<局部性质>

虽然 Liénard 方程看起来很简单，但已知的关于最大极限环数的全局结果却很少。相反，若分析仅限于局部分岔，则可得到更多的结果。考虑 Liénard 系统

$
  dot(x) &= y\
  dot(y) &= -g(x) - f(x) y
$

其中，$f(x) = sum_(i = 0)^m a_i x^i, g(x) = x + sum_(j = 2)^n b_j x^j$；$m$和$n$是自然数。令$hat(H)(m, n)$表示系统可从原点分岔的 SALC 的最大数目，其中，$m$为$f$的次，$n$为$g$的次。

1984 年，Blows 和 Lloyd @blowsNumberSmallAmplitudeLimit1984 证明了系统的以下结果。

- 若$∂f = m = 2 i|2 i + 1$，则$hat(H)(m, 1) = i$。
- 若$g$为奇数，$∂f = m = 2 i|2 i + 1$，则$hat(H)(m, n) = i$。

在此基础上，Lynch 证明

- 若$∂g = n = 2 j|2 j + 1$，则$hat(H)(1, n) = j$。
- 若$f$为偶数，$∂f = 2 i$，则$hat(H)(2 i, n) = i$。
- 若$f$为奇数，$∂f = 2 i + 1$，且
  $∂g = n = 2 j + 2|2 j + 3$；则$hat(H)(2 i + 1, n) = i + j$。
- 若$∂f = 2$，$g(x) = x + g_e(x)$，其中，$g_e$为偶数，$∂g = 2 j$；则$hat(H)(2, 2 j) = j$

Christopher 和 Lynch @christopherSmallAmplitudeLimitCycle1999 最近又提出了一种新的代数方法来确定 Lyapunov 量，这就可进一步计算。令$.$表示整数部分。新的结果列举如下

- $hat(H)(2, n) = [frac(2 n+1, 3)]$
- $hat(H)(m, 2) = [frac(2 m + 1, 3)]$
- $hat(H)(3, n) = 2 [frac(3 n + 6, 8)], ∀1 < n ≤ 50$
- $hat(H)(m, 3) = 2 [frac(3 m + 6, 8)], ∀1 < m ≤ 50$

#figure(
  image("images/ch08/table-lynch.png", width: 80%),
  caption: "table lynch",
)

Christopher 和 Lloyd @christopherSmallAmplitudeLimitCycles1996 已经证明了上表是对称的，但只是在$f(x)$中的线性系数非零的情况下，最终目的是建立$hat(H)(m, n)$作为$f$和$g$的次数函数的一般公式。2013 年，韩茂安和 Romanovski @hanNumberLimitCycles2013 使用新的方法给出了更多的结果。

#tip[
  需要注意的是，数学包编程必须谨慎使用。例如，可能在计算机屏幕上无法区分从细焦点分岔出来的两个极限环。
]

#bibliography("lib/dynam.bib", style: "future-science")
