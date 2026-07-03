# Job Resignation Handover

离职交接 Skill for WorkBuddy。

## 功能

5 阶段流程帮你系统化完成离职交接：

1. **信息收集** — 批量问关键问题（离职日期、竞业保密、项目归属、账号性质）
2. **资产盘点** — 红/黄/绿三类分类（公司资产 / 混合资产 / 个人资产）
3. **倒排时间表** — 按离职日倒推，生成每日任务清单
4. **文档生成** — KOL/客户/项目/账号 4 个交接文档模板
5. **最终核对** — 7 大模块 checklist，走之前逐项打勾

## 产出

单文件 HTML 工具箱，4 个 tab：
- 倒排表（可勾选、状态高亮、localStorage 持久化）
- 资产盘点（可编辑表格）
- 交接模板（可直接填写）
- 最终核对（勾选 + 进度条）

## 使用

在 WorkBuddy 中安装此 Skill，触发词：

`离职`、`辞职`、`resign`、`quit`、`离开公司`、`job handover`、`交接`

## 结构

```
job-resignation-handover/
├── SKILL.md                        # Skill 主文件
├── assets/
│   └── 离职交接模板.html            # HTML 模板（含占位符）
├── references/
│   ├── asset-classification.md     # 资产分类参考
│   └── workflow.md                 # 5 阶段详细流程
└── scripts/
    └── generalize_template.py      # 模板通用化脚本
```

## License

MIT
