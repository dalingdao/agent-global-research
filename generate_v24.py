#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V24: Push last 3 categories over 50 with PRECISE patterns only
Base: V23 (97 large cats). Targets: 旅游/导航(49→50+), 安全/SOC(47→50+), 媒体/多媒体(37→50+)
Key: Only capture from small (<30) categories, use very specific keywords
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
with open(r"D:\testa\generate_v23.py", "r", encoding="utf-8") as f:
    v23_code = f.read()

v17_func_code = v17_code[v17_code.find("def get_v17_category"):v17_code.rfind("\n# Count categories")]
v18_func_code = v18_code[v18_code.find("def get_v18_category"):v18_code.rfind("\n# Count categories")]
v19_func_code = v19_code[v19_code.find("def get_v19_category"):v19_code.rfind("\n# Count categories")]
v20_func_code = v20_code[v20_code.find("def get_v20_category"):v20_code.rfind("\n# Count categories")]
v21_func_code = v21_code[v21_code.find("def get_v21_category"):v21_code.rfind("\n# Count categories")]
v22_func_code = v22_code[v22_code.find("def get_v22_category"):v22_code.rfind("\n# Count categories")]
v23_func_code = v23_code[v23_code.find("def get_v23_category"):v23_code.rfind("\n# Count categories")]

scope = {}
exec(v17_func_code + "\n" + v18_func_code + "\n", scope)
exec(v19_func_code, scope)
exec(v20_func_code, scope)
exec(v21_func_code, scope)
exec(v22_func_code, scope)
exec(v23_func_code, scope)
get_v23_category = scope['get_v23_category']

# Small categories (<30 tools in V23) that can safely donate tools
SMALL_CATS = {
    "硬件/单片机": 29, "AI模型/训练模型": 28, "文档/文档工具": 27,
    "可视化/可视化工具": 27, "媒体/图形": 27, "开源/开源工具": 27,
    "教育/论文": 26, "硬件/电路": 26, "音乐/制作": 26, "机器人/工业": 25,
    "项目管理/项目工具": 25, "桌面/桌面工具": 25, "通信/平台": 25,
    "数据/数据集": 24, "工程/工程": 24, "AI/RAG/向量": 24,
    "分析/商业分析": 24, "教育/教程": 24, "教育/教学": 24,
    "生产力/协作": 23, "系统/优化": 23, "工具/系统集合": 23,
    "浏览器/其他": 23, "平台/层": 23, "系统/OS": 23,
    "API/API工具": 23, "编程语言/编程语言工具": 23,
    "数据库/管理工具": 22, "金融/交易": 21, "网络/代理": 21,
    "系统/Shell": 21, "日志/日志工具": 21, "工具/轻量工具": 21,
    "办公/文档": 20,
}

