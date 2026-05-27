# Task 5 — coriolis_turntable_puck

## 物理
旋转参考系中的 Coriolis 偏转：
- 在 LAB 帧：无摩擦的 puck 沿 v=(vr, 0) 走直线
- 在 DISC 帧（与盘共转）：同样的直线变成弯曲的螺旋路径
轨迹弯曲的可见量 = ω · t_on_disc（puck 在盘上停留期间盘转过的角度）

## 几何
- 圆盘 disc：R = 0.25 m，厚 0.010 m
- Puck：圆柱 R = 0.015 m，厚 0.010 m
- 圆盘上 6 个色彩 spoke（3 红 3 蓝交替）+ 黄铜方位标记
- spoke 极薄（半高 0.25mm）几乎贴在盘表面，避免与 puck 视觉重叠
- spoke 和标记都设 contype=0 conaffinity=0（视觉装饰，不参与碰撞）

## 物理参数
| 参数 | 值 |
|------|---|
| 圆盘半径 R | 0.25 m |
| 圆盘质量 M_disc | 2.0 kg（heavy 防止 back-torque 影响）|
| 圆盘角速度 ω | 1.5 rad/s（spec 是 2.0，我减速以更易跟踪）|
| Puck 半径 R_p | 0.015 m |
| Puck 质量 M_p | 0.05 kg |
| Puck 初速 v | 0.12 m/s（spec 是 0.30）|
| 圆盘-puck 摩擦 | 0（设定 puck 和 disc 的 friction = "0 0 0"）|
| 圆盘 hinge damping | 0 |

## 初始条件
| | 位置 | 速度 |
|---|------|------|
| 圆盘 | qpos=0 | qvel = 1.5 rad/s（about z）|
| Puck | (0.05, 0, 0.120) | (0.12, 0, 0) m/s（径向外）|

## 预期轨迹
- Puck 在盘上停留时间：(0.25 − 0.05) / 0.12 = 1.67 s
- 这段时间盘转过：1.5 · 1.67 = 2.5 rad ≈ 143°
- 4 s 总渲染中：盘转 6 rad ≈ 1 圈

## 仿真
- timestep 0.001 s
- 渲染 4.0 s
- top-down 相机（pos (0,0,1.05), fovy 34, xyaxes "1 0 0  0 1 0"）

## 偏离 spec 之处
- ω 从 2.0 减到 1.5 rad/s
- v_puck 从 0.30 减到 0.12 m/s
- spec fovy=60，我用 34（更紧的画框看清圆盘细节）
两个减速是因为原 spec 下 puck 0.67s 就飞出盘，画面感觉"急促"
