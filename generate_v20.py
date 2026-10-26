#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V20: Add name-based matching patterns to capture 其他 tools and push categories over 50 threshold
"""

import re
import sys
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

with open(r"D:\testa\all-tools-final-v5.txt", "r", encoding="utf-8") as f:
    tools = f.readlines()

print(f"Total tools: {len(tools)}")

# Read V17 and V18 functions
with open(r"D:\testa\generate_v17_final.py", "r", encoding="utf-8") as f:
    v17_code = f.read()
with open(r"D:\testa\generate_v18.py", "r", encoding="utf-8") as f:
    v18_code = f.read()

v17_func_start = v17_code.find("def get_v17_category")
v17_func_end = v17_code.rfind("\n# Count categories")
v18_func_start = v18_code.find("def get_v18_category")
v18_func_end = v18_code.rfind("\n# Count categories")

v17_func_code = v17_code[v17_func_start:v17_func_end]
v18_func_code = v18_code[v18_func_start:v18_func_end]
full_code = v17_func_code + "\n" + v18_func_code + "\n"

scope = {}
exec(full_code, scope)
get_v18_category = scope['get_v18_category']

# Read V19 function
with open(r"D:\testa\generate_v19_final.py", "r", encoding="utf-8") as f:
    v19_code = f.read()

v19_func_start = v19_code.find("def get_v19_category")
v19_func_end = v19_code.rfind("\n# Count categories")
v19_func_code = v19_code[v19_func_start:v19_func_end]

exec(v19_func_code, scope)
get_v19_category = scope['get_v19_category']

def get_v20_category(name, desc):
    name_lower = name.lower()
    desc_lower = desc.lower()
    
    # First try V19 categorization
    cat = get_v19_category(name, desc)
    
    # If it's still "其他/综合工具", try V20 additional patterns
    if cat != "其他/综合工具":
        return cat
    
    # ===== V20 NEW: Name-based matching patterns =====
    
    # --- Security/Hacking tools ---
    if 'hack' in name_lower:
        return "安全/渗透测试"
    if 'phish' in name_lower:
        return "安全/渗透测试"
    if 'brute' in name_lower:
        return "安全/渗透测试"
    if 'sniff' in name_lower:
        return "安全/渗透测试"
    if 'fuzz' in name_lower:
        return "安全/渗透测试"
    if 'injection' in name_lower:
        return "安全/渗透测试"
    if 'exploit' in name_lower:
        return "安全/渗透测试"
    if 'dork' in name_lower:
        return "安全/渗透测试"
    if 'crack' in name_lower:
        return "安全/渗透测试"
    if 'malware' in name_lower or 'malicious' in name_lower:
        return "安全/渗透测试"
    if 'waf' in name_lower:
        return "安全/渗透测试"
    if 'xss' in name_lower:
        return "安全/渗透测试"
    if 'sqli' in name_lower:
        return "安全/渗透测试"
    if 'cve' in name_lower:
        return "安全/渗透测试"
    if 'vulnerab' in name_lower:
        return "安全/渗透测试"
    if 'pentest' in name_lower:
        return "安全/渗透测试"
    if 'nmap' in name_lower:
        return "安全/渗透测试"
    if 'metasploit' in name_lower:
        return "安全/渗透测试"
    if 'burp' in name_lower:
        return "安全/渗透测试"
    if 'zab' in name_lower:
        return "安全/渗透测试"
    if 'sqlmap' in name_lower:
        return "安全/渗透测试"
    if 'nikto' in name_lower:
        return "安全/渗透测试"
    if 'nessus' in name_lower:
        return "安全/渗透测试"
    if 'openvas' in name_lower:
        return "安全/渗透测试"
    if 'wireshark' in name_lower:
        return "安全/渗透测试"
    if 'tcpdump' in name_lower:
        return "安全/渗透测试"
    if 'mitm' in name_lower:
        return "安全/渗透测试"
    if 'proxy' in name_lower and 'tool' in desc_lower:
        return "安全/渗透测试"
    if 'guard' in name_lower and 'tool' in desc_lower:
        return "安全/安全工具"
    if 'shield' in name_lower:
        return "安全/安全工具"
    if 'encrypt' in name_lower:
        return "安全/加密"
    if 'decrypt' in name_lower:
        return "安全/加密"
    if 'cipher' in name_lower:
        return "安全/加密"
    if 'crypto' in name_lower:
        return "安全/加密"
    if 'hash' in name_lower:
        return "安全/加密"
    if 'otp' in name_lower:
        return "安全/加密"
    if 'auth' in name_lower:
        return "安全/认证"
    if 'token' in name_lower:
        return "安全/认证"
    if 'oauth' in name_lower:
        return "安全/认证"
    if 'sso' in name_lower:
        return "安全/认证"
    if 'jwt' in name_lower:
        return "安全/认证"
    if 'saml' in name_lower:
        return "安全/认证"
    if 'ldap' in name_lower:
        return "安全/认证"
    if 'ssh' in name_lower:
        return "安全/SSH"
    if 'vpn' in name_lower:
        return "安全/VPN"
    if 'firewall' in name_lower:
        return "安全/防火墙"
    if 'antivirus' in name_lower or 'antimalware' in name_lower:
        return "安全/杀毒"
    if 'scanner' in name_lower:
        return "安全/扫描"
    if 'monitor' in name_lower and ('security' in desc_lower or 'sec' in desc_lower):
        return "安全/安全监控"
    if 'alert' in name_lower:
        return "安全/告警"
    if 'log' in name_lower and 'sec' in name_lower:
        return "安全/安全日志"
    
    # --- Analysis tools ---
    if 'analy' in name_lower:
        if 'weather' in desc_lower or 'meteo' in desc_lower:
            return "气象/气象分析"
        if 'stock' in desc_lower or 'invest' in desc_lower:
            return "金融/投资分析"
        if 'image' in desc_lower or 'photo' in desc_lower:
            return "图像/图像分析"
        if 'data' in desc_lower or 'dataset' in desc_lower:
            return "数据/数据分析"
        return "分析/分析工具"
    if 'stat' in name_lower and 'tool' in desc_lower:
        return "分析/统计分析"
    if 'calculat' in name_lower:
        return "计算/计算器"
    if 'calc' in name_lower:
        return "计算/计算器"
    if 'measure' in name_lower:
        return "测量/测量工具"
    if 'meter' in name_lower:
        return "测量/测量工具"
    if 'benchmark' in name_lower:
        return "测试/性能测试"
    if 'profiler' in name_lower or 'profile' in name_lower:
        return "性能/性能分析"
    if 'debug' in name_lower:
        return "开发/调试工具"
    
    # --- Data tools ---
    if 'sql' in name_lower:
        return "数据库/SQL工具"
    if 'mysql' in name_lower:
        return "数据库/MySQL"
    if 'postgres' in name_lower:
        return "数据库/PostgreSQL"
    if 'mongo' in name_lower:
        return "数据库/MongoDB"
    if 'redis' in name_lower:
        return "数据库/Redis"
    if 'database' in name_lower:
        return "数据库/数据库工具"
    if 'db' in name_lower and len(name_lower.split('/')[1]) <= 3:
        return "数据库/数据库工具"
    if 'query' in name_lower:
        return "数据库/查询工具"
    if 'dump' in name_lower:
        return "数据库/数据导出"
    if 'backup' in name_lower:
        return "备份/备份工具"
    if 'restore' in name_lower:
        return "备份/恢复工具"
    if 'migration' in name_lower:
        return "数据库/数据迁移"
    if 'etl' in name_lower:
        return "数据/ETL工具"
    if 'crawler' in name_lower or 'scraper' in name_lower:
        return "数据/Web爬虫"
    if 'spider' in name_lower:
        return "数据/Web爬虫"
    if 'parser' in name_lower:
        return "解析/解析工具"
    if 'extract' in name_lower:
        return "提取/提取工具"
    if 'convert' in name_lower:
        return "转换/转换工具"
    if 'transform' in name_lower:
        return "转换/转换工具"
    
    # --- Cloud tools ---
    if 'aws' in name_lower:
        return "云/AWS工具"
    if 'azure' in name_lower:
        return "云/Azure工具"
    if 'gcp' in name_lower or 'google cloud' in desc_lower:
        return "云/GCP工具"
    if 'docker' in name_lower:
        return "云/容器工具"
    if 'kubernetes' in name_lower or 'k8s' in name_lower:
        return "云/Kubernetes"
    if 'terraform' in name_lower:
        return "云/Terraform"
    if 'ansible' in name_lower:
        return "云/Ansible"
    if 'vault' in name_lower:
        return "云/密钥管理"
    
    # --- Development tools ---
    if 'linter' in name_lower or 'lint' in name_lower:
        return "编码/Lint工具"
    if 'formatter' in name_lower or 'format' in name_lower:
        return "编码/格式化工具"
    if 'compiler' in name_lower:
        return "编译/编译器"
    if 'build' in name_lower:
        return "构建/构建工具"
    if 'pack' in name_lower:
        return "包管理/包工具"
    if 'npm' in name_lower:
        return "包管理/npm"
    if 'pip' in name_lower:
        return "包管理/pip"
    if 'brew' in name_lower:
        return "包管理/Homebrew"
    if 'package' in name_lower:
        return "包管理/包管理"
    if 'sdk' in name_lower:
        return "开发/SDK工具"
    if 'api' in name_lower:
        return "API/API工具"
    if 'rest' in name_lower:
        return "API/REST工具"
    if 'graphql' in name_lower:
        return "API/GraphQL"
    if 'webhook' in name_lower:
        return "集成/Webhook"
    if 'plugin' in name_lower:
        return "插件/插件工具"
    if 'extension' in name_lower:
        return "插件/扩展工具"
    if 'addon' in name_lower:
        return "插件/附加工具"
    if 'theme' in name_lower:
        return "主题/主题工具"
    if 'widget' in name_lower:
        return "UI/小部件"
    if 'component' in name_lower:
        return "UI/组件工具"
    if 'template' in name_lower:
        return "模板/模板工具"
    if 'boilerplate' in name_lower:
        return "模板/样板工具"
    if 'starter' in name_lower:
        return "模板/起步工具"
    
    # --- Image/Media tools ---
    if 'image' in name_lower:
        return "图像/图像工具"
    if 'photo' in name_lower:
        return "图像/照片工具"
    if 'video' in name_lower:
        return "视频/视频工具"
    if 'audio' in name_lower:
        return "音频/音频工具"
    if 'music' in name_lower:
        return "音乐/音乐工具"
    if 'media' in name_lower:
        return "媒体/媒体工具"
    if 'video' in desc_lower and 'tool' in desc_lower:
        return "视频/视频工具"
    if 'audio' in desc_lower and 'tool' in desc_lower:
        return "音频/音频工具"
    if 'music' in desc_lower and 'tool' in desc_lower:
        return "音乐/音乐工具"
    if 'edit' in name_lower and ('image' in desc_lower or 'photo' in desc_lower or 'video' in desc_lower):
        return "编辑/媒体编辑"
    
    # --- Network tools ---
    if 'network' in name_lower:
        return "网络/网络工具"
    if 'net' in name_lower and len(name_lower.split('/')[1]) <= 3:
        return "网络/网络工具"
    if 'socket' in name_lower:
        return "网络/Socket工具"
    if 'http' in name_lower:
        return "网络/HTTP工具"
    if 'dns' in name_lower:
        return "网络/DNS工具"
    if 'whois' in name_lower:
        return "网络/Whois工具"
    if 'ping' in name_lower:
        return "网络/Ping工具"
    if 'traceroute' in name_lower:
        return "网络/追踪路由"
    if 'proxy' in name_lower:
        return "网络/代理工具"
    if 'cdn' in name_lower:
        return "网络/CDN工具"
    if 'loadbalancer' in name_lower:
        return "网络/负载均衡"
    if 'gateway' in name_lower:
        return "网络/网关工具"
    if 'router' in name_lower:
        return "网络/路由工具"
    if 'switch' in name_lower:
        return "网络/交换机工具"
    
    # --- Game tools ---
    if 'game' in name_lower:
        return "游戏/游戏工具"
    if 'gaming' in name_lower:
        return "游戏/游戏工具"
    if 'game' in desc_lower and 'tool' in desc_lower:
        return "游戏/游戏工具"
    if 'mod' in name_lower and 'game' in desc_lower:
        return "游戏/游戏模组"
    if 'sprite' in name_lower:
        return "游戏/精灵工具"
    if 'unity' in name_lower:
        return "游戏/Unity"
    if 'unreal' in name_lower:
        return "游戏/Unreal"
    if 'godot' in name_lower:
        return "游戏/Godot"
    
    # --- Education tools ---
    if 'learn' in name_lower:
        return "学习/学习工具"
    if 'study' in name_lower:
        return "学习/学习工具"
    if 'course' in name_lower:
        return "学习/课程工具"
    if 'tutorial' in name_lower:
        return "学习/教程工具"
    if 'textbook' in name_lower:
        return "学习/教材工具"
    if 'quiz' in name_lower:
        return "学习/测验工具"
    if 'exam' in name_lower:
        return "学习/考试工具"
    if 'homework' in name_lower:
        return "学习/作业工具"
    if 'assignment' in name_lower:
        return "学习/作业工具"
    if 'grade' in name_lower:
        return "学习/评分工具"
    if 'score' in name_lower:
        return "学习/评分工具"
    if 'education' in name_lower:
        return "学习/教育工具"
    if 'school' in name_lower:
        return "学习/学校工具"
    if 'teacher' in name_lower:
        return "教育/教师工具"
    if 'student' in name_lower:
        return "教育/学生工具"
    
    # --- Health/Medical tools ---
    if 'health' in name_lower:
        return "医疗/健康工具"
    if 'medical' in name_lower:
        return "医疗/医疗工具"
    if 'doctor' in name_lower:
        return "医疗/医生工具"
    if 'patient' in name_lower:
        return "医疗/患者工具"
    if 'hospital' in name_lower:
        return "医疗/医院工具"
    if 'medicine' in name_lower:
        return "医疗/药品工具"
    if 'drug' in name_lower:
        return "医疗/药品工具"
    if 'disease' in name_lower:
        return "医疗/疾病工具"
    if 'diagnos' in name_lower:
        return "医疗/诊断工具"
    if 'treat' in name_lower:
        return "医疗/治疗工具"
    if 'clinic' in name_lower:
        return "医疗/诊所工具"
    if 'pharma' in name_lower:
        return "医疗/药品工具"
    if 'biomarker' in name_lower:
        return "医疗/生物标志物"
    
    # --- Finance tools ---
    if 'finance' in name_lower:
        return "金融/金融工具"
    if 'financial' in name_lower:
        return "金融/金融工具"
    if 'stock' in name_lower:
        return "金融/股票工具"
    if 'trading' in name_lower:
        return "金融/交易工具"
    if 'trade' in name_lower:
        return "金融/交易工具"
    if 'crypto' in name_lower and 'tool' in desc_lower:
        return "金融/加密交易"
    if 'bitcoin' in name_lower:
        return "金融/加密交易"
    if 'ethereum' in name_lower:
        return "金融/加密交易"
    if 'wallet' in name_lower:
        return "金融/钱包工具"
    if 'payment' in name_lower:
        return "金融/支付工具"
    if 'invoice' in name_lower:
        return "金融/发票工具"
    if 'billing' in name_lower:
        return "金融/账单工具"
    if 'account' in name_lower and ('financ' in desc_lower or 'bank' in desc_lower):
        return "金融/账户工具"
    if 'bank' in name_lower:
        return "金融/银行工具"
    if 'tax' in name_lower:
        return "金融/税务工具"
    if 'budget' in name_lower:
        return "金融/预算工具"
    if 'invest' in name_lower:
        return "金融/投资工具"
    if 'fund' in name_lower:
        return "金融/基金工具"
    if 'bond' in name_lower:
        return "金融/债券工具"
    if 'forex' in name_lower:
        return "金融/外汇工具"
    if 'currency' in name_lower:
        return "金融/货币工具"
    if 'exchange' in name_lower:
        return "金融/交易所工具"
    
    # --- Travel tools ---
    if 'travel' in name_lower:
        return "旅游/旅行工具"
    if 'trip' in name_lower:
        return "旅游/旅行工具"
    if 'tour' in name_lower:
        return "旅游/旅游工具"
    if 'flight' in name_lower:
        return "旅游/航班工具"
    if 'hotel' in name_lower:
        return "旅游/酒店工具"
    if 'vacation' in name_lower:
        return "旅游/度假工具"
    if 'booking' in name_lower:
        return "旅游/预订工具"
    if 'itinerary' in name_lower:
        return "旅游/行程工具"
    if 'map' in name_lower and ('travel' in desc_lower or 'trip' in desc_lower or 'tour' in desc_lower):
        return "旅游/地图工具"
    if 'navigation' in name_lower:
        return "旅游/导航工具"
    if 'gps' in name_lower:
        return "旅游/GPS工具"
    if 'weather' in name_lower:
        return "气象/天气工具"
    if 'forecast' in name_lower:
        return "气象/天气预报"
    if 'climate' in name_lower:
        return "气象/气候工具"
    
    # --- Food tools ---
    if 'food' in name_lower:
        return "美食/美食工具"
    if 'recipe' in name_lower:
        return "美食/菜谱工具"
    if 'cook' in name_lower:
        return "美食/烹饪工具"
    if 'meal' in name_lower:
        return "美食/餐食工具"
    if 'nutrition' in name_lower:
        return "美食/营养工具"
    if 'diet' in name_lower:
        return "健康/饮食工具"
    if 'calorie' in name_lower:
        return "健康/卡路里工具"
    if 'weight' in name_lower:
        return "健康/体重工具"
    if 'fitness' in name_lower:
        return "健康/健身工具"
    if 'workout' in name_lower:
        return "健康/锻炼工具"
    if 'exercise' in name_lower:
        return "健康/锻炼工具"
    if 'gym' in name_lower:
        return "健康/健身房工具"
    if 'yoga' in name_lower:
        return "健康/瑜伽工具"
    
    # --- Social tools ---
    if 'social' in name_lower:
        return "社交/社交工具"
    if 'chat' in name_lower:
        return "社交/聊天工具"
    if 'messaging' in name_lower:
        return "社交/消息工具"
    if 'message' in name_lower:
        return "社交/消息工具"
    if 'forum' in name_lower:
        return "社交/论坛工具"
    if 'comment' in name_lower:
        return "社交/评论工具"
    if 'blog' in name_lower:
        return "社交/博客工具"
    if 'blog' in desc_lower and 'tool' in desc_lower:
        return "社交/博客工具"
    if 'twitter' in name_lower:
        return "社交/Twitter工具"
    if 'facebook' in name_lower:
        return "社交/Facebook工具"
    if 'instagram' in name_lower:
        return "社交/Instagram工具"
    if 'discord' in name_lower:
        return "社交/Discord工具"
    if 'slack' in name_lower:
        return "社交/Slack工具"
    if 'telegram' in name_lower:
        return "社交/Telegram工具"
    if 'whatsapp' in name_lower:
        return "社交/WhatsApp工具"
    
    # --- Legal tools ---
    if 'legal' in name_lower:
        return "法律/法律工具"
    if 'law' in name_lower:
        return "法律/法律工具"
    if 'contract' in name_lower:
        return "法律/合同工具"
    if 'compliance' in name_lower:
        return "法律/合规工具"
    if 'patent' in name_lower:
        return "法律/专利工具"
    if 'copyright' in name_lower:
        return "法律/版权工具"
    if 'license' in name_lower:
        return "法律/许可证工具"
    if 'regulation' in name_lower:
        return "法律/法规工具"
    if 'policy' in name_lower:
        return "法律/政策工具"
    
    # --- Science tools ---
    if 'scienc' in name_lower:
        return "科学/科学工具"
    if 'physics' in name_lower:
        return "科学/物理工具"
    if 'chemistry' in name_lower:
        return "科学/化学工具"
    if 'biology' in name_lower:
        return "科学/生物工具"
    if 'math' in name_lower:
        return "科学/数学工具"
    if 'mathematic' in name_lower:
        return "科学/数学工具"
    if 'statistics' in name_lower:
        return "科学/统计工具"
    if 'statistic' in name_lower:
        return "科学/统计工具"
    if 'algorithm' in name_lower:
        return "科学/算法工具"
    if 'algorithm' in desc_lower and 'tool' in desc_lower:
        return "科学/算法工具"
    if 'simulation' in name_lower:
        return "科学/模拟工具"
    if 'simul' in name_lower:
        return "科学/模拟工具"
    if 'model' in name_lower and 'data' in desc_lower:
        return "科学/数据模型"
    if 'research' in name_lower:
        return "科学/研究工具"
    if 'lab' in name_lower:
        return "科学/实验室工具"
    if 'experiment' in name_lower:
        return "科学/实验工具"
    
    # --- Environmental tools ---
    if 'environ' in name_lower:
        return "环境/环境工具"
    if 'climate' in name_lower:
        return "环境/气候工具"
    if 'pollution' in name_lower:
        return "环境/污染工具"
    if 'energy' in name_lower:
        return "能源/能源工具"
    if 'solar' in name_lower:
        return "能源/太阳能工具"
    if 'wind' in name_lower:
        return "能源/风能工具"
    if 'renewable' in name_lower:
        return "能源/可再生能源工具"
    if 'emission' in name_lower:
        return "环境/排放工具"
    if 'carbon' in name_lower:
        return "环境/碳排放工具"
    if 'water' in name_lower and 'tool' in desc_lower:
        return "环境/水资源工具"
    if 'air' in name_lower and 'tool' in desc_lower:
        return "环境/空气质量工具"
    
    # --- Construction/Building tools ---
    if 'construction' in name_lower:
        return "建筑/建筑工具"
    if 'building' in name_lower:
        return "建筑/建筑工具"
    if 'architect' in name_lower:
        return "建筑/建筑工具"
    if 'civil' in name_lower:
        return "建筑/土木工具"
    if 'structural' in name_lower:
        return "建筑/结构工具"
    if 'engineer' in name_lower and 'tool' in desc_lower:
        return "工程/工程工具"
    if 'mechanical' in name_lower:
        return "工程/机械工程工具"
    if 'electrical' in name_lower:
        return "工程/电气工程工具"
    if 'plumbing' in name_lower:
        return "工程/管道工具"
    if 'hvac' in name_lower:
        return "工程/HVAC工具"
    
    # --- Transportation tools ---
    if 'transport' in name_lower:
        return "运输/运输工具"
    if 'vehicle' in name_lower:
        return "运输/车辆工具"
    if 'car' in name_lower and 'tool' in desc_lower:
        return "运输/汽车工具"
    if 'truck' in name_lower:
        return "运输/卡车工具"
    if 'train' in name_lower:
        return "运输/火车工具"
    if 'ship' in name_lower:
        return "运输/船舶工具"
    if 'airplane' in name_lower:
        return "运输/飞机工具"
    if 'aircraft' in name_lower:
        return "运输/航空器工具"
    if 'drone' in name_lower:
        return "运输/无人机工具"
    if 'robot' in name_lower and 'tool' in desc_lower:
        return "机器人/机器人工具"
    
    # --- Agriculture tools ---
    if 'farm' in name_lower:
        return "农业/农业工具"
    if 'farming' in name_lower:
        return "农业/农业工具"
    if 'agricultur' in name_lower:
        return "农业/农业工具"
    if 'crop' in name_lower:
        return "农业/作物工具"
    if 'plant' in name_lower and 'tool' in desc_lower:
        return "农业/植物工具"
    if 'livestock' in name_lower:
        return "农业/畜牧工具"
    if 'veterinary' in name_lower:
        return "农业/兽医工具"
    if 'animal' in name_lower and 'tool' in desc_lower:
        return "农业/动物工具"
    
    # --- Retail/E-commerce tools ---
    if 'retail' in name_lower:
        return "零售/零售工具"
    if 'ecommerce' in name_lower or 'e-commerce' in name_lower:
        return "零售/电商工具"
    if 'shop' in name_lower:
        return "零售/商店工具"
    if 'store' in name_lower and 'tool' in desc_lower:
        return "零售/商店工具"
    if 'marketplace' in name_lower:
        return "零售/市场工具"
    if 'cart' in name_lower:
        return "零售/购物车工具"
    if 'checkout' in name_lower:
        return "零售/结账工具"
    if 'product' in name_lower and 'tool' in desc_lower:
        return "零售/产品工具"
    if 'inventory' in name_lower:
        return "零售/库存工具"
    if 'warehouse' in name_lower:
        return "零售/仓库工具"
    if 'supply' in name_lower:
        return "供应链/供应链工具"
    if 'logistic' in name_lower:
        return "供应链/物流工具"
    if 'shipping' in name_lower:
        return "供应链/运输工具"
    if 'delivery' in name_lower:
        return "供应链/配送工具"
    
    # --- HR/People tools ---
    if 'hr' in name_lower:
        return "人力/HR工具"
    if 'human' in name_lower and 'resource' in desc_lower:
        return "人力/人力资源工具"
    if 'employee' in name_lower:
        return "人力/员工工具"
    if 'staff' in name_lower:
        return "人力/员工工具"
    if 'payroll' in name_lower:
        return "人力/薪资工具"
    if 'recruit' in name_lower:
        return "人力/招聘工具"
    if 'hiring' in name_lower:
        return "人力/招聘工具"
    if 'interview' in name_lower:
        return "人力/面试工具"
    if 'resume' in name_lower:
        return "人力/简历工具"
    if 'cv' in name_lower:
        return "人力/简历工具"
    if 'performance' in name_lower and 'review' in desc_lower:
        return "人力/绩效评估"
    if 'training' in name_lower:
        return "人力/培训工具"
    if 'onboard' in name_lower:
        return "人力/入职工具"
    
    # --- Sales/Marketing tools ---
    if 'sales' in name_lower:
        return "销售/销售工具"
    if 'crm' in name_lower:
        return "销售/CRM工具"
    if 'marketing' in name_lower:
        return "营销/营销工具"
    if 'ad' in name_lower and 'tool' in desc_lower:
        return "营销/广告工具"
    if 'seo' in name_lower:
        return "营销/SEO工具"
    if 'sem' in name_lower:
        return "营销/SEM工具"
    if 'analytics' in name_lower:
        return "营销/分析工具"
    if 'analytic' in name_lower:
        return "营销/分析工具"
    if 'campaign' in name_lower:
        return "营销/营销活动工具"
    if 'lead' in name_lower and 'tool' in desc_lower:
        return "销售/线索工具"
    if 'funnel' in name_lower:
        return "销售/销售漏斗"
    if 'conversion' in name_lower:
        return "营销/转化率工具"
    if 'traffic' in name_lower:
        return "营销/流量工具"
    if 'engagement' in name_lower:
        return "营销/互动工具"
    
    # --- Content tools ---
    if 'content' in name_lower:
        return "内容/内容工具"
    if 'article' in name_lower:
        return "内容/文章工具"
    if 'post' in name_lower and 'tool' in desc_lower:
        return "内容/文章工具"
    if 'publish' in name_lower:
        return "内容/发布工具"
    if 'editor' in name_lower:
        return "编辑/编辑工具"
    if 'writer' in name_lower:
        return "写作/写作工具"
    if 'writing' in name_lower:
        return "写作/写作工具"
    if 'grammar' in name_lower:
        return "写作/语法工具"
    if 'spell' in name_lower:
        return "写作/拼写工具"
    if 'translate' in name_lower:
        return "翻译/翻译工具"
    if 'translation' in name_lower:
        return "翻译/翻译工具"
    if 'localiz' in name_lower:
        return "本地化/本地化工具"
    if 'language' in name_lower:
        return "语言/语言工具"
    if 'dictionary' in name_lower:
        return "语言/词典工具"
    if 'thesaurus' in name_lower:
        return "语言/同义词工具"
    
    # --- Design tools ---
    if 'design' in name_lower:
        return "设计/设计工具"
    if 'drawing' in name_lower:
        return "设计/绘图工具"
    if 'illustration' in name_lower:
        return "设计/插图工具"
    if 'icon' in name_lower:
        return "设计/图标工具"
    if 'logo' in name_lower:
        return "设计/Logo工具"
    if 'color' in name_lower:
        return "设计/颜色工具"
    if 'font' in name_lower:
        return "设计/字体工具"
    if 'typograph' in name_lower:
        return "设计/排印工具"
    if 'layout' in name_lower:
        return "设计/布局工具"
    if 'wireframe' in name_lower:
        return "设计/线框工具"
    if 'prototype' in name_lower:
        return "设计/原型工具"
    if 'mockup' in name_lower:
        return "设计/模型工具"
    if 'sketch' in name_lower:
        return "设计/草图工具"
    if 'paint' in name_lower:
        return "设计/绘画工具"
    if 'draw' in name_lower:
        return "设计/绘图工具"
    if 'graphic' in name_lower:
        return "设计/图形工具"
    if 'vector' in name_lower:
        return "设计/矢量工具"
    if 'bitmap' in name_lower:
        return "设计/位图工具"
    if 'raster' in name_lower:
        return "设计/栅格工具"
    if '3d' in name_lower:
        return "3D/3D工具"
    if 'cad' in name_lower:
        return "3D/CAD工具"
    if 'cam' in name_lower:
        return "3D/CAM工具"
    if 'cam' in name_lower:
        return "3D/CAM工具"
    if 'render' in name_lower:
        return "3D/渲染工具"
    if 'animation' in name_lower:
        return "3D/动画工具"
    if 'motion' in name_lower:
        return "3D/运动工具"
    
    # --- AI/ML tools ---
    if 'ai' in name_lower and len(name_lower.split('/')[1]) <= 2:
        return "AI/AI工具"
    if 'ml' in name_lower and len(name_lower.split('/')[1]) <= 2:
        return "AI/ML工具"
    if 'neural' in name_lower:
        return "AI/神经网络工具"
    if 'deep' in name_lower and 'learning' in desc_lower:
        return "AI/深度学习工具"
    if 'machine' in name_lower and 'learning' in desc_lower:
        return "AI/机器学习工具"
    if 'model' in name_lower and 'predict' in desc_lower:
        return "AI/预测模型"
    if 'predict' in name_lower:
        return "AI/预测工具"
    if 'recommend' in name_lower:
        return "AI/推荐系统"
    if 'classif' in name_lower:
        return "AI/分类工具"
    if 'cluster' in name_lower:
        return "AI/聚类工具"
    if 'regression' in name_lower:
        return "AI/回归工具"
    if 'optimiz' in name_lower:
        return "AI/优化工具"
    if 'reinforce' in name_lower:
        return "AI/强化学习"
    if 'supervis' in name_lower:
        return "AI/监督学习"
    if 'unsupervis' in name_lower:
        return "AI/无监督学习"
    if 'semi-supervis' in name_lower:
        return "AI/半监督学习"
    if 'transfer' in name_lower and 'learning' in desc_lower:
        return "AI/迁移学习"
    if 'generative' in name_lower:
        return "AI/生成模型"
    if 'gan' in name_lower and len(name_lower.split('/')[1]) <= 2:
        return "AI/GAN工具"
    if 'transformer' in name_lower:
        return "AI/Transformer"
    if 'attention' in name_lower:
        return "AI/注意力机制"
    if 'bert' in name_lower:
        return "AI/BERT"
    if 'gpt' in name_lower:
        return "AI/GPT"
    if 'llm' in name_lower:
        return "AI/LLM工具"
    if 'nlp' in name_lower:
        return "AI/NLP工具"
    if 'cv' in name_lower and len(name_lower.split('/')[1]) <= 2:
        return "AI/CV工具"
    if 'ocr' in name_lower:
        return "AI/OCR工具"
    if 'speech' in name_lower:
        return "AI/语音工具"
    if 'voice' in name_lower:
        return "AI/语音工具"
    if 'text' in name_lower and 'tool' in desc_lower:
        return "AI/文本工具"
    if 'sentiment' in name_lower:
        return "AI/情感分析"
    if 'topic' in name_lower:
        return "AI/主题分析"
    if 'entity' in name_lower:
        return "AI/实体识别"
    if 'nlp' in desc_lower and 'tool' in desc_lower:
        return "AI/NLP工具"
    
    # --- Robotics tools ---
    if 'robot' in name_lower:
        return "机器人/机器人工具"
    if 'robotic' in name_lower:
        return "机器人/机器人工具"
    if 'drone' in name_lower:
        return "机器人/无人机工具"
    if 'autonomous' in name_lower:
        return "机器人/自主工具"
    if 'autonom' in name_lower:
        return "机器人/自主工具"
    if 'autopilot' in name_lower:
        return "机器人/自动驾驶工具"
    if 'navigation' in name_lower and 'robot' in desc_lower:
        return "机器人/导航工具"
    if 'sensor' in name_lower:
        return "传感器/传感器工具"
    if 'actuator' in name_lower:
        return "机器人/执行器工具"
    if 'motor' in name_lower:
        return "机器人/电机工具"
    if 'servo' in name_lower:
        return "机器人/舵机工具"
    if 'arduino' in name_lower:
        return "嵌入式/Arduino"
    if 'raspberry' in name_lower:
        return "嵌入式/RaspberryPi"
    if 'stm32' in name_lower:
        return "嵌入式/STM32"
    if 'esp32' in name_lower:
        return "嵌入式/ESP32"
    if 'fpga' in name_lower:
        return "嵌入式/FPGA工具"
    if 'embedded' in name_lower:
        return "嵌入式/嵌入式工具"
    
    # --- Desktop/UI tools ---
    if 'desktop' in name_lower:
        return "桌面/桌面工具"
    if 'gui' in name_lower:
        return "UI/GUI工具"
    if 'ui' in name_lower:
        return "UI/UI工具"
    if 'ux' in name_lower:
        return "UI/UX工具"
    if 'frontend' in name_lower:
        return "UI/前端工具"
    if 'backend' in name_lower:
        return "后端/后端工具"
    if 'fullstack' in name_lower:
        return "全栈/全栈工具"
    if 'web' in name_lower and 'tool' in desc_lower:
        return "Web/Web工具"
    if 'mobile' in name_lower:
        return "移动/移动工具"
    if 'android' in name_lower:
        return "移动/Android工具"
    if 'ios' in name_lower:
        return "移动/iOS工具"
    if 'iphone' in name_lower:
        return "移动/iPhone工具"
    if 'ipad' in name_lower:
        return "移动/iPad工具"
    if 'tablet' in name_lower:
        return "移动/平板工具"
    if 'phone' in name_lower:
        return "移动/手机工具"
    if 'watch' in name_lower and ('tool' in desc_lower or 'app' in desc_lower):
        return "移动/手表工具"
    
    # --- Office/Productivity tools ---
    if 'office' in name_lower:
        return "办公/办公工具"
    if 'document' in name_lower:
        return "办公/文档工具"
    if 'spreadsheet' in name_lower:
        return "办公/电子表格工具"
    if 'excel' in name_lower:
        return "办公/Excel工具"
    if 'word' in name_lower and 'tool' in desc_lower:
        return "办公/Word工具"
    if 'powerpoint' in name_lower:
        return "办公/PPT工具"
    if 'ppt' in name_lower:
        return "办公/PPT工具"
    if 'presentation' in name_lower:
        return "办公/演示工具"
    if 'pdf' in name_lower:
        return "办公/PDF工具"
    if 'email' in name_lower:
        return "办公/邮件工具"
    if 'mail' in name_lower and 'tool' in desc_lower:
        return "办公/邮件工具"
    if 'calendar' in name_lower:
        return "办公/日历工具"
    if 'schedule' in name_lower:
        return "办公/日程工具"
    if 'reminder' in name_lower:
        return "办公/提醒工具"
    if 'task' in name_lower and 'tool' in desc_lower:
        return "生产力/任务工具"
    if 'todo' in name_lower:
        return "生产力/待办工具"
    if 'note' in name_lower:
        return "笔记/笔记工具"
    if 'memo' in name_lower:
        return "笔记/备忘工具"
    if 'bookmark' in name_lower:
        return "书签/书签工具"
    if 'shortcut' in name_lower:
        return "快捷方式/快捷方式工具"
    if 'clipboard' in name_lower:
        return "剪贴板/剪贴板工具"
    if 'file' in name_lower and 'tool' in desc_lower:
        return "文件/文件工具"
    if 'folder' in name_lower:
        return "文件/文件夹工具"
    if 'sync' in name_lower:
        return "同步/同步工具"
    if 'share' in name_lower:
        return "共享/共享工具"
    if 'upload' in name_lower:
        return "上传/上传工具"
    if 'download' in name_lower:
        return "下载/下载工具"
    if 'compress' in name_lower:
        return "压缩/压缩工具"
    if 'extract' in name_lower:
        return "解压/解压工具"
    if 'archive' in name_lower:
        return "归档/归档工具"
    
    # --- Search tools ---
    if 'search' in name_lower:
        return "搜索/搜索工具"
    if 'find' in name_lower:
        return "搜索/查找工具"
    if 'grep' in name_lower:
        return "搜索/Grep工具"
    if 'regex' in name_lower:
        return "搜索/正则表达式工具"
    if 'pattern' in name_lower:
        return "搜索/模式匹配工具"
    if 'index' in name_lower:
        return "搜索/索引工具"
    if 'sort' in name_lower:
        return "排序/排序工具"
    if 'filter' in name_lower:
        return "过滤/过滤工具"
    if 'select' in name_lower:
        return "选择/选择工具"
    
    # --- Monitoring/Observability tools ---
    if 'monitor' in name_lower:
        return "监控/监控工具"
    if 'observab' in name_lower:
        return "可观测性/可观测性工具"
    if 'trace' in name_lower:
        return "追踪/追踪工具"
    if 'audit' in name_lower:
        return "审计/审计工具"
    if 'metric' in name_lower:
        return "指标/指标工具"
    if 'dashboard' in name_lower:
        return "仪表盘/仪表盘工具"
    if 'report' in name_lower:
        return "报告/报告工具"
    if 'log' in name_lower and 'tool' in desc_lower:
        return "日志/日志工具"
    if 'logging' in name_lower:
        return "日志/日志工具"
    if 'debug' in name_lower:
        return "调试/调试工具"
    if 'diagnos' in name_lower:
        return "诊断/诊断工具"
    if 'health' in name_lower and 'check' in desc_lower:
        return "健康检查/健康检查工具"
    if 'status' in name_lower:
        return "状态/状态工具"
    if 'uptime' in name_lower:
        return "状态/在线工具"
    if 'ping' in name_lower:
        return "状态/Ping工具"
    
    # --- Automation tools ---
    if 'automat' in name_lower:
        return "自动化/自动化工具"
    if 'script' in name_lower:
        return "脚本/脚本工具"
    if 'cron' in name_lower:
        return "调度/Cron工具"
    if 'schedule' in name_lower and 'task' in desc_lower:
        return "调度/任务调度工具"
    if 'queue' in name_lower:
        return "队列/队列工具"
    if 'worker' in name_lower:
        return "工作器/工作器工具"
    if 'job' in name_lower and 'tool' in desc_lower:
        return "任务/任务工具"
    if 'task' in name_lower and 'tool' in desc_lower:
        return "任务/任务工具"
    if 'workflow' in name_lower:
        return "工作流/工作流工具"
    if 'pipeline' in name_lower:
        return "工作流/管道工具"
    if 'orchestrat' in name_lower:
        return "编排/编排工具"
    if 'rpa' in name_lower:
        return "自动化/RPA工具"
    if 'bot' in name_lower:
        return "机器人/Bot工具"
    if 'agent' in name_lower:
        return "Agent/Agent工具"
    
    # --- Version control tools ---
    if 'git' in name_lower:
        return "Git/Git工具"
    if 'version' in name_lower and 'control' in desc_lower:
        return "版本控制/版本控制工具"
    if 'vcs' in name_lower:
        return "版本控制/VCS工具"
    if 'branch' in name_lower:
        return "Git/分支工具"
    if 'commit' in name_lower:
        return "Git/提交工具"
    if 'merge' in name_lower:
        return "Git/合并工具"
    if 'rebase' in name_lower:
        return "Git/变基工具"
    if 'stash' in name_lower:
        return "Git/Stash工具"
    if 'clone' in name_lower:
        return "Git/克隆工具"
    if 'fork' in name_lower:
        return "Git/Fork工具"
    if 'pull' in name_lower:
        return "Git/拉取工具"
    if 'push' in name_lower:
        return "Git/推送工具"
    
    # --- Configuration tools ---
    if 'config' in name_lower:
        return "配置/配置工具"
    if 'setting' in name_lower:
        return "配置/设置工具"
    if 'preference' in name_lower:
        return "配置/偏好工具"
    if 'option' in name_lower:
        return "配置/选项工具"
    if 'environment' in name_lower and 'var' in desc_lower:
        return "环境/环境变量工具"
    if 'env' in name_lower and 'var' in desc_lower:
        return "环境/环境变量工具"
    
    # --- Language-specific tools ---
    if 'python' in name_lower:
        return "编程语言/Python工具"
    if 'javascript' in name_lower or 'js' in name_lower:
        return "编程语言/JavaScript工具"
    if 'java' in name_lower:
        return "编程语言/Java工具"
    if 'go' in name_lower and 'tool' in desc_lower:
        return "编程语言/Go工具"
    if 'golang' in name_lower:
        return "编程语言/Go工具"
    if 'rust' in name_lower:
        return "编程语言/Rust工具"
    if 'c#' in name_lower or 'csharp' in name_lower:
        return "编程语言/C#工具"
    if 'cpp' in name_lower:
        return "编程语言/C++工具"
    if 'c' in name_lower and 'tool' in desc_lower:
        return "编程语言/C工具"
    if 'ruby' in name_lower:
        return "编程语言/Ruby工具"
    if 'php' in name_lower:
        return "编程语言/PHP工具"
    if 'swift' in name_lower:
        return "编程语言/Swift工具"
    if 'kotlin' in name_lower:
        return "编程语言/Kotlin工具"
    if 'typescript' in name_lower or 'ts' in name_lower:
        return "编程语言/TypeScript工具"
    if 'bash' in name_lower:
        return "Shell/Bash工具"
    if 'shell' in name_lower:
        return "Shell/Shell工具"
    if 'powershell' in name_lower or 'ps' in name_lower:
        return "Shell/PowerShell工具"
    if 'ruby' in name_lower:
        return "编程语言/Ruby工具"
    if 'perl' in name_lower:
        return "编程语言/Perl工具"
    if 'scala' in name_lower:
        return "编程语言/Scala工具"
    if 'clojure' in name_lower:
        return "编程语言/Clojure工具"
    if 'haskell' in name_lower:
        return "编程语言/Haskell工具"
    if 'elixir' in name_lower:
        return "编程语言/Elixir工具"
    if 'erlang' in name_lower:
        return "编程语言/Erlang工具"
    if 'lua' in name_lower:
        return "编程语言/Lua工具"
    if 'lua' in name_lower:
        return "编程语言/Lua工具"
    if 'dart' in name_lower:
        return "编程语言/Dart工具"
    if 'rust' in name_lower:
        return "编程语言/Rust工具"
    
    # --- Framework-specific tools ---
    if 'react' in name_lower:
        return "框架/React工具"
    if 'vue' in name_lower:
        return "框架/Vue工具"
    if 'angular' in name_lower:
        return "框架/Angular工具"
    if 'svelte' in name_lower:
        return "框架/Svelte工具"
    if 'next' in name_lower:
        return "框架/Next.js工具"
    if 'nuxt' in name_lower:
        return "框架/Nuxt工具"
    if 'flask' in name_lower:
        return "框架/Flask工具"
    if 'django' in name_lower:
        return "框架/Django工具"
    if 'fastapi' in name_lower:
        return "框架/FastAPI工具"
    if 'express' in name_lower:
        return "框架/Express工具"
    if 'spring' in name_lower:
        return "框架/Spring工具"
    if 'laravel' in name_lower:
        return "框架/Laravel工具"
    if 'rails' in name_lower:
        return "框架/Rails工具"
    if 'svelte' in name_lower:
        return "框架/Svelte工具"
    
    # --- Test tools ---
    if 'test' in name_lower:
        return "测试/测试工具"
    if 'unittest' in name_lower:
        return "测试/单元测试"
    if 'integration' in name_lower and 'test' in desc_lower:
        return "测试/集成测试"
    if 'e2e' in name_lower:
        return "测试/E2E测试"
    if 'selenium' in name_lower:
        return "测试/Selenium"
    if 'cypress' in name_lower:
        return "测试/Cypress"
    if 'jest' in name_lower:
        return "测试/Jest"
    if 'mocha' in name_lower:
        return "测试/Mocha"
    if 'pytest' in name_lower:
        return "测试/Pytest"
    if 'unittest' in name_lower:
        return "测试/单元测试"
    if 'tdd' in name_lower:
        return "测试/TDD"
    if 'bdd' in name_lower:
        return "测试/BDD"
    
    # --- Final fallback: classify based on broader patterns
    if 'tool' in name_lower:
        # If it just has "tool" in the name, try to categorize by description
        if 'dev' in desc_lower or 'development' in desc_lower:
            return "开发/开发工具"
        if 'data' in desc_lower:
            return "数据/数据工具"
        if 'web' in desc_lower:
            return "Web/Web工具"
        if 'api' in desc_lower:
            return "API/API工具"
        if 'server' in desc_lower:
            return "服务器/服务器工具"
        if 'client' in desc_lower:
            return "客户端/客户端工具"
        return "工具/通用工具"
    
    if 'kit' in name_lower:
        return "工具/工具包"
    
    if 'util' in name_lower or 'utility' in name_lower:
        return "工具/实用工具"
    
    if 'helper' in name_lower:
        return "工具/助手工具"
    
    if 'wrapper' in name_lower:
        return "包装器/包装器工具"
    
    if 'bridge' in name_lower:
        return "桥接/桥接工具"
    
    if 'gateway' in name_lower:
        return "网关/网关工具"
    
    if 'proxy' in name_lower:
        return "代理/代理工具"
    
    if 'manager' in name_lower:
        return "管理/管理工具"
    
    if 'admin' in name_lower:
        return "管理/管理工具"
    
    if 'control' in name_lower:
        return "控制/控制工具"
    
    if 'panel' in name_lower:
        return "面板/面板工具"
    
    if 'dashboard' in name_lower:
        return "仪表盘/仪表盘工具"
    
    if 'console' in name_lower:
        return "控制台/控制台工具"
    
    if 'terminal' in name_lower:
        return "终端/终端工具"
    
    if 'cli' in name_lower:
        return "CLI/CLI工具"
    
    if 'app' in name_lower:
        return "应用/应用工具"
    
    if 'platform' in name_lower:
        return "平台/平台工具"
    
    if 'service' in name_lower:
        return "服务/服务工具"
    
    if 'library' in name_lower:
        return "库/库工具"
    
    if 'framework' in name_lower:
        return "框架/框架工具"
    
    if 'plugin' in name_lower:
        return "插件/插件工具"
    
    if 'extension' in name_lower:
        return "插件/扩展工具"
    
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
    
    cat = get_v20_category(name, desc)
    
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

# Also show categories 30-50 to see how many we need to push over
print("\n=== Categories 30-50 tools ===")
for cat, count in sorted(categories.items(), key=lambda x: -x[1]):
    if 30 <= count < 50:
        print(f"  {cat}: {count}")