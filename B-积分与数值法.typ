#import "@local/qooklet:0.1.0": *
#show: qooklet.with(
  title: "附录B：积分与数值法",
  author: "Yāng Xīnbīn",
  footer-cap: "Yāng Xīnbīn",
  header-cap: "动力系统入门",
  lang: "zh",
)

= 符号积分
<符号积分>

== 常规积分
<常规积分>

$ ∫_a^b f(x) dd(x) = F(b) - F(a) $

其中，$f(x) = dv(F, x)$

== 曲线积分
<曲线积分>

- 弧长积分（$f$为标量）

$ I_l = ∫_l f(x, y, z) dd(s) $

若

$ x = x(t), y = y(t), z = z(t) $

其中，弧长$s = sqrt(x_t^(′2) + y_t^(′2) + z_t^(′2)) dd(t)$

则

$
  I = ∫_(t_m)^(t_M) f [x(t), y(t), z(t)] sqrt(x_t^(′2) + y_t^(′2) + z_t^(′2)) dd(t)
$

- 坐标积分（$f$为向量）

$ I_l = ∫_l 𝒇 (x, y, z) d 𝐬 $

若

$ f(x, y, z) = [P (x, y, z), Q (x, y, z), R (x, y, z)] $

其中，$d 𝐬 = |dv(x, t), dv(y, t), dv(z, t)|^(⊤) dd(t)$，则

$
  I = ∫_a^b [P (x, y, z), Q (x, y, z), R (x, y, z)] |dv(x, t), dv(y, t), dv(z, t)|^(⊤) dd(t)
$

== 曲面积分
<曲面积分>

- 标量面积

$
  I = ∬_S ϕ (x, y, z) d S = ∬ σ_(x y) ϕ [x, y, f(x, y)] sqrt(1 + f_x^2 + f_y^2) dd(x, y)
$

其中，$σ_(x y)$为积分区域

对极坐标

$ x = x(u, v), y = y(u, t), z = z(u, v) $

$ I = ∬ ∑ ϕ [x(u, v), y(u, v), z(u, v)] sqrt(E G - F^2) dd(u, v) $

其中，$E = x_u^2 + y_u^2 + z_u^2$，$G = x_v^2 + y_v^2 + z_v^2$，$F = x_u x_v + y_u y_v + z_u z_v$

- 向量面积

#pagebreak()

= 多重积分
<多重积分>

对矩形区域 $[a, b] × [c, d]$，

$ ∫_a^b ∫_c^d f(x, y) dd(y, x) $

拆分

$∫_a^b ∫_c^d f(x, y) dd(y, x) = ∫_a^b g(x) dd(x), g(x) = ∫_c^d f(x, y) dd(y)$

由中点法可得

$
  g(x) = ∫_c^d f(x, y) dd(y)≈ h_y ∑_(j = 0)^(n_y - 1) f(x, y_j), y_j = c + 1 / 2 h_y + j h_y
$

以及

$
  ∫_a^b g(x) dd(x) ≈ h_x ∑_(i = 0)^(n_x - 1) g(x_i), x_i = a + 1 / 2 h_x + i h_x
$

最终

$
  ∫_a^b ∫_c^d f(x, y) dd(y, x) & ≈ h_x ∑_(i = 0)^(n_x - 1) h_y ∑_(j = 0)^(n_y - 1) f(x_i, y_j)\
  &= h_x h_y ∑_(i = 0)^(n_x - 1) ∑_(j = 0)^(n_y - 1) f(a + h_x / 2 + i h_x, c + h_y / 2 + j h_y)
$

其中，$(x_i, y_j)$为中点

= 数值微分
<数值微分>

== 差商公式
<差商公式>

- 向前差商公式

$ y_i^′ ≈ frac(Δ y_i, Δ t) = frac(y_(i + 1) - y_i, Δ t) $

- 向后差商公式

$ y_i^′ ≈ frac(Δ y_i, Δ t) = frac(y_i - y_(i -1), Δ t) $

