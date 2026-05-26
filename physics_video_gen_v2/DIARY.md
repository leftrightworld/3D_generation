# physics_video_gen 开发日志

## 项目目标
基于 MuJoCo 的物理场景渲染器，产出一系列 IPhO 力学题型的高质量演示视频。
作为 Sim2Reason / P1 流水线（物理仿真 → 题目生成 → RL 训练）的前端。

风格：紫色 flat skybox + 浅米色地面 + 暖木质结构 + 黄铜/红蓝点缀，
两灯（暖 key + 冷 fill），3/4 视角为主。详见 `~/.claude/.../style_guide.md`。

## 进度（2026-05-25）— v2 合并后

**104 个力学场景已完成。**

输出位置：全部 mp4 在 `out/scenes/`，showreel 在 `out/showreels/`。

⚠️ 约定：所有场景 mp4 渲染到 `out/scenes/<name>.mp4`，showreel 放 `out/showreels/`。

---

## 进度（2026-05-23）— 原始 23 个

**23 个力学场景已完成。**

### 已完成清单
| # | 场景 | 物理点 | 备注 |
|---|------|--------|------|
| 1 | bowling | 碰撞 + 摩擦 | 早期 |
| 2 | marble ramp | 重力 + 滚动 | 早期 |
| 3 | pendulum | 单摆周期 | 早期 |
| 4 | projectile + jenga | 抛体 + 塔的稳定性 | 早期 |
| 5 | Newton's cradle | 弹性碰撞 + 动量传递 | 需要刚硬接触 + 小 timestep |
| 6 | double pendulum | 混沌 | |
| 7 | incline + friction | μ 对照（共享面 μ→0） | gotcha #1 |
| 8 | dominoes | 链式倒塌 | 注意 hinge 轴向（gotcha #3） |
| 9 | spring-mass | SHM | tendon 当弹簧 |
| 10 | Atwood | 不可伸长绳 | joint equality（gotcha #6） |
| 11 | spinning top | 进动 + 章动 | ω_min, Ω 初始条件（gotcha #11-13） |
| 12 | conical pendulum | 锥摆 | gimbal 代 ball joint（gotcha #8） |
| 13 | loop-the-loop | 离心力 | 闭环 + 初速度（gotcha #9） |
| 14 | rolling race | I/MR² 对比 | inertial override（gotcha #14） |
| 15 | pendulum waves | 多摆同步图样 | 程序化生成 |
| 16 | coupled pendulums | 拍频 | |
| 17 | block overhang | 调和级数 ∑L/(2k) | |
| 18 | Galileo dropballs | 自由落体等时 | |
| 19 | elastic collision | 等质量速度交换 | freejoint + 刚硬接触（gotcha #16） |
| 20 | brachistochrone | 最速降线 vs 直线 | 程序化生成（cycloid） |
| 21 | Maxwell wheel | 转动 + 平动能量 | slide+hinge equality（gotcha #6 扩展） |
| 22 | beam buckling | Euler 屈曲 | 10 段离散梁 + 扭簧，margin 1.22（gotcha #17） |
| 23 | **rotating fluid** | 离心抛物面（颗粒近似） | 72 颗球当"水"，top-down 视角看出干涸中心 + 环形堆积（gotcha #18） |

### 本次 session 新做的
- **brachistochrone**（之前 session 留下的，已迁到 out/scenes/）
- **Maxwell wheel**（新做，slide+hinge joint equality 实现绳不滑）
- **beam buckling**（新做，离散柱+扭簧+顶端重物，调参三轮才稳）
- **rotating fluid**（新做，颗粒近似流体，160 球太慢→减到 72，侧视看不出来→换 top-down 出环形分布）

### 还没做的
1. **hydrostatic buoyancy**（静水浮力）

颗粒近似在 rotating fluid 里勉强 work（top-down 视角能看出离心环形分布 + 中央干涸），但对浮力来说颗粒比流体差更多——没有静压梯度，浮力本质需要连续介质。可选方案：
- 用颗粒勉强做，效果可能很差
- 跳过，把力学部分宣告收官
- 切换技术栈（Taichi / Genesis / Bullet+SPH）做浮力

### Pipeline
```
渲染：  python3 render.py    --scene scenes/X.xml --out out/scenes/X.mp4    --duration T [--init-qpos ...]
验证：  python3 make_grid.py --scene scenes/X.xml --out out/X_grid.png          --duration T --cols 4 --rows 2 [--init-qpos ...]
```
约定：声明做完之前必须看 grid PNG，视频会藏取景/物理问题。

程序化场景的生成脚本：`scenes/gen_*.py`，运行后会写出对应的 `scenes/*.xml`。

## 已踩坑总结
（详见 `~/.claude/projects/-Users-maiwang-physics-video-gen/memory/mujoco_gotchas.md`）

