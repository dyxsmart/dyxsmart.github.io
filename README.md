# 邓云馨 · 个人作品集

原生 HTML、CSS、JavaScript 静态网站，无构建步骤。

## 本地查看

在仓库根目录运行 `python3 -m http.server 8000`，打开 http://localhost:8000 。

## 目录

| 路径 | 用途 |
| --- | --- |
| `index.html` | 首页与项目入口 |
| 根目录其他 HTML | 项目详情；保留现有网址 |
| `assets/css/style.css` | 全站基础样式与首页样式 |
| `assets/css/detail.css` | 多个项目页共用样式 |
| `assets/css/其他文件` | 对应项目页的独立样式 |
| `assets/js/` | 导航等交互 |
| `assets/images/` | 网页展示图片与视频封面 |
| `assets/videos/` | 网页播放视频 |
| `assets/documents/` | 简历、作品集和茶煲仔 PDF |
| `assets/portfolio-source/` | 原始图片与素材索引 |
| `docs/` | 历史规划及设计草稿 |

## 内容维护

修改项目内容时编辑相应 HTML；通用项目页样式编辑 `detail.css`，项目特有样式编辑对应 CSS。`work.html` 保留为旧入口的跳转页。

《书法之于我》位于 `documentary.html#portrait-documentary`，归入现有纪录片项目。播放文件为 `assets/videos/calligraphy.mp4`（720p，约 27.2 MiB，05:29），封面为 `assets/images/calligraphy-poster.jpg`；点击后加载，不自动播放。原始 4K 视频保留在仓库外。

PDF 下载位于 `assets/documents/`。其中 `resume.pdf` 为原始简历，包含电话和微信；更新公开版时替换此文件即可。

## 分支与发布

- `dev`：当前开发与整理分支。
- `portfolio-assets`、`ljx_dev`：此前保留的一致基准；不随本次整理变更。
- `main`：原始版本。

GitHub 仓库 Settings → Pages → Deploy from a branch，选择包含所需内容的分支及 `/ (root)`。若发布 `dev`，推送该分支后自动更新。网站地址为 https://dyxsmart.github.io/ 。`.nojekyll` 用于直接发布静态资源。

普通 Git 上传的单文件需小于 100 MiB；视频通过 Git 上传，不使用网页上传。

## 修改后检查

运行 `python3 scripts/check_site.py` 检查本地页面资源、页面锚点及文件大小，再在浏览器检查受影响页面与视频播放。
