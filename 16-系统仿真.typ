#import "lib/lib.typ": *
#show: chapter-style.with(title: "系统仿真", info: info)

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
