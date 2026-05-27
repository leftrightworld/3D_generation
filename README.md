# 3D_generation — 仓库结构说明

本仓库收录一系列经典力学物理演示视频，以及配套的评审页面、标注数据与历史归档资料。
以下说明根目录下每个一级文件夹 / 文件的内容（2026-05-27 重新整理后的结构）。

## generated_videos/ — 当前主交付内容
成套的物理演示视频 + 浏览器评审页面 + 评审标注数据。

- **`A/` … `O/`**：15 批（A–O）物理演示视频集合，共约 225 个渲染好的 `.mp4` 片段，
  覆盖单摆 / 碰撞 / 刚体与陀螺 / 链条 / 齿轮机构 / 驻波与色散 / 颗粒堆积等经典力学主题。
  多数批次内是直接平铺的 `.mp4`；个别批次带子目录：`A/param/`（场景参数）、
  `E/scenes/`、以及 `N/scenes/` 与 `N/params/`。
- **`review.html`**：浏览器评审页面。以相对路径加载同目录下 A–O 的视频；登录 GitHub
  token 后通过 GitHub API 把每位评审人的标注实时读写到
  `generated_videos/annotations/<github-login>.json`（见下）。未登录为只读。
- **`annotations/`**：每位评审人的标注数据（`<github-login>.json`），由 `review.html`
  自动读写、约每 15 秒轮询合并。格式与约定详见 `annotations/README.md`。

## oldvideos/ — 历史 / 归档资料
早期迭代产物，已不是主交付，集中归档于此。

- **`scenes/`**：约 104 个早期渲染的单场景 `.mp4`。
- **`dev/`**：场景的网格预览图与缩略图（`*_grid.png` / `*_preview.png`）等验证用图片。
- **`disk/`**：按文件夹和日期打包的 `*.tar.gz` 备份（如 `A_2026-05-23.tar.gz`）。
- **`showreels/`**：把多个场景拼成网格的合集 `.mp4`。
- **`physics_video_gen_v2/`**：早期的渲染流水线代码项目
  （`render.py`、`make_grid.py`、`make_showreel.py`、`docs/`、`CLAUDE.md`、`BACKLOG.md` 等）。
- **`index.html`**：早期的视频画廊页面（原为 GitHub Pages 站点首页，见文末说明）。

## test_editing_video.zip
视频编辑测试素材压缩包（约 22 MB），保留在根目录。

## README.md
本说明文件。

---

> **GitHub Pages 提示**：本仓库已开启 Pages（`main` 分支 / 根目录），站点地址为
> `https://leftrightworld.github.io/3D_generation/`。由于 `index.html` 已移入
> `oldvideos/`，站点根目录不再有首页（会 404）；评审页面现位于
> `https://leftrightworld.github.io/3D_generation/generated_videos/review.html`。
> 如需保留站点首页，可在根目录新增一个跳转到该评审页的 `index.html`。
