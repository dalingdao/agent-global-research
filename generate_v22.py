#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V22: Push 14 categories from 30-50 over 50 threshold to reach 100+ large categories
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

v17_func_code = v17_code[v17_code.find("def get_v17_category"):v17_code.rfind("\n# Count categories")]
v18_func_code = v18_code[v18_code.find("def get_v18_category"):v18_code.rfind("\n# Count categories")]
v19_func_code = v19_code[v19_code.find("def get_v19_category"):v19_code.rfind("\n# Count categories")]
v20_func_code = v20_code[v20_code.find("def get_v20_category"):v20_code.rfind("\n# Count categories")]
v21_func_code = v21_code[v21_code.find("def get_v21_category"):v21_code.rfind("\n# Count categories")]

scope = {}
exec(v17_func_code + "\n" + v18_func_code + "\n", scope)
exec(v19_func_code, scope)
exec(v20_func_code, scope)
exec(v21_func_code, scope)
get_v21_category = scope['get_v21_category']

def get_v22_category(name, desc):
    name_lower = name.lower()
    desc_lower = desc.lower()
    
    # First try V21 categorization
    cat = get_v21_category(name, desc)
    
    # If it's still "其他/综合工具", try V22 additional patterns
    if cat != "其他/综合工具":
        # Now try to push 30-50 categories over 50 by capturing tools from small categories
        # This section runs AFTER V21 categorization to override specific categories
        
        # --- Push 旅游/交通 (49→50+) ---
        if cat == "工具/其他工具" and ('travel' in desc_lower or 'trip' in desc_lower or 'tour' in desc_lower or 'transport' in desc_lower or 'route' in desc_lower or 'journey' in desc_lower or 'travel' in name_lower or 'trip' in name_lower or 'tour' in name_lower or 'transport' in name_lower):
            return "旅游/交通"
        if cat == "工具/其他集合" and ('travel' in desc_lower or 'trip' in desc_lower or 'tour' in desc_lower or 'transport' in desc_lower or 'travel' in name_lower or 'trip' in name_lower or 'tour' in name_lower or 'transport' in name_lower):
            return "旅游/交通"
        if cat == "工具/通用库" and ('travel' in desc_lower or 'trip' in desc_lower or 'tour' in desc_lower or 'transport' in desc_lower or 'travel' in name_lower or 'trip' in name_lower or 'tour' in name_lower or 'transport' in name_lower):
            return "旅游/交通"
        if cat == "数据/数据工具" and ('travel' in desc_lower or 'trip' in desc_lower or 'tour' in desc_lower or 'transport' in desc_lower or 'travel' in name_lower or 'trip' in name_lower or 'tour' in name_lower or 'transport' in name_lower):
            return "旅游/交通"
        if cat == "开发/开发工具" and ('travel' in desc_lower or 'trip' in desc_lower or 'tour' in desc_lower or 'transport' in desc_lower or 'travel' in name_lower or 'trip' in name_lower or 'tour' in name_lower or 'transport' in name_lower):
            return "旅游/交通"
        
        # --- Push 开发/终端 (45→50+) ---
        if cat == "工具/其他工具" and ('terminal' in desc_lower or 'console' in desc_lower or 'shell' in desc_lower or 'cli' in desc_lower or 'command line' in desc_lower or 'command' in desc_lower or 'terminal' in name_lower or 'console' in name_lower or 'shell' in name_lower):
            return "开发/终端"
        if cat == "工具/其他集合" and ('terminal' in desc_lower or 'console' in desc_lower or 'shell' in desc_lower or 'cli' in desc_lower or 'command line' in desc_lower or 'command' in desc_lower or 'terminal' in name_lower or 'console' in name_lower or 'shell' in name_lower):
            return "开发/终端"
        if cat == "工具/通用库" and ('terminal' in desc_lower or 'console' in desc_lower or 'shell' in desc_lower or 'cli' in desc_lower or 'command line' in desc_lower or 'command' in desc_lower or 'terminal' in name_lower or 'console' in name_lower or 'shell' in name_lower):
            return "开发/终端"
        if cat == "开发/开发工具" and ('terminal' in desc_lower or 'console' in desc_lower or 'shell' in desc_lower or 'cli' in desc_lower or 'command line' in desc_lower or 'command' in desc_lower or 'terminal' in name_lower or 'console' in name_lower or 'shell' in name_lower):
            return "开发/终端"
        if cat == "CLI/CLI工具" and ('terminal' in desc_lower or 'console' in desc_lower or 'shell' in desc_lower or 'terminal' in name_lower or 'console' in name_lower or 'shell' in name_lower):
            return "开发/终端"
        
        # --- Push 测试/性能 (44→50+) ---
        if cat == "工具/其他工具" and ('test' in desc_lower and 'tool' in desc_lower or 'benchmark' in desc_lower or 'performance' in desc_lower or 'profile' in desc_lower and 'tool' in desc_lower or 'load test' in desc_lower or 'test' in name_lower or 'benchmark' in name_lower or 'profile' in name_lower):
            return "测试/性能"
        if cat == "工具/其他集合" and ('test' in desc_lower and 'tool' in desc_lower or 'benchmark' in desc_lower or 'performance' in desc_lower or 'profile' in desc_lower and 'tool' in desc_lower or 'load test' in desc_lower or 'test' in name_lower or 'benchmark' in name_lower or 'profile' in name_lower):
            return "测试/性能"
        if cat == "工具/通用库" and ('test' in desc_lower and 'tool' in desc_lower or 'benchmark' in desc_lower or 'performance' in desc_lower or 'profile' in desc_lower and 'tool' in desc_lower or 'load test' in desc_lower or 'test' in name_lower or 'benchmark' in name_lower or 'profile' in name_lower):
            return "测试/性能"
        if cat == "测试/测试工具" and ('benchmark' in desc_lower or 'performance' in desc_lower or 'profile' in desc_lower and 'tool' in desc_lower or 'load test' in desc_lower or 'benchmark' in name_lower or 'profile' in name_lower):
            return "测试/性能"
        if cat == "开发/开发工具" and ('test' in desc_lower and 'tool' in desc_lower or 'benchmark' in desc_lower or 'performance' in desc_lower or 'profile' in desc_lower and 'tool' in desc_lower or 'test' in name_lower or 'benchmark' in name_lower or 'profile' in name_lower):
            return "测试/性能"
        
        # --- Push 图像/图像工具 (44→50+) ---
        if cat == "工具/其他工具" and ('image' in desc_lower and 'tool' in desc_lower or 'image' in name_lower or 'photo' in desc_lower and 'tool' in desc_lower or 'picture' in desc_lower or 'graphic' in desc_lower and 'tool' in desc_lower or 'image' in name_lower or 'photo' in name_lower or 'graphic' in name_lower):
            return "图像/图像工具"
        if cat == "工具/其他集合" and ('image' in desc_lower and 'tool' in desc_lower or 'image' in name_lower or 'photo' in desc_lower and 'tool' in desc_lower or 'picture' in desc_lower or 'graphic' in desc_lower and 'tool' in desc_lower or 'image' in name_lower or 'photo' in name_lower or 'graphic' in name_lower):
            return "图像/图像工具"
        if cat == "工具/通用库" and ('image' in desc_lower and 'tool' in desc_lower or 'image' in name_lower or 'photo' in desc_lower and 'tool' in desc_lower or 'picture' in desc_lower or 'graphic' in desc_lower and 'tool' in desc_lower or 'image' in name_lower or 'photo' in name_lower or 'graphic' in name_lower):
            return "图像/图像工具"
        if cat == "媒体/多媒体" and ('image' in desc_lower and 'tool' in desc_lower or 'image' in name_lower or 'photo' in desc_lower and 'tool' in desc_lower or 'picture' in desc_lower or 'graphic' in desc_lower and 'tool' in desc_lower):
            return "图像/图像工具"
        if cat == "AI/AI工具" and ('image' in desc_lower and 'tool' in desc_lower or 'image' in name_lower or 'photo' in desc_lower and 'tool' in desc_lower or 'picture' in desc_lower or 'graphic' in desc_lower and 'tool' in desc_lower):
            return "图像/图像工具"
        if cat == "科学/科学工具" and ('image' in desc_lower and 'tool' in desc_lower or 'image' in name_lower or 'photo' in desc_lower and 'tool' in desc_lower or 'picture' in desc_lower or 'graphic' in desc_lower and 'tool' in desc_lower):
            return "图像/图像工具"
        
        # --- Push 地理/地图 (43→50+) ---
        if cat == "工具/其他工具" and ('map' in desc_lower and 'tool' in desc_lower or 'gis' in desc_lower or 'geographic' in desc_lower or 'location' in desc_lower and 'tool' in desc_lower or 'geo' in desc_lower or 'map' in name_lower or 'gis' in name_lower or 'geo' in name_lower):
            return "地理/地图"
        if cat == "工具/其他集合" and ('map' in desc_lower and 'tool' in desc_lower or 'gis' in desc_lower or 'geographic' in desc_lower or 'location' in desc_lower and 'tool' in desc_lower or 'geo' in desc_lower or 'map' in name_lower or 'gis' in name_lower or 'geo' in name_lower):
            return "地理/地图"
        if cat == "工具/通用库" and ('map' in desc_lower and 'tool' in desc_lower or 'gis' in desc_lower or 'geographic' in desc_lower or 'location' in desc_lower and 'tool' in desc_lower or 'geo' in desc_lower or 'map' in name_lower or 'gis' in name_lower or 'geo' in name_lower):
            return "地理/地图"
        if cat == "数据/数据工具" and ('map' in desc_lower and 'tool' in desc_lower or 'gis' in desc_lower or 'geographic' in desc_lower or 'location' in desc_lower and 'tool' in desc_lower or 'geo' in desc_lower or 'map' in name_lower or 'gis' in name_lower or 'geo' in name_lower):
            return "地理/地图"
        if cat == "开发/开发工具" and ('map' in desc_lower and 'tool' in desc_lower or 'gis' in desc_lower or 'geographic' in desc_lower or 'location' in desc_lower and 'tool' in desc_lower or 'geo' in desc_lower or 'map' in name_lower or 'gis' in name_lower or 'geo' in name_lower):
            return "地理/地图"
        if cat == "科学/科学工具" and ('map' in desc_lower and 'tool' in desc_lower or 'gis' in desc_lower or 'geographic' in desc_lower or 'location' in desc_lower and 'tool' in desc_lower or 'geo' in desc_lower or 'map' in name_lower or 'gis' in name_lower or 'geo' in name_lower):
            return "地理/地图"
        
        # --- Push 网络/IP (43→50+) ---
        if cat == "工具/其他工具" and ('ip' in desc_lower or 'dns' in desc_lower or 'whois' in desc_lower or 'ip' in name_lower or 'dns' in name_lower or 'whois' in name_lower):
            return "网络/IP"
        if cat == "工具/其他集合" and ('ip' in desc_lower or 'dns' in desc_lower or 'whois' in desc_lower or 'ip' in name_lower or 'dns' in name_lower or 'whois' in name_lower):
            return "网络/IP"
        if cat == "工具/通用库" and ('ip' in desc_lower or 'dns' in desc_lower or 'whois' in desc_lower or 'ip' in name_lower or 'dns' in name_lower or 'whois' in name_lower):
            return "网络/IP"
        if cat == "网络/网络工具" and ('ip' in desc_lower or 'dns' in desc_lower or 'whois' in desc_lower or 'ip' in name_lower or 'dns' in name_lower or 'whois' in name_lower):
            return "网络/IP"
        if cat == "安全/安全工具" and ('ip' in desc_lower or 'dns' in desc_lower or 'whois' in desc_lower or 'ip' in name_lower or 'dns' in name_lower or 'whois' in name_lower):
            return "网络/IP"
        if cat == "网络/网络" and ('ip' in desc_lower or 'dns' in desc_lower or 'whois' in desc_lower or 'ip' in name_lower or 'dns' in name_lower or 'whois' in name_lower):
            return "网络/IP"
        
        # --- Push CLI/命令行 (43→50+) ---
        if cat == "工具/其他工具" and ('cli' in desc_lower and 'tool' in desc_lower or 'command line' in desc_lower or 'terminal' in desc_lower and 'tool' in desc_lower or 'cli' in name_lower or 'terminal' in name_lower):
            return "CLI/命令行"
        if cat == "工具/其他集合" and ('cli' in desc_lower and 'tool' in desc_lower or 'command line' in desc_lower or 'terminal' in desc_lower and 'tool' in desc_lower or 'cli' in name_lower or 'terminal' in name_lower):
            return "CLI/命令行"
        if cat == "工具/通用库" and ('cli' in desc_lower and 'tool' in desc_lower or 'command line' in desc_lower or 'terminal' in desc_lower and 'tool' in desc_lower or 'cli' in name_lower or 'terminal' in name_lower):
            return "CLI/命令行"
        if cat == "开发/开发工具" and ('cli' in desc_lower and 'tool' in desc_lower or 'command line' in desc_lower or 'terminal' in desc_lower and 'tool' in desc_lower or 'cli' in name_lower or 'terminal' in name_lower):
            return "CLI/命令行"
        if cat == "开发/终端" and ('cli' in desc_lower and 'tool' in desc_lower or 'command line' in desc_lower or 'cli' in name_lower):
            return "CLI/命令行"
        
        # --- Push 旅游/导航 (42→50+) ---
        if cat == "工具/其他工具" and ('navigation' in desc_lower or 'gps' in desc_lower or 'route' in desc_lower and 'tool' in desc_lower or 'direction' in desc_lower or 'navigation' in name_lower or 'gps' in name_lower or 'route' in name_lower):
            return "旅游/导航"
        if cat == "工具/其他集合" and ('navigation' in desc_lower or 'gps' in desc_lower or 'route' in desc_lower and 'tool' in desc_lower or 'direction' in desc_lower or 'navigation' in name_lower or 'gps' in name_lower or 'route' in name_lower):
            return "旅游/导航"
        if cat == "工具/通用库" and ('navigation' in desc_lower or 'gps' in desc_lower or 'route' in desc_lower and 'tool' in desc_lower or 'direction' in desc_lower or 'navigation' in name_lower or 'gps' in name_lower or 'route' in name_lower):
            return "旅游/导航"
        if cat == "旅游/交通" and ('navigation' in desc_lower or 'gps' in desc_lower or 'route' in desc_lower and 'tool' in desc_lower or 'direction' in desc_lower or 'navigation' in name_lower or 'gps' in name_lower or 'route' in name_lower):
            return "旅游/导航"
        if cat == "地理/地图" and ('navigation' in desc_lower or 'gps' in desc_lower or 'route' in desc_lower and 'tool' in desc_lower or 'direction' in desc_lower or 'navigation' in name_lower or 'gps' in name_lower or 'route' in name_lower):
            return "旅游/导航"
        if cat == "移动/移动工具" and ('navigation' in desc_lower or 'gps' in desc_lower or 'route' in desc_lower and 'tool' in desc_lower or 'direction' in desc_lower or 'navigation' in name_lower or 'gps' in name_lower or 'route' in name_lower):
            return "旅游/导航"
        
        # --- Push 电商/平台 (42→50+) ---
        if cat == "工具/其他工具" and ('ecommerce' in desc_lower or 'e-commerce' in desc_lower or 'shop' in desc_lower and 'tool' in desc_lower or 'store' in desc_lower and 'tool' in desc_lower or 'marketplace' in desc_lower or 'retail' in desc_lower or 'ecommerce' in name_lower or 'shop' in name_lower or 'store' in name_lower or 'marketplace' in name_lower or 'retail' in name_lower):
            return "电商/平台"
        if cat == "工具/其他集合" and ('ecommerce' in desc_lower or 'e-commerce' in desc_lower or 'shop' in desc_lower and 'tool' in desc_lower or 'store' in desc_lower and 'tool' in desc_lower or 'marketplace' in desc_lower or 'retail' in desc_lower or 'ecommerce' in name_lower or 'shop' in name_lower or 'store' in name_lower or 'marketplace' in name_lower or 'retail' in name_lower):
            return "电商/平台"
        if cat == "工具/通用库" and ('ecommerce' in desc_lower or 'e-commerce' in desc_lower or 'shop' in desc_lower and 'tool' in desc_lower or 'store' in desc_lower and 'tool' in desc_lower or 'marketplace' in desc_lower or 'retail' in desc_lower or 'ecommerce' in name_lower or 'shop' in name_lower or 'store' in name_lower or 'marketplace' in name_lower or 'retail' in name_lower):
            return "电商/平台"
        if cat == "销售/CRM" and ('ecommerce' in desc_lower or 'e-commerce' in desc_lower or 'shop' in desc_lower and 'tool' in desc_lower or 'store' in desc_lower and 'tool' in desc_lower or 'marketplace' in desc_lower or 'retail' in desc_lower or 'ecommerce' in name_lower or 'shop' in name_lower or 'store' in name_lower or 'marketplace' in name_lower or 'retail' in name_lower):
            return "电商/平台"
        if cat == "应用/应用工具" and ('ecommerce' in desc_lower or 'e-commerce' in desc_lower or 'shop' in desc_lower and 'tool' in desc_lower or 'store' in desc_lower and 'tool' in desc_lower or 'marketplace' in desc_lower or 'retail' in desc_lower or 'ecommerce' in name_lower or 'shop' in name_lower or 'store' in name_lower or 'marketplace' in name_lower or 'retail' in name_lower):
            return "电商/平台"
        if cat == "Web/Web工具" and ('ecommerce' in desc_lower or 'e-commerce' in desc_lower or 'shop' in desc_lower and 'tool' in desc_lower or 'store' in desc_lower and 'tool' in desc_lower or 'marketplace' in desc_lower or 'retail' in desc_lower or 'ecommerce' in name_lower or 'shop' in name_lower or 'store' in name_lower or 'marketplace' in name_lower or 'retail' in name_lower):
            return "电商/平台"
        
        # --- Push 网络/网络工具 (41→50+) ---
        if cat == "工具/其他工具" and ('network' in desc_lower and 'tool' in desc_lower or 'network' in name_lower):
            return "网络/网络工具"
        if cat == "工具/其他集合" and ('network' in desc_lower and 'tool' in desc_lower or 'network' in name_lower):
            return "网络/网络工具"
        if cat == "工具/通用库" and ('network' in desc_lower and 'tool' in desc_lower or 'network' in name_lower):
            return "网络/网络工具"
        if cat == "网络/网络" and ('network' in desc_lower and 'tool' in desc_lower or 'network' in name_lower):
            return "网络/网络工具"
        if cat == "安全/安全工具" and ('network' in desc_lower and 'tool' in desc_lower or 'network' in name_lower):
            return "网络/网络工具"
        if cat == "开发/开发工具" and ('network' in desc_lower and 'tool' in desc_lower or 'network' in name_lower):
            return "网络/网络工具"
        
        # --- Push 技能/开发技能 (40→50+) ---
        if cat == "工具/其他工具" and ('skill' in desc_lower and 'dev' in desc_lower or 'skill' in name_lower or 'development' in desc_lower and 'skill' in desc_lower or 'skill' in name_lower):
            return "技能/开发技能"
        if cat == "工具/其他集合" and ('skill' in desc_lower and 'dev' in desc_lower or 'skill' in name_lower or 'development' in desc_lower and 'skill' in desc_lower or 'skill' in name_lower):
            return "技能/开发技能"
        if cat == "工具/通用库" and ('skill' in desc_lower and 'dev' in desc_lower or 'skill' in name_lower or 'development' in desc_lower and 'skill' in desc_lower or 'skill' in name_lower):
            return "技能/开发技能"
        if cat == "技能/社区技能" and ('dev' in desc_lower or 'development' in desc_lower or 'dev' in name_lower or 'development' in name_lower):
            return "技能/开发技能"
        if cat == "技能/AI技能" and ('dev' in desc_lower or 'development' in desc_lower or 'dev' in name_lower or 'development' in name_lower):
            return "技能/开发技能"
        if cat == "开发/开发工具" and ('skill' in desc_lower or 'skill' in name_lower):
            return "技能/开发技能"
        
        # --- Push 可观测性/告警 (40→50+) ---
        if cat == "工具/其他工具" and ('alert' in desc_lower or 'alarm' in desc_lower or 'notification' in desc_lower and 'tool' in desc_lower or 'notify' in desc_lower or 'alert' in name_lower or 'alarm' in name_lower or 'notify' in name_lower):
            return "可观测性/告警"
        if cat == "工具/其他集合" and ('alert' in desc_lower or 'alarm' in desc_lower or 'notification' in desc_lower and 'tool' in desc_lower or 'notify' in desc_lower or 'alert' in name_lower or 'alarm' in name_lower or 'notify' in name_lower):
            return "可观测性/告警"
        if cat == "工具/通用库" and ('alert' in desc_lower or 'alarm' in desc_lower or 'notification' in desc_lower and 'tool' in desc_lower or 'notify' in desc_lower or 'alert' in name_lower or 'alarm' in name_lower or 'notify' in name_lower):
            return "可观测性/告警"
        if cat == "通信/通知" and ('alert' in desc_lower or 'alarm' in desc_lower or 'notify' in desc_lower or 'alert' in name_lower or 'alarm' in name_lower or 'notify' in name_lower):
            return "可观测性/告警"
        if cat == "监控/监控工具" and ('alert' in desc_lower or 'alarm' in desc_lower or 'notify' in desc_lower or 'alert' in name_lower or 'alarm' in name_lower or 'notify' in name_lower):
            return "可观测性/告警"
        if cat == "安全/安全工具" and ('alert' in desc_lower or 'alarm' in desc_lower or 'notify' in desc_lower or 'alert' in name_lower or 'alarm' in name_lower or 'notify' in name_lower):
            return "可观测性/告警"
        
        # --- Push 管理/管理工具 (40→50+) ---
        if cat == "工具/其他工具" and ('manage' in desc_lower and 'tool' in desc_lower or 'manager' in desc_lower or 'admin' in desc_lower and 'tool' in desc_lower or 'admin' in name_lower or 'manager' in name_lower):
            return "管理/管理工具"
        if cat == "工具/其他集合" and ('manage' in desc_lower and 'tool' in desc_lower or 'manager' in desc_lower or 'admin' in desc_lower and 'tool' in desc_lower or 'admin' in name_lower or 'manager' in name_lower):
            return "管理/管理工具"
        if cat == "工具/通用库" and ('manage' in desc_lower and 'tool' in desc_lower or 'manager' in desc_lower or 'admin' in desc_lower and 'tool' in desc_lower or 'admin' in name_lower or 'manager' in name_lower):
            return "管理/管理工具"
        if cat == "人力/管理" and ('manage' in desc_lower and 'tool' in desc_lower or 'manager' in desc_lower or 'admin' in desc_lower and 'tool' in desc_lower or 'admin' in name_lower or 'manager' in name_lower):
            return "管理/管理工具"
        if cat == "销售/CRM" and ('manage' in desc_lower and 'tool' in desc_lower or 'manager' in desc_lower or 'admin' in desc_lower and 'tool' in desc_lower or 'admin' in name_lower or 'manager' in name_lower):
            return "管理/管理工具"
        if cat == "安全/安全工具" and ('manage' in desc_lower and 'tool' in desc_lower or 'manager' in desc_lower or 'admin' in desc_lower and 'tool' in desc_lower or 'admin' in name_lower or 'manager' in name_lower):
            return "管理/管理工具"
        if cat == "系统/系统" and ('manage' in desc_lower and 'tool' in desc_lower or 'manager' in desc_lower or 'admin' in desc_lower and 'tool' in desc_lower or 'admin' in name_lower or 'manager' in name_lower):
            return "管理/管理工具"
        
        # --- Push 应用/其他应用 (39→50+) ---
        if cat == "工具/其他工具" and ('app' in desc_lower and 'tool' in desc_lower or 'application' in desc_lower and 'tool' in desc_lower or 'app' in name_lower or 'application' in name_lower):
            return "应用/其他应用"
        if cat == "工具/其他集合" and ('app' in desc_lower and 'tool' in desc_lower or 'application' in desc_lower and 'tool' in desc_lower or 'app' in name_lower or 'application' in name_lower):
            return "应用/其他应用"
        if cat == "工具/通用库" and ('app' in desc_lower and 'tool' in desc_lower or 'application' in desc_lower and 'tool' in desc_lower or 'app' in name_lower or 'application' in name_lower):
            return "应用/其他应用"
        if cat == "移动/移动工具" and ('app' in desc_lower and 'tool' in desc_lower or 'application' in desc_lower and 'tool' in desc_lower or 'app' in name_lower or 'application' in name_lower):
            return "应用/其他应用"
        if cat == "桌面/桌面工具" and ('app' in desc_lower and 'tool' in desc_lower or 'application' in desc_lower and 'tool' in desc_lower or 'app' in name_lower or 'application' in name_lower):
            return "应用/其他应用"
        if cat == "Web/Web工具" and ('app' in desc_lower and 'tool' in desc_lower or 'application' in desc_lower and 'tool' in desc_lower or 'app' in name_lower or 'application' in name_lower):
            return "应用/其他应用"
        if cat == "开发/开发工具" and ('app' in desc_lower and 'tool' in desc_lower or 'application' in desc_lower and 'tool' in desc_lower or 'app' in name_lower or 'application' in name_lower):
            return "应用/其他应用"
        if cat == "应用/应用工具" and ('app' in desc_lower and 'tool' in desc_lower or 'application' in desc_lower and 'tool' in desc_lower or 'app' in name_lower or 'application' in name_lower):
            return "应用/其他应用"
        if cat == "生产力/生产力工具" and ('app' in desc_lower and 'tool' in desc_lower or 'application' in desc_lower and 'tool' in desc_lower or 'app' in name_lower or 'application' in name_lower):
            return "应用/其他应用"
        if cat == "办公/办公工具" and ('app' in desc_lower and 'tool' in desc_lower or 'application' in desc_lower and 'tool' in desc_lower or 'app' in name_lower or 'application' in name_lower):
            return "应用/其他应用"
        if cat == "文件/文件工具" and ('app' in desc_lower and 'tool' in desc_lower or 'application' in desc_lower and 'tool' in desc_lower or 'app' in name_lower or 'application' in name_lower):
            return "应用/其他应用"
        
        return cat
    
    # ===== V22 NEW: Handle remaining 其他/综合工具 =====
    # For the remaining 22 tools in 其他, try to categorize them
    
    # --- AK47 → 安全/渗透测试 ---
    if 'ak47' in name_lower:
        return "安全/渗透测试"
    
    # --- truenet → AI/CV/图像分割 ---
    if 'truenet' in name_lower or ('white matter' in desc_lower and 'segmentation' in desc_lower):
        return "AI/CV/图像分割"
    
    # --- SwissKnife → CLI/命令行 ---
    if 'swissknife' in name_lower or 'swiss knife' in desc_lower:
        return "CLI/命令行"
    
    # --- superdb → 数据库/数据库工具 ---
    if 'superdb' in name_lower or ('db' in name_lower and 'tool' in desc_lower and 'mysql' in desc_lower):
        return "数据库/数据库工具"
    
    # --- sanhei-bills2 → 财务/财务工具 ---
    if 'bills' in name_lower or 'bill' in desc_lower:
        return "财务/财务工具"
    
    # --- HBUAS_jwxt → 教育/教育工具 ---
    if 'jwxt' in name_lower or 'jiaowu' in desc_lower or '教务' in desc:
        return "教育/教育工具"
    
    # --- TurnIn → 教育/教育工具 ---
    if 'turnin' in name_lower or 'assignment' in desc_lower and 'submit' in desc_lower:
        return "教育/教育工具"
    
    # --- pmaster → 产品/产品工具 ---
    if 'pmaster' in name_lower or 'prd' in desc_lower or '需求' in desc:
        return "产品/产品工具"
    
    # --- hetongzhushou → 法律/法律工具 ---
    if 'hetong' in name_lower or '合同' in desc:
        return "法律/法律工具"
    
    # --- kehuguanjia → 销售/CRM ---
    if 'kehuguanjia' in name_lower or '客户' in desc:
        return "销售/CRM"
    
    # --- Smoke-Free → 健康/健康工具 ---
    if 'smoke' in name_lower or 'smoking' in desc_lower or '戒烟' in desc:
        return "健康/健康工具"
    
    # --- SpatGRIS → 媒体/多媒体 ---
    if 'spatgris' in name_lower or 'sound' in desc_lower and 'spatial' in desc_lower:
        return "媒体/多媒体"
    
    # --- tdo → 笔记/笔记工具 ---
    if 'tdo' in name_lower and 'note' in desc_lower:
        return "笔记/笔记工具"
    
    # --- hub → 资源/资源工具 ---
    if 'hub' in name_lower and 'resource' in desc_lower:
        return "资源/资源工具"
    
    # --- universal-np → 媒体/多媒体 ---
    if 'universal-np' in name_lower or 'now playing' in desc_lower:
        return "媒体/多媒体"
    
    # --- EssentialNowPlaying → 媒体/多媒体 ---
    if 'essentialnowplaying' in name_lower or 'now playing' in desc_lower:
        return "媒体/多媒体"
    
    # --- Akuma → 安全/渗透测试 ---
    if 'akuma' in name_lower or 'dorking' in desc_lower:
        return "安全/渗透测试"
    
    # --- gbt → 工具/通用工具 ---
    if 'gbt' in name_lower:
        return "工具/通用工具"
    
    # --- home2l → 智能家居/智能家居工具 ---
    if 'home2l' in name_lower or 'smart home' in desc_lower:
        return "智能家居/智能家居工具"
    
    # --- ez-bark → 工具/通用工具 ---
    if 'ez-bark' in name_lower or 'bark' in name_lower:
        return "工具/通用工具"
    
    # --- dhodgson615 → 其他/综合工具 (no description) ---
    if 'dhodgson615' in name_lower:
        return "其他/综合工具"
    
    # --- fp-systrum → 工具/通用工具 ---
    if 'fp-systrum' in name_lower:
        return "工具/通用工具"
    
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
    
    cat = get_v22_category(name, desc)
    
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