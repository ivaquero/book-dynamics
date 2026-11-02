#import "lib/lib.typ": *
#show: chapter-style.with(title: "二元振荡器", info: info)

= FHN 方程
<FHN-方程>

著名的 Fitzhugh-Nagumo（FHN）振荡器用于模拟神经元的动作电位，是 Hodgkin-Huxley 方程的两变量简化。Fitzhugh-Nagumo 模型创造了相当准确的动作电位，并对神经元的定性行为进行建模。微分方程的计算公式为

$
  dot(u) & = -u(u - θ)(u - 1) - v + ω \
  dot(v) & = ɛ (u - γ v)
$

其中，$u$为电压，$v$为恢复电压，$θ$为阈值，$γ$为分流变量，$ω$为恒定电压。对于某些参数值，解表现出电压的缓慢收集和快速释放，这种行为被标记为集成（integrate）和开火（fire）。注意，对于生物系统来说，神经元在发射后不能立即收集电压，需要休息。

当$ω = ω(t)$是一个周期性的外部输入时，系统就会变成非自治的，会表现出混沌行为。

== 简单神经元
<简单神经元>

考虑最简单的神经元模型，即 FHN 模型

$
  V^' & = 1 / ɛ (-W + V(1 - V))(V - a) + I_(e x t) \
  W^' & = V - γ W
$

其中，$𝑨 = 0.1$，$ɛ = 0.01$，$γ= 1$。$I_(e x t)$是给系统的外部刺激。

== 耦合神经元
<耦合神经元>

现在将把 2 个神经元联系在一起，神经元 1 到神经元 2 的流量由以下给出

$
  I_(2 → 1) & = frac(V_2 - V_1, R) \
  I_(1 → 2) & = frac(V_1 - V_2, R)
$

神经元耦合的完全竞争是

$
  V_1^' & = 1 / ɛ (-W_1 + V_1 (1 - V_1))(V_1 - a) + I_(2 → 1) + I_(e x t) \
  W_1^' & = V_1 - γ W_1 \
  V_2^' & = 1 / ɛ (-W_2 + V_2 (1 - V_2))(V_2 - a) + I_(1 → 2) \
  W_2^' & = V_2 - γ W_2
$

取$ɛ = 0.008, R = 45, γ = 0.5, a = 0.1$及$I_(e x t) = 0.025$

#figure(
  image("images/ch13/fitzhugh-nagumo.png", width: 70%),
  caption: [FitzHugh-Nagumo 系统的相平面：红色为极限环轨迹，蓝色虚线为两条零倾线（nullclines）],
)

#genby("python/ch13_eq_fhn_lim.py")

= 配套代码

FHN 振荡器的相图、零倾线、极限环与耦合神经元模拟由以下脚本生成：

#companion(
  "python/ch13_eq_fhn.py",
  "python/ch13_eq_fhn2.py",
  "python/ch13_eq_fhn_coupled.py",
  "python/ch13_eq_fhn_lim.py",
  "python/ch13_eq_fhn_nullclines.py",
)