- 算法精度：$𝜊(Δ t)$

== 中心公式
<中心公式>

=== 第一种
<第一种>

- 公式

$ y_i^′ ≈ frac(Δ y_i, Δ t) = frac(y_(i + 1) - y_(i -1), 2 Δ t) $

- Taylor 级数展开式

$ tilde(f)(x) = f^′(x) + frac(Δ t^2, 3!) f^″(ξ) $

- 算法精度：$𝜊(Δ t^2)$

=== 第二种
<第二种>

- 公式

$ y_i^′ ≈ frac(Δ y_i, Δ t) = frac(y_(i + 1) - y_(i -1), 2 Δ t) $

- 算法精度：$𝜊(Δ t^4)$

= 数值积分
<数值积分>

== 梯形法
<梯形法>

令

$ x_i = a + i h, i = 0, 1, …, n $

其中，$h = frac(b - a, n)$

可得

$
  ∫_a^b f(x) dd(x) = & ∫_(x_0)^(x_1) f(x) dd(x) + ∫_(x_1)^(x_2) f(x) dd(x) + … + ∫_(x_(n -1))^(x_n) f(x) dd(x)\
  ≈ & h frac(f(x_0) + f(x_1), 2) + h frac(f(x_1) + f(x_2), 2) + … + h frac(f(x_(n -1)) + f(x_n), 2)
$

即

$ ∫_a^b f(x) dd(x) ≈ h [1 / 2 f(x_0) + ∑_(i=1)^(n -1) f(x_i) + 1 / 2 f(x_n)] $

== 中点法
<中点法>

$
  ∫_a^b f(x) dd(x) &= ∫_(x_0)^(x_1) f(x) dd(x) + ∫_(x_1)^(x_2) f(x) dd(x) + … + ∫_(x_(n -1))^(x_n) f(x) dd(x)\
  & ≈ h f(frac(x_0 + x_1, 2)) + h f(frac(x_1 + x_2, 2)) + … + h t(frac(x_(n -1) + x_n, 2))\
  & ≈ h(t(frac(x_0 + x_1, 2)) + f(frac(x_1 + x_2, 2)) + … + f(frac(x_(n -1) + x_n, 2)))
$

即

$ ∫_a^b f(x) dd(x) ≈ h ∑_(i = 0)^(n -1) f(x_i) $

其中，

$ x_i = (a + h / 2) + i h $

#pagebreak()

== Monte Carlo 法
<Monte-Carlo-法>

对于不规则区域$Ω$，可选用 Monte Carlo 法

$ ∫_Ω f(x, y) dd(x, x) $

其中，

$ Ω = {(x, y)|g(x, y) ≥ 0} $

令$A(Ω)$为$Ω$的面积，则其可由以下步骤估计

+ 将几何图形$Ω$嵌入矩形区域$R$
+ 在$R$中绘制大量随机点$(x, y)$
+ 计算在$Ω$内部点的占比$q$
+ 通过$q$近似$A(Ω)/A(R)$，即设$A(Ω) = q A(R)$
+ 在$A(Ω)$内部点评估$f$的均值$bar(f)$
+ 将积分估计为$A(Ω)bar(f)$

= 数值差分
<数值差分>

== 有限差分
<有限差分>

+ 在时间上引入$N_t + 1$个点$t_0, t_1, …, t_N$的网格。在网格点$t_n$处寻找未知$u$，并引入$u^n$作为$u(t_n)$的数值近似值。
+ 设微分方程在网格点处有效。
+ 通过有限差分近似导数。
+ 基于先前计算的值$u_i(i < n)$

$ u^(n+1) = u^n + Δ t f(u^n, t_n), u^0 = U_0, n = 0, 1, …, N_t -1 $

== 前向 Euler 法
<前向-Euler-法>

$ u^(n+1) = u^n + Δ t f(u^n, t_n), n = 0, …, N_t -1 $
