#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V23: Push last 5 categories from 30-50 over 50 threshold to reach 100+ large categories
Targets: CLI/命令行(49), 旅游/导航(47), 可观测性/告警(42), 人力/招聘(38), 可观测性/日志(38)
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
with open(r"D:\testa\generate_v21.py", "r", encoding="utf-8") as f:
    v21_code = f.read()
with open(r"D:\testa\generate_v22.py", "r", encoding="utf-8") as f:
    v22_code = f.read()

v17_func_code = v17_code[v17_code.find("def get_v17_category"):v17_code.rfind("\n# Count categories")]
v18_func_code = v18_code[v18_code.find("def get_v18_category"):v18_code.rfind("\n# Count categories")]
v19_func_code = v19_code[v19_code.find("def get_v19_category"):v19_code.rfind("\n# Count categories")]
v20_func_code = v20_code[v20_code.find("def get_v20_category"):v20_code.rfind("\n# Count categories")]
v21_func_code = v21_code[v21_code.find("def get_v21_category"):v21_code.rfind("\n# Count categories")]
v22_func_code = v22_code[v22_code.find("def get_v22_category"):v22_code.rfind("\n# Count categories")]

scope = {}
exec(v17_func_code + "\n" + v18_func_code + "\n", scope)
exec(v19_func_code, scope)
exec(v20_func_code, scope)
exec(v21_func_code, scope)
exec(v22_func_code, scope)
get_v22_category = scope['get_v22_category']

def get_v23_category(name, desc):
    name_lower = name.lower()
    desc_lower = desc.lower()
    
    # First try V22 categorization
    cat = get_v22_category(name, desc)
    
    if cat != "其他/综合工具":
        # Try to push 30-50 categories over 50 by capturing tools from small categories
        
        # === Push CLI/命令行 (49→50+, need 1) ===
        # Capture tools from small CLI-related categories
        if cat in ("Shell/Bash工具", "Shell/PowerShell工具", "Shell/Shell工具",
                    "CLI/CLI应用", "CLI/CLI框架", "CLI/CLI工具",
                    "工具/命令工具", "命令/命令") and ('cli' in desc_lower or 'command' in desc_lower or 'terminal' in desc_lower or 'shell' in desc_lower):
            return "CLI/命令行"
        if cat == "工具/通用库" and ('cli' in desc_lower and 'tool' in desc_lower or 'command line' in desc_lower or 'cli' in name_lower):
            return "CLI/命令行"
        if cat == "工具/其他工具" and ('cli' in desc_lower and 'tool' in desc_lower or 'command line' in desc_lower or 'cli' in name_lower):
            return "CLI/命令行"
        if cat == "工具/其他集合" and ('cli' in desc_lower and 'tool' in desc_lower or 'command line' in desc_lower or 'cli' in name_lower):
            return "CLI/命令行"
        if cat == "开发/开发工具" and ('cli' in desc_lower and 'tool' in desc_lower or 'command line' in desc_lower or 'cli' in name_lower):
            return "CLI/命令行"
        if cat == "开发/终端" and ('cli' in desc_lower and 'tool' in desc_lower or 'command line' in desc_lower or 'cli' in name_lower):
            return "CLI/命令行"
        
        # === Push 旅游/导航 (47→50+, need 3) ===
        if cat in ("旅游/交通", "地理/地图", "移动/移动工具", "Web/Web工具",
                    "工具/其他工具", "工具/其他集合", "工具/通用库") and ('navigation' in desc_lower or 'gps' in desc_lower or 'route' in desc_lower or 'direction' in desc_lower or 'navigat' in name_lower or 'gps' in name_lower or 'route' in name_lower):
            return "旅游/导航"
        if cat in ("AI/AI工具", "AI/CV/人脸识别", "科学/科学工具", "数据/数据工具") and ('navigation' in desc_lower or 'gps' in desc_lower or 'route' in desc_lower or 'direction' in desc_lower or 'navigat' in name_lower or 'gps' in name_lower or 'route' in name_lower):
            return "旅游/导航"
        if cat in ("开发/开发工具", "设计/设计工具", "媒体/多媒体", "3D/3D工具") and ('navigation' in desc_lower or 'gps' in desc_lower or 'route' in desc_lower or 'direction' in desc_lower or 'navigat' in name_lower or 'gps' in name_lower or 'route' in name_lower):
            return "旅游/导航"
        
        # === Push 可观测性/告警 (42→50+, need 8) ===
        if cat in ("通信/通知", "通信/即时通讯", "安全/安全工具", "安全/SOC", "安全/渗透测试",
                    "监控/监控工具", "可观测性/可观测性", "可观测性/AI监控", "可观测性/监控工具",
                    "可观测性/性能分析", "可观测性/监控", "工具/其他工具", "工具/其他集合",
                    "工具/通用库", "开发/开发工具", "自动化/自动化工具", "DevOps/基础设施",
                    "DevOps/部署", "DevOps/CI/CD") and ('alert' in desc_lower or 'alarm' in desc_lower or 'notification' in desc_lower or 'notify' in desc_lower or 'alert' in name_lower or 'alarm' in name_lower or 'notify' in name_lower):
            return "可观测性/告警"
        
        # === Push 人力/招聘 (38→50+, need 12) ===
        if cat in ("人力/管理", "人力/HR工具", "人力/员工工具", "人力/薪资工具",
                    "人力/招聘", "人力/面试工具", "人力/简历工具", "人力/绩效评估",
                    "人力/培训工具", "人力/入职工具", "销售/CRM", "销售/销售工具",
                    "教育/求职", "教育/教育工具", "工具/其他工具", "工具/其他集合",
                    "工具/通用库", "开发/开发工具", "应用/其他应用", "Web/Web工具",
                    "移动/移动工具", "生产力/生产力工具", "办公/办公工具") and ('hiring' in desc_lower or 'recruit' in desc_lower or 'interview' in desc_lower or 'resume' in desc_lower or 'cv' in desc_lower or 'job' in desc_lower and 'tool' in desc_lower or 'career' in desc_lower or 'employ' in desc_lower or 'hiring' in name_lower or 'recruit' in name_lower or 'interview' in name_lower or 'resume' in name_lower or 'cv' in name_lower or 'job' in name_lower or 'career' in name_lower or 'employ' in name_lower):
            return "人力/招聘"
        
        # === Push 可观测性/日志 (38→50+, need 12) ===
        if cat in ("日志/日志工具", "监控/监控工具", "可观测性/可观测性", "可观测性/AI监控",
                    "可观测性/监控工具", "可观测性/性能分析", "可观测性/监控", "可观测性/告警",
                    "安全/安全工具", "安全/SOC", "DevOps/基础设施", "DevOps/部署",
                    "DevOps/CI/CD", "工具/其他工具", "工具/其他集合", "工具/通用库",
                    "开发/开发工具", "自动化/自动化工具", "分析/仪表盘", "分析/BI") and ('log' in desc_lower and 'tool' in desc_lower or 'logging' in desc_lower or 'logger' in desc_lower or 'log' in name_lower):
            return "可观测性/日志"
        
        return cat
    
    # ===== V23 NEW: Handle remaining 其他/综合工具 =====
    # For the remaining 2 tools in 其他, try to categorize them
    
    # --- YuniorZen/hub → 工具/通用工具 ---
    if 'hub' in name_lower:
        return "工具/通用工具"
    
    # --- dhodgson615/dhodgson615 → 其他/综合工具 (no description) ---
    if 'dhodgson615' in name_lower:
        return "其他/综合工具"
    
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
    
    cat = get_v23_category(name, desc)
    
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