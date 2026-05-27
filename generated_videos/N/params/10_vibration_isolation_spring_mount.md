# Task 10 — vibration_isolation_spring_mount

## 物理
振动隔离 / 传递率（transmissibility）：
机器放在弹簧上，地板按 z_floor(t) = A·sin(ω·t) 振动。
机器响应（弹簧-质量-阻尼器）的稳态绝对振幅：
   T = √(1 + (2ζr)²) / √((1−r²)² + (2ζr)²)
其中 r = ω_drive/ω_n，ζ = c/(2√(km))

当 ω_drive > √2·ω_n → T < 1，振动被衰减（隔离区）
当 ω_drive = ω_n → T 很大（共振区）
当 ω_drive << ω_n → T ≈ 1（刚性传递）

## 几何
- "Floor"（蓝色 slab，5 kg）通过 slide z 在 world 中振动
- "Machine"（红色 slab，2 kg）是 floor 的子 body，通过 slide z 弹簧连接
- 弹簧用 spatial tendon 可视化（floor 顶面 site → machine 底面 site）
- 两侧暗木色细柱作为静态参考（标定位置）

## 物理参数
| 参数 | 值 |
|------|---|
| Floor 质量 M_floor | 5 kg |
| Machine 质量 M | 2 kg |
| 弹簧刚度 k | 500 N/m |
| 弹簧阻尼 c | 8.0 N·s/m（spec 是 0.5，加大让瞬态衰减快）|
| 自然频率 ω_n | √(k/M) = √250 ≈ 15.81 rad/s |
| 阻尼比 ζ | c/(2√(km)) ≈ 0.126 |
| 驱动频率 ω_drive | 2·ω_n = 31.62 rad/s |
| Floor 振幅 A | 0.020 m |
| 预测传递率 T | 1/|1−r²| = 1/3 ≈ 0.333 |

## 驱动方式
Floor 由 `<position>` actuator 强制跟随目标位置：
```
<position name="floor_drive" joint="ground_z" kp="80000" kv="120"
          ctrlrange="-0.05 0.05"/>
```
gen 脚本每步设：
```
data.ctrl[floor_drive] = A·sin(ω_drive·t)
```

注：用位置 actuator（不是直接 kinematic 覆写 qpos），这样弹簧
能感受到 floor 真实的反作用力 → 机器才会响应。

## 实测
- Floor 实际振幅：±21.1 mm
- Machine 实际振幅（绝对位置）：±7.8 mm
- 传递率比 = 0.367（理论 0.333，差 10% 来自数值阻尼）

## 仿真
- timestep 0.0005 s（小 dt 保证 actuator 稳定）
- 渲染 6 s（前 ~1 s 瞬态，剩 5 s 稳态）

## 相机
侧视图，pos (0, −1.50, 0.45), fovy 36
xyaxes "1 0 0  0 0.10 0.995"
