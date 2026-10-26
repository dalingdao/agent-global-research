#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V19 Final: Standalone script with all categorization logic inline
"""

import re
import sys
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

with open(r"D:\testa\all-tools-final-v5.txt", "r", encoding="utf-8") as f:
    tools = f.readlines()

print(f"Total tools: {len(tools)}")

# Read all function definitions
with open(r"D:\testa\generate_v17_final.py", "r", encoding="utf-8") as f:
    v17_code = f.read()

with open(r"D:\testa\generate_v18.py", "r", encoding="utf-8") as f:
    v18_code = f.read()

# Extract V17 function - use newline-prefixed marker to avoid matching inside strings
v17_func_start = v17_code.find("def get_v17_category")
v17_func_end = v17_code.rfind("\n# Count categories")

# Extract V18 function - same approach
v18_func_start = v18_code.find("def get_v18_category")
v18_func_end = v18_code.rfind("\n# Count categories")

print(f"V17: start={v17_func_start}, end={v17_func_end}")
print(f"V18: start={v18_func_start}, end={v18_func_end}")

if v17_func_start != -1 and v17_func_end != -1 and v18_func_start != -1 and v18_func_end != -1:
    # Extract V17 function code
    v17_func_code = v17_code[v17_func_start:v17_func_end]
    
    # Extract V18 function code
    v18_func_code = v18_code[v18_func_start:v18_func_end]
    
    print(f"V17 func code length: {len(v17_func_code)} chars")
    print(f"V18 func code length: {len(v18_func_code)} chars")
    
    # Build the complete code string with V17 then V18
    full_code = v17_func_code + "\n" + v18_func_code + "\n"
    
    # Execute all code together in a single scope
    scope = {}
    exec(full_code, scope)
    
    # Get the functions from the scope
    get_v17_category = scope['get_v17_category']
    get_v18_category = scope['get_v18_category']
    print("V17 and V18 functions loaded successfully")
else:
    print(f"Error extracting functions")
    sys.exit(1)

def get_v19_category(name, desc):
    name_lower = name.lower()
    desc_lower = desc.lower()
    
    # First try V18 categorization
    cat = get_v18_category(name, desc)
    
    # If it's still "其他/综合工具", try V19 additional patterns
    if cat != "其他/综合工具":
        return cat
    
    # ===== V19 NEW: Broader description-based patterns =====
    
    # OS-related
    if 'os' in desc_lower or 'operating system' in desc_lower:
        if 'linux' in desc_lower:
            return "系统/Linux"
        if 'windows' in desc_lower:
            return "系统/Windows"
        if 'mac' in desc_lower or 'macos' in desc_lower:
            return "系统/Mac"
        if 'tool' in desc_lower:
            return "工具/OS工具"
        return "系统/OS"
    
    # Agent-related (broad)
    if 'agent' in desc_lower:
        if 'ai' in desc_lower or 'llm' in desc_lower:
            return "AI/LLM/Agent"
        if 'tool' in desc_lower:
            return "Agent/工具"
        if 'tool' in name_lower:
            return "Agent/工具"
        return "Agent/通用Agent"
    
    # CI/CD-related
    if 'ci' in desc_lower or 'cd' in desc_lower:
        if 'ci/cd' in desc_lower:
            return "DevOps/CI/CD"
        if 'continuous' in desc_lower:
            return "DevOps/持续"
        return "DevOps/CI工具"
    
    # UI-related
    if 'ui' in desc_lower or 'user interface' in desc_lower:
        if 'design' in desc_lower:
            return "设计/UI设计"
        if 'component' in desc_lower:
            return "UI/组件"
        if 'framework' in desc_lower:
            return "UI/框架"
        return "UI/UI工具"
    
    # API-related (broad)
    if 'api' in desc_lower:
        if 'server' in desc_lower:
            return "API/API服务器"
        if 'client' in desc_lower:
            return "API/API客户端"
        if 'gateway' in desc_lower:
            return "API/API网关"
        if 'tool' in desc_lower:
            return "API/API工具"
        if 'wrapper' in desc_lower:
            return "API/API包装"
        return "API/API工具"
    
    # IP-related
    if 'ip' in desc_lower or 'internet protocol' in desc_lower:
        return "网络/IP"
    
    # Manage-related
    if 'manage' in desc_lower or 'management' in desc_lower:
        if 'project' in desc_lower:
            return "项目管理/项目"
        if 'config' in desc_lower:
            return "配置/配置管理"
        if 'file' in desc_lower:
            return "文件/文件管理"
        if 'server' in desc_lower:
            return "系统/服务器管理"
        if 'tool' in desc_lower:
            return "管理/管理工具"
        return "管理/管理"
    
    # Code-related (broad)
    if 'code' in desc_lower:
        if 'editor' in desc_lower:
            return "开发/代码编辑"
        if 'review' in desc_lower:
            return "编码/代码审查"
        if 'quality' in desc_lower:
            return "编码/代码质量"
        if 'snippet' in desc_lower:
            return "编码/代码片段"
        if 'generator' in desc_lower:
            return "编码/代码生成"
        if 'tool' in desc_lower:
            return "编码/代码工具"
        if 'base' in desc_lower:
            return "编码/Codebase"
        return "编码/代码"
    
    # App-related (broad)
    if 'app' in desc_lower or 'application' in desc_lower:
        if 'builder' in desc_lower:
            return "应用/应用构建"
        if 'builder' in name_lower:
            return "应用/应用构建"
        if 'tool' in desc_lower:
            return "应用/应用工具"
        if 'store' in desc_lower:
            return "应用/应用商店"
        return "应用/App"
    
    # Server-related (broad)
    if 'server' in desc_lower:
        if 'web' in desc_lower:
            return "Web/Web服务器"
        if 'api' in desc_lower:
            return "API/API服务器"
        if 'proxy' in desc_lower:
            return "网络/代理服务器"
        if 'game' in desc_lower:
            return "游戏/游戏服务器"
        if 'tool' in desc_lower:
            return "服务器/服务器工具"
        return "服务器/服务器"
    
    # Project-related (broad)
    if 'project' in desc_lower:
        if 'management' in desc_lower:
            return "项目管理/项目管理"
        if 'manager' in desc_lower:
            return "项目管理/项目管理"
        if 'tool' in desc_lower:
            return "项目管理/项目工具"
        if 'template' in desc_lower:
            return "项目管理/项目模板"
        return "项目管理/项目"
    
    # GIS-related
    if 'gis' in desc_lower or 'geographic' in desc_lower:
        if 'info' in desc_lower:
            return "地理/GIS信息"
        if 'tool' in desc_lower:
            return "地理/GIS工具"
        return "地理/GIS"
    
    # Log-related
    if 'log' in desc_lower or 'logging' in desc_lower:
        if 'aggregator' in desc_lower:
            return "日志/日志聚合"
        if 'shipper' in desc_lower:
            return "日志/日志传输"
        if 'parser' in desc_lower:
            return "日志/日志解析"
        if 'viewer' in desc_lower:
            return "日志/日志查看"
        if 'tool' in desc_lower:
            return "日志/日志工具"
        return "日志/日志"
    
    # CLI-related (broad)
    if 'cli' in desc_lower or 'command line' in desc_lower:
        if 'tool' in desc_lower:
            return "CLI/CLI工具"
        if 'app' in desc_lower:
            return "CLI/CLI应用"
        if 'framework' in desc_lower:
            return "CLI/CLI框架"
        return "CLI/命令行"
    
    # System-related (broad)
    if 'system' in desc_lower:
        if 'tool' in desc_lower:
            return "系统/系统工具"
        if 'monitor' in desc_lower:
            return "系统/系统监控"
        if 'update' in desc_lower:
            return "系统/系统更新"
        if 'backup' in desc_lower:
            return "系统/系统备份"
        return "系统/系统"
    
    # Monitor-related (broad)
    if 'monitor' in desc_lower or 'monitoring' in desc_lower:
        if 'tool' in desc_lower:
            return "监控/监控工具"
        if 'server' in desc_lower:
            return "监控/服务器监控"
        if 'network' in desc_lower:
            return "监控/网络监控"
        if 'performance' in desc_lower:
            return "监控/性能监控"
        return "监控/监控"
    
    # Command-related
    if 'command' in desc_lower:
        if 'line' in desc_lower:
            return "CLI/命令行"
        if 'tool' in desc_lower:
            return "工具/命令工具"
        if 'runner' in desc_lower:
            return "工具/命令执行"
        return "命令/命令"
    
    # Build-related
    if 'build' in desc_lower:
        if 'tool' in desc_lower:
            return "构建/构建工具"
        if 'system' in desc_lower:
            return "构建/构建系统"
        if 'automation' in desc_lower:
            return "构建/构建自动化"
        if 'pack' in desc_lower:
            return "构建/构建包"
        return "构建/构建"
    
    # Track-related
    if 'track' in desc_lower or 'tracking' in desc_lower:
        if 'tool' in desc_lower:
            return "追踪/追踪工具"
        if 'issue' in desc_lower:
            return "追踪/问题追踪"
        if 'package' in desc_lower:
            return "追踪/包追踪"
        if 'package' in name_lower:
            return "追踪/包追踪"
        return "追踪/追踪"
    
    # Learn-related
    if 'learn' in desc_lower or 'learning' in desc_lower:
        if 'tool' in desc_lower:
            return "学习/学习工具"
        if 'platform' in desc_lower:
            return "学习/学习平台"
        if 'resource' in desc_lower:
            return "学习/学习资源"
        if 'course' in desc_lower:
            return "学习/学习课程"
        return "学习/学习"
    
    # Mac-related
    if 'mac' in desc_lower or 'macos' in desc_lower or 'osx' in desc_lower:
        if 'tool' in desc_lower:
            return "系统/Mac工具"
        if 'app' in desc_lower:
            return "系统/Mac应用"
        return "系统/Mac"
    
    # Library-related (broad)
    if 'library' in desc_lower:
        if 'python' in desc_lower:
            return "编程语言/Python库"
        if 'javascript' in desc_lower or 'js' in desc_lower:
            return "编程语言/JS库"
        if 'java' in desc_lower:
            return "编程语言/Java库"
        if 'go' in desc_lower:
            return "编程语言/Go库"
        if 'rust' in desc_lower:
            return "编程语言/Rust库"
        if 'c' in desc_lower:
            return "编程语言/C库"
        if 'cpp' in desc_lower:
            return "编程语言/CPP库"
        if 'tool' in desc_lower:
            return "库/库工具"
        return "库/库"
    
    # Coding-related (broad)
    if 'coding' in desc_lower:
        if 'tool' in desc_lower:
            return "编码/编码工具"
        if 'agent' in desc_lower:
            return "编码/编码Agent"
        if 'assistant' in desc_lower:
            return "编码/编码助手"
        if 'platform' in desc_lower:
            return "编码/编码平台"
        return "编码/编码"
    
    # Git-related (broad)
    if 'git' in desc_lower:
        if 'tool' in desc_lower:
            return "Git/Git工具"
        if 'client' in desc_lower:
            return "Git/Git客户端"
        if 'server' in desc_lower:
            return "Git/Git服务器"
        if 'hosting' in desc_lower:
            return "Git/Git托管"
        if 'repository' in desc_lower:
            return "Git/Git仓库"
        return "Git/Git"
    
    # Framework-related (broad)
    if 'framework' in desc_lower:
        if 'tool' in desc_lower:
            return "框架/框架工具"
        if 'library' in desc_lower:
            return "框架/框架库"
        if 'app' in desc_lower:
            return "框架/框架应用"
        return "框架/框架"
    
    # Service-related
    if 'service' in desc_lower:
        if 'tool' in desc_lower:
            return "服务/服务工具"
        if 'management' in desc_lower:
            return "服务/服务管理"
        if 'mesh' in desc_lower:
            return "服务/服务网格"
        if 'registry' in desc_lower:
            return "服务/服务注册"
        return "服务/服务"
    
    # Doc-related (broad)
    if 'doc' in desc_lower or 'documentation' in desc_lower:
        if 'tool' in desc_lower:
            return "文档/文档工具"
        if 'generator' in desc_lower:
            return "文档/文档生成"
        if 'viewer' in desc_lower:
            return "文档/文档查看"
        if 'editor' in desc_lower:
            return "文档/文档编辑"
        if 'site' in desc_lower:
            return "文档/文档站"
        return "文档/文档"
    
    # Perf-related
    if 'perf' in desc_lower or 'performance' in desc_lower:
        if 'tool' in desc_lower:
            return "性能/性能工具"
        if 'monitor' in desc_lower:
            return "性能/性能监控"
        if 'profile' in desc_lower:
            return "性能/性能分析"
        if 'optimize' in desc_lower:
            return "性能/性能优化"
        return "性能/性能"
    
    # Additional patterns for specific tool types
    if 'assistant' in desc_lower:
        if 'ai' in desc_lower:
            return "AI/LLM/助手"
        if 'coding' in desc_lower:
            return "编码/编码助手"
        return "助手/助手"
    
    if 'chatbot' in desc_lower:
        return "机器人/聊天机器人"
    
    if 'bot' in desc_lower:
        if 'chat' in desc_lower:
            return "机器人/聊天机器人"
        if 'discord' in desc_lower:
            return "通信/Discord"
        if 'slack' in desc_lower:
            return "通信/Slack"
        if 'telegram' in desc_lower:
            return "通信/Telegram"
        return "机器人/Bot"
    
    if 'plugin' in desc_lower:
        return "插件/插件"
    
    if 'extension' in desc_lower:
        return "插件/扩展"
    
    if 'addon' in desc_lower:
        return "插件/附加"
    
    if 'template' in desc_lower:
        return "模板/模板"
    
    if 'boilerplate' in desc_lower:
        return "模板/样板"
    
    if 'starter' in desc_lower:
        return "模板/起步"
    
    if 'sample' in desc_lower:
        return "示例/示例"
    
    if 'example' in desc_lower:
        return "示例/示例"
    
    if 'demo' in desc_lower:
        return "示例/演示"
    
    if 'tutorial' in desc_lower:
        return "教程/教程"
    
    if 'blog' in desc_lower:
        return "博客/博客"
    
    if 'post' in desc_lower:
        return "博客/文章"
    
    if 'article' in desc_lower:
        return "博客/文章"
    
    if 'news' in desc_lower:
        return "新闻/新闻"
    
    if 'widget' in desc_lower:
        return "UI/小部件"
    
    if 'component' in desc_lower:
        return "UI/组件"
    
    if 'upload' in desc_lower:
        return "文件/上传"
    
    if 'download' in desc_lower:
        return "文件/下载"
    
    if 'share' in desc_lower:
        return "文件/共享"
    
    if 'transfer' in desc_lower:
        return "文件/传输"
    
    if 'parse' in desc_lower:
        return "解析/解析"
    
    if 'extract' in desc_lower:
        return "提取/提取"
    
    if 'convert' in desc_lower:
        return "转换/转换"
    
    if 'transform' in desc_lower:
        return "转换/转换"
    
    if 'generator' in desc_lower:
        return "生成/生成"
    
    if 'create' in desc_lower:
        return "创建/创建"
    
    if 'make' in desc_lower:
        return "创建/制作"
    
    if 'build' in desc_lower:
        return "构建/构建"
    
    if 'control' in desc_lower:
        return "控制/控制"
    
    if 'operate' in desc_lower:
        return "操作/操作"
    
    if 'admin' in desc_lower:
        return "管理/管理"
    
    if 'watch' in desc_lower:
        return "监控/监控"
    
    if 'observe' in desc_lower:
        return "监控/监控"
    
    if 'cron' in desc_lower:
        return "调度/Cron"
    
    if 'timer' in desc_lower:
        return "调度/计时器"
    
    if 'job' in desc_lower:
        return "调度/任务"
    
    if 'queue' in desc_lower:
        return "调度/队列"
    
    if 'config' in desc_lower:
        return "配置/配置"
    
    if 'setting' in desc_lower:
        return "配置/设置"
    
    if 'preference' in desc_lower:
        return "配置/偏好"
    
    if 'option' in desc_lower:
        return "配置/选项"
    
    if 'logger' in desc_lower:
        return "日志/Logger"
    
    if 'trace' in desc_lower:
        return "追踪/追踪"
    
    if 'audit' in desc_lower:
        return "审计/审计"
    
    if 'cache' in desc_lower:
        return "缓存/缓存"
    
    if 'caching' in desc_lower:
        return "缓存/缓存"
    
    if 'memory' in desc_lower:
        return "内存/内存"
    
    if 'login' in desc_lower:
        return "认证/登录"
    
    if 'oauth' in desc_lower:
        return "认证/OAuth"
    
    if 'sso' in desc_lower:
        return "认证/SSO"
    
    if 'token' in desc_lower:
        return "认证/Token"
    
    if 'jwt' in desc_lower:
        return "认证/JWT"
    
    if 'decrypt' in desc_lower:
        return "加密/解密"
    
    if 'crypto' in desc_lower:
        return "加密/加密"
    
    if 'cipher' in desc_lower:
        return "加密/密码"
    
    if 'hash' in desc_lower:
        return "加密/哈希"
    
    if 'scanner' in desc_lower:
        return "扫描/扫描"
    
    if 'detection' in desc_lower:
        return "检测/检测"
    
    if 'optimize' in desc_lower:
        return "优化/优化"
    
    if 'speed' in desc_lower:
        return "性能/速度"
    
    if 'clean' in desc_lower:
        return "清理/清理"
    
    if 'cleanup' in desc_lower:
        return "清理/清理"
    
    if 'tidy' in desc_lower:
        return "清理/整理"
    
    if 'format' in desc_lower:
        return "格式/格式"
    
    if 'lint' in desc_lower:
        return "Lint/Lint"
    
    if 'readme' in desc_lower:
        return "文档/README"
    
    if 'guide' in desc_lower:
        return "文档/指南"
    
    if 'book' in desc_lower:
        return "书籍/书籍"
    
    if 'chapter' in desc_lower:
        return "书籍/章节"
    
    if 'read' in desc_lower:
        return "读取/读取"
    
    if 'reading' in desc_lower:
        return "读取/阅读"
    
    if 'paper' in desc_lower:
        return "论文/论文"
    
    if 'research' in desc_lower:
        return "科研/科研"
    
    if 'scientific' in desc_lower:
        return "科研/科学"
    
    if 'scholar' in desc_lower:
        return "科研/学者"
    
    if 'study' in desc_lower:
        return "学习/学习"
    
    if 'practice' in desc_lower:
        return "练习/练习"
    
    if 'exercise' in desc_lower:
        return "练习/练习"
    
    if 'quiz' in desc_lower:
        return "考试/测验"
    
    if 'exam' in desc_lower:
        return "考试/考试"
    
    if 'grade' in desc_lower:
        return "评分/评分"
    
    if 'score' in desc_lower:
        return "评分/评分"
    
    if 'evaluation' in desc_lower:
        return "评估/评估"
    
    if 'interview' in desc_lower:
        return "面试/面试"
    
    if 'offer' in desc_lower:
        return "招聘/Offer"
    
    if 'job' in desc_lower:
        return "招聘/工作"
    
    if 'career' in desc_lower:
        return "职业/职业"
    
    if 'resume' in desc_lower:
        return "招聘/简历"
    
    if 'cv' in desc_lower:
        return "招聘/CV"
    
    if 'hr' in desc_lower:
        return "人力/HR"
    
    if 'human' in desc_lower:
        return "人力/人力"
    
    if 'employee' in desc_lower:
        return "人力/员工"
    
    if 'staff' in desc_lower:
        return "人力/员工"
    
    if 'payroll' in desc_lower:
        return "人力/薪资"
    
    if 'legal' in desc_lower:
        return "法律/法律"
    
    if 'law' in desc_lower:
        return "法律/法律"
    
    if 'contract' in desc_lower:
        return "法律/合同"
    
    if 'compliance' in desc_lower:
        return "法律/合规"
    
    if 'patent' in desc_lower:
        return "法律/专利"
    
    if 'tax' in desc_lower:
        return "财务/税务"
    
    if 'accounting' in desc_lower:
        return "财务/会计"
    
    if 'finance' in desc_lower:
        return "财务/财务"
    
    if 'billing' in desc_lower:
        return "财务/账单"
    
    if 'invoice' in desc_lower:
        return "财务/发票"
    
    if 'supply' in desc_lower:
        return "供应链/供应链"
    
    if 'logistics' in desc_lower:
        return "供应链/物流"
    
    if 'inventory' in desc_lower:
        return "供应链/库存"
    
    if 'warehouse' in desc_lower:
        return "供应链/仓库"
    
    if 'shipping' in desc_lower:
        return "供应链/运输"
    
    if 'real estate' in desc_lower:
        return "房产/房产"
    
    if 'property' in desc_lower:
        return "房产/房产"
    
    if 'housing' in desc_lower:
        return "房产/住房"
    
    if 'construction' in desc_lower:
        return "建筑/建筑"
    
    if 'architecture' in desc_lower:
        return "建筑/建筑"
    
    if 'robot' in desc_lower:
        return "机器人/机器人"
    
    if 'robotics' in desc_lower:
        return "机器人/机器人"
    
    if 'iot' in desc_lower:
        return "IoT/IoT"
    
    if 'sensor' in desc_lower:
        return "IoT/传感器"
    
    if 'embedded' in desc_lower:
        return "嵌入式/嵌入式"
    
    if 'fpga' in desc_lower:
        return "硬件/FPGA"
    
    if 'hardware' in desc_lower:
        return "硬件/硬件"
    
    if 'kicad' in desc_lower:
        return "硬件/KiCad"
    
    if 'pcb' in desc_lower:
        return "硬件/PCB"
    
    if 'circuit' in desc_lower:
        return "硬件/电路"
    
    if 'arduino' in desc_lower:
        return "硬件/Arduino"
    
    if 'raspberry' in desc_lower:
        return "硬件/RaspberryPi"
    
    if 'map' in desc_lower:
        return "地理/地图"
    
    if 'terrain' in desc_lower:
        return "地理/地形"
    
    if 'geotiff' in desc_lower:
        return "地理/GeoTIFF"
    
    if 'satellite' in desc_lower:
        return "地理/卫星"
    
    if 'remote' in desc_lower:
        return "远程/远程"
    
    if 'sandbox' in desc_lower:
        return "运行/沙箱"
    
    if 'runtime' in desc_lower:
        return "运行/运行时"
    
    if 'container' in desc_lower:
        return "容器/容器"
    
    if 'vm' in desc_lower:
        return "运行/虚拟机"
    
    if 'virtual' in desc_lower:
        return "运行/虚拟化"
    
    if 'docker' in desc_lower:
        return "容器/Docker"
    
    if 'sdk' in desc_lower:
        return "SDK/SDK"
    
    if 'utility' in desc_lower:
        return "工具/工具"
    
    if 'linux' in desc_lower:
        return "系统/Linux"
    
    if 'windows' in desc_lower:
        return "系统/Windows"
    
    if 'mac' in desc_lower:
        return "系统/Mac"
    
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
    
    cat = get_v19_category(name, desc)
    
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