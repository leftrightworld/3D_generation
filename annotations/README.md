# annotations/

每个评审人的标注存为 `annotations/<github-login>.json`，由评审页面（`/review.html`）在登录后自动读写。

格式：
```json
{ "<视频相对路径>": { "keep": "yes|no|", "comment": "点评文字" } }
```
- `keep`: `yes`=保留, `no`=删除, 空=待定
- 页面每 ~15 秒拉取本目录下所有人的文件并合并显示。
- 请勿手工编辑命名冲突；正常通过页面操作即可。
