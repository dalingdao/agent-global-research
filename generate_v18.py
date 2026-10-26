#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V18 Final: Add 25+ new categories to reach 100+ large categories
"""

import re
import sys
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

with open(r"D:\testa\all-tools-final-v5.txt", "r", encoding="utf-8") as f:
    tools = f.readlines()

print(f"Total tools: {len(tools)}")

# Read V17 function
with open(r"D:\testa\generate_v17_final.py", "r", encoding="utf-8") as f:
    v17_code = f.read()

# Extract the function
func_start = v17_code.find("def get_v17_category")
func_end = v17_code.find("# Count categories")

if func_start != -1 and func_end != -1:
    v17_func = v17_code[func_start:func_end]
    exec(v17_func)
else:
    print("Error extracting function")
    sys.exit(1)

def get_v18_category(name, desc):
    name_lower = name.lower()
    desc_lower = desc.lower()
    
    # First try V17 categorization
    cat = get_v17_category(name, desc)
    
    # If it's still "其他/综合工具", try V18 additional patterns
    if cat != "其他/综合工具":
        return cat
    
    # ===== V18 NEW: More specific patterns =====
    
    # AI/LLM specific patterns
    if 'model' in desc_lower and 'tiny' in desc_lower:
        return "AI/LLM/小模型"
    if 'model' in desc_lower and 'device' in desc_lower:
        return "AI/LLM/设备模型"
    if 'rag' in desc_lower and 'everything' in desc_lower:
        return "AI/RAG/通用RAG"
    if 'api' in desc_lower and '1000' in desc_lower:
        return "API/API网关"
    if 'agent' in desc_lower and 'intelligence' in desc_lower:
        return "AI/LLM/智能体"
    if 'agent' in desc_lower and 'coding' in desc_lower:
        return "编码/代码Agent"
    if 'coding agent' in desc_lower:
        return "编码/代码Agent"
    if 'claude code' in desc_lower:
        return "编码/代码工具"
    if 'cursor' in desc_lower and 'code' in desc_lower:
        return "编码/代码工具"
    if 'codex' in desc_lower and 'code' in desc_lower:
        return "编码/代码工具"
    if 'gemini' in desc_lower and 'code' in desc_lower:
        return "编码/代码工具"
    if 'source control' in desc_lower and 'agent' in desc_lower:
        return "Agent/版本控制"
    if 'backup' in desc_lower and 'postgres' in desc_lower:
        return "数据库/备份"
    if 'backup' in desc_lower and 'tool' in desc_lower:
        return "备份/备份工具"
    if 'alternative' in desc_lower and 'bot' in desc_lower:
        return "AI/LLM/替代"
    if 'alternative' in desc_lower and 'muse' in desc_lower:
        return "AI/LLM/替代"
    if 'agent' in desc_lower and 'network' in desc_lower:
        return "Agent/网络"
    if 'agent' in desc_lower and 'team' in desc_lower:
        return "Agent/团队"
    if 'content discovery' in desc_lower:
        return "安全/扫描"
    if 'whatsapp' in desc_lower:
        return "通信/WhatsApp"
    if 'wasm' in desc_lower:
        return "编程语言/WASM"
    if 'wasm' in name_lower:
        return "编程语言/WASM"
    if 'workspace' in desc_lower and 'developer' in desc_lower:
        return "开发/工作区"
    if 'comics' in desc_lower:
        return "媒体/漫画"
    if 'manga' in desc_lower:
        return "媒体/漫画"
    if 'ebook' in desc_lower:
        return "文档/电子书"
    if 'serverless' in desc_lower and 'developer' in desc_lower:
        return "云/无服务器"
    if 'terminal' in desc_lower and 'agent' in desc_lower:
        return "编码/CLI Agent"
    if 'self-service' in desc_lower:
        return "DevOps/运维"
    if 'development environment' in desc_lower:
        return "开发/开发环境"
    if 'dev-setup' in desc_lower:
        return "开发/开发环境"
    if 'zero-config' in desc_lower and 'code' in desc_lower:
        return "编码/代码工具"
    if 'code flow' in desc_lower:
        return "编码/代码工具"
    if '渗透' in desc_lower:
        return "安全/渗透测试"
    if '扫描器' in desc_lower:
        return "安全/扫描"
    if 'vulnerability' in desc_lower and 'scan' in desc_lower:
        return "安全/漏洞扫描"
    if 'agentos' in desc_lower:
        return "Agent/操作系统"
    if 'portfolio' in desc_lower and 'trader' in desc_lower:
        return "金融/机器学习"
    if 'machine learning' in desc_lower and 'portfolio' in desc_lower:
        return "金融/机器学习"
    if 'deliberation' in desc_lower:
        return "AI/LLM/决策"
    if 'reinforcement learning' in desc_lower:
        return "AI/LLM/强化学习"
    if 'rl' in desc_lower and 'agent' in desc_lower:
        return "AI/LLM/强化学习"
    if 'ppo' in desc_lower:
        return "AI/LLM/强化学习"
    if 'android library' in desc_lower:
        return "移动/Android"
    if 'android' in desc_lower and 'library' in desc_lower:
        return "移动/Android"
    if 'harness preset' in desc_lower:
        return "Agent/预设"
    if 'browser' in desc_lower and 'test' in desc_lower:
        return "测试/浏览器测试"
    if 'interface design' in desc_lower:
        return "设计/原型设计"
    if 'prototyping' in desc_lower:
        return "设计/原型设计"
    if 'linux management' in desc_lower:
        return "系统/Linux管理"
    if 'linux' in desc_lower and 'script' in desc_lower:
        return "系统/Linux管理"
    if 'replicate data' in desc_lower:
        return "数据/数据同步"
    if 'data warehouse' in desc_lower:
        return "数据/数据仓库"
    if 'server management' in desc_lower:
        return "系统/服务器管理"
    if 'aws usage' in desc_lower:
        return "云/AWS"
    if 'project management' in desc_lower:
        return "项目管理/项目管理"
    if 'qq' in desc_lower:
        return "通信/QQ"
    if 'rust' in desc_lower and 'build' in desc_lower:
        return "编程语言/Rust构建"
    if 'android automation' in desc_lower:
        return "移动/Android自动化"
    if 'vision language' in desc_lower and 'automation' in desc_lower:
        return "移动/Android自动化"
    if 'graphql' in desc_lower:
        return "API/GraphQL"
    if 'dag' in desc_lower and 'framework' in desc_lower:
        return "框架/DAG框架"
    if 'mind map' in desc_lower:
        return "开发/思维导图"
    if 'health check' in desc_lower:
        return "可观测性/健康检查"
    if 'status check' in desc_lower:
        return "可观测性/健康检查"
    if 'web performance' in desc_lower:
        return "可观测性/Web性能"
    if 'reproducible' in desc_lower and 'development' in desc_lower:
        return "开发/开发环境"
    if 'meta repo' in desc_lower:
        return "开发/元仓库"
    if 'mcp app' in desc_lower:
        return "框架/MCP框架"
    if 'agile retrospective' in desc_lower:
        return "项目管理/回顾工具"
    if 'copy text' in desc_lower:
        return "工具/文本复制"
    if 'api spec' in desc_lower and 'code' in desc_lower:
        return "API/代码生成"
    if 'type-safe' in desc_lower and 'code' in desc_lower:
        return "API/代码生成"
    if 'social simulation' in desc_lower:
        return "AI/LLM/模拟"
    if 'chatbot' in desc_lower:
        return "机器人/聊天机器人"
    if 'web framework' in desc_lower:
        return "编程语言/Web框架"
    if 'django' in desc_lower:
        return "编程语言/Django"
    if 'python web' in desc_lower:
        return "编程语言/PythonWeb"
    if 'quantify' in desc_lower:
        return "数据/数据工具"
    if 'sandbox' in desc_lower:
        return "运行/沙箱"
    if 'architecture decision' in desc_lower:
        return "文档/架构决策"
    if 'adr' in desc_lower:
        return "文档/架构决策"
    if 'music composition' in desc_lower:
        return "音乐/作曲"
    if 'sample-based' in desc_lower:
        return "音乐/作曲"
    if 'alternative' in desc_lower and 'notion' in desc_lower:
        return "笔记/Notion替代"
    if 'alternative' in desc_lower and 'otter' in desc_lower:
        return "生产力/笔记替代"
    if 'alternative' in desc_lower and 'granola' in desc_lower:
        return "生产力/笔记替代"
    if 'steam' in desc_lower:
        return "游戏/Steam"
    if 'ebpf' in desc_lower:
        return "可观测性/eBPF"
    if 'room' in desc_lower and 'agent' in desc_lower:
        return "Agent/协作"
    if 'multimodal' in desc_lower:
        return "AI/LLM/多模态"
    if 'meteorological' in desc_lower:
        return "气象/气象工具"
    if 'entity relation' in desc_lower:
        return "数据库/ER图"
    if 'erd' in desc_lower:
        return "数据库/ER图"
    if 'html' in desc_lower and 'challenge' in desc_lower:
        return "Web/Web挑战"
    if 'developer resource' in desc_lower:
        return "参考/资源列表"
    if 'resource' in desc_lower and 'developer' in desc_lower:
        return "参考/资源列表"
    if 'decorator' in desc_lower:
        return "编程语言/Go工具"
    if 'notification' in desc_lower and 'tool' in desc_lower:
        return "通信/通知工具"
    if 'cloudformation' in desc_lower:
        return "DevOps/CFN检查"
    if 'lint' in desc_lower and 'cloudformation' in desc_lower:
        return "DevOps/CFN检查"
    if 'pi-agent' in desc_lower:
        return "Agent/学习"
    if 'terraform' in desc_lower and 'migration' in desc_lower:
        return "DevOps/Terraform"
    if 'cmdb' in desc_lower:
        return "系统/ITSM"
    if 'it service management' in desc_lower:
        return "系统/ITSM"
    if 'tutorial' in desc_lower and 'agent' in desc_lower:
        return "AI/LLM/教程"
    if 'figma' in desc_lower and 'mcp' in desc_lower:
        return "MCP/Figma"
    if 'recall' in desc_lower and 'coding' in desc_lower:
        return "编码/代码搜索"
    if 'git blame' in desc_lower:
        return "编码/代码搜索"
    if 'multimodal data' in desc_lower:
        return "AI/LLM/多模态"
    if 'cryptanalysis' in desc_lower:
        return "安全/密码分析"
    if 'osint' in desc_lower:
        return "安全/OSINT"
    if 'digital forensics' in desc_lower:
        return "安全/数字取证"
    if 'ssh-agent' in desc_lower:
        return "安全/密钥管理"
    if 'gpg-agent' in desc_lower:
        return "安全/密钥管理"
    if 'keychain' in desc_lower:
        return "安全/密钥管理"
    if 'text span' in desc_lower:
        return "AI/NLP/标注"
    if 'annotation' in desc_lower and 'text' in desc_lower:
        return "AI/NLP/标注"
    if 'schema migration' in desc_lower:
        return "数据库/Schema迁移"
    if 'postgres schema' in desc_lower:
        return "数据库/Schema迁移"
    if 'declarative' in desc_lower and 'postgres' in desc_lower:
        return "数据库/Schema迁移"
    if 'postgresql' in desc_lower and 'backup' in desc_lower:
        return "数据库/备份"
    if 'point-in-time' in desc_lower:
        return "备份/PITR"
    if 'restore' in desc_lower and 'verification' in desc_lower:
        return "备份/恢复验证"
    if 'rust' in desc_lower and 'wasm' in desc_lower:
        return "编程语言/RustWASM"
    if 'workflow tool' in desc_lower:
        return "工具/工作流工具"
    if 'snippets' in desc_lower:
        return "开发/代码片段"
    if 'notes' in desc_lower and 'http' in desc_lower:
        return "开发/笔记HTTP"
    if 'opds' in desc_lower:
        return "文档/OPDS"
    if 'kobo' in desc_lower:
        return "文档/Kobo"
    if 'koreader' in desc_lower:
        return "文档/KOReader"
    if 'spin' in desc_lower and 'serverless' in desc_lower:
        return "云/Spin"
    if 'free coding' in desc_lower:
        return "编码/免费代码"
    if 'terminal' in desc_lower and 'free' in desc_lower:
        return "编码/免费CLI"
    if 'cobalt strike' in desc_lower:
        return "安全/CobaltStrike"
    if 'powershell' in desc_lower:
        return "安全/PowerShell"
    if 'memory load' in desc_lower:
        return "安全/内存加载"
    if 'fileless' in desc_lower:
        return "安全/无文件"
    if 'port scan' in desc_lower:
        return "安全/端口扫描"
    if 'service identification' in desc_lower:
        return "安全/服务识别"
    if 'network asset' in desc_lower:
        return "安全/网络资产"
    if 'password audit' in desc_lower:
        return "安全/密码审计"
    if 'vulnerability exploitation' in desc_lower:
        return "安全/漏洞利用"
    if 'password read' in desc_lower:
        return "安全/密码读取"
    if 'getshell' in desc_lower:
        return "安全/GetShell"
    if 'discord' in desc_lower:
        return "通信/Discord"
    if 'multi-perspective' in desc_lower:
        return "AI/LLM/多视角"
    if 'decision' in desc_lower and 'agent' in desc_lower:
        return "AI/LLL/决策"
    if 'library' in desc_lower and 'reinforcement' in desc_lower:
        return "AI/LLM/强化学习"
    if 'agent' in desc_lower and 'component' in desc_lower:
        return "AI/LLM/组件"
    if 'android' in desc_lower and 'library' in desc_lower:
        return "移动/Android库"
    if 'demo project' in desc_lower:
        return "移动/演示项目"
    if 'deepseek harness' in desc_lower:
        return "Agent/DeepSeek"
    if 'preset' in desc_lower:
        return "Agent/预设"
    if 'two-phase' in desc_lower:
        return "Agent/两阶段"
    if 'bootstrap' in desc_lower:
        return "Agent/引导"
    if 'browser' in desc_lower and 'test' in desc_lower:
        return "测试/浏览器测试"
    if 'expect' in desc_lower and 'agent' in desc_lower:
        return "测试/Agent测试"
    if 'figcraft' in desc_lower:
        return "设计/FigmaCraft"
    if 'clean-room' in desc_lower:
        return "设计/清洁室"
    if 'reimplementation' in desc_lower:
        return "设计/重新实现"
    if 'linux' in desc_lower and 'script' in desc_lower:
        return "系统/Linux脚本"
    if 'all-in-one' in desc_lower and 'linux' in desc_lower:
        return "系统/Linux全能"
    if 'replicate' in desc_lower and 'postgres' in desc_lower:
        return "数据/Postgres复制"
    if 'data warehouse' in desc_lower:
        return "数据/数据仓库"
    if 'cost effective' in desc_lower:
        return "数据/成本效益"
    if 'free' in desc_lower and 'self-hosted' in desc_lower:
        return "自托管/免费自托管"
    if 'server management' in desc_lower:
        return "系统/服务器管理"
    if 'aws' in desc_lower and 'usage' in desc_lower:
        return "云/AWS使用"
    if 'project management' in desc_lower and 'tiny' in desc_lower:
        return "项目管理/小型团队"
    if 'qq' in desc_lower:
        return "通信/QQ"
    if 'bridge' in desc_lower and 'qq' in desc_lower:
        return "通信/QQ桥"
    if 'onbot' in desc_lower:
        return "通信/OneBot"
    if 'snowluma' in desc_lower:
        return "通信/SnowLuma"
    if 'rust' in desc_lower and 'build' in desc_lower:
        return "编程语言/Rust构建"
    if 'blazing fast' in desc_lower:
        return "编程语言/快速构建"
    if 'android automation' in desc_lower:
        return "移动/Android自动化"
    if 'vision language' in desc_lower:
        return "AI/CV/视觉语言"
    if 'graphql server' in desc_lower:
        return "API/GraphQL服务器"
    if 'schema-first' in desc_lower:
        return "API/SchemaFirst"
    if 'python library' in desc_lower and 'graphql' in desc_lower:
        return "编程语言/PythonGraphQL"
    if 'cpp' in desc_lower and 'dag' in desc_lower:
        return "编程语言/CPPDAG"
    if 'python' in desc_lower and 'dag' in desc_lower:
        return "编程语言/PythonDAG"
    if 'flow graph' in desc_lower:
        return "框架/流程图"
    if 'parallel computation' in desc_lower:
        return "框架/并行计算"
    if 'awesome-cpp' in desc_lower:
        return "参考/awesome-cpp"
    if 'cross-platform' in desc_lower and 'framework' in desc_lower:
        return "框架/跨平台框架"
    if 'no third-party' in desc_lower:
        return "框架/无依赖框架"
    if 'terminal-based' in desc_lower:
        return "终端/终端工具"
    if 'keyboard-centric' in desc_lower:
        return "终端/键盘工具"
    if 'hackers' in desc_lower:
        return "黑客/黑客工具"
    if 'health status' in desc_lower:
        return "可观测性/健康状态"
    if 'lightweight' in desc_lower and 'tool' in desc_lower:
        return "工具/轻量工具"
    if 'standalone' in desc_lower:
        return "工具/独立工具"
    if 'chromium' in desc_lower:
        return "浏览器/Chromium"
    if 'headless' in desc_lower:
        return "浏览器/无头"
    if 'performance metrics' in desc_lower:
        return "可观测性/性能指标"
    if 'monitoring tool' in desc_lower:
        return "可观测性/监控工具"
    if 'development environment' in desc_lower:
        return "开发/开发环境"
    if 'reproducible' in desc_lower:
        return "开发/可重现"
    if 'many repos' in desc_lower:
        return "开发/多仓库"
    if 'monolithic' in desc_lower:
        return "开发/单体仓库"
    if 'typescript framework' in desc_lower:
        return "编程语言/TypeScript框架"
    if 'mcp app' in desc_lower:
        return "框架/MCP应用框架"
    if 'chatgpt app' in desc_lower:
        return "框架/ChatGPT应用框架"
    if 'type-safe' in desc_lower:
        return "框架/类型安全"
    if 'multi-agent' in desc_lower and 'ppo' in desc_lower:
        return "AI/LLM/MultiAgentPPO"
    if 'implementation' in desc_lower and 'paper' in desc_lower:
        return "AI/LLM/论文实现"
    if 'agile' in desc_lower:
        return "项目管理/敏捷"
    if 'retrospective' in desc_lower:
        return "项目管理/回顾"
    if 'meeting tool' in desc_lower:
        return "项目管理/会议工具"
    if 'copy text' in desc_lower:
        return "工具/文本复制"
    if 'stop retyping' in desc_lower:
        return "工具/防重输"
    if 'api spec' in desc_lower:
        return "API/规范"
    if 'generate' in desc_lower and 'typescript' in desc_lower:
        return "编程语言/TypeScript生成"
    if 'api client' in desc_lower:
        return "API/API客户端"
    if 'hook' in desc_lower and 'vue' in desc_lower:
        return "框架/Vue钩子"
    if 'generative' in desc_lower:
        return "AI/LLM/生成式"
    if 'social simulation' in desc_lower:
        return "AI/LLM/社会模拟"
    if 'chatbot' in desc_lower:
        return "机器人/聊天机器人"
    if 'with ease' in desc_lower:
        return "机器人/易建机器人"
    if 'fastest' in desc_lower and 'python' in desc_lower:
        return "编程语言/Python最快"
    if 'web framework' in desc_lower:
        return "编程语言/Web框架"
    if 'django' in desc_lower:
        return "编程语言/Django"
    if 'rust' in desc_lower and 'actix' in desc_lower:
        return "编程语言/RustActix"
    if 'http server' in desc_lower:
        return "Web/HTTP服务器"
    if 'async' in desc_lower and 'type' in desc_lower:
        return "编程语言/异步类型"
    if 'open source' in desc_lower and 'tool' in desc_lower:
        return "开源/开源工具"
    if 'quantify' in desc_lower:
        return "数据/量化"
    if 'sqlite' in desc_lower:
        return "数据库/SQLite"
    if 'sandbox' in desc_lower:
        return "运行/沙箱"
    if 'self-hosted' in desc_lower:
        return "自托管/自托管"
    if 'e2b' in desc_lower:
        return "运行/E2B"
    if 'one machine' in desc_lower:
        return "运行/单机"
    if 'architecture decision' in desc_lower:
        return "文档/架构决策"
    if 'adr' in desc_lower:
        return "文档/ADR"
    if 'management' in desc_lower and 'publication' in desc_lower:
        return "文档/管理发布"
    if 'sample-based' in desc_lower:
        return "音乐/采样"
    if 'music composition' in desc_lower:
        return "音乐/作曲"
    if 'old school' in desc_lower:
        return "音乐/复古"
    if 'granola' in desc_lower:
        return "生产力/Granola替代"
    if 'otter' in desc_lower:
        return "生产力/Otter替代"
    if 'local-first' in desc_lower:
        return "生产力/本地优先"
    if 'steam' in desc_lower:
        return "游戏/Steam"
    if 'library categorizing' in desc_lower:
        return "游戏/库分类"
    if 'ebpf' in desc_lower:
        return "可观测性/eBPF"
    if 'agent' in desc_lower and 'traffic' in desc_lower:
        return "可观测性/流量Agent"
    if 'pre-encrypted' in desc_lower:
        return "安全/预加密"
    if 'rich context' in desc_lower:
        return "可观测性/丰富上下文"
    if 'room' in desc_lower and 'people' in desc_lower:
        return "Agent/房间"
    if 'metpy' in desc_lower:
        return "气象/MetPy"
    if 'meteorological' in desc_lower:
        return "气象/气象"
    if 'python' in desc_lower and 'visualization' in desc_lower:
        return "编程语言/Python可视化"
    if 'entity relation' in desc_lower:
        return "数据库/ER"
    if 'diagram' in desc_lower and 'generation' in desc_lower:
        return "图表/图表生成"
    if 'one html page' in desc_lower:
        return "Web/单页挑战"
    if 'without modern tools' in desc_lower:
        return "Web/无现代工具"
    if 'developer resource' in desc_lower:
        return "参考/开发者资源"
    if 'collaborative list' in desc_lower:
        return "参考/协作列表"
    if 'decorator' in desc_lower:
        return "编程语言/装饰器"
    if 'go interface' in desc_lower:
        return "编程语言/Go接口"
    if 'command line' in desc_lower:
        return "CLI/命令行"
    if 'notification' in desc_lower:
        return "通信/通知"
    if 'safe and simple' in desc_lower:
        return "通信/安全简单"
    if 'command line tool' in desc_lower:
        return "CLI/命令行工具"
    if 'cloudformation' in desc_lower:
        return "DevOps/CloudFormation"
    if 'linting' in desc_lower:
        return "Lint/Linting"
    if 'typescript' in desc_lower and 'mini' in desc_lower:
        return "编程语言/TypeScript迷你"
    if 'pi-agent' in desc_lower:
        return "Agent/PI-Agent"
    if 'from 0' in desc_lower:
        return "教育/从零开始"
    if 'terraform' in desc_lower:
        return "DevOps/Terraform"
    if 'opentofu' in desc_lower:
        return "DevOps/OpenTofu"
    if 'state migration' in desc_lower:
        return "DevOps/状态迁移"
    if 'gitops' in desc_lower:
        return "DevOps/GitOps"
    if 'cmdb' in desc_lower:
        return "系统/CMDB"
    if 'it service management' in desc_lower:
        return "系统/ITSM"
    if 'web based' in desc_lower:
        return "Web/WebBased"
    if 'project' in desc_lower and 'autogen' in desc_lower:
        return "AI/LLM/AutoGen项目"
    if 'tutorial' in desc_lower:
        return "教育/教程"
    if 'figma' in desc_lower:
        return "设计/Figma"
    if 'mcp server' in desc_lower:
        return "MCP/MCPServer"
    if 'design into' in desc_lower:
        return "设计/设计转代码"
    if 'framework-aware' in desc_lower:
        return "设计/框架感知"
    if 'push code back' in desc_lower:
        return "设计/代码回推"
    if 'instant recall' in desc_lower:
        return "编码/即时回忆"
    if 'coding agent' in desc_lower:
        return "编码/编码Agent"
    if 'search history' in desc_lower:
        return "编码/历史搜索"
    if 'git blame' in desc_lower:
        return "编码/GitBlame"
    if 'multimodal data' in desc_lower:
        return "AI/LLM/多模态数据"
    if 'machine learning project' in desc_lower:
        return "AI/LLM/ML项目"
    if 'cryptanalysis' in desc_lower:
        return "安全/密码分析"
    if 'weapon of math' in desc_lower:
        return "安全/数学武器"
    if 'dust' in desc_lower:
        return "安全/Dust"
    if 'osint' in desc_lower:
        return "安全/OSINT"
    if 'digital forensics' in desc_lower:
        return "安全/数字取证"
    if 'built in python' in desc_lower:
        return "编程语言/Python构建"
    if 'ssh-agent' in desc_lower:
        return "安全/SSH-Agent"
    if 'gpg-agent' in desc_lower:
        return "安全/GPG-Agent"
    if 'now in python' in desc_lower:
        return "编程语言/Python"
    if 'text span' in desc_lower:
        return "AI/NLP/文本跨度"
    if 'collaborative' in desc_lower and 'text' in desc_lower:
        return "AI/NLP/协作文本"
    if 'annotation tool' in desc_lower:
        return "AI/NLP/标注工具"
    if 'acl' in desc_lower:
        return "AI/NLP/ACL"
    if 'best demo' in desc_lower:
        return "AI/NLP/最佳演示"
    if 'postgres schema' in desc_lower:
        return "数据库/PostgresSchema"
    if 'terraform-style' in desc_lower:
        return "数据库/Terraform风格"
    if 'declarative' in desc_lower:
        return "数据库/声明式"
    if 'schema migration' in desc_lower:
        return "数据库/Schema迁移"
    if 'agent friendly' in desc_lower:
        return "数据库/Agent友好"
    
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
    
    cat = get_v18_category(name, desc)
    
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