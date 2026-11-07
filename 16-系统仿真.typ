#import "lib/lib.typ": *
#show: chapter-style.with(title: "系统仿真", info: info)

本章讨论从连续模型走到可计算结果的完整链路：先给出描述物理空间的两种视角，再依次交代解析积分、多重积分、数值微分、数值积分与有限差分五组工具。

= 物理空间
<物理空间>

思想：现象 → PDE → 离散化 → 数值解

== Eulerian 途径
<Eulerian-途径>

要将空间维度纳入模型中，也有不同的途径。可从一个观察者的角度出发，他坐在空间的固定位置$𝒙$，并记录下他所看到的东西，例如每分钟经过的汽车数量。这就是 Eulerian 途径：从观察者的角度出发，在每个空间位置附加系统的属性。

Eulerian 途径中，空间可是连续的，也可是以单元为单位的离散化，形成覆盖感兴趣区域的网格。

== Lagrangian 途径
<Lagrangian-途径>

Lagrangian 途径从运动物体的角度出发。给出所有感兴趣的物体的位置，作为时间的函数。例如，月球的运动用其轨迹$𝒙(t)$来描述，其中，$𝒙$是一个连续的变量。在一个交通模型中，可给出所有车辆在时间上的位置。

#figure(
  image("images/ch16/approaches.png", width: 60%),
  caption: "approaches",
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

其中，弧长$s = sqrt(x_t^('2) + y_t^('2) + z_t^('2)) dd(t)$

则

$
  I = ∫_(t_m)^(t_M) f [x(t), y(t), z(t)] sqrt(x_t^('2) + y_t^('2) + z_t^('2)) dd(t)
$

- 坐标积分（$f$为向量）

$ I_l = ∫_l 𝒇 (x, y, z) d 𝐬 $

若

$ f(x, y, z) = [P (x, y, z), Q (x, y, z), R (x, y, z)] $

其中，$d 𝐬 = |dv(x, t), dv(y, t), dv(z, t)|^⊤ dd(t)$，则

$
  I = ∫_a^b [P (x, y, z), Q (x, y, z), R (x, y, z)] |dv(x, t), dv(y, t), dv(z, t)|^⊤ dd(t)
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

$ I = ∬ sum ϕ [x(u, v), y(u, v), z(u, v)] sqrt(E G - F^2) dd(u, v) $

其中，$E = x_u^2 + y_u^2 + z_u^2$，$G = x_v^2 + y_v^2 + z_v^2$，$F = x_u x_v + y_u y_v + z_u z_v$

- 向量面积

= 多重积分
<多重积分>

对矩形区域 $[a, b] × [c, d]$，

$ ∫_a^b ∫_c^d f(x, y) dd(y, x) $

拆分

$∫_a^b ∫_c^d f(x, y) dd(y, x) = ∫_a^b g(x) dd(x), g(x) = ∫_c^d f(x, y) dd(y)$

由中点法可得

$
  g(x) = ∫_c^d f(x, y) dd(y)≈ h_y sum_(j = 0)^(n_y - 1) f(x, y_j), y_j = c + 1 / 2 h_y + j h_y
$

以及

$
  ∫_a^b g(x) dd(x) ≈ h_x sum_(i = 0)^(n_x - 1) g(x_i), x_i = a + 1 / 2 h_x + i h_x
$

最终

$
  ∫_a^b ∫_c^d f(x, y) dd(y, x) & ≈ h_x sum_(i = 0)^(n_x - 1) h_y sum_(j = 0)^(n_y - 1) f(x_i, y_j)\
  &= h_x h_y sum_(i = 0)^(n_x - 1) sum_(j = 0)^(n_y - 1) f(a + h_x / 2 + i h_x, c + h_y / 2 + j h_y)
$

其中，$(x_i, y_j)$为中点

= 数值微分
<数值微分>

== 差商公式
<差商公式>

- 向前差商公式

$ y_i^' ≈ frac(Δ y_i, Δ t) = frac(y_(i + 1) - y_i, Δ t) $

- 向后差商公式

$ y_i^' ≈ frac(Δ y_i, Δ t) = frac(y_i - y_(i -1), Δ t) $

- 算法精度：$𝜊(Δ t)$

== 中心公式
<中心公式>

=== 第一种
<第一种>

- 公式

$ y_i^' ≈ frac(Δ y_i, Δ t) = frac(y_(i + 1) - y_(i -1), 2 Δ t) $

- Taylor 级数展开式

$ tilde(f)(x) = f^'(x) + frac(Δ t^2, 3!) f^''(ξ) $

- 算法精度：$𝜊(Δ t^2)$

=== 第二种
<第二种>

- 公式

$ y_i^' ≈ frac(Δ y_i, Δ t) = frac(y_(i + 1) - y_(i -1), 2 Δ t) $

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
  ∫_a^b f(x) dd(x) = & ∫_(x_0)^(x_1) f(x) dd(x) + ∫_(x_1)^(x_2) f(x) dd(x) + … + ∫_(x_(n -1))^(x_n) f(x) dd(x) \
                   ≈ & h frac(f(x_0) + f(x_1), 2) + h frac(f(x_1) + f(x_2), 2) + … + h frac(f(x_(n -1)) + f(x_n), 2)
$

即

$ ∫_a^b f(x) dd(x) ≈ h [1 / 2 f(x_0) + sum_(i=1)^(n -1) f(x_i) + 1 / 2 f(x_n)] $

== 中点法
<中点法>

$
  ∫_a^b f(x) dd(x) & = ∫_(x_0)^(x_1) f(x) dd(x) + ∫_(x_1)^(x_2) f(x) dd(x) + … + ∫_(x_(n -1))^(x_n) f(x) dd(x) \
                   & ≈ h f(frac(x_0 + x_1, 2)) + h f(frac(x_1 + x_2, 2)) + … + h t(frac(x_(n -1) + x_n, 2)) \
                   & ≈ h(t(frac(x_0 + x_1, 2)) + f(frac(x_1 + x_2, 2)) + … + f(frac(x_(n -1) + x_n, 2)))
$

即

$ ∫_a^b f(x) dd(x) ≈ h sum_(i = 0)^(n -1) f(x_i) $

其中，

$ x_i = (a + h / 2) + i h $

梯形法与中点法均可由 Lagrange 插值在相应节点上构造得出，插值节点的选取与截断误差阶的估计，见附录 B「微积分技术」。

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
+ 通过$q$近似$A(Ω) / A(R)$，即设$A(Ω) = q A(R)$
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
<前向-Euler-格式>

$ u^(n+1) = u^n + Δ t f(u^n, t_n), n = 0, …, N_t -1 $

前向 Euler 格式的误差阶与稳定性分析，以及后向 Euler、改进 Euler 与 Runge–Kutta 各族的构造，见附录 A「常微分方程」的数值解法部分。