def get_v24_category(name, desc):
    name_lower = name.lower()
    desc_lower = desc.lower()
    
    # First try V23 categorization
    cat = get_v23_category(name, desc)
    
    if cat != "其他/综合工具":
        # Only push tools FROM small categories (<30) TO the 3 target categories
        if cat in SMALL_CATS:
            # === Push 旅游/导航 (49→50+, need 1) ===
            # Very specific: tools from small categories that are clearly about navigation/travel
            if (
                'gps' in name_lower or 'gps' in desc_lower
                or 'navigat' in name_lower or 'navigat' in desc_lower and 'tool' in desc_lower
                or 'route' in name_lower or 'route' in desc_lower and 'tool' in desc_lower
                or 'waypoint' in desc_lower or 'waypoint' in name_lower
                or 'geofenc' in desc_lower or 'geofenc' in name_lower
                or 'geocod' in desc_lower or 'geocod' in name_lower
                or 'geoip' in desc_lower or 'geoip' in name_lower
                or 'qgis' in desc_lower or 'qgis' in name_lower
                or 'postgis' in desc_lower
                or 'shapefile' in desc_lower
                or 'geojson' in desc_lower
                or 'topojson' in desc_lower
                or 'kml' in desc_lower
                or 'atlas' in desc_lower or 'atlas' in name_lower
                or 'globe' in name_lower
                or 'geospatial' in desc_lower
                or 'spatial' in desc_lower and 'geo' in desc_lower
                or 'lidar' in desc_lower or 'lidar' in name_lower
                or 'radar' in name_lower
                or 'sonar' in name_lower
                or 'mapbox' in desc_lower or 'mapbox' in name_lower
                or 'openstreetmap' in desc_lower
                or 'geograph' in desc_lower
                or 'cartograph' in desc_lower
                or 'topograph' in desc_lower
                or 'aerial' in desc_lower
                or 'satellite' in name_lower
                or 'satellite' in desc_lower and 'tool' in desc_lower
                or 'remote' in desc_lower and 'sensor' in desc_lower
                or 'air' in desc_lower and 'photo' in desc_lower
                or 'thermal' in desc_lower and 'sensor' in desc_lower
                or 'multispectral' in desc_lower
                or 'hyperspectral' in desc_lower
                or 'projection' in name_lower
                or 'datum' in name_lower
                or 'reproject' in name_lower
                or 'zoom' in name_lower
                or 'pan' in name_lower and 'map' in desc_lower
                or 'drag' in name_lower and 'map' in desc_lower
                or 'tooltip' in name_lower
                or 'infowindow' in name_lower
                or 'popup' in name_lower and 'map' in desc_lower
                or 'heatmap' in desc_lower
                or 'choropleth' in desc_lower
                or 'compass' in name_lower
                or 'bearing' in name_lower or 'bearing' in desc_lower
                or 'azimuth' in name_lower or 'azimuth' in desc_lower
            ):
                return "旅游/导航"
            
            # === Push 安全/SOC (47→50+, need 3) ===
            # Very specific: tools from small categories that are clearly about SOC
            if (
                'soc' in name_lower
                or 'soc2' in desc_lower or 'soc 2' in desc_lower
                or 'soc3' in desc_lower or 'soc 3' in desc_lower
                or 'security operations' in desc_lower
                or 'security operation center' in desc_lower
                or 'soc analyst' in desc_lower
                or 'soc analysis' in desc_lower
                or 'soc analytics' in desc_lower
                or 'soc automation' in desc_lower
                or 'soc orchestration' in desc_lower
                or 'soc platform' in desc_lower
                or 'soc tool' in desc_lower or 'soc tools' in desc_lower
                or 'siem' in desc_lower or 'siem' in name_lower
                or 'splunk' in desc_lower or 'splunk' in name_lower
                or 'elastic' in desc_lower and 'security' in desc_lower
                or 'elasticsearch' in desc_lower and 'security' in desc_lower
                or 'sentinel' in desc_lower and 'security' in desc_lower
                or 'defender' in desc_lower and 'security' in desc_lower
                or 'sec' in desc_lower and 'ops' in desc_lower
                or 'sec' in name_lower and 'ops' in name_lower
            ):
                return "安全/SOC"
            
            # === Push 媒体/多媒体 (37→50+, need 13) ===
            # Very specific: tools from small categories that are clearly about media/multimedia
            if (
                'multimedia' in desc_lower or 'multimedia' in name_lower
                or 'media' in name_lower and 'tool' in desc_lower
                or 'media' in desc_lower and 'tool' in desc_lower
                or 'video' in name_lower and 'tool' in desc_lower
                or 'video' in desc_lower and 'tool' in desc_lower
                or 'audio' in name_lower and 'tool' in desc_lower
                or 'audio' in desc_lower and 'tool' in desc_lower
                or 'video' in desc_lower and 'editor' in desc_lower
                or 'video' in name_lower and 'editor' in name_lower
                or 'audio' in desc_lower and 'editor' in desc_lower
                or 'audio' in name_lower and 'editor' in name_lower
                or 'image' in desc_lower and 'editor' in desc_lower
                or 'image' in name_lower and 'editor' in name_lower
                or 'media' in desc_lower and 'editor' in desc_lower
                or 'media' in name_lower and 'editor' in name_lower
                or 'video' in desc_lower and 'player' in desc_lower
                or 'video' in name_lower and 'player' in name_lower
                or 'audio' in desc_lower and 'player' in desc_lower
                or 'audio' in name_lower and 'player' in name_lower
                or 'video' in desc_lower and 'encoder' in desc_lower
                or 'video' in name_lower and 'encoder' in name_lower
                or 'audio' in desc_lower and 'encoder' in desc_lower
                or 'audio' in name_lower and 'encoder' in name_lower
                or 'video' in desc_lower and 'decoder' in desc_lower
                or 'video' in name_lower and 'decoder' in name_lower
                or 'audio' in desc_lower and 'decoder' in desc_lower
                or 'audio' in name_lower and 'decoder' in name_lower
                or 'video' in desc_lower and 'converter' in desc_lower
                or 'video' in name_lower and 'converter' in name_lower
                or 'audio' in desc_lower and 'converter' in desc_lower
                or 'audio' in name_lower and 'converter' in name_lower
                or 'video' in desc_lower and 'compressor' in desc_lower
                or 'video' in name_lower and 'compressor' in name_lower
                or 'audio' in desc_lower and 'compressor' in desc_lower
                or 'audio' in name_lower and 'compressor' in name_lower
            ):
                return "媒体/多媒体"
            
            return cat
        
        return cat
    
    # ===== V24 NEW: Handle remaining 其他/综合工具 =====
    # For the remaining 1 tool in 其他, try to categorize it
    
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
    
    cat = get_v24_category(name, desc)
    
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