17 条坑，覆盖：
- 接触/摩擦的合成规则
- `<tendon>` 顶层放置
- hinge 轴方向 / 自由关节 qvel 的坐标系
- 弹性碰撞所需的刚硬接触参数
- ball joint 的坑（用 gimbal 替代）
- 顶部稳定性 ω_min, Ω 联立条件
- I/MR² 通过 inertial 覆盖
- Euler 屈曲的 margin/damping 窄窗口

## 下一步
等用户决定要不要做流体那两个；如果跳过，力学部分基本就收官了。
之后顺着 Sim2Reason / P1 思路往下是：
- 给每个场景加上"题目"标注（初末状态、未知量、答案）
- 接入 LLM 做物理 QA 生成
- 用这些场景训练 / 评测物理推理

但那是另一个 repo / 另一个工作流的事，这个 repo 的范围目前是 "scenes + render"。

## Round 1 合并（2026-05-25）— 员工 A/B/C/D/F

**新增 81 个场景，合计 104 个。** 全部用新版 render.py 重渲，6 分钟完成。

### 员工 A（13/17）
| # | 场景 | 物理点 | 时长 |
|---|------|--------|------|
| 24 | bifilar_pendulum | 双线悬摆扭振 | 6s |
| 25 | wilberforce_pendulum | 弹簧-扭转能量交换 | 18s |
| 26 | damped_pendulum_decay | 粘性阻尼衰减 | 8s |
| 27 | yoyo_with_reversal | Maxwell溜溜球反转 | 9s |
| 28 | coin_spiral | 硬币进动→倒下 | 7s |
| 29 | inelastic_collision | 完全非弹性碰撞 | 3.5s |
| 30 | coefficient_of_restitution | 弹跳高度几何衰减 | 14s |
| 31 | com_pair_track | 弹簧弹开，质心不动 | 5s |
| 32 | beats | 拍频包络 | 18s |
| 33 | wave_reflection_fixed | 固定端反射（反相） | 5s |
| 34 | capstan_effect | 绳绕转轴摩擦放大 | 7s |
| 35 | falling_chain_classical | 链条从桌上滑落加速 | 3.5s |
| 36 | bead_on_helix | 螺旋轨道下滑 | 7.5s |

未完成（标 incomplete）：tippe_top / slider_crank_mechanism / arch_compression / cone_balanced_on_tip

### 员工 B（17/17）
| # | 场景 | 物理点 | 时长 |
|---|------|--------|------|
| 37 | trifilar_pendulum | 三线盘扭振 | 4s |
| 38 | pendulum_with_air_drag | 二次阻尼衰减 | 8s |
| 39 | anharmonic_pendulum_large_swing | 大角度偏离SHM | 8s |
| 40 | rolling_cone | 圆锥圆周滚动 | 5s |
| 41 | gyroscope_on_string | 陀螺进动 | 5s |
| 42 | falling_chimney | 刚体倒塌 | 1.5s |
| 43 | ballistic_pendulum | 子弹嵌入摆 | 3s |
| 44 | glancing_2d_collision | 二维斜碰弹性 | 2s |
| 45 | cannon_recoil | 牛顿第三定律 | 2.5s |
| 46 | normal_modes_2mass | 两质量耦合弹簧模式 | 4s |
| 47 | wave_reflection_free | 自由端反射（同相） | 4s |
| 48 | stick_slip | 静/动摩擦振荡 | 6s |
| 49 | dzhanibekov_effect | 中间轴翻转 | 5s |
| 50 | sliding_chain_off_table | 链条悬挂加速 | 1.5s |
| 51 | bead_on_cycloid_track_isochrony | 等时降线三珠同到 | 1.8s |
| 52 | geneva_drive | 日内瓦间歇机构 | 5s |
| 53 | balance_beam_lever | 杠杆转矩平衡 | 3s |

### 员工 C（17/17）
| # | 场景 | 物理点 | 时长 |
|---|------|--------|------|
| 54 | compound_pendulum_shapes | 复摆周期vs形状 | 6s |
| 55 | triple_pendulum | 三重摆混沌 | 8s |
| 56 | spherical_pendulum_2d | 球面摆玫瑰线轨迹 | 14s |
| 57 | spool_with_string | 线轴滚转绳方向 | 4s |
| 58 | mass_through_hole | 穿孔绳角动量守恒 | 5s |
| 59 | reuleaux_triangle_rolling | 鲁洛三角等宽滚动 | 4s |
| 60 | basketball_tennis_drop | 叠球能量传递 | 4s |
| 61 | line_collision_chain | 无绳牛顿摆动量传递 | 2.5s |
| 62 | two_pendulums_collide | 两摆底部弹性碰撞 | 3s |
| 63 | vertical_spring_mass | 竖直弹簧SHM | 5s |
| 64 | wave_on_heavy_rope | 重绳脉冲传播 | 3s |
| 65 | tipping_vs_sliding | 倾覆vs滑动 | 4s |
| 66 | rattleback | 凯尔特石自旋反转 | 8s |
| 67 | hanging_chain_catenary | 悬链线下沉成形 | 6s |
| 68 | bead_on_parabolic_wire | 抛物线导轨SHM | 4s |
| 69 | domino_branching | Y形多米诺级联 | 5s |
| 70 | pyramid_keystone_removal | 楔石移除拱坍塌 | 4s |

