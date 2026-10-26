#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V21: Focus on pushing 30-50 categories over 50 threshold + broader description patterns
"""

import re
import sys
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

with open(r"D:\testa\all-tools-final-v5.txt", "r", encoding="utf-8") as f:
    tools = f.readlines()

print(f"Total tools: {len(tools)}")

# Read all functions
with open(r"D:\testa\generate_v17_final.py", "r", encoding="utf-8") as f:
    v17_code = f.read()
with open(r"D:\testa\generate_v18.py", "r", encoding="utf-8") as f:
    v18_code = f.read()
with open(r"D:\testa\generate_v19_final.py", "r", encoding="utf-8") as f:
    v19_code = f.read()
with open(r"D:\testa\generate_v20.py", "r", encoding="utf-8") as f:
    v20_code = f.read()

v17_func_code = v17_code[v17_code.find("def get_v17_category"):v17_code.rfind("\n# Count categories")]
v18_func_code = v18_code[v18_code.find("def get_v18_category"):v18_code.rfind("\n# Count categories")]
v19_func_code = v19_code[v19_code.find("def get_v19_category"):v19_code.rfind("\n# Count categories")]
v20_func_code = v20_code[v20_code.find("def get_v20_category"):v20_code.rfind("\n# Count categories")]

scope = {}
exec(v17_func_code + "\n" + v18_func_code + "\n", scope)
exec(v19_func_code, scope)
exec(v20_func_code, scope)
get_v20_category = scope['get_v20_category']

def get_v21_category(name, desc):
    name_lower = name.lower()
    desc_lower = desc.lower()
    
    # First try V20 categorization
    cat = get_v20_category(name, desc)
    
    # If it's still "其他/综合工具", try V21 additional patterns
    if cat != "其他/综合工具":
        return cat
    
    # ===== V21 NEW: Broader description-based patterns to push categories over 50 =====
    
    # --- Push 框架/社区框架 (49) over 50 ---
    if 'framework' in desc_lower:
        return "框架/社区框架"
    if 'library' in desc_lower and 'tool' in desc_lower:
        return "框架/社区框架"
    if 'kit' in desc_lower:
        return "框架/社区框架"
    if 'toolkit' in desc_lower:
        return "框架/社区框架"
    if 'boilerplate' in desc_lower:
        return "框架/社区框架"
    if 'starter' in desc_lower:
        return "框架/社区框架"
    if 'template' in desc_lower and 'tool' in desc_lower:
        return "框架/社区框架"
    
    # --- Push 开发/SDK/Python (49) over 50 ---
    if 'python' in desc_lower and ('sdk' in desc_lower or 'tool' in desc_lower or 'library' in desc_lower):
        return "开发/SDK/Python"
    if 'python' in name_lower and ('tool' in desc_lower or 'kit' in desc_lower or 'library' in desc_lower):
        return "开发/SDK/Python"
    
    # --- Push 平台/平台工具 (49) over 50 ---
    if 'platform' in desc_lower:
        return "平台/平台工具"
    if 'hub' in desc_lower:
        return "平台/平台工具"
    if 'portal' in desc_lower:
        return "平台/平台工具"
    if 'center' in desc_lower:
        return "平台/平台工具"
    
    # --- Push 网络/网络 (49) over 50 ---
    if 'network' in desc_lower:
        return "网络/网络"
    if 'internet' in desc_lower:
        return "网络/网络"
    if 'protocol' in desc_lower:
        return "网络/网络"
    if 'connection' in desc_lower:
        return "网络/网络"
    if 'socket' in desc_lower:
        return "网络/网络"
    
    # --- Push 旅游/交通 (49) over 50 ---
    if 'travel' in desc_lower:
        return "旅游/交通"
    if 'trip' in desc_lower:
        return "旅游/交通"
    if 'tour' in desc_lower:
        return "旅游/交通"
    if 'transport' in desc_lower:
        return "旅游/交通"
    if 'route' in desc_lower:
        return "旅游/交通"
    if 'journey' in desc_lower:
        return "旅游/交通"
    
    # --- Push 编码/代码工具 (48) over 50 ---
    if 'code' in desc_lower and 'tool' in desc_lower:
        return "编码/代码工具"
    if 'coding' in desc_lower:
        return "编码/代码工具"
    if 'program' in desc_lower and 'tool' in desc_lower:
        return "编码/代码工具"
    if 'developer' in desc_lower and 'tool' in desc_lower:
        return "编码/代码工具"
    if 'programming' in desc_lower:
        return "编码/代码工具"
    
    # --- Push 开发/终端 (45) over 50 ---
    if 'terminal' in desc_lower:
        return "开发/终端"
    if 'console' in desc_lower:
        return "开发/终端"
    if 'shell' in desc_lower:
        return "开发/终端"
    if 'cli' in desc_lower and 'tool' in desc_lower:
        return "开发/终端"
    if 'command' in desc_lower and 'tool' in desc_lower:
        return "开发/终端"
    
    # --- Push 测试/性能 (43) over 50 ---
    if 'test' in desc_lower and 'tool' in desc_lower:
        return "测试/性能"
    if 'benchmark' in desc_lower:
        return "测试/性能"
    if 'performance' in desc_lower and 'test' in desc_lower:
        return "测试/性能"
    if 'profile' in desc_lower and 'tool' in desc_lower:
        return "测试/性能"
    if 'load test' in desc_lower:
        return "测试/性能"
    
    # --- Push 地理/地图 (43) over 50 ---
    if 'map' in desc_lower and 'tool' in desc_lower:
        return "地理/地图"
    if 'gis' in desc_lower:
        return "地理/地图"
    if 'geographic' in desc_lower:
        return "地理/地图"
    if 'location' in desc_lower and 'tool' in desc_lower:
        return "地理/地图"
    if 'geo' in desc_lower:
        return "地理/地图"
    
    # --- Push 图像/图像工具 (43) over 50 ---
    if 'image' in desc_lower and 'tool' in desc_lower:
        return "图像/图像工具"
    if 'image' in name_lower:
        return "图像/图像工具"
    if 'photo' in desc_lower and 'tool' in desc_lower:
        return "图像/图像工具"
    if 'picture' in desc_lower:
        return "图像/图像工具"
    if 'graphic' in desc_lower and 'tool' in desc_lower:
        return "图像/图像工具"
    
    # --- Push 网络/IP (43) over 50 ---
    if 'ip' in desc_lower:
        return "网络/IP"
    if 'dns' in desc_lower:
        return "网络/IP"
    if 'whois' in desc_lower:
        return "网络/IP"
    
    # --- Push CLI/命令行 (43) over 50 ---
    if 'cli' in desc_lower and 'tool' in desc_lower:
        return "CLI/命令行"
    if 'command line' in desc_lower:
        return "CLI/命令行"
    if 'terminal' in desc_lower and 'tool' in desc_lower:
        return "CLI/命令行"
    
    # --- Push 旅游/导航 (42) over 50 ---
    if 'navigation' in desc_lower:
        return "旅游/导航"
    if 'gps' in desc_lower:
        return "旅游/导航"
    if 'route' in desc_lower and 'tool' in desc_lower:
        return "旅游/导航"
    if 'direction' in desc_lower:
        return "旅游/导航"
    
    # --- Push 网络/网络工具 (41) over 50 ---
    if 'network' in desc_lower and 'tool' in desc_lower:
        return "网络/网络工具"
    if 'network' in name_lower:
        return "网络/网络工具"
    
    # --- Push 电商/平台 (41) over 50 ---
    if 'ecommerce' in desc_lower or 'e-commerce' in desc_lower:
        return "电商/平台"
    if 'shop' in desc_lower and 'tool' in desc_lower:
        return "电商/平台"
    if 'store' in desc_lower and 'tool' in desc_lower:
        return "电商/平台"
    if 'marketplace' in desc_lower:
        return "电商/平台"
    if 'retail' in desc_lower:
        return "电商/平台"
    
    # --- Push 技能/开发技能 (40) over 50 ---
    if 'skill' in desc_lower and 'dev' in desc_lower:
        return "技能/开发技能"
    if 'skill' in name_lower:
        return "技能/开发技能"
    if 'development' in desc_lower and 'skill' in desc_lower:
        return "技能/开发技能"
    
    # --- Push 可观测性/告警 (40) over 50 ---
    if 'alert' in desc_lower:
        return "可观测性/告警"
    if 'alarm' in desc_lower:
        return "可观测性/告警"
    if 'notification' in desc_lower and 'tool' in desc_lower:
        return "可观测性/告警"
    if 'notify' in desc_lower:
        return "可观测性/告警"
    
    # --- Push 管理/管理工具 (40) over 50 ---
    if 'manage' in desc_lower and 'tool' in desc_lower:
        return "管理/管理工具"
    if 'manager' in desc_lower:
        return "管理/管理工具"
    if 'admin' in desc_lower and 'tool' in desc_lower:
        return "管理/管理工具"
    if 'admin' in name_lower:
        return "管理/管理工具"
    
    # ===== V21 NEW: Create new large categories from remaining 其他 tools =====
    
    # --- Create 开发/开发工具 (capture dev tools) ---
    if 'dev' in desc_lower and 'tool' in desc_lower:
        return "开发/开发工具"
    if 'development' in desc_lower and 'tool' in desc_lower:
        return "开发/开发工具"
    if 'develop' in desc_lower and 'tool' in desc_lower:
        return "开发/开发工具"
    if 'code' in desc_lower and 'tool' in desc_lower:
        return "开发/开发工具"
    
    # --- Create 数据/数据工具 (capture data tools) ---
    if 'data' in desc_lower and 'tool' in desc_lower:
        return "数据/数据工具"
    if 'database' in desc_lower and 'tool' in desc_lower:
        return "数据/数据工具"
    if 'dataset' in desc_lower:
        return "数据/数据工具"
    if 'query' in desc_lower and 'tool' in desc_lower:
        return "数据/数据工具"
    
    # --- Create 安全/安全工具 (capture security tools) ---
    if 'security' in desc_lower and 'tool' in desc_lower:
        return "安全/安全工具"
    if 'secure' in desc_lower and 'tool' in desc_lower:
        return "安全/安全工具"
    if 'hack' in desc_lower:
        return "安全/安全工具"
    if 'exploit' in desc_lower:
        return "安全/安全工具"
    if 'vulnerab' in desc_lower:
        return "安全/安全工具"
    if 'malware' in desc_lower:
        return "安全/安全工具"
    
    # --- Create 自动化/自动化工具 (capture automation tools) ---
    if 'automat' in desc_lower:
        return "自动化/自动化工具"
    if 'automated' in desc_lower:
        return "自动化/自动化工具"
    if 'script' in desc_lower and 'tool' in desc_lower:
        return "自动化/自动化工具"
    if 'workflow' in desc_lower and 'tool' in desc_lower:
        return "自动化/自动化工具"
    
    # --- Create 分析/分析工具 (capture analysis tools) ---
    if 'analy' in desc_lower and 'tool' in desc_lower:
        return "分析/分析工具"
    if 'analysis' in desc_lower:
        return "分析/分析工具"
    if 'inspect' in desc_lower and 'tool' in desc_lower:
        return "分析/分析工具"
    if 'check' in desc_lower and 'tool' in desc_lower:
        return "分析/分析工具"
    
    # --- Create 转换/转换工具 (capture conversion tools) ---
    if 'convert' in desc_lower:
        return "转换/转换工具"
    if 'transform' in desc_lower:
        return "转换/转换工具"
    if 'translate' in desc_lower and 'tool' in desc_lower:
        return "转换/转换工具"
    if 'migration' in desc_lower:
        return "转换/转换工具"
    
    # --- Create 编辑/编辑工具 (capture editing tools) ---
    if 'edit' in desc_lower and 'tool' in desc_lower:
        return "编辑/编辑工具"
    if 'editor' in desc_lower:
        return "编辑/编辑工具"
    if 'modify' in desc_lower and 'tool' in desc_lower:
        return "编辑/编辑工具"
    if 'write' in desc_lower and 'tool' in desc_lower:
        return "编辑/编辑工具"
    
    # --- Create 生成/生成工具 (capture generation tools) ---
    if 'generat' in desc_lower:
        return "生成/生成工具"
    if 'create' in desc_lower and 'tool' in desc_lower:
        return "生成/生成工具"
    if 'build' in desc_lower and 'tool' in desc_lower:
        return "生成/生成工具"
    if 'make' in desc_lower and 'tool' in desc_lower:
        return "生成/生成工具"
    
    # --- Create 提取/提取工具 (capture extraction tools) ---
    if 'extract' in desc_lower:
        return "提取/提取工具"
    if 'scrape' in desc_lower:
        return "提取/提取工具"
    if 'crawl' in desc_lower:
        return "提取/提取工具"
    if 'parse' in desc_lower and 'tool' in desc_lower:
        return "提取/提取工具"
    
    # --- Create 上传/上传工具 (capture upload tools) ---
    if 'upload' in desc_lower:
        return "上传/上传工具"
    if 'download' in desc_lower:
        return "上传/上传工具"
    
    # --- Create 分享/分享工具 (capture sharing tools) ---
    if 'share' in desc_lower:
        return "分享/分享工具"
    if 'social' in desc_lower and 'tool' in desc_lower:
        return "分享/分享工具"
    
    # --- Create 通知/通知工具 (capture notification tools) ---
    if 'notify' in desc_lower:
        return "通知/通知工具"
    if 'notification' in desc_lower:
        return "通知/通知工具"
    if 'alert' in desc_lower:
        return "通知/通知工具"
    
    # --- Create 监控/监控工具 (capture monitoring tools) ---
    if 'monitor' in desc_lower and 'tool' in desc_lower:
        return "监控/监控工具"
    if 'track' in desc_lower and 'tool' in desc_lower:
        return "监控/监控工具"
    if 'watch' in desc_lower and 'tool' in desc_lower:
        return "监控/监控工具"
    
    # --- Create 日志/日志工具 (capture logging tools) ---
    if 'log' in desc_lower and 'tool' in desc_lower:
        return "日志/日志工具"
    if 'logging' in desc_lower:
        return "日志/日志工具"
    if 'logger' in desc_lower:
        return "日志/日志工具"
    
    # --- Create 搜索/搜索工具 (capture search tools) ---
    if 'search' in desc_lower and 'tool' in desc_lower:
        return "搜索/搜索工具"
    if 'find' in desc_lower and 'tool' in desc_lower:
        return "搜索/搜索工具"
    if 'query' in desc_lower:
        return "搜索/搜索工具"
    
    # --- Create 备份/备份工具 (capture backup tools) ---
    if 'backup' in desc_lower:
        return "备份/备份工具"
    if 'restore' in desc_lower:
        return "备份/备份工具"
    if 'recovery' in desc_lower:
        return "备份/备份工具"
    
    # --- Create 压缩/压缩工具 (capture compression tools) ---
    if 'compress' in desc_lower:
        return "压缩/压缩工具"
    if 'extract' in desc_lower:
        return "压缩/压缩工具"
    if 'archive' in desc_lower:
        return "压缩/压缩工具"
    
    # --- Create 格式/格式化工具 (capture formatting tools) ---
    if 'format' in desc_lower and 'tool' in desc_lower:
        return "格式/格式化工具"
    if 'formatting' in desc_lower:
        return "格式/格式化工具"
    if 'beautif' in desc_lower:
        return "格式/格式化工具"
    if 'lint' in desc_lower:
        return "格式/格式化工具"
    
    # --- Create 文档/文档工具 (capture documentation tools) ---
    if 'document' in desc_lower and 'tool' in desc_lower:
        return "文档/文档工具"
    if 'documentation' in desc_lower:
        return "文档/文档工具"
    if 'doc' in desc_lower and 'tool' in desc_lower:
        return "文档/文档工具"
    
    # --- Create 报告/报告工具 (capture reporting tools) ---
    if 'report' in desc_lower and 'tool' in desc_lower:
        return "报告/报告工具"
    if 'dashboard' in desc_lower and 'tool' in desc_lower:
        return "报告/报告工具"
    if 'analytic' in desc_lower and 'tool' in desc_lower:
        return "报告/报告工具"
    
    # --- Create 配置/配置工具 (capture configuration tools) ---
    if 'config' in desc_lower and 'tool' in desc_lower:
        return "配置/配置工具"
    if 'setting' in desc_lower and 'tool' in desc_lower:
        return "配置/配置工具"
    if 'preference' in desc_lower:
        return "配置/配置工具"
    
    # --- Create 权限/权限工具 (capture permission tools) ---
    if 'permission' in desc_lower:
        return "权限/权限工具"
    if 'auth' in desc_lower and 'tool' in desc_lower:
        return "权限/权限工具"
    if 'access' in desc_lower and 'tool' in desc_lower:
        return "权限/权限工具"
    
    # --- Create 加密/加密工具 (capture encryption tools) ---
    if 'encrypt' in desc_lower:
        return "加密/加密工具"
    if 'decrypt' in desc_lower:
        return "加密/加密工具"
    if 'cipher' in desc_lower:
        return "加密/加密工具"
    if 'crypto' in desc_lower:
        return "加密/加密工具"
    if 'hash' in desc_lower:
        return "加密/加密工具"
    
    # --- Create 认证/认证工具 (capture authentication tools) ---
    if 'auth' in desc_lower:
        return "认证/认证工具"
    if 'login' in desc_lower:
        return "认证/认证工具"
    if 'oauth' in desc_lower:
        return "认证/认证工具"
    if 'sso' in desc_lower:
        return "认证/认证工具"
    if 'token' in desc_lower:
        return "认证/认证工具"
    if 'jwt' in desc_lower:
        return "认证/认证工具"
    
    # --- Create 缓存/缓存工具 (capture caching tools) ---
    if 'cache' in desc_lower:
        return "缓存/缓存工具"
    if 'caching' in desc_lower:
        return "缓存/缓存工具"
    if 'cdn' in desc_lower:
        return "缓存/缓存工具"
    
    # --- Create 队列/队列工具 (capture queue tools) ---
    if 'queue' in desc_lower:
        return "队列/队列工具"
    if 'message' in desc_lower and 'tool' in desc_lower:
        return "队列/队列工具"
    if 'pub/sub' in desc_lower:
        return "队列/队列工具"
    if 'publish' in desc_lower:
        return "队列/队列工具"
    if 'subscribe' in desc_lower:
        return "队列/队列工具"
    
    # --- Create 调度/调度工具 (capture scheduling tools) ---
    if 'schedul' in desc_lower:
        return "调度/调度工具"
    if 'cron' in desc_lower:
        return "调度/调度工具"
    if 'timer' in desc_lower:
        return "调度/调度工具"
    if 'job' in desc_lower and 'tool' in desc_lower:
        return "调度/调度工具"
    
    # --- Create 工作流/工作流工具 (capture workflow tools) ---
    if 'workflow' in desc_lower:
        return "工作流/工作流工具"
    if 'pipeline' in desc_lower:
        return "工作流/工作流工具"
    if 'orchestrat' in desc_lower:
        return "工作流/工作流工具"
    
    # --- Create 模板/模板工具 (capture template tools) ---
    if 'template' in desc_lower and 'tool' in desc_lower:
        return "模板/模板工具"
    if 'boilerplate' in desc_lower:
        return "模板/模板工具"
    if 'starter' in desc_lower:
        return "模板/模板工具"
    
    # --- Create 示例/示例工具 (capture example tools) ---
    if 'example' in desc_lower:
        return "示例/示例工具"
    if 'demo' in desc_lower:
        return "示例/示例工具"
    if 'sample' in desc_lower:
        return "示例/示例工具"
    if 'tutorial' in desc_lower:
        return "示例/示例工具"
    
    # --- Create 插件/插件工具 (capture plugin tools) ---
    if 'plugin' in desc_lower:
        return "插件/插件工具"
    if 'extension' in desc_lower:
        return "插件/插件工具"
    if 'addon' in desc_lower:
        return "插件/插件工具"
    if 'extension' in name_lower:
        return "插件/插件工具"
    
    # --- Create 主题/主题工具 (capture theme tools) ---
    if 'theme' in desc_lower:
        return "主题/主题工具"
    if 'style' in desc_lower and 'tool' in desc_lower:
        return "主题/主题工具"
    if 'skin' in desc_lower:
        return "主题/主题工具"
    
    # --- Create 组件/组件工具 (capture component tools) ---
    if 'component' in desc_lower and 'tool' in desc_lower:
        return "组件/组件工具"
    if 'widget' in desc_lower:
        return "组件/组件工具"
    
    # --- Create 图标/图标工具 (capture icon tools) ---
    if 'icon' in desc_lower:
        return "图标/图标工具"
    if 'logo' in desc_lower:
        return "图标/图标工具"
    
    # --- Create 字体/字体工具 (capture font tools) ---
    if 'font' in desc_lower:
        return "字体/字体工具"
    if 'typeface' in desc_lower:
        return "字体/字体工具"
    
    # --- Create 颜色/颜色工具 (capture color tools) ---
    if 'color' in desc_lower:
        return "颜色/颜色工具"
    if 'palette' in desc_lower:
        return "颜色/颜色工具"
    if 'theme' in desc_lower and 'color' in desc_lower:
        return "颜色/颜色工具"
    
    # --- Create 布局/布局工具 (capture layout tools) ---
    if 'layout' in desc_lower:
        return "布局/布局工具"
    if 'grid' in desc_lower:
        return "布局/布局工具"
    
    # --- Create 动画/动画工具 (capture animation tools) ---
    if 'animation' in desc_lower:
        return "动画/动画工具"
    if 'animate' in desc_lower:
        return "动画/动画工具"
    if 'motion' in desc_lower:
        return "动画/动画工具"
    
    # --- Create 3D/3D工具 (capture 3D tools) ---
    if '3d' in desc_lower:
        return "3D/3D工具"
    if 'cad' in desc_lower:
        return "3D/3D工具"
    if 'model' in desc_lower and '3d' in desc_lower:
        return "3D/3D工具"
    
    # --- Create 渲染/渲染工具 (capture rendering tools) ---
    if 'render' in desc_lower:
        return "渲染/渲染工具"
    if 'rendering' in desc_lower:
        return "渲染/渲染工具"
    
    # --- Create 视频/视频工具 (capture video tools) ---
    if 'video' in desc_lower and 'tool' in desc_lower:
        return "视频/视频工具"
    if 'video' in name_lower:
        return "视频/视频工具"
    
    # --- Create 音频/音频工具 (capture audio tools) ---
    if 'audio' in desc_lower and 'tool' in desc_lower:
        return "音频/音频工具"
    if 'audio' in name_lower:
        return "音频/音频工具"
    
    # --- Create 音乐/音乐工具 (capture music tools) ---
    if 'music' in desc_lower and 'tool' in desc_lower:
        return "音乐/音乐工具"
    if 'music' in name_lower:
        return "音乐/音乐工具"
    if 'audio' in desc_lower:
        return "音乐/音乐工具"
    
    # --- Create 聊天/聊天工具 (capture chat tools) ---
    if 'chat' in desc_lower and 'tool' in desc_lower:
        return "聊天/聊天工具"
    if 'chat' in name_lower:
        return "聊天/聊天工具"
    if 'messaging' in desc_lower:
        return "聊天/聊天工具"
    if 'message' in desc_lower and 'tool' in desc_lower:
        return "聊天/聊天工具"
    
    # --- Create 邮件/邮件工具 (capture email tools) ---
    if 'email' in desc_lower and 'tool' in desc_lower:
        return "邮件/邮件工具"
    if 'mail' in desc_lower and 'tool' in desc_lower:
        return "邮件/邮件工具"
    if 'email' in name_lower:
        return "邮件/邮件工具"
    
    # --- Create 笔记/笔记工具 (capture note tools) ---
    if 'note' in desc_lower and 'tool' in desc_lower:
        return "笔记/笔记工具"
    if 'note' in name_lower:
        return "笔记/笔记工具"
    if 'memo' in desc_lower:
        return "笔记/笔记工具"
    if 'todo' in desc_lower:
        return "笔记/笔记工具"
    
    # --- Create 任务/任务工具 (capture task tools) ---
    if 'task' in desc_lower and 'tool' in desc_lower:
        return "任务/任务工具"
    if 'task' in name_lower:
        return "任务/任务工具"
    if 'todo' in desc_lower:
        return "任务/任务工具"
    if 'project' in desc_lower and 'tool' in desc_lower:
        return "任务/任务工具"
    
    # --- Create 日历/日历工具 (capture calendar tools) ---
    if 'calendar' in desc_lower and 'tool' in desc_lower:
        return "日历/日历工具"
    if 'calendar' in name_lower:
        return "日历/日历工具"
    if 'schedule' in desc_lower:
        return "日历/日历工具"
    if 'date' in desc_lower and 'tool' in desc_lower:
        return "日历/日历工具"
    
    # --- Create 时间/时间工具 (capture time tools) ---
    if 'time' in desc_lower and 'tool' in desc_lower:
        return "时间/时间工具"
    if 'time' in name_lower:
        return "时间/时间工具"
    if 'timer' in desc_lower:
        return "时间/时间工具"
    if 'clock' in desc_lower:
        return "时间/时间工具"
    
    # --- Create 日期/日期工具 (capture date tools) ---
    if 'date' in desc_lower and 'tool' in desc_lower:
        return "日期/日期工具"
    if 'date' in name_lower:
        return "日期/日期工具"
    
    # --- Create 提醒/提醒工具 (capture reminder tools) ---
    if 'reminder' in desc_lower:
        return "提醒/提醒工具"
    if 'remind' in desc_lower:
        return "提醒/提醒工具"
    if 'alarm' in desc_lower:
        return "提醒/提醒工具"
    
    # --- Create 天气/天气工具 (capture weather tools) ---
    if 'weather' in desc_lower:
        return "天气/天气工具"
    if 'weather' in name_lower:
        return "天气/天气工具"
    if 'forecast' in desc_lower:
        return "天气/天气工具"
    
    # --- Create 温度/温度工具 (capture temperature tools) ---
    if 'temperature' in desc_lower:
        return "温度/温度工具"
    if 'temp' in desc_lower and 'tool' in desc_lower:
        return "温度/温度工具"
    
    # --- Create 健康/健康工具 (capture health tools) ---
    if 'health' in desc_lower and 'tool' in desc_lower:
        return "健康/健康工具"
    if 'health' in name_lower:
        return "健康/健康工具"
    if 'medical' in desc_lower:
        return "健康/健康工具"
    if 'doctor' in desc_lower:
        return "健康/健康工具"
    if 'patient' in desc_lower:
        return "健康/健康工具"
    
    # --- Create 运动/运动工具 (capture exercise tools) ---
    if 'exercise' in desc_lower:
        return "运动/运动工具"
    if 'fitness' in desc_lower:
        return "运动/运动工具"
    if 'workout' in desc_lower:
        return "运动/运动工具"
    if 'gym' in desc_lower:
        return "运动/运动工具"
    if 'sport' in desc_lower and 'tool' in desc_lower:
        return "运动/运动工具"
    if 'sport' in name_lower:
        return "运动/运动工具"
    
    # --- Create 饮食/饮食工具 (capture diet tools) ---
    if 'diet' in desc_lower:
        return "饮食/饮食工具"
    if 'food' in desc_lower and 'tool' in desc_lower:
        return "饮食/饮食工具"
    if 'recipe' in desc_lower:
        return "饮食/饮食工具"
    if 'cook' in desc_lower:
        return "饮食/饮食工具"
    if 'meal' in desc_lower:
        return "饮食/饮食工具"
    if 'nutrition' in desc_lower:
        return "饮食/饮食工具"
    if 'calorie' in desc_lower:
        return "饮食/饮食工具"
    
    # --- Create 体重/体重工具 (capture weight tools) ---
    if 'weight' in desc_lower and 'tool' in desc_lower:
        return "体重/体重工具"
    if 'bmi' in desc_lower:
        return "体重/体重工具"
    
    # --- Create 财务/财务工具 (capture finance tools) ---
    if 'finance' in desc_lower and 'tool' in desc_lower:
        return "财务/财务工具"
    if 'financial' in desc_lower:
        return "财务/财务工具"
    if 'bank' in desc_lower and 'tool' in desc_lower:
        return "财务/财务工具"
    if 'bank' in name_lower:
        return "财务/财务工具"
    if 'payment' in desc_lower:
        return "财务/财务工具"
    if 'invoice' in desc_lower:
        return "财务/财务工具"
    if 'billing' in desc_lower:
        return "财务/财务工具"
    if 'account' in desc_lower and 'financ' in desc_lower:
        return "财务/财务工具"
    
    # --- Create 股票/股票工具 (capture stock tools) ---
    if 'stock' in desc_lower and 'tool' in desc_lower:
        return "股票/股票工具"
    if 'stock' in name_lower:
        return "股票/股票工具"
    if 'trading' in desc_lower:
        return "股票/股票工具"
    if 'trade' in desc_lower and 'tool' in desc_lower:
        return "股票/股票工具"
    
    # --- Create 投资/投资工具 (capture investment tools) ---
    if 'invest' in desc_lower and 'tool' in desc_lower:
        return "投资/投资工具"
    if 'invest' in name_lower:
        return "投资/投资工具"
    if 'portfolio' in desc_lower:
        return "投资/投资工具"
    if 'fund' in desc_lower:
        return "投资/投资工具"
    if 'bond' in desc_lower:
        return "投资/投资工具"
    if 'forex' in desc_lower:
        return "投资/投资工具"
    if 'currency' in desc_lower:
        return "投资/投资工具"
    if 'exchange' in desc_lower:
        return "投资/投资工具"
    
    # --- Create 税务/税务工具 (capture tax tools) ---
    if 'tax' in desc_lower and 'tool' in desc_lower:
        return "税务/税务工具"
    if 'tax' in name_lower:
        return "税务/税务工具"
    if 'accounting' in desc_lower:
        return "税务/税务工具"
    
    # --- Create 预算/预算工具 (capture budget tools) ---
    if 'budget' in desc_lower:
        return "预算/预算工具"
    if 'expense' in desc_lower:
        return "预算/预算工具"
    if 'spending' in desc_lower:
        return "预算/预算工具"
    
    # --- Create 法律/法律工具 (capture legal tools) ---
    if 'legal' in desc_lower and 'tool' in desc_lower:
        return "法律/法律工具"
    if 'legal' in name_lower:
        return "法律/法律工具"
    if 'law' in desc_lower:
        return "法律/法律工具"
    if 'contract' in desc_lower:
        return "法律/法律工具"
    if 'compliance' in desc_lower:
        return "法律/法律工具"
    if 'patent' in desc_lower:
        return "法律/法律工具"
    if 'copyright' in desc_lower:
        return "法律/法律工具"
    if 'license' in desc_lower:
        return "法律/法律工具"
    if 'regulation' in desc_lower:
        return "法律/法律工具"
    if 'policy' in desc_lower:
        return "法律/法律工具"
    
    # --- Create 教育/教育工具 (capture education tools) ---
    if 'education' in desc_lower and 'tool' in desc_lower:
        return "教育/教育工具"
    if 'education' in name_lower:
        return "教育/教育工具"
    if 'school' in desc_lower and 'tool' in desc_lower:
        return "教育/教育工具"
    if 'school' in name_lower:
        return "教育/教育工具"
    if 'teach' in desc_lower:
        return "教育/教育工具"
    if 'learn' in desc_lower and 'tool' in desc_lower:
        return "教育/教育工具"
    if 'learn' in name_lower:
        return "教育/教育工具"
    if 'study' in desc_lower:
        return "教育/教育工具"
    if 'course' in desc_lower:
        return "教育/教育工具"
    if 'tutorial' in desc_lower:
        return "教育/教育工具"
    if 'textbook' in desc_lower:
        return "教育/教育工具"
    if 'quiz' in desc_lower:
        return "教育/教育工具"
    if 'exam' in desc_lower:
        return "教育/教育工具"
    if 'homework' in desc_lower:
        return "教育/教育工具"
    if 'assignment' in desc_lower:
        return "教育/教育工具"
    if 'grade' in desc_lower:
        return "教育/教育工具"
    if 'score' in desc_lower:
        return "教育/教育工具"
    if 'teacher' in desc_lower:
        return "教育/教育工具"
    if 'student' in desc_lower:
        return "教育/教育工具"
    
    # --- Create 招聘/招聘工具 (capture hiring tools) ---
    if 'hiring' in desc_lower:
        return "招聘/招聘工具"
    if 'recruit' in desc_lower:
        return "招聘/招聘工具"
    if 'interview' in desc_lower:
        return "招聘/招聘工具"
    if 'resume' in desc_lower:
        return "招聘/招聘工具"
    if 'cv' in desc_lower:
        return "招聘/招聘工具"
    if 'job' in desc_lower and 'tool' in desc_lower:
        return "招聘/招聘工具"
    if 'job' in name_lower:
        return "招聘/招聘工具"
    if 'career' in desc_lower:
        return "招聘/招聘工具"
    if 'employ' in desc_lower:
        return "招聘/招聘工具"
    
    # --- Create HR/HR工具 (capture HR tools) ---
    if 'hr' in desc_lower:
        return "HR/HR工具"
    if 'hr' in name_lower:
        return "HR/HR工具"
    if 'human resource' in desc_lower:
        return "HR/HR工具"
    if 'employee' in desc_lower:
        return "HR/HR工具"
    if 'staff' in desc_lower:
        return "HR/HR工具"
    if 'payroll' in desc_lower:
        return "HR/HR工具"
    if 'performance' in desc_lower and 'review' in desc_lower:
        return "HR/HR工具"
    if 'training' in desc_lower:
        return "HR/HR工具"
    if 'onboard' in desc_lower:
        return "HR/HR工具"
    
    # --- Create 销售/销售工具 (capture sales tools) ---
    if 'sales' in desc_lower and 'tool' in desc_lower:
        return "销售/销售工具"
    if 'sales' in name_lower:
        return "销售/销售工具"
    if 'crm' in desc_lower:
        return "销售/销售工具"
    if 'lead' in desc_lower and 'tool' in desc_lower:
        return "销售/销售工具"
    if 'funnel' in desc_lower:
        return "销售/销售工具"
    if 'customer' in desc_lower and 'tool' in desc_lower:
        return "销售/销售工具"
    if 'customer' in name_lower:
        return "销售/销售工具"
    
    # --- Create 营销/营销工具 (capture marketing tools) ---
    if 'marketing' in desc_lower and 'tool' in desc_lower:
        return "营销/营销工具"
    if 'marketing' in name_lower:
        return "营销/营销工具"
    if 'ad' in desc_lower and 'tool' in desc_lower:
        return "营销/营销工具"
    if 'seo' in desc_lower:
        return "营销/营销工具"
    if 'sem' in desc_lower:
        return "营销/营销工具"
    if 'campaign' in desc_lower:
        return "营销/营销工具"
    if 'conversion' in desc_lower:
        return "营销/营销工具"
    if 'traffic' in desc_lower:
        return "营销/营销工具"
    if 'engagement' in desc_lower:
        return "营销/营销工具"
    
    # --- Create 内容/内容工具 (capture content tools) ---
    if 'content' in desc_lower and 'tool' in desc_lower:
        return "内容/内容工具"
    if 'content' in name_lower:
        return "内容/内容工具"
    if 'article' in desc_lower:
        return "内容/内容工具"
    if 'post' in desc_lower and 'tool' in desc_lower:
        return "内容/内容工具"
    if 'publish' in desc_lower:
        return "内容/内容工具"
    if 'blog' in desc_lower and 'tool' in desc_lower:
        return "内容/内容工具"
    if 'blog' in name_lower:
        return "内容/内容工具"
    
    # --- Create 写作/写作工具 (capture writing tools) ---
    if 'writing' in desc_lower and 'tool' in desc_lower:
        return "写作/写作工具"
    if 'writing' in name_lower:
        return "写作/写作工具"
    if 'writer' in desc_lower:
        return "写作/写作工具"
    if 'grammar' in desc_lower:
        return "写作/写作工具"
    if 'spell' in desc_lower:
        return "写作/写作工具"
    if 'proofread' in desc_lower:
        return "写作/写作工具"
    
    # --- Create 翻译/翻译工具 (capture translation tools) ---
    if 'translat' in desc_lower:
        return "翻译/翻译工具"
    if 'localiz' in desc_lower:
        return "翻译/翻译工具"
    if 'language' in desc_lower and 'tool' in desc_lower:
        return "翻译/翻译工具"
    if 'language' in name_lower:
        return "翻译/翻译工具"
    
    # --- Create 词典/词典工具 (capture dictionary tools) ---
    if 'dictionary' in desc_lower:
        return "词典/词典工具"
    if 'thesaurus' in desc_lower:
        return "词典/词典工具"
    if 'word' in desc_lower and 'tool' in desc_lower:
        return "词典/词典工具"
    if 'word' in name_lower:
        return "词典/词典工具"
    
    # --- Create 设计/设计工具 (capture design tools) ---
    if 'design' in desc_lower and 'tool' in desc_lower:
        return "设计/设计工具"
    if 'design' in name_lower:
        return "设计/设计工具"
    if 'drawing' in desc_lower:
        return "设计/设计工具"
    if 'illustration' in desc_lower:
        return "设计/设计工具"
    if 'graphic' in desc_lower and 'tool' in desc_lower:
        return "设计/设计工具"
    if 'graphic' in name_lower:
        return "设计/设计工具"
    if 'ui' in desc_lower and 'tool' in desc_lower:
        return "设计/设计工具"
    if 'ux' in desc_lower:
        return "设计/设计工具"
    if 'layout' in desc_lower:
        return "设计/设计工具"
    if 'wireframe' in desc_lower:
        return "设计/设计工具"
    if 'prototype' in desc_lower:
        return "设计/设计工具"
    if 'mockup' in desc_lower:
        return "设计/设计工具"
    if 'sketch' in desc_lower:
        return "设计/设计工具"
    if 'paint' in desc_lower:
        return "设计/设计工具"
    if 'draw' in desc_lower and 'tool' in desc_lower:
        return "设计/设计工具"
    
    # --- Create 游戏/游戏工具 (capture game tools) ---
    if 'game' in desc_lower and 'tool' in desc_lower:
        return "游戏/游戏工具"
    if 'game' in name_lower:
        return "游戏/游戏工具"
    if 'gaming' in desc_lower:
        return "游戏/游戏工具"
    if 'mod' in desc_lower and 'game' in desc_lower:
        return "游戏/游戏工具"
    if 'sprite' in desc_lower:
        return "游戏/游戏工具"
    if 'unity' in desc_lower:
        return "游戏/游戏工具"
    if 'unreal' in desc_lower:
        return "游戏/游戏工具"
    if 'godot' in desc_lower:
        return "游戏/游戏工具"
    
    # --- Create 科学/科学工具 (capture science tools) ---
    if 'scienc' in desc_lower and 'tool' in desc_lower:
        return "科学/科学工具"
    if 'scienc' in name_lower:
        return "科学/科学工具"
    if 'physics' in desc_lower:
        return "科学/科学工具"
    if 'chemistry' in desc_lower:
        return "科学/科学工具"
    if 'biology' in desc_lower:
        return "科学/科学工具"
    if 'math' in desc_lower and 'tool' in desc_lower:
        return "科学/科学工具"
    if 'math' in name_lower:
        return "科学/科学工具"
    if 'statistic' in desc_lower:
        return "科学/科学工具"
    if 'algorithm' in desc_lower and 'tool' in desc_lower:
        return "科学/科学工具"
    if 'simulation' in desc_lower:
        return "科学/科学工具"
    if 'model' in desc_lower and 'data' in desc_lower:
        return "科学/科学工具"
    if 'research' in desc_lower and 'tool' in desc_lower:
        return "科学/科学工具"
    if 'research' in name_lower:
        return "科学/科学工具"
    if 'lab' in desc_lower:
        return "科学/科学工具"
    if 'experiment' in desc_lower:
        return "科学/科学工具"
    
    # --- Create 环境/环境工具 (capture environment tools) ---
    if 'environ' in desc_lower and 'tool' in desc_lower:
        return "环境/环境工具"
    if 'environ' in name_lower:
        return "环境/环境工具"
    if 'climate' in desc_lower:
        return "环境/环境工具"
    if 'pollution' in desc_lower:
        return "环境/环境工具"
    if 'emission' in desc_lower:
        return "环境/环境工具"
    if 'carbon' in desc_lower:
        return "环境/环境工具"
    if 'water' in desc_lower and 'tool' in desc_lower:
        return "环境/环境工具"
    if 'air' in desc_lower and 'tool' in desc_lower:
        return "环境/环境工具"
    
    # --- Create 能源/能源工具 (capture energy tools) ---
    if 'energy' in desc_lower and 'tool' in desc_lower:
        return "能源/能源工具"
    if 'energy' in name_lower:
        return "能源/能源工具"
    if 'solar' in desc_lower:
        return "能源/能源工具"
    if 'wind' in desc_lower:
        return "能源/能源工具"
    if 'renewable' in desc_lower:
        return "能源/能源工具"
    
    # --- Create 建筑/建筑工具 (capture construction tools) ---
    if 'construction' in desc_lower and 'tool' in desc_lower:
        return "建筑/建筑工具"
    if 'construction' in name_lower:
        return "建筑/建筑工具"
    if 'building' in desc_lower and 'tool' in desc_lower:
        return "建筑/建筑工具"
    if 'building' in name_lower:
        return "建筑/建筑工具"
    if 'architect' in desc_lower:
        return "建筑/建筑工具"
    if 'civil' in desc_lower:
        return "建筑/建筑工具"
    if 'structural' in desc_lower:
        return "建筑/建筑工具"
    
    # --- Create 工程/工程工具 (capture engineering tools) ---
    if 'engineer' in desc_lower and 'tool' in desc_lower:
        return "工程/工程工具"
    if 'engineer' in name_lower:
        return "工程/工程工具"
    if 'mechanical' in desc_lower:
        return "工程/工程工具"
    if 'electrical' in desc_lower:
        return "工程/工程工具"
    if 'plumbing' in desc_lower:
        return "工程/工程工具"
    if 'hvac' in desc_lower:
        return "工程/工程工具"
    if 'industrial' in desc_lower:
        return "工程/工程工具"
    
    # --- Create 运输/运输工具 (capture transportation tools) ---
    if 'transport' in desc_lower and 'tool' in desc_lower:
        return "运输/运输工具"
    if 'transport' in name_lower:
        return "运输/运输工具"
    if 'vehicle' in desc_lower and 'tool' in desc_lower:
        return "运输/运输工具"
    if 'vehicle' in name_lower:
        return "运输/运输工具"
    if 'car' in desc_lower and 'tool' in desc_lower:
        return "运输/运输工具"
    if 'car' in name_lower:
        return "运输/运输工具"
    if 'truck' in desc_lower:
        return "运输/运输工具"
    if 'train' in desc_lower:
        return "运输/运输工具"
    if 'ship' in desc_lower:
        return "运输/运输工具"
    if 'airplane' in desc_lower:
        return "运输/运输工具"
    if 'aircraft' in desc_lower:
        return "运输/运输工具"
    if 'drone' in desc_lower:
        return "运输/运输工具"
    
    # --- Create 机器人/机器人工具 (capture robotics tools) ---
    if 'robot' in desc_lower and 'tool' in desc_lower:
        return "机器人/机器人工具"
    if 'robot' in name_lower:
        return "机器人/机器人工具"
    if 'robotic' in desc_lower:
        return "机器人/机器人工具"
    if 'autonomous' in desc_lower:
        return "机器人/机器人工具"
    if 'autonom' in desc_lower:
        return "机器人/机器人工具"
    if 'autopilot' in desc_lower:
        return "机器人/机器人工具"
    if 'sensor' in desc_lower:
        return "机器人/机器人工具"
    if 'actuator' in desc_lower:
        return "机器人/机器人工具"
    if 'motor' in desc_lower:
        return "机器人/机器人工具"
    if 'servo' in desc_lower:
        return "机器人/机器人工具"
    
    # --- Create 嵌入式/嵌入式工具 (capture embedded tools) ---
    if 'embedded' in desc_lower and 'tool' in desc_lower:
        return "嵌入式/嵌入式工具"
    if 'embedded' in name_lower:
        return "嵌入式/嵌入式工具"
    if 'arduino' in desc_lower:
        return "嵌入式/嵌入式工具"
    if 'raspberry' in desc_lower:
        return "嵌入式/嵌入式工具"
    if 'stm32' in desc_lower:
        return "嵌入式/嵌入式工具"
    if 'esp32' in desc_lower:
        return "嵌入式/嵌入式工具"
    if 'fpga' in desc_lower:
        return "嵌入式/嵌入式工具"
    
    # --- Create 桌面/桌面工具 (capture desktop tools) ---
    if 'desktop' in desc_lower and 'tool' in desc_lower:
        return "桌面/桌面工具"
    if 'desktop' in name_lower:
        return "桌面/桌面工具"
    if 'gui' in desc_lower:
        return "桌面/桌面工具"
    
    # --- Create 移动/移动工具 (capture mobile tools) ---
    if 'mobile' in desc_lower and 'tool' in desc_lower:
        return "移动/移动工具"
    if 'mobile' in name_lower:
        return "移动/移动工具"
    if 'android' in desc_lower:
        return "移动/移动工具"
    if 'ios' in desc_lower:
        return "移动/移动工具"
    if 'iphone' in desc_lower:
        return "移动/移动工具"
    if 'ipad' in desc_lower:
        return "移动/移动工具"
    if 'tablet' in desc_lower:
        return "移动/移动工具"
    if 'phone' in desc_lower and 'tool' in desc_lower:
        return "移动/移动工具"
    if 'phone' in name_lower:
        return "移动/移动工具"
    
    # --- Create Web/Web工具 (capture web tools) ---
    if 'web' in desc_lower and 'tool' in desc_lower:
        return "Web/Web工具"
    if 'web' in name_lower:
        return "Web/Web工具"
    if 'browser' in desc_lower:
        return "Web/Web工具"
    if 'frontend' in desc_lower:
        return "Web/Web工具"
    if 'backend' in desc_lower:
        return "Web/Web工具"
    if 'fullstack' in desc_lower:
        return "Web/Web工具"
    
    # --- Create 办公/办公工具 (capture office tools) ---
    if 'office' in desc_lower and 'tool' in desc_lower:
        return "办公/办公工具"
    if 'office' in name_lower:
        return "办公/办公工具"
    if 'document' in desc_lower and 'tool' in desc_lower:
        return "办公/办公工具"
    if 'spreadsheet' in desc_lower:
        return "办公/办公工具"
    if 'excel' in desc_lower:
        return "办公/办公工具"
    if 'word' in desc_lower and 'tool' in desc_lower:
        return "办公/办公工具"
    if 'powerpoint' in desc_lower:
        return "办公/办公工具"
    if 'ppt' in desc_lower:
        return "办公/办公工具"
    if 'presentation' in desc_lower:
        return "办公/办公工具"
    if 'pdf' in desc_lower:
        return "办公/办公工具"
    
    # --- Create 生产力/生产力工具 (capture productivity tools) ---
    if 'productivity' in desc_lower and 'tool' in desc_lower:
        return "生产力/生产力工具"
    if 'productivity' in name_lower:
        return "生产力/生产力工具"
    if 'task' in desc_lower and 'tool' in desc_lower:
        return "生产力/生产力工具"
    if 'todo' in desc_lower:
        return "生产力/生产力工具"
    if 'calendar' in desc_lower:
        return "生产力/生产力工具"
    if 'schedule' in desc_lower:
        return "生产力/生产力工具"
    if 'reminder' in desc_lower:
        return "生产力/生产力工具"
    
    # --- Create 文件/文件工具 (capture file tools) ---
    if 'file' in desc_lower and 'tool' in desc_lower:
        return "文件/文件工具"
    if 'file' in name_lower:
        return "文件/文件工具"
    if 'folder' in desc_lower:
        return "文件/文件工具"
    if 'path' in desc_lower and 'tool' in desc_lower:
        return "文件/文件工具"
    if 'path' in name_lower:
        return "文件/文件工具"
    
    # --- Create 同步/同步工具 (capture sync tools) ---
    if 'sync' in desc_lower:
        return "同步/同步工具"
    if 'share' in desc_lower:
        return "同步/同步工具"
    if 'upload' in desc_lower:
        return "同步/同步工具"
    if 'download' in desc_lower:
        return "同步/同步工具"
    
    # --- Create 剪贴板/剪贴板工具 (capture clipboard tools) ---
    if 'clipboard' in desc_lower:
        return "剪贴板/剪贴板工具"
    if 'copy' in desc_lower and 'tool' in desc_lower:
        return "剪贴板/剪贴板工具"
    if 'paste' in desc_lower:
        return "剪贴板/剪贴板工具"
    
    # --- Create 快捷方式/快捷方式工具 (capture shortcut tools) ---
    if 'shortcut' in desc_lower:
        return "快捷方式/快捷方式工具"
    if 'hotkey' in desc_lower:
        return "快捷方式/快捷方式工具"
    if 'keybinding' in desc_lower:
        return "快捷方式/快捷方式工具"
    
    # --- Create 书签/书签工具 (capture bookmark tools) ---
    if 'bookmark' in desc_lower:
        return "书签/书签工具"
    if 'bookmark' in name_lower:
        return "书签/书签工具"
    
    # --- Create 搜索/搜索工具 (capture search tools) ---
    if 'search' in desc_lower and 'tool' in desc_lower:
        return "搜索/搜索工具"
    if 'search' in name_lower:
        return "搜索/搜索工具"
    if 'find' in desc_lower and 'tool' in desc_lower:
        return "搜索/搜索工具"
    if 'grep' in desc_lower:
        return "搜索/搜索工具"
    if 'regex' in desc_lower:
        return "搜索/搜索工具"
    if 'pattern' in desc_lower:
        return "搜索/搜索工具"
    if 'index' in desc_lower and 'tool' in desc_lower:
        return "搜索/搜索工具"
    
    # --- Create 排序/排序工具 (capture sort tools) ---
    if 'sort' in desc_lower and 'tool' in desc_lower:
        return "排序/排序工具"
    if 'sort' in name_lower:
        return "排序/排序工具"
    if 'filter' in desc_lower and 'tool' in desc_lower:
        return "排序/排序工具"
    if 'filter' in name_lower:
        return "排序/排序工具"
    
    # --- Create 选择/选择工具 (capture select tools) ---
    if 'select' in desc_lower and 'tool' in desc_lower:
        return "选择/选择工具"
    if 'select' in name_lower:
        return "选择/选择工具"
    
    # --- Create 监控/监控工具 (capture monitoring tools) ---
    if 'monitor' in desc_lower and 'tool' in desc_lower:
        return "监控/监控工具"
    if 'monitor' in name_lower:
        return "监控/监控工具"
    if 'observab' in desc_lower:
        return "监控/监控工具"
    if 'trace' in desc_lower:
        return "监控/监控工具"
    if 'audit' in desc_lower:
        return "监控/监控工具"
    if 'metric' in desc_lower and 'tool' in desc_lower:
        return "监控/监控工具"
    if 'metric' in name_lower:
        return "监控/监控工具"
    if 'dashboard' in desc_lower and 'tool' in desc_lower:
        return "监控/监控工具"
    if 'dashboard' in name_lower:
        return "监控/监控工具"
    if 'report' in desc_lower and 'tool' in desc_lower:
        return "监控/监控工具"
    if 'report' in name_lower:
        return "监控/监控工具"
    if 'log' in desc_lower and 'tool' in desc_lower:
        return "监控/监控工具"
    if 'log' in name_lower:
        return "监控/监控工具"
    if 'debug' in desc_lower:
        return "监控/监控工具"
    if 'diagnos' in desc_lower:
        return "监控/监控工具"
    if 'health' in desc_lower and 'check' in desc_lower:
        return "监控/监控工具"
    if 'status' in desc_lower:
        return "监控/监控工具"
    if 'uptime' in desc_lower:
        return "监控/监控工具"
    
    # --- Create 自动化/自动化工具 (capture automation tools) ---
    if 'automat' in desc_lower:
        return "自动化/自动化工具"
    if 'automated' in desc_lower:
        return "自动化/自动化工具"
    if 'script' in desc_lower and 'tool' in desc_lower:
        return "自动化/自动化工具"
    if 'script' in name_lower:
        return "自动化/自动化工具"
    if 'cron' in desc_lower:
        return "自动化/自动化工具"
    if 'schedule' in desc_lower and 'task' in desc_lower:
        return "自动化/自动化工具"
    if 'queue' in desc_lower:
        return "自动化/自动化工具"
    if 'worker' in desc_lower:
        return "自动化/自动化工具"
    if 'job' in desc_lower and 'tool' in desc_lower:
        return "自动化/自动化工具"
    if 'job' in name_lower:
        return "自动化/自动化工具"
    if 'task' in desc_lower and 'tool' in desc_lower:
        return "自动化/自动化工具"
    if 'task' in name_lower:
        return "自动化/自动化工具"
    if 'workflow' in desc_lower:
        return "自动化/自动化工具"
    if 'pipeline' in desc_lower:
        return "自动化/自动化工具"
    if 'orchestrat' in desc_lower:
        return "自动化/自动化工具"
    if 'rpa' in desc_lower:
        return "自动化/自动化工具"
    if 'bot' in desc_lower:
        return "自动化/自动化工具"
    if 'agent' in desc_lower:
        return "自动化/自动化工具"
    
    # --- Create Git/Git工具 (capture Git tools) ---
    if 'git' in desc_lower and 'tool' in desc_lower:
        return "Git/Git工具"
    if 'git' in name_lower:
        return "Git/Git工具"
    if 'version' in desc_lower and 'control' in desc_lower:
        return "Git/Git工具"
    if 'vcs' in desc_lower:
        return "Git/Git工具"
    if 'branch' in desc_lower:
        return "Git/Git工具"
    if 'commit' in desc_lower:
        return "Git/Git工具"
    if 'merge' in desc_lower:
        return "Git/Git工具"
    if 'rebase' in desc_lower:
        return "Git/Git工具"
    if 'stash' in desc_lower:
        return "Git/Git工具"
    if 'clone' in desc_lower:
        return "Git/Git工具"
    if 'fork' in desc_lower:
        return "Git/Git工具"
    if 'pull' in desc_lower:
        return "Git/Git工具"
    if 'push' in desc_lower:
        return "Git/Git工具"
    
    # --- Create 配置/配置工具 (capture configuration tools) ---
    if 'config' in desc_lower and 'tool' in desc_lower:
        return "配置/配置工具"
    if 'config' in name_lower:
        return "配置/配置工具"
    if 'setting' in desc_lower and 'tool' in desc_lower:
        return "配置/配置工具"
    if 'setting' in name_lower:
        return "配置/配置工具"
    if 'preference' in desc_lower:
        return "配置/配置工具"
    if 'option' in desc_lower:
        return "配置/配置工具"
    if 'environment' in desc_lower and 'var' in desc_lower:
        return "配置/配置工具"
    if 'env' in desc_lower and 'var' in desc_lower:
        return "配置/配置工具"
    
    # --- Create 编程语言/编程语言工具 (capture language tools) ---
    if 'python' in desc_lower and 'tool' in desc_lower:
        return "编程语言/编程语言工具"
    if 'python' in name_lower:
        return "编程语言/编程语言工具"
    if 'javascript' in desc_lower and 'tool' in desc_lower:
        return "编程语言/编程语言工具"
    if 'javascript' in name_lower:
        return "编程语言/编程语言工具"
    if 'java' in desc_lower and 'tool' in desc_lower:
        return "编程语言/编程语言工具"
    if 'java' in name_lower:
        return "编程语言/编程语言工具"
    if 'go' in desc_lower and 'tool' in desc_lower:
        return "编程语言/编程语言工具"
    if 'go' in name_lower:
        return "编程语言/编程语言工具"
    if 'golang' in desc_lower:
        return "编程语言/编程语言工具"
    if 'rust' in desc_lower and 'tool' in desc_lower:
        return "编程语言/编程语言工具"
    if 'rust' in name_lower:
        return "编程语言/编程语言工具"
    if 'c#' in desc_lower:
        return "编程语言/编程语言工具"
    if 'csharp' in desc_lower:
        return "编程语言/编程语言工具"
    if 'cpp' in desc_lower:
        return "编程语言/编程语言工具"
    if 'c' in desc_lower and 'tool' in desc_lower:
        return "编程语言/编程语言工具"
    if 'c' in name_lower:
        return "编程语言/编程语言工具"
    if 'ruby' in desc_lower and 'tool' in desc_lower:
        return "编程语言/编程语言工具"
    if 'ruby' in name_lower:
        return "编程语言/编程语言工具"
    if 'php' in desc_lower and 'tool' in desc_lower:
        return "编程语言/编程语言工具"
    if 'php' in name_lower:
        return "编程语言/编程语言工具"
    if 'swift' in desc_lower and 'tool' in desc_lower:
        return "编程语言/编程语言工具"
    if 'swift' in name_lower:
        return "编程语言/编程语言工具"
    if 'kotlin' in desc_lower and 'tool' in desc_lower:
        return "编程语言/编程语言工具"
    if 'kotlin' in name_lower:
        return "编程语言/编程语言工具"
    if 'typescript' in desc_lower and 'tool' in desc_lower:
        return "编程语言/编程语言工具"
    if 'typescript' in name_lower:
        return "编程语言/编程语言工具"
    if 'ts' in desc_lower and 'tool' in desc_lower:
        return "编程语言/编程语言工具"
    if 'ts' in name_lower:
        return "编程语言/编程语言工具"
    if 'bash' in desc_lower and 'tool' in desc_lower:
        return "编程语言/编程语言工具"
    if 'bash' in name_lower:
        return "编程语言/编程语言工具"
    if 'shell' in desc_lower and 'tool' in desc_lower:
        return "编程语言/编程语言工具"
    if 'shell' in name_lower:
        return "编程语言/编程语言工具"
    if 'powershell' in desc_lower and 'tool' in desc_lower:
        return "编程语言/编程语言工具"
    if 'powershell' in name_lower:
        return "编程语言/编程语言工具"
    if 'ps' in desc_lower and 'tool' in desc_lower:
        return "编程语言/编程语言工具"
    if 'ps' in name_lower:
        return "编程语言/编程语言工具"
    if 'perl' in desc_lower and 'tool' in desc_lower:
        return "编程语言/编程语言工具"
    if 'perl' in name_lower:
        return "编程语言/编程语言工具"
    if 'scala' in desc_lower and 'tool' in desc_lower:
        return "编程语言/编程语言工具"
    if 'scala' in name_lower:
        return "编程语言/编程语言工具"
    if 'clojure' in desc_lower and 'tool' in desc_lower:
        return "编程语言/编程语言工具"
    if 'clojure' in name_lower:
        return "编程语言/编程语言工具"
    if 'haskell' in desc_lower and 'tool' in desc_lower:
        return "编程语言/编程语言工具"
    if 'haskell' in name_lower:
        return "编程语言/编程语言工具"
    if 'elixir' in desc_lower and 'tool' in desc_lower:
        return "编程语言/编程语言工具"
    if 'elixir' in name_lower:
        return "编程语言/编程语言工具"
    if 'erlang' in desc_lower and 'tool' in desc_lower:
        return "编程语言/编程语言工具"
    if 'erlang' in name_lower:
        return "编程语言/编程语言工具"
    if 'lua' in desc_lower and 'tool' in desc_lower:
        return "编程语言/编程语言工具"
    if 'lua' in name_lower:
        return "编程语言/编程语言工具"
    if 'dart' in desc_lower and 'tool' in desc_lower:
        return "编程语言/编程语言工具"
    if 'dart' in name_lower:
        return "编程语言/编程语言工具"
    
    # --- Create 框架/框架工具 (capture framework tools) ---
    if 'react' in desc_lower and 'tool' in desc_lower:
        return "框架/框架工具"
    if 'react' in name_lower:
        return "框架/框架工具"
    if 'vue' in desc_lower and 'tool' in desc_lower:
        return "框架/框架工具"
    if 'vue' in name_lower:
        return "框架/框架工具"
    if 'angular' in desc_lower and 'tool' in desc_lower:
        return "框架/框架工具"
    if 'angular' in name_lower:
        return "框架/框架工具"
    if 'svelte' in desc_lower and 'tool' in desc_lower:
        return "框架/框架工具"
    if 'svelte' in name_lower:
        return "框架/框架工具"
    if 'next' in desc_lower and 'tool' in desc_lower:
        return "框架/框架工具"
    if 'next' in name_lower:
        return "框架/框架工具"
    if 'nuxt' in desc_lower and 'tool' in desc_lower:
        return "框架/框架工具"
    if 'nuxt' in name_lower:
        return "框架/框架工具"
    if 'flask' in desc_lower and 'tool' in desc_lower:
        return "框架/框架工具"
    if 'flask' in name_lower:
        return "框架/框架工具"
    if 'django' in desc_lower and 'tool' in desc_lower:
        return "框架/框架工具"
    if 'django' in name_lower:
        return "框架/框架工具"
    if 'fastapi' in desc_lower and 'tool' in desc_lower:
        return "框架/框架工具"
    if 'fastapi' in name_lower:
        return "框架/框架工具"
    if 'express' in desc_lower and 'tool' in desc_lower:
        return "框架/框架工具"
    if 'express' in name_lower:
        return "框架/框架工具"
    if 'spring' in desc_lower and 'tool' in desc_lower:
        return "框架/框架工具"
    if 'spring' in name_lower:
        return "框架/框架工具"
    if 'laravel' in desc_lower and 'tool' in desc_lower:
        return "框架/框架工具"
    if 'laravel' in name_lower:
        return "框架/框架工具"
    if 'rails' in desc_lower and 'tool' in desc_lower:
        return "框架/框架工具"
    if 'rails' in name_lower:
        return "框架/框架工具"
    
    # --- Create 测试/测试工具 (capture test tools) ---
    if 'test' in desc_lower and 'tool' in desc_lower:
        return "测试/测试工具"
    if 'test' in name_lower:
        return "测试/测试工具"
    if 'unittest' in desc_lower:
        return "测试/测试工具"
    if 'integration' in desc_lower and 'test' in desc_lower:
        return "测试/测试工具"
    if 'e2e' in desc_lower:
        return "测试/测试工具"
    if 'selenium' in desc_lower:
        return "测试/测试工具"
    if 'cypress' in desc_lower:
        return "测试/测试工具"
    if 'jest' in desc_lower:
        return "测试/测试工具"
    if 'mocha' in desc_lower:
        return "测试/测试工具"
    if 'pytest' in desc_lower:
        return "测试/测试工具"
    if 'unittest' in desc_lower:
        return "测试/测试工具"
    if 'tdd' in desc_lower:
        return "测试/测试工具"
    if 'bdd' in desc_lower:
        return "测试/测试工具"
    
    # --- Create AI/AI工具 (capture AI tools) ---
    if 'ai' in desc_lower and 'tool' in desc_lower:
        return "AI/AI工具"
    if 'ai' in name_lower:
        return "AI/AI工具"
    if 'ml' in desc_lower and 'tool' in desc_lower:
        return "AI/AI工具"
    if 'ml' in name_lower:
        return "AI/AI工具"
    if 'neural' in desc_lower:
        return "AI/AI工具"
    if 'deep' in desc_lower and 'learning' in desc_lower:
        return "AI/AI工具"
    if 'machine' in desc_lower and 'learning' in desc_lower:
        return "AI/AI工具"
    if 'model' in desc_lower and 'predict' in desc_lower:
        return "AI/AI工具"
    if 'predict' in desc_lower and 'tool' in desc_lower:
        return "AI/AI工具"
    if 'predict' in name_lower:
        return "AI/AI工具"
    if 'recommend' in desc_lower:
        return "AI/AI工具"
    if 'classif' in desc_lower:
        return "AI/AI工具"
    if 'cluster' in desc_lower:
        return "AI/AI工具"
    if 'regression' in desc_lower:
        return "AI/AI工具"
    if 'optimiz' in desc_lower and 'tool' in desc_lower:
        return "AI/AI工具"
    if 'optimiz' in name_lower:
        return "AI/AI工具"
    if 'reinforce' in desc_lower:
        return "AI/AI工具"
    if 'supervis' in desc_lower:
        return "AI/AI工具"
    if 'unsupervis' in desc_lower:
        return "AI/AI工具"
    if 'semi-supervis' in desc_lower:
        return "AI/AI工具"
    if 'transfer' in desc_lower and 'learning' in desc_lower:
        return "AI/AI工具"
    if 'generative' in desc_lower:
        return "AI/AI工具"
    if 'gan' in desc_lower:
        return "AI/AI工具"
    if 'transformer' in desc_lower:
        return "AI/AI工具"
    if 'attention' in desc_lower:
        return "AI/AI工具"
    if 'bert' in desc_lower:
        return "AI/AI工具"
    if 'gpt' in desc_lower:
        return "AI/AI工具"
    if 'llm' in desc_lower:
        return "AI/AI工具"
    if 'nlp' in desc_lower:
        return "AI/AI工具"
    if 'cv' in desc_lower and 'tool' in desc_lower:
        return "AI/AI工具"
    if 'cv' in name_lower:
        return "AI/AI工具"
    if 'ocr' in desc_lower:
        return "AI/AI工具"
    if 'speech' in desc_lower:
        return "AI/AI工具"
    if 'voice' in desc_lower:
        return "AI/AI工具"
    if 'text' in desc_lower and 'tool' in desc_lower:
        return "AI/AI工具"
    if 'text' in name_lower:
        return "AI/AI工具"
    if 'sentiment' in desc_lower:
        return "AI/AI工具"
    if 'topic' in desc_lower:
        return "AI/AI工具"
    if 'entity' in desc_lower:
        return "AI/AI工具"
    if 'nlp' in desc_lower and 'tool' in desc_lower:
        return "AI/AI工具"
    
    # Final fallback
    return "其他/综合工具"

# Count categories
categories = {}
for line in tools:
    line = line.strip()
    if not line:
        continue
    parts = line.split('|', 5)
    if len(parts) < 5:
        continue
    name = parts[0]
    desc = parts[3]
    
    cat = get_v21_category(name, desc)
    
    if cat not in categories:
        categories[cat] = 0
    categories[cat] += 1

# Print results
print(f"\nTotal categories: {len(categories)}")
print("\n=== Categories with >50 tools ===")
large_cats = [(cat, count) for cat, count in categories.items() if count >= 50]
large_cats.sort(key=lambda x: x[1], reverse=True)
for cat, count in large_cats:
    print(f"  {cat}: {count}")

print(f"\n=== Total large categories (>50): {len(large_cats)} ===")
print(f"=== '其他/综合工具': {categories.get('其他/综合工具', 0)} ===")

# Also show categories 30-50
print("\n=== Categories 30-50 tools ===")
for cat, count in sorted(categories.items(), key=lambda x: -x[1]):
    if 30 <= count < 50:
        print(f"  {cat}: {count}")