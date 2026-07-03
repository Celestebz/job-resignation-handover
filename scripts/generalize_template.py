#!/usr/bin/env python3
"""将离职交接HTML模板中的个人信息通用化"""
import re
from pathlib import Path

html_path = Path(__file__).parent.parent / "assets" / "离职交接模板.html"
content = html_path.read_text(encoding="utf-8")

# 1. 替换个人信息为占位符
replacements = [
    # 签字表和账号表里的姓名
    ("王宝珍", "{{USER_NAME}}"),
    # checklist的panel-sub日期
    ("离职日期：2026-07-15", "离职日期：{{RESIGN_DATE}}"),
]

for old, new in replacements:
    content = content.replace(old, new)

# 2. 替换defaultTemplate中的硬编码日期
content = content.replace('const resignDate = "2026-07-15";',
                          'const resignDate = "{{RESIGN_DATE}}";')

# 3. 资产盘点表 - 替换具体项目为通用占位符行
# 黄色混合资产表
yellow_old = """            <tr><td>KOL联系方式</td><td>想带走自用</td><td>下份做KOL营销专员会用到，但保密协议约束</td><td>⚠️ 公开渠道找到的IG/邮箱可重新建联；公司整理的带合作进度、带价格的名单绝对不能带走。建议到新公司后从公开渠道重新联系，不要复制公司表</td></tr>
            <tr><td>KOL合作方法论</td><td>个人经验</td><td>经验属于自己</td><td>✅ 可以带走。但别用公司的具体案例、报价、合作条款做新工作素材</td></tr>
            <tr><td>1688供应商数据</td><td>下班后自己折腾，存在个人飞书</td><td>数据来源公开(1688平台)，个人时间产出</td><td>✅ 归属偏向你。建议留一份给公司作为业务参考，避免争议。技能本身无争议带走</td></tr>
            <tr><td>TikTok美甲供应商表(34家)</td><td>下班后自己折腾，存在个人飞书</td><td>⚠️ 虽下班后做，但为公司的TikTok Shop美甲品类业务服务</td><td>⚠️ 归属有争议。即便下班后做，如果用了公司业务身份联系供应商、筛选为的是公司品类，公司可能主张归属。强烈建议留给公司，筛选方法论可复用到其他品类</td></tr>
            <tr><td>Job Scout项目</td><td>下班后自己折腾，存在个人飞书</td><td>技能和数据都是个人时间产出</td><td>✅ 归属偏向你。个人飞书直接带走。技能本身无争议带走</td></tr>"""

yellow_new = """            <tr><td>{{ASSET_YELLOW_ROWS}}</td><td></td><td></td><td></td></tr>"""

content = content.replace(yellow_old, yellow_new)

# 绿色个人资产表
green_old = """            <tr><td>Job Scout / find-1688-suppliers 技能本身（代码、流程、SOP）</td><td>直接带走</td><td>能力产物</td></tr>
            <tr><td>WorkBuddy账号、配置</td><td>自己付费直接带走</td><td>⚠️ 清理掉公司项目相关的memory（客户数据、KOL合作细节等）</td></tr>
            <tr><td>法语学习飞书表</td><td>直接带走</td><td>纯个人</td></tr>
            <tr><td>健身视频字幕模板、个人笔记</td><td>直接带走</td><td>—</td></tr>
            <tr><td>个人社媒账号（非公司号）</td><td>直接带走</td><td>确认没绑公司邮箱</td></tr>"""

green_new = """            <tr><td>{{ASSET_GREEN_ROWS}}</td><td></td><td></td><td></td></tr>"""

content = content.replace(green_old, green_new)

# 风险提醒
risk_old = """        <strong>最大风险：</strong>下份做KOL营销专员，跟现在工作高度相关。保密协议+同行业跳槽，公司如果较真，最容易盯的就是KOL资源。<br><br>"""
risk_new = """        <strong>最大风险：</strong>{{RISK_REMINDER}}<br><br>"""
content = content.replace(risk_old, risk_new)

# 归属判断补充说明
belong_old = "2. 为公司的业务服务 — TikTok供应商表踩了这条<br>"
belong_new = "2. 为公司的业务服务 — 为公司业务做的项目，即便下班后做，归属也有争议<br>"
content = content.replace(belong_old, belong_new)

# 4. defaultTemplate中的具体任务改为通用
# D-6和D-7的项目相关任务
content = content.replace(
    '{ id: genId(), name: "项目状态文档：每个项目写明背景+当前进度+下一步+负责人", note: "Job Scout、1688技能、TikTok供应商表", done: false },',
    '{ id: genId(), name: "项目状态文档：每个项目写明背景+当前进度+下一步+负责人", note: "{{PROJECT_NAMES}}", done: false },'
)
content = content.replace(
    '{ id: genId(), name: "三个自建项目归属跟公司谈清楚", note: "Job Scout、1688技能、TikTok供应商表——数据留公司，技能自己带走", done: false },',
    '{ id: genId(), name: "自建项目归属跟公司谈清楚", note: "{{PROJECT_OWNERSHIP_NOTE}}", done: false },'
)
content = content.replace(
    '{ id: genId(), name: "TikTok美甲供应商表(34家)交接给公司", note: "公司业务产出，强烈建议留下", done: false },',
    '{ id: genId(), name: "{{COMPANY_ASSET_HANDOVER}}", note: "", done: false },'
)
content = content.replace(
    '{ id: genId(), name: "1688供应商数据：留一份给公司，自己重新跑干净的", note: "避免归属争议", done: false },',
    '{ id: genId(), name: "{{MIXED_ASSET_HANDOVER}}", note: "避免归属争议", done: false },'
)
content = content.replace(
    '{ id: genId(), name: "个人数据导出：法语学习飞书表", note: "纯个人，直接带走", done: false },',
    '{ id: genId(), name: "个人数据导出：个人项目和学习资料", note: "{{PERSONAL_DATA_NOTE}}", done: false },'
)

# 5. checklist中的具体项目改为通用
content = content.replace('"Job Scout数据归属已跟公司谈清楚"', '"自建项目1归属已跟公司谈清楚"')
content = content.replace('"1688供应商数据归属已谈清楚（数据留公司，技能带走）"', '"自建项目2归属已谈清楚"')
content = content.replace('"TikTok美甲供应商表已交接给公司"', '"为公司业务做的项目已交接给公司"')
content = content.replace('"法语学习飞书表已导出带走"', '"个人学习资料已导出带走"')

html_path.write_text(content, encoding="utf-8")
print("模板通用化完成")
print(f"文件: {html_path}")