注：C 的 render.py/make_grid.py 修改已合入主库（含FABRIK悬链线、rattleback双段渲染等）。修复了 mass_through_hole 关节查询的条件判断 bug。

### 员工 D（17/17）
| # | 场景 | 物理点 | 时长 |
|---|------|--------|------|
| 71 | cycloidal_pendulum_huygens | 摆线导槽等时摆 | 4s |
| 72 | rolling_chain | 坦克履带链 | 4.5s |
| 73 | centrifugal_governor | 瓦特离心调速器 | 4s |
| 74 | pulley_with_inertia | 有质量滑轮Atwood | 3s |
| 75 | n_body_1d_collisions | 7球1D弹性链 | 2s |
| 76 | block_on_accelerating_wedge | 加速楔块上的滑块 | 1.5s |
| 77 | pendulum_with_lateral_spring | 侧向弹簧能量交换 | 12s |
| 78 | hanging_slinky_drop | 弹簧底端悬挂释放 | 1.5s |
| 79 | standing_wave_on_string | 驻波基频 | 4s |
| 80 | belt_friction | 皮带传动 | 4s |
| 81 | block_on_block_static_friction | 叠块摩擦启动 | 2s |
| 82 | tumbling_book | 中间轴翻转（书本） | 5s |
| 83 | swinging_chain_pendulum | 柔性链摆甩动 | 5s |
| 84 | bead_in_rotating_ring | 转环内珠离心平衡 | 4s |
| 85 | block_and_tackle | 动滑轮2:1机械增益 | 3s |
| 86 | cantilever_load_curve | 悬臂梁端部挠度 | 3s |
| 87 | symmetry_breaking_ball_on_dome | 半球顶不稳定平衡 | 2s |

### 员工 F（17/17）
| # | 场景 | 物理点 | 时长 |
|---|------|--------|------|
| 88 | galileo_pendulum_peg | 钉子摆能量守恒 | 3s |
| 89 | horizontal_vs_dropped_balls | 平抛与自由落体等时 | 0.6s |
| 90 | chain_jet_classic | 链条自喷射 | 3.5s |
| 91 | rolling_disc_inscribes_cycloid | 圆盘滚动画摆线 | 4s |
| 92 | bucket_of_water_overhead_swing | 水桶头顶甩圆 | 3s |
| 93 | two_marbles_curved_track_collision | U型槽弹性碰撞 | 4s |
| 94 | planetary_gear_train | 行星齿轮 | 3s |
| 95 | gear_train_2_gears | 两齿轮传动比 | 3s |
| 96 | four_bar_linkage | Grashof四杆机构 | 4s |
| 97 | ratchet_pawl | 棘轮止逆 | 3s |
| 98 | chain_unspooling_from_pile | 链堆自解链 | 3.5s |
| 99 | triple_block_friction_chain | 三叠块摩擦链 | 2.5s |
| 100 | chain_on_scale_falling | 链条落秤冲击力 | 2s |
| 101 | two_bodies_on_incline_string | 斜面绳约束两物体 | 3s |
| 102 | double_atwood | 嵌套Atwood机 | 3.5s |
| 103 | galileo_inclined_plane_squared | 斜面d∝t² | 4s |
| 104 | rolling_dumbbell | 哑铃滚地翻转 | 4s |

### v2 结构变更（2026-05-25）
- `out/new_scenes/` → 拆分为 `out/scenes/`（场景mp4）和 `out/showreels/`（showreel）
- `render.py` 337行全功能版，`make_showreel.py` 动态扫描版
- `docs/gotchas.md` 从18条扩充至30条
- 全部104场景用新render.py重渲，约6分钟

## Handoff 准备（2026-05-23）

仓库已经整理成可以打包发给员工 / AI agents 继续 scaling 的状态。新增了：

- **[CLAUDE.md](CLAUDE.md)** — AI agents 进 repo 第一个读的文件，告诉它工作流、约定、禁忌
- **[README.md](README.md)** — 人类 onboarding 文档，含 5 步加新场景的 recipe
- **[BACKLOG.md](BACKLOG.md)** — ~70 个候选场景按难度分 3 tier，员工可以 claim
- **[docs/style_guide.md](docs/style_guide.md)** — 视觉风格配方（从 memory 搬进来）
- **[docs/gotchas.md](docs/gotchas.md)** — 18 条已踩坑（从 memory 搬进来）

理论 scaling 上限估算：Tier 1 (~30) + Tier 2 (~25) + Tier 3 (~10) + 已完成 (23)
≈ **88 个力学场景**。5 人并行 1 周可达。再往后就是参数变体，意义递减。

流体 / 电磁 / 光学 / 热力学不在 MuJoCo 适配范围内，已在 BACKLOG Tier 4 明确列出。
