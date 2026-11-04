# 基金盯盘台

静态站点：单位净值日涨跌、区间涨跌幅、历史涨跌记录、净值历史分位与估值星级、周定投回测。
部署在 GitHub Pages；数据由 GitHub Actions 每个工作日定时抓取并写入仓库，页面本身不含任何后端。

## 目录

```
funds.json                    基金清单（改这里增删基金）
scripts/build-data.mjs        抓取 + 计算，产出 data/funds.js 与 data/funds.json
data/funds.js                 页面读取的数据（自动生成，勿手改）
index.html                    单页站点（哈希路由，按基金切换）
.github/workflows/update-fund-data.yml   定时更新
```

## 部署步骤

1. 在 GitHub 新建一个空仓库（Public，Pages 免费用），不要勾选自动生成 README。
2. 本目录已经是一个初始化好的 git 仓库（分支 `main`，含一次提交），解压后只需接上远端：

```bash
cd fund-dashboard
git remote add origin https://github.com/<你的用户名>/<仓库名>.git
git push -u origin main
```

3. 打开仓库 Settings → Actions → General → Workflow permissions，选 **Read and write permissions** 并保存。
   否则定时任务无法把数据提交回仓库。

4. 打开 Settings → Pages，Source 选 **Deploy from a branch**，Branch 选 `main`、目录选 `/ (root)`，保存。
   约 1 分钟后站点出现在 `https://<你的用户名>.github.io/<仓库名>/`。

5. 进入 Actions 页签，选中「更新基金数据」，点 **Run workflow** 手动跑一次，确认抓取成功并产生一次数据提交。

## 增删基金

编辑 `funds.json`，`code` 为 6 位基金代码，`note` 只是备忘（页面显示的名字取自数据源）：

```json
[
  { "code": "000248", "note": "汇添富中证主要消费ETF联接A" },
  { "code": "005827", "note": "易方达蓝筹精选" }
]
```

提交后到 Actions 手动跑一次「更新基金数据」，或在本地执行：

```bash
node scripts/build-data.mjs   # 需要 Node 18+，仅用内置 fetch
```

只想本地打开页面：先跑一次上面的命令生成 `data/funds.js`，再用浏览器打开 `index.html` 即可（数据是 JS 文件，不受本地 `file://` 跨域限制）。

## 口径

- **净值分位**：当前单位净值在近五年全部净值序列中的百分位（0% 历史最低，100% 历史最高）。不足五年则用成立以来。
- **估值星级**：由分位机械映射 —— ≤20% 五颗星，≤40% 四颗星，≤60% 三颗星，≤80% 两颗星，>80% 一颗星。分位低只说明相对自身历史便宜，不代表未来收益。
- **区间涨跌**：按交易日回溯（1 周 5 / 1 月 21 / 3 月 63 / 6 月 126 / 1 年 244 个交易日），3 年与 5 年按自然日回溯，成立以来取首末净值。
- **定投回测**：每周一投入 100 元，按当日（或最近交易日）单位净值买入，不计申购费与赎回费，分红按单位净值口径处理。
- **数据源**：天天基金 `pingzhongdata` 接口，单请求返回建仓以来全量单位净值。抓取失败时脚本会沿用上一版该基金数据并在日志中标注。

## 免责

本项目只做数据整理与展示，不构成任何投资建议。
