# Task 1 — resonance_forced_oscillation

## 物理
共振 vs 偏离共振。无阻尼弹簧-质量振子在 ω₀ = √(k/M) 驱动下振幅线性增长；
在 0.7·ω₀ 驱动下保持有界小振幅。

## 几何
- 两个并排弹簧-质量振子，x 间距 0.3 m
- 共用木质支架（双柱+横梁，高度 1.94 m）
- 质量块：0.06×0.06×0.06 m 立方体

## 物理参数
| 参数 | 值 |
|------|---|
| 弹簧刚度 k | 100 N/m |
| 质量 M | 0.1 kg |
| 自然频率 ω₀ | √(k/M) ≈ 31.62 rad/s (5.03 Hz) |
| 周期 T₀ | 0.199 s |
| 阻尼 | 0（两个 joint 都无阻尼） |
| 滑动范围 | ±0.85 m |
| 驱动加速度 A | 1.5 m/s² |
| Mass A 驱动频率 | ω_drive = ω₀ （共振） |
| Mass B 驱动频率 | ω_drive = 0.7·ω₀ |

## 驱动方式
`gen_resonance_forced_oscillation.py` 在每个 sim step 注入正弦速度脉冲：
```
data.qvel[slide_a] += A * sin(ω₀ * t) * dt
data.qvel[slide_b] += A * sin(0.7·ω₀ * t) * dt
```

## 仿真
- timestep 0.001 s
- gravity (0, 0, −9.81) — 引入恒定平衡偏移 mg/k ≈ 9.8 mm
- 渲染 15 s（共振模式 ~75 个周期）

## 预期峰值
- 共振质量 A：x_peak(T) = A·T/(2·ω₀) = 1.5·15/(2·31.62) ≈ 0.36 m
- 实测：A peak 31 cm（含微小数值阻尼），B peak 2.3 cm
- 比率 ≈ 13.7×

## 相机
侧视图，pos (0, −2.65, 1.00), fovy 42, xyaxes "1 0 0  0 0 1"
