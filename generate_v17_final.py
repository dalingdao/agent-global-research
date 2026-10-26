#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V17 Final: Complete standalone categorization
Goal: 100+ large categories, '其他/综合工具' < 500
"""

import re
import sys
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

with open(r"D:\testa\all-tools-final-v5.txt", "r", encoding="utf-8") as f:
    tools = f.readlines()

print(f"Total tools: {len(tools)}")

def get_v17_category(name, desc):
    name_lower = name.lower()
    desc_lower = desc.lower()
    
    # ===== MCP =====
    if 'mcp' in name_lower:
        return "MCP/其他"
    
    # ===== Skills =====
    if any(x in name_lower for x in ['claude-skill', 'codex-skill', 'cursor-skill', 'gemini-skill', 'openai-skill']):
        return "技能/官方技能"
    if 'skill' in name_lower or 'skills' in name_lower:
        if 'chinese' in name_lower or '中文' in name_lower:
            return "技能/中文技能"
        if 'prompt' in name_lower:
            return "技能/提示词技能"
        if 'writing' in name_lower or 'novel' in name_lower or 'story' in name_lower:
            return "技能/写作技能"
        if 'code' in name_lower or 'dev' in name_lower:
            return "技能/开发技能"
        if 'design' in name_lower or 'ui' in name_lower:
            return "技能/设计技能"
        if 'security' in name_lower:
            return "技能/安全技能"
        if 'data' in name_lower or 'analytics' in name_lower:
            return "技能/数据技能"
        if 'test' in name_lower or 'qa' in name_lower:
            return "技能/测试技能"
        return "技能/社区技能"
    if any(x in name_lower for x in ['caveman', 'humanizer', 'archify', 'distilly', 'prompt-master', 'promptfoo']):
        return "技能/提示词技能"
    if any(x in name_lower for x in ['khazix', 'ian-xiaohei', 'answer-me', 'chinese-novelist', 'nihaixia']):
        return "技能/中文技能"
    if any(x in name_lower for x in ['effective-html', 'acontext', 'natural-japanese', 'math-modeling', 'zhengxi', 'paper2code', 'vibe-motion', 'enterprise-ai']):
        return "技能/专业技能"
    if 'xiaohu-ip-studio' in name_lower:
        return "技能/配图技能"
    
    # ===== Agent Frameworks =====
    if any(x in name_lower for x in ['langchain', 'langgraph', 'crewai', 'llamaindex', 'autogen', 'llm-agent']):
        return "框架/Python框架"
    if 'agent' in name_lower and any(x in desc_lower for x in ['framework', 'runtime', 'platform', 'harness']):
        return "框架/通用框架"
    if any(x in name_lower for x in ['superpowers', 'ecc', 'deer-flow', 'ruflo', 'flowise', 'huginn']):
        return "框架/工作流框架"
    if any(x in name_lower for x in ['camel', 'eliza', 'coze', 'astrbot', 'openfang', 'edict', 'deepcode', 'bettafish', 'mini-swe', 'mycroft', 'maka', 'kagent', 'arcree', 'miroflow', 'mirothinker', 'sympozium', 'spacelab', 'agentx']):
        return "框架/社区框架"
    if any(x in name_lower for x in ['openclaude', 'opencli', 'fay', 'hive', 'invariant', 'aidd', 'veadk', 'kitaru']):
        return "框架/专业框架"
    if 'deepcode' in name_lower:
        return "框架/编码框架"
    if 'langalpha' in name_lower:
        return "框架/金融框架"
    if 'elephant-agent' in name_lower:
        return "框架/进化框架"
    if any(x in name_lower for x in ['web-use', 'browser-agent']):
        return "框架/浏览器框架"
    
    # ===== Coding Agents =====
    if any(x in name_lower for x in ['claude-code', 'codex', 'cursor', 'gemini-cli', 'openai-codex']):
        return "编码/官方Agent"
    if any(x in name_lower for x in ['coding-agent', 'code-agent', 'code-assistant', 'codewhale', 'jcode', 'cockpit-tools', 'anthology']):
        return "编码/社区Agent"
    if any(x in name_lower for x in ['open-code-review', 'qlib', 'anatomy', 'oh-my-pi', 'costrict', 'devsecops']):
        return "编码/专业Agent"
    if 'swival' in name_lower:
        return "编码/CLI Agent"
    if 'pilot' in name_lower:
        return "编码/工单Agent"
    
    # ===== Browser =====
    if any(x in name_lower for x in ['browser-use', 'steel-browser', 'browser-automation', 'puppeteer', 'playwright']):
        return "浏览器/自动化"
    if 'browser' in name_lower and any(x in desc_lower for x in ['automation', 'agent', 'scraping']):
        return "浏览器/爬虫"
    if any(x in name_lower for x in ['agent-reach', 'obscura', 'moli', 'ego-lite', 'cua']):
        return "浏览器/视觉"
    if any(x in name_lower for x in ['web-use', 'cdp']):
        return "浏览器/CDP"
    if 'browser' in name_lower:
        return "浏览器/其他"
    
    # ===== Data Collection =====
    if any(x in name_lower for x in ['scrapling', 'apify', 'firecrawl', 'crawl4ai', 'crawler', 'scraper']):
        return "数据/Web爬虫"
    if any(x in name_lower for x in ['scraping', 'crawling']) and any(x in desc_lower for x in ['web', 'data']):
        return "数据/Web爬虫"
    if any(x in name_lower for x in ['airbyte', 'huggingface', 'datasets', 'easy-dataset']):
        return "数据/数据集"
    if any(x in name_lower for x in ['seatunnel', 'risingwave', 'datasette', 'durable-streams']):
        return "数据/数据流"
    
    # ===== Tool Libraries =====
    if any(x in name_lower for x in ['tool-library', 'toolkit', 'tool-kit', 'tools-library']):
        return "工具/通用库"
    if ('tool' in name_lower or 'kit' in name_lower) and any(x in desc_lower for x in ['library', 'collection']):
        return "工具/专用库"
    if any(x in name_lower for x in ['awesome', 'collection', 'curated', 'list']):
        if any(x in name_lower for x in ['ai', 'agent', 'llm']):
            return "工具/AI集合"
        if any(x in name_lower for x in ['python', 'go', 'rust', 'java']):
            return "工具/语言集合"
        if any(x in name_lower for x in ['js', 'javascript', 'typescript', 'node', 'vue', 'react']):
            return "工具/前端集合"
        if any(x in name_lower for x in ['devops', 'docker', 'k8s', 'kubernetes']):
            return "工具/DevOps集合"
        if any(x in name_lower for x in ['security', 'pentest', 'hacking']):
            return "工具/安全集合"
        if any(x in name_lower for x in ['data', 'database', 'sql', 'nosql']):
            return "工具/数据集合"
        if any(x in name_lower for x in ['cloud', 'aws', 'azure', 'gcp']):
            return "工具/云集合"
        if any(x in name_lower for x in ['mobile', 'ios', 'android']):
            return "工具/移动集合"
        if any(x in name_lower for x in ['game', 'gaming']):
            return "工具/游戏集合"
        if any(x in name_lower for x in ['iot', 'embedded', 'robot']):
            return "工具/嵌入式集合"
        if any(x in name_lower for x in ['web', 'frontend', 'css', 'html']):
            return "工具/Web集合"
        if any(x in name_lower for x in ['backend', 'server', 'api']):
            return "工具/后端集合"
        if any(x in name_lower for x in ['network', 'security']):
            return "工具/网络集合"
        if any(x in name_lower for x in ['os', 'operating', 'linux', 'windows', 'mac']):
            return "工具/系统集合"
        return "工具/其他集合"
    
    # ===== Workflow Automation =====
    if any(x in name_lower for x in ['n8n', 'workflow', 'automation', 'zapier', 'make']):
        return "自动化/通用平台"
    if any(x in name_lower for x in ['kestra', 'activepieces', 'trigger', 'wireflow']):
        return "自动化/专用平台"
    if any(x in name_lower for x in ['airflow', 'dagster', 'prefect']):
        return "自动化/数据管道"
    if any(x in name_lower for x in ['xiaobei', 'xiaofeishu', 'aiwritex']):
        return "自动化/自媒体"
    if 'openilink' in name_lower:
        return "自动化/Bot平台"
    
    # ===== AI Models =====
    if any(x in name_lower for x in ['llama', 'gpt', 'chatgpt', 'claude', 'gemini', 'mistral', 'qwen', 'deepseek']):
        return "AI模型/开源模型"
    if any(x in name_lower for x in ['llm', 'large-language-model']):
        return "AI模型/模型库"
    if any(x in name_lower for x in ['markitdown', 'cl4r1t4s', 'funasr', 'applio', 'miru-ai']):
        return "AI模型/应用模型"
    if any(x in name_lower for x in ['whisper', 'tts', 'asr']):
        return "AI模型/语音模型"
    if any(x in name_lower for x in ['stable-diffusion', 'midjourney', 'dall-e']):
        return "AI模型/图像模型"
    if any(x in name_lower for x in ['mini-verl', 'ppo', 'grpo']):
        return "AI模型/训练模型"
    if any(x in name_lower for x in ['reevo', 'evolution']):
        return "AI模型/进化模型"
    if any(x in name_lower for x in ['plugmem', 'memory']):
        return "AI模型/记忆模型"
    
    # ===== NLP Tools =====
    if any(x in name_lower for x in ['nlp', 'text-analysis', 'sentiment', 'named-entity', 'ner']):
        return "AI/NLP/文本分析"
    if 'supervision' in name_lower:
        return "AI/NLP/监督工具"
    if any(x in name_lower for x in ['translation', 'translate']):
        return "AI/NLP/翻译"
    if any(x in name_lower for x in ['summarization', 'summary']):
        return "AI/NLP/摘要"
    if any(x in name_lower for x in ['ner', 'entity']):
        return "AI/NLP/实体识别"
    if any(x in name_lower for x in ['token', 'lemmatiz', 'stem']):
        return "AI/NLP/分词"
    if 'nlp' in name_lower or 'text' in name_lower:
        return "AI/NLP/其他"
    
    # ===== Computer Vision =====
    if any(x in name_lower for x in ['opencv', 'computer-vision', 'image-processing', 'cv-']):
        return "AI/CV/图像处理"
    if 'graphify' in name_lower:
        return "AI/CV/图形识别"
    if ('cv' in name_lower or 'vision' in name_lower) and any(x in desc_lower for x in ['image', 'video', 'object']):
        return "AI/CV/对象检测"
    if any(x in name_lower for x in ['ocr', 'text-detection']):
        return "AI/CV/OCR"
    if any(x in name_lower for x in ['face', 'detection']):
        return "AI/CV/人脸识别"
    
    # ===== RAG Tools =====
    if any(x in name_lower for x in ['rag', 'retrieval-augmented', 'vector-db']):
        return "AI/RAG/检索"
    if any(x in name_lower for x in ['rag-techniques', 'code-review-graph', 'context-mode', 'mergekit']):
        return "AI/RAG/增强"
    if any(x in name_lower for x in ['embedding', 'vector', 'index']):
        return "AI/RAG/向量"
    
    # ===== Database Tools =====
    if any(x in name_lower for x in ['sql', 'postgres', 'mysql', 'mongodb', 'redis', 'elasticsearch']):
        return "数据库/关系型"
    if ('database' in name_lower or name_lower.startswith('db-')) and any(x in desc_lower for x in ['tool', 'query', 'manage']):
        return "数据库/管理工具"
    if any(x in name_lower for x in ['dbeaver', 'tidb', 'bytebase', 'doris', 'prisma', 'dbx', 'vanna']):
        return "数据库/客户端"
    if any(x in name_lower for x in ['seatunnel', 'risingwave', 'datasette', 'gormt']):
        return "数据库/数据同步"
    if 'netbox' in name_lower:
        return "数据库/网络设备"
    
    # ===== Cloud Tools =====
    if any(x in name_lower for x in ['aws', 'azure', 'gcp', 'google-cloud', 'cloudflare']):
        return "云/云平台"
    if ('cloud' in name_lower or 'serverless' in name_lower or 'lambda' in name_lower or 'function' in name_lower) and any(x in desc_lower for x in ['service', 'tool']):
        return "云/无服务器"
    if any(x in name_lower for x in ['appwrite', '1panel', 'nacos', 'go-zero', 'kubesphere']):
        return "云/管理工具"
    if any(x in name_lower for x in ['docker', 'kubernetes', 'k8s']):
        return "云/容器"
    if any(x in name_lower for x in ['minio', 'object-store']):
        return "云/对象存储"
    if 'nixopus' in name_lower:
        return "云/基础设施"
    
    # ===== DevOps Tools =====
    if any(x in name_lower for x in ['docker', 'kubernetes', 'k8s', 'terraform', 'ansible', 'jenkins', 'gitlab']):
        return "DevOps/CI/CD"
    if any(x in name_lower for x in ['devops', 'cicd', 'deployment', 'infrastructure']):
        return "DevOps/基础设施"
    if any(x in name_lower for x in ['sealos', 'labring']):
        return "DevOps/管理平台"
    if any(x in name_lower for x in ['arthas', 'ast-grep', 'prowler', 'lynis', 'reviewdog', 'winmerge', 'arkade', 'swiftbar']):
        return "DevOps/开发工具"
    if any(x in name_lower for x in ['caz', 'phpmetrics', 'cf-nag', 'loggie', 'saml-tool', 'kibana-tool']):
        return "DevOps/质量工具"
    if 'devsecops' in name_lower:
        return "DevOps/安全"
    
    # ===== Observability =====
    if any(x in name_lower for x in ['grafana', 'prometheus', 'datadog']):
        return "可观测性/监控"
    if any(x in name_lower for x in ['logging', 'monitoring', 'tracing']):
        return "可观测性/日志"
    if ('monitor' in name_lower or 'logging' in name_lower or 'metrics' in name_lower or 'alerting' in name_lower) and any(x in desc_lower for x in ['tool', 'service']):
        return "可观测性/告警"
    if any(x in name_lower for x in ['worldmonitor', 'trends-radar', 'headroom', 'langfuse', 'signoz', 'opik', 'mlflow', 'phoenix', 'openinference']):
        return "可观测性/AI监控"
    if any(x in name_lower for x in ['pinpoint', 'viztracer', 'micrometer', 'redelk', 'sysmontools', 'traceway', 'perfmon', 'coroot']):
        return "可观测性/性能分析"
    if any(x in name_lower for x in ['longview', 'linode']):
        return "可观测性/Linode"
    
    # ===== Security Tools =====
    if any(x in name_lower for x in ['security', 'pentest', 'vulnerability', 'firewall', 'crypto', 'encryption']):
        return "安全/渗透测试"
    if 'auth' in name_lower:
        return "安全/认证"
    if ('security' in name_lower or 'safe' in name_lower or 'protect' in name_lower) and any(x in desc_lower for x in ['tool', 'scan']):
        return "安全/扫描"
    if any(x in name_lower for x in ['pentagi', 'lynis', 'prowler', 'casdoor', 'infisical', 'sops']):
        return "安全/平台"
    if any(x in name_lower for x in ['merlin', 'mosint', 'ssrfmap', 'sstimap', 'xspear', 'loki', 'qu1cksc0pe', 'aiscan']):
        return "安全/分析"
    if any(x in name_lower for x in ['argus', 'soc', 'siem']):
        return "安全/SOC"
    if 'viper' in name_lower:
        return "安全/红队"
    if any(x in name_lower for x in ['covertutils', 'backdoor']):
        return "安全/后门"
    if any(x in name_lower for x in ['ssh', 'tpm', 'agent']):
        return "安全/SSH"
    
    # ===== Robotics & IoT =====
    if any(x in name_lower for x in ['robotics', 'robot']):
        return "机器人/机器人"
    if any(x in name_lower for x in ['iot', 'sensor', 'embedded', 'fpga']):
        return "机器人/IoT"
    if any(x in name_lower for x in ['drone', 'uav']):
        return "机器人/无人机"
    if any(x in name_lower for x in ['industrial', 'factory']):
        return "机器人/工业"
    if any(x in name_lower for x in ['fpga', 'prjxray']):
        return "机器人/FPGA"
    
    # ===== Low-Code =====
    if any(x in name_lower for x in ['dify', 'flowise', 'jeecgboot', 'tooljet', '1panel', 'nocobase', 'silex']):
        return "低代码/应用开发"
    if any(x in name_lower for x in ['low-code', 'no-code', 'lowcode']):
        return "低代码/通用"
    if any(x in name_lower for x in ['bubble', 'adalo']):
        return "低代码/SaaS"
    
    # ===== API Tools =====
    if any(x in name_lower for x in ['api', 'rest', 'graphql', 'grpc', 'webhook']):
        return "API/通用"
    if any(x in name_lower for x in ['hoppscotch', 'copilotkit', 'googleworkspace']):
        return "API/客户端"
    if any(x in name_lower for x in ['swagger', 'openapi']):
        return "API/文档"
    if any(x in name_lower for x in ['postman', 'insomnia']):
        return "API/测试"
    if any(x in name_lower for x in ['rate-limit', 'ratelimit', 'rate.limit']):
        return "API/限流"
    
    # ===== Knowledge Management =====
    if any(x in name_lower for x in ['siyuan', 'khoj', 'context7', 'notion', 'obsidian']):
        return "知识/笔记"
    if any(x in name_lower for x in ['knowledge', 'note', 'wiki', 'docs']):
        return "知识/文档"
    if any(x in name_lower for x in ['weknora', 'unstructured', 'monkeycode', 'tooluniverse', 'koala-ai']):
        return "知识/知识库"
    if any(x in name_lower for x in ['confluence', 'mediawiki']):
        return "知识/Wiki"
    if any(x in name_lower for x in ['agentero', 'powercontext']):
        return "知识/科研"
    
    # ===== Business Intelligence =====
    if any(x in name_lower for x in ['metabase', 'posthog', 'analytics', 'bi-']):
        return "分析/BI"
    if any(x in desc_lower for x in ['business-intelligence', 'analytics', 'dashboard']):
        return "分析/仪表盘"
    if any(x in name_lower for x in ['openmetadata', 'sacred']):
        return "分析/数据目录"
    
    # ===== Investment/Quant =====
    if any(x in name_lower for x in ['qlib', 'stock', 'trading']):
        return "金融/交易"
    if any(x in name_lower for x in ['investment', 'quant', 'fincept', 'ai-berkshire', 'finnewshunter', 'langalpha']):
        return "金融/分析"
    if any(x in name_lower for x in ['finance', 'banking', 'payment']):
        return "金融/财务"
    if any(x in name_lower for x in ['crypto', 'bitcoin', 'ethereum']):
        return "金融/加密货币"
    
    # ===== Productivity =====
    if any(x in name_lower for x in ['productivity', 'notes', 'task', 'project', 'todo', 'calendar', 'reminder']):
        return "生产力/任务管理"
    if 'productivity' in name_lower and any(x in desc_lower for x in ['tool', 'app']):
        return "生产力/通用"
    if any(x in name_lower for x in ['cherry-studio', 'cowagent', 'nanobot', 'leon']):
        return "生产力/AI助手"
    if any(x in name_lower for x in ['planning-with-files', 'repomix', 'hermes-desktop', 'noi', 'classisland', 'spacebot', 'offerpilot']):
        return "生产力/协作"
    if 'pogo' in name_lower:
        return "生产力/服务器"
    if 'trrex' in name_lower:
        return "生产力/剪贴板"
    if 'lemonpush' in name_lower:
        return "生产力/推送"
    
    # ===== Design Tools =====
    if any(x in name_lower for x in ['design', 'ui', 'ux', 'figma', 'sketch', 'illustrator', 'photoshop']):
        return "设计/UI/UX"
    if ('design' in name_lower or 'ui-ux' in name_lower) and any(x in desc_lower for x in ['tool', 'creator']):
        return "设计/图形设计"
    if any(x in name_lower for x in ['aseprite', 'openmontage', 'ppt-master', 'next-ai-draw-io', 'onlook', 'pascalorg', 'drawnix', 'eigent', 'nodeppt', 'app-store-screenshots']):
        return "设计/演示"
    if any(x in name_lower for x in ['excalidraw', 'prevue', 'bonzomatic']):
        return "设计/绘图"
    if any(x in name_lower for x in ['shader', 'glsl']):
        return "设计/着色器"
    if any(x in name_lower for x in ['animation', '3d', 'blender', 'unity', 'unreal']):
        return "设计/3D"
    if 'figures4papers' in name_lower:
        return "设计/学术图表"
    if 'nika-character' in name_lower:
        return "设计/角色设计"
    
    # ===== Social Media =====
    if any(x in name_lower for x in ['social', 'twitter', 'facebook', 'instagram', 'linkedin', 'tiktok']):
        return "社交/发布"
    if 'social-media' in name_lower and any(x in desc_lower for x in ['tool', 'platform']):
        return "社交/分析"
    if any(x in name_lower for x in ['postiz', 'social-media-scheduling']):
        return "社交/调度"
    if any(x in name_lower for x in ['waoowaoo', 'toonflow', 'ai-goofish', 'xiaobei', 'aiwritex', 'openilink', 'xiaofeishu']):
        return "社交/创作"
    
    # ===== E-commerce =====
    if any(x in name_lower for x in ['e-commerce', 'ecommerce', 'shop', 'commerce']):
        return "电商/平台"
    if any(x in name_lower for x in ['cart', 'checkout', 'payment']):
        return "电商/支付"
    if any(x in name_lower for x in ['wecommerce', 'shopify', 'woocommerce']):
        return "电商/独立站"
    
    # ===== Marketing =====
    if any(x in name_lower for x in ['marketing', 'seo', 'sem', 'ads', 'advertising']):
        return "营销/广告"
    if 'campaign' in name_lower:
        return "营销/活动"
    if any(x in name_lower for x in ['email', 'newsletter', 'mailchimp']):
        return "营销/邮件"
    if any(x in name_lower for x in ['content', 'blog', 'article']):
        return "营销/内容"
    
    # ===== Sales & CRM =====
    if any(x in name_lower for x in ['crm', 'sales', 'lead', 'pipeline', 'deal']):
        return "销售/CRM"
    if any(x in name_lower for x in ['salesforce', 'hubspot', 'zoho']):
        return "销售/SaaS"
    
    # ===== Education =====
    if any(x in name_lower for x in ['education', 'learning', 'course', 'training']):
        return "教育/学习"
    if any(x in name_lower for x in ['student', 'teacher', 'school']):
        return "教育/教学"
    if any(x in name_lower for x in ['ai-agent-book', 'math-modeling', 'embodied-ai', 'learn-agent', 'learn-harness', 'easy-langent', 'deerflow-book', 'dsh-handbook']):
        return "教育/书籍"
    if any(x in name_lower for x in ['mooc', 'edtech', 'lms']):
        return "教育/平台"
    if any(x in name_lower for x in ['interview', 'offer', 'resume', 'job', 'career', 'recruitment']):
        return "教育/求职"
    if any(x in name_lower for x in ['paper', 'iclr', 'neurips', 'icml']):
        return "教育/论文"
    if any(x in name_lower for x in ['weekly', 'blog']):
        return "教育/博客"
    if any(x in name_lower for x in ['tutorial', 'course', 'class']):
        return "教育/教程"
    if any(x in name_lower for x in ['ai-playground', 'rokbenko']):
        return "教育/演练"
    if any(x in name_lower for x in ['dev-encyclopedia', 'buzzpy']):
        return "教育/百科"
    
    # ===== Healthcare =====
    if any(x in name_lower for x in ['health', 'medical', 'hospital', 'doctor', 'patient']):
        return "医疗/诊断"
    if any(x in name_lower for x in ['diagnosis', 'treatment']):
        return "医疗/治疗"
    if any(x in name_lower for x in ['healthcare', 'fhir', 'hl7']):
        return "医疗/系统"
    
    # ===== Legal =====
    if any(x in name_lower for x in ['legal', 'law', 'lawyer', 'court']):
        return "法律/诉讼"
    if any(x in name_lower for x in ['contract', 'compliance', 'ip', 'patent']):
        return "法律/合规"
    if ('legal' in name_lower or 'law' in name_lower) and any(x in desc_lower for x in ['tool', 'platform']):
        return "法律/平台"
    
    # ===== Real Estate =====
    if any(x in name_lower for x in ['real-estate', 'property', 'housing']):
        return "工程/房产"
    if any(x in name_lower for x in ['construction', 'architecture']):
        return "工程/建筑"
    if 'engineering' in name_lower:
        return "工程/工程"
    
    # ===== Media Tools =====
    if any(x in name_lower for x in ['video', 'audio', 'image', 'photo']):
        return "媒体/多媒体"
    if any(x in name_lower for x in ['animation', 'graphics', '3d', 'media']):
        return "媒体/图形"
    if any(x in name_lower for x in ['nuclear', 'toonflow', 'waoowaoo', 'merlin', 'input-remapper', 'amber', 'arcree']):
        return "媒体/创作"
    if any(x in name_lower for x in ['edit', 'cut', 'trim']):
        return "媒体/编辑"
    if any(x in name_lower for x in ['openoi', 'comic']):
        return "媒体/漫画"
    
    # ===== Gaming =====
    if any(x in name_lower for x in ['game', 'gaming', 'unity', 'unreal', 'engine']):
        return "游戏/开发"
    if any(x in name_lower for x in ['objmc', 'comic-dl']):
        return "游戏/资源"
    if any(x in name_lower for x in ['mod', 'plugin', 'addon']):
        return "游戏/模组"
    
    # ===== Music =====
    if any(x in name_lower for x in ['music', 'audio-production', 'synth', 'beat', 'mixing']):
        return "音乐/制作"
    if any(x in name_lower for x in ['midi', 'daw', 'sequencer']):
        return "音乐/录音"
    
    # ===== Travel =====
    if any(x in name_lower for x in ['travel', 'tourism', 'transportation']):
        return "旅游/交通"
    if any(x in name_lower for x in ['food', 'restaurant', 'hotel', 'booking']):
        return "旅游/预订"
    if any(x in name_lower for x in ['map', 'navigation', 'gps']):
        return "旅游/导航"
    
    # ===== Communication =====
    if any(x in name_lower for x in ['communication', 'messaging', 'chat']):
        return "通信/即时通讯"
    if any(x in name_lower for x in ['email', 'notification', 'collaboration']):
        return "通信/协作"
    if any(x in name_lower for x in ['gotify', 'smsforwarder', 'prowler', 'swiftmailer', 'tio', 'otphelper']):
        return "通信/通知"
    if any(x in name_lower for x in ['slack', 'discord', 'telegram', 'wechat']):
        return "通信/平台"
    
    # ===== HR & Recruitment =====
    if any(x in name_lower for x in ['hr', 'human-resources']):
        return "人力/管理"
    if any(x in name_lower for x in ['recruitment', 'resume', 'cv', 'career', 'job']):
        return "人力/招聘"
    if any(x in name_lower for x in ['payroll', 'salary', 'benefit']):
        return "人力/薪资"
    
    # ===== Supply Chain =====
    if any(x in name_lower for x in ['supply-chain', 'logistics', 'inventory']):
        return "供应链/物流"
    if any(x in name_lower for x in ['warehouse', 'shipping', 'delivery']):
        return "供应链/仓储"
    
    # ===== Tax & Accounting =====
    if any(x in name_lower for x in ['tax', 'accounting']):
        return "财务/税务"
    if any(x in name_lower for x in ['billing', 'invoicing', 'expense']):
        return "财务/发票"
    
    # ===== Search & Discovery =====
    if any(x in name_lower for x in ['search', 'discover', 'explore', 'find', 'lookup']):
        return "搜索/通用"
    if any(x in name_lower for x in ['xerj', 'openmetadata', 'nxtrace']):
        return "搜索/专用"
    if any(x in name_lower for x in ['semantic', 'vector', 'embedding']):
        return "搜索/语义"
    if any(x in name_lower for x in ['filecodebox', 'file-share']):
        return "搜索/文件共享"
    
    # ===== Analytics =====
    if any(x in name_lower for x in ['analytics', 'analytical', 'insights', 'report', 'dashboard']):
        return "分析/商业分析"
    if any(x in name_lower for x in ['web-analytics', 'seo-analytics']):
        return "分析/Web分析"
    if 'mlnotify' in name_lower:
        return "分析/ML通知"
    
    # ===== Testing =====
    if any(x in name_lower for x in ['test', 'testing', 'qa', 'quality-assurance']):
        return "测试/自动化"
    if any(x in name_lower for x in ['unit-test', 'integration-test']):
        return "测试/单元测试"
    if any(x in name_lower for x in ['performance', 'load', 'stress']):
        return "测试/性能"
    if any(x in name_lower for x in ['security', 'pentest']):
        return "测试/安全"
    if any(x in name_lower for x in ['automation', 'auto']):
        return "测试/自动化"
    
    # ===== Documentation =====
    if any(x in name_lower for x in ['docs', 'documentation', 'wiki', 'readme', 'guide']):
        return "文档/技术文档"
    if any(x in name_lower for x in ['api-doc', 'swagger', 'openapi']):
        return "文档/API文档"
    if 'dsh-handbook' in name_lower:
        return "文档/手册"
    
    # ===== Reference =====
    if any(x in name_lower for x in ['cheatsheet', 'reference', 'guide', 'book']):
        return "参考/手册"
    if any(x in name_lower for x in ['awesome-cheatsheets', 'front-end-checklist', 'system-prompts', 'hacker-roadmap']):
        return "参考/清单"
    if any(x in name_lower for x in ['awesome-ai-tools', 'awesome-aitools', 'awesome-mlops', 'awesome-ci', 'clean-code-dotnet']):
        return "参考/精选"
    if any(x in name_lower for x in ['dev-encyclopedia', 'buzzpy']):
        return "参考/百科"
    if 'agent-java-offer' in name_lower:
        return "参考/面试"
    if any(x in name_lower for x in ['offercontext', 'offerpilot']):
        return "参考/求职"
    
    # ===== Agent Management =====
    if any(x in name_lower for x in ['lobehub', 'paperclip', 'agent-ops']):
        return "管理/平台"
    if any(x in name_lower for x in ['agent-management', 'agent-monitoring', 'traceroot']):
        return "管理/监控"
    
    # ===== Personal AI Assistant =====
    if any(x in name_lower for x in ['personal-ai', 'assistant']):
        return "助手/通用"
    if any(x in name_lower for x in ['cowagent', 'nanobot', 'leon', 'jenssegers']):
        return "助手/社区"
    if any(x in name_lower for x in ['voice', 'text', 'chat']):
        return "助手/交互"
    if 'window-summoner' in name_lower:
        return "助手/窗口"
    
    # ===== Office Tools =====
    if any(x in name_lower for x in ['office', 'excel', 'word', 'powerpoint', 'spreadsheet']):
        return "办公/文档"
    if any(x in name_lower for x in ['officecli', 'teable']):
        return "办公/表格"
    if any(x in name_lower for x in ['pdf', 'markpdfdown']):
        return "办公/PDF"
    if any(x in name_lower for x in ['presentation', 'slides']):
        return "办公/演示"
    if 'monkeycode' in name_lower:
        return "办公/企业AI"
    
    # ===== IDE/Editor =====
    if any(x in name_lower for x in ['editor', 'ide', 'code-editor', 'terminal']):
        return "开发/代码编辑"
    if any(x in name_lower for x in ['electerm', 'ohmyzsh', 'acode', 'air']):
        return "开发/终端"
    if any(x in name_lower for x in ['vim', 'emacs', 'neovim']):
        return "开发/文本编辑"
    if any(x in name_lower for x in ['vscode', 'intellij', 'pycharm']):
        return "开发/集成开发"
    if any(x in name_lower for x in ['xcode', 'xcactionbar']):
        return "开发/Xcode"
    if any(x in name_lower for x in ['php', 'inhere']):
        return "开发/PHP"
    if 'deno' in name_lower:
        return "开发/Deno"
    
    # ===== Network Tools =====
    if any(x in name_lower for x in ['network', 'proxy', 'vpn', 'dns']):
        return "网络/网络"
    if any(x in name_lower for x in ['brook', 'flare-solverr']):
        return "网络/代理"
    if any(x in name_lower for x in ['rate-limit', 'ratelimit', 'rate.limit']):
        return "网络/限流"
    if any(x in name_lower for x in ['express-rate-limit', 'hono-rate-limiter', 'node-rate-limiter']):
        return "网络/限流中间件"
    if any(x in name_lower for x in ['openstatus', 'statuspage']):
        return "网络/状态页"
    
    # ===== Backup Tools =====
    if any(x in name_lower for x in ['backup', 'sync', 'restore']):
        return "备份/同步"
    if any(x in name_lower for x in ['kopia', 's5cmd', 'mc']):
        return "备份/存储"
    if any(x in name_lower for x in ['snapshot', 'clone']):
        return "备份/快照"
    
    # ===== Data Engineering =====
    if any(x in name_lower for x in ['data-pipeline', 'elt', 'etl', 'data-engineering']):
        return "数据/管道"
    if any(x in name_lower for x in ['airbyte', 'huggingface', 'datasets', 'easy-dataset']):
        return "数据/采集"
    if any(x in name_lower for x in ['seatunnel', 'risingwave', 'datasette', 'durable-streams']):
        return "数据/处理"
    if any(x in name_lower for x in ['unstructured', 'document', 'doc-parser']):
        return "数据/文档处理"
    
    # ===== Sandbox Tools =====
    if any(x in name_lower for x in ['sandbox', 'runtime', 'container']):
        return "运行/容器"
    if any(x in name_lower for x in ['opensandbox', 'e2b']):
        return "运行/云沙箱"
    if any(x in name_lower for x in ['vm', 'virtual', 'docker']):
        return "运行/虚拟"
    if 'nixopus' in name_lower:
        return "运行/基础设施"
    
    # ===== SDK/Client =====
    if any(x in name_lower for x in ['sdk', 'client', 'python-sdk']):
        return "开发/SDK/Python"
    if any(x in name_lower for x in ['js', 'javascript', 'typescript', 'node']):
        return "开发/SDK/JavaScript"
    if any(x in name_lower for x in ['java', 'golang', 'rust']):
        return "开发/SDK/其他语言"
    if any(x in name_lower for x in ['veadk', 'volcengine']):
        return "开发/SDK/火山引擎"
    
    # ===== OS Tools =====
    if any(x in name_lower for x in ['os', 'system', 'utility']):
        return "系统/系统"
    if any(x in name_lower for x in ['optimizer', 'swiftbar', 'input-remapper', 'minisign', 'snoop', 'sampler', 'neatshift', 'hyperion']):
        return "系统/优化"
    if any(x in name_lower for x in ['linux', 'ubuntu', 'debian', 'centos']):
        return "系统/Linux"
    if any(x in name_lower for x in ['windows', 'win']):
        return "系统/Windows"
    if any(x in name_lower for x in ['macos', 'osx']):
        return "系统/macOS"
    if any(x in name_lower for x in ['classisland', 'class-widgets']):
        return "系统/桌面组件"
    if any(x in name_lower for x in ['clockindle', 'kindle']):
        return "系统/Kindle"
    if 'dsh-plugin-hub' in name_lower:
        return "系统/插件"
    if 'portainer' in name_lower:
        return "系统/管理"
    if 'opskat' in name_lower:
        return "系统/运维"
    if any(x in name_lower for x in ['f2', 'downloader']):
        return "系统/下载器"
    if any(x in name_lower for x in ['ohmyzsh', 'oh-my-bash', 'zsh', 'bash']):
        return "系统/Shell"
    
    # ===== Git Tools =====
    if any(x in name_lower for x in ['git', 'gits', 'worktree']):
        return "开发/Git/版本控制"
    if 'wtp' in name_lower:
        return "开发/Git/工作树"
    if any(x in name_lower for x in ['github', 'gitlab', 'bitbucket']):
        return "开发/Git/平台"
    if any(x in name_lower for x in ['commit', 'branch', 'merge']):
        return "开发/Git/操作"
    
    # ===== Hardware Tools =====
    if any(x in name_lower for x in ['hardware', 'kicad', 'pcb', 'circuit']):
        return "硬件/电路"
    if 'kicad' in name_lower:
        return "硬件/PCB"
    if any(x in name_lower for x in ['arduino', 'raspberry', 'esp']):
        return "硬件/单片机"
    if any(x in name_lower for x in ['fpga', 'prjxray']):
        return "硬件/FPGA"
    
    # ===== GIS Tools =====
    if any(x in name_lower for x in ['gis', 'map', 'terrain', 'geotiff']):
        return "地理/地图"
    if 'tin-terrain' in name_lower:
        return "地理/地形"
    if any(x in name_lower for x in ['satellite', 'remote', 'imaging']):
        return "地理/遥感"
    if any(x in name_lower for x in ['embodied-ai', 'octoday']):
        return "地理/具身智能"
    
    # ===== V16/V17 NEW: Additional patterns =====
    
    # AI/LLM specific
    if 'ai' in desc_lower and 'llm' in desc_lower:
        if 'agent' in desc_lower:
            return "AI/LLM/Agent"
        if 'framework' in desc_lower:
            return "AI/LLM/框架"
        if 'observability' in desc_lower or 'monitor' in desc_lower or 'trace' in desc_lower:
            return "AI/LLM/监控"
        if 'eval' in desc_lower or 'test' in desc_lower:
            return "AI/LLM/评测"
        return "AI/LLM/其他"
    
    if 'llm' in desc_lower:
        if 'agent' in desc_lower:
            return "AI/LLM/Agent"
        if 'framework' in desc_lower:
            return "AI/LLM/框架"
        if 'model' in desc_lower:
            return "AI/LLM/模型"
        return "AI/LLM/其他"
    
    if 'ai' in desc_lower and 'agent' in desc_lower:
        return "AI/LLM/Agent"
    
    if 'ai' in desc_lower and 'framework' in desc_lower:
        return "AI/LLM/框架"
    
    if 'ai' in desc_lower and 'observability' in desc_lower:
        return "AI/LLM/监控"
    
    if 'ai' in desc_lower and 'eval' in desc_lower:
        return "AI/LLM/评测"
    
    if 'ai' in desc_lower and 'tool' in desc_lower:
        return "AI/LLM/工具"
    
    if 'ai' in desc_lower:
        return "AI/LLM/其他"
    
    # CLI specific
    if 'cli' in desc_lower and 'tool' in desc_lower:
        return "CLI/工具"
    if 'command-line' in desc_lower and 'tool' in desc_lower:
        return "CLI/工具"
    if 'cli' in name_lower:
        return "CLI/工具"
    
    # DevOps/Operations
    if 'devops' in desc_lower or 'dev ops' in desc_lower:
        return "DevOps/运维"
    if 'infrastructure' in desc_lower:
        return "DevOps/基础设施"
    if 'deploy' in desc_lower or 'deployment' in desc_lower:
        return "DevOps/部署"
    if 'ci' in desc_lower and 'cd' in desc_lower:
        return "DevOps/CI/CD"
    if 'automation' in desc_lower and 'operation' in desc_lower:
        return "DevOps/运维"
    if 'operation' in desc_lower and 'platform' in desc_lower:
        return "DevOps/运维"
    
    # Security/CTF
    if 'security' in desc_lower and 'tool' in desc_lower:
        return "安全/安全工具"
    if 'pentest' in desc_lower or 'penetration' in desc_lower:
        return "安全/渗透测试"
    if 'vulnerability' in desc_lower:
        return "安全/漏洞"
    if 'scan' in desc_lower and 'tool' in desc_lower:
        return "安全/扫描"
    if 'scanner' in desc_lower:
        return "安全/扫描"
    if 'recon' in desc_lower:
        return "安全/侦察"
    if 'red team' in desc_lower or 'redteam' in desc_lower:
        return "安全/红队"
    if 'offensive' in desc_lower:
        return "安全/进攻"
    if 'firewall' in desc_lower:
        return "安全/防火墙"
    if 'proxy' in desc_lower and 'bypass' in desc_lower:
        return "安全/代理"
    
    # CMS/Website
    if 'cms' in desc_lower:
        return "CMS/内容管理"
    if 'headless' in desc_lower and 'cms' in desc_lower:
        return "CMS/无头"
    if 'website' in desc_lower and 'builder' in desc_lower:
        return "网站/构建器"
    
    # Database
    if 'database' in desc_lower and 'tool' in desc_lower:
        return "数据库/数据库工具"
    if 'sql' in desc_lower and 'workspace' in desc_lower:
        return "数据库/SQL工作区"
    if 'data layer' in desc_lower:
        return "数据库/数据层"
    
    # Productivity
    if 'productivity' in desc_lower:
        return "生产力/生产力工具"
    if 'presentation' in desc_lower and 'generator' in desc_lower:
        return "生产力/演示生成"
    if 'all-in-one' in desc_lower and 'tool' in desc_lower:
        return "生产力/全能工具"
    
    # Framework
    if 'framework' in desc_lower and 'agent' in desc_lower:
        return "框架/Agent框架"
    if 'framework' in desc_lower and 'application' in desc_lower:
        return "框架/应用框架"
    if 'open framework' in desc_lower:
        return "框架/开放框架"
    
    # Network
    if 'network' in desc_lower and 'execution' in desc_lower:
        return "网络/网络执行"
    if 'network' in desc_lower and 'tool' in desc_lower:
        return "网络/网络工具"
    if 'proxy' in desc_lower:
        return "网络/代理"
    
    # Observability
    if 'observability' in desc_lower:
        return "可观测性/可观测性"
    if 'monitor' in desc_lower and 'platform' in desc_lower:
        return "可观测性/监控平台"
    if 'trace' in desc_lower and 'test' in desc_lower:
        return "可观测性/追踪测试"
    
    # Documentation
    if 'documentation' in desc_lower and 'tool' in desc_lower:
        return "文档/文档工具"
    if 'doc' in name_lower and 'tool' in desc_lower:
        return "文档/文档工具"
    
    # Testing
    if 'mock' in desc_lower and 'server' in desc_lower:
        return "测试/Mock服务器"
    if 'test' in desc_lower and 'tool' in desc_lower:
        return "测试/测试工具"
    
    # Desktop
    if 'desktop' in desc_lower and 'assistant' in desc_lower:
        return "桌面/桌面助手"
    if 'desktop' in desc_lower and 'tool' in desc_lower:
        return "桌面/桌面工具"
    
    # IDE
    if 'ide' in desc_lower:
        return "开发/IDE"
    
    # Search
    if 'search' in desc_lower and 'tool' in desc_lower:
        return "搜索/搜索工具"
    if 'search' in desc_lower and 'engine' in desc_lower:
        return "搜索/搜索引擎"
    
    # File
    if 'file' in desc_lower and 'manager' in desc_lower:
        return "文件/文件管理"
    if 'file' in desc_lower and 'tool' in desc_lower:
        return "文件/文件工具"
    
    # Image
    if 'image' in desc_lower and 'tool' in desc_lower:
        return "图像/图像工具"
    if 'image' in desc_lower and 'processor' in desc_lower:
        return "图像/图像处理"
    
    # Video
    if 'video' in desc_lower and 'tool' in desc_lower:
        return "视频/视频工具"
    if 'video' in desc_lower and 'editor' in desc_lower:
        return "视频/视频编辑"
    
    # Audio
    if 'audio' in desc_lower and 'tool' in desc_lower:
        return "音频/音频工具"
    
    # Design
    if 'design' in desc_lower and 'tool' in desc_lower:
        return "设计/设计工具"
    if 'design' in desc_lower and 'ui' in desc_lower:
        return "设计/UI设计"
    
    # Chart/Visualization
    if 'chart' in desc_lower:
        return "图表/图表工具"
    if 'visualization' in desc_lower:
        return "可视化/可视化工具"
    if 'data visualization' in desc_lower:
        return "可视化/数据可视化"
    
    # Skill
    if 'skill' in desc_lower:
        return "技能/AI技能"
    if 'skills' in desc_lower:
        return "技能/AI技能"
    
    # Runtime
    if 'runtime' in desc_lower:
        return "运行/Runtime"
    if 'execution' in desc_lower and 'layer' in desc_lower:
        return "运行/执行层"
    
    # Platform
    if 'platform' in desc_lower and 'tool' in desc_lower:
        return "平台/平台工具"
    if 'platform' in desc_lower and 'open' in desc_lower:
        return "平台/开放平台"
    
    # Cloud
    if 'cloud' in desc_lower and 'os' in desc_lower:
        return "云/云OS"
    if 'cloud' in desc_lower and 'platform' in desc_lower:
        return "云/云平台"
    
    # Kubernetes
    if 'kubernetes' in desc_lower or 'k8s' in desc_lower:
        return "云/Kubernetes"
    if 'pod' in desc_lower and 'kubernetes' in desc_lower:
        return "云/Kubernetes"
    
    # IaC
    if 'iac' in desc_lower or 'infrastructure as code' in desc_lower:
        return "DevOps/IaC"
    
    # Mock Server
    if 'mock' in desc_lower and 'server' in desc_lower:
        return "测试/Mock服务器"
    
    # RPA
    if 'rpa' in desc_lower:
        return "自动化/RPA"
    
    # CMS
    if 'cms' in desc_lower:
        return "CMS/内容管理"
    
    # Debug
    if 'debug' in desc_lower:
        return "开发/调试"
    if 'debugging' in desc_lower:
        return "开发/调试"
    
    # Graphics
    if 'graphics' in desc_lower:
        return "图形/图形工具"
    if 'render' in desc_lower and 'tool' in desc_lower:
        return "图形/渲染工具"
    
    # Identity
    if 'identity' in desc_lower:
        return "安全/身份"
    if 'communication' in desc_lower and 'payment' in desc_lower:
        return "支付/支付工具"
    
    # Collaboration
    if 'collaboration' in desc_lower:
        return "协作/协作工具"
    if 'collaborate' in desc_lower:
        return "协作/协作工具"
    
    # Dataset
    if 'dataset' in desc_lower:
        return "数据/数据集"
    if 'datasets' in desc_lower:
        return "数据/数据集"
    
    # IaC
    if 'iac' in desc_lower:
        return "DevOps/IaC"
    
    # IaC
    if 'infrastructure' in desc_lower and 'code' in desc_lower:
        return "DevOps/IaC"
    
    # Desktop
    if 'desktop' in desc_lower:
        return "桌面/桌面工具"
    
    # Assistant
    if 'assistant' in desc_lower:
        return "助手/AI助手"
    
    # Layer
    if 'layer' in desc_lower:
        return "平台/层"
    
    # Cross-platform
    if 'cross-platform' in desc_lower:
        return "桌面/跨平台"
    
    # Desktop
    if 'desktop' in name_lower:
        return "桌面/桌面工具"
    
    # SQL
    if 'sql' in name_lower:
        return "数据库/SQL工具"
    
    # Debug
    if 'debug' in name_lower:
        return "开发/调试"
    
    # Render
    if 'render' in name_lower:
        return "图形/渲染工具"
    
    # Mock
    if 'mock' in name_lower:
        return "测试/Mock服务器"
    
    # IaC
    if 'iac' in name_lower:
        return "DevOps/IaC"
    
    # RPA
    if 'rpa' in name_lower:
        return "自动化/RPA"
    
    # CMS
    if 'cms' in name_lower:
        return "CMS/内容管理"
    
    # Chart
    if 'chart' in name_lower:
        return "图表/图表工具"
    
    # Visual
    if 'visual' in name_lower:
        return "可视化/可视化工具"
    
    # Skill
    if 'skill' in name_lower:
        return "技能/AI技能"
    
    # Runtime
    if 'runtime' in name_lower:
        return "运行/Runtime"
    
    # Cloud
    if 'cloud' in name_lower:
        return "云/云工具"
    
    # K8s
    if 'k8s' in name_lower or 'kubernetes' in name_lower:
        return "云/Kubernetes"
    
    # DevOps
    if 'devops' in name_lower or 'dev-ops' in name_lower:
        return "DevOps/DevOps"
    
    # Security
    if 'security' in name_lower:
        return "安全/安全工具"
    
    # Network
    if 'network' in name_lower:
        return "网络/网络工具"
    
    # Test
    if 'test' in name_lower:
        return "测试/测试工具"
    
    # Doc
    if 'doc' in name_lower:
        return "文档/文档工具"
    
    # Search
    if 'search' in name_lower:
        return "搜索/搜索工具"
    
    # File
    if 'file' in name_lower:
        return "文件/文件工具"
    
    # Image
    if 'image' in name_lower:
        return "图像/图像工具"
    
    # Video
    if 'video' in name_lower:
        return "视频/视频工具"
    
    # Audio
    if 'audio' in name_lower:
        return "音频/音频工具"
    
    # Design
    if 'design' in name_lower:
        return "设计/设计工具"
    
    # IDE
    if 'ide' in name_lower:
        return "开发/IDE"
    
    # Fallback to broader categories based on name
    if any(x in name_lower for x in ['tool', 'kit', 'util']):
        return "工具/其他工具"
    if any(x in name_lower for x in ['app', 'application']):
        return "应用/其他应用"
    if any(x in name_lower for x in ['server']):
        return "服务器/其他服务器"
    if any(x in name_lower for x in ['client']):
        return "客户端/其他客户端"
    if any(x in name_lower for x in ['lib', 'library']):
        return "库/其他库"
    if any(x in name_lower for x in ['core']):
        return "核心/其他核心"
    if any(x in name_lower for x in ['get']):
        return "获取/其他获取"
    if any(x in name_lower for x in ['link']):
        return "链接/其他链接"
    if any(x in name_lower for x in ['trace']):
        return "追踪/其他追踪"
    if any(x in name_lower for x in ['view']):
        return "查看/其他查看"
    if any(x in name_lower for x in ['scan']):
        return "扫描/其他扫描"
    if any(x in name_lower for x in ['store']):
        return "存储/其他存储"
    if any(x in name_lower for x in ['shell']):
        return "Shell/其他Shell"
    if any(x in name_lower for x in ['read']):
        return "读取/其他读取"
    if any(x in name_lower for x in ['sso']):
        return "认证/SSO"
    if any(x in name_lower for x in ['lint']):
        return "Lint/其他Lint"
    if any(x in name_lower for x in ['control']):
        return "控制/其他控制"
    if any(x in name_lower for x in ['connect']):
        return "连接/其他连接"
    if any(x in name_lower for x in ['analyze']):
        return "分析/其他分析"
    if any(x in name_lower for x in ['keep']):
        return "保持/其他保持"
    if any(x in name_lower for x in ['detect']):
        return "检测/其他检测"
    if any(x in name_lower for x in ['analysis']):
        return "分析/其他分析"
    if any(x in name_lower for x in ['human']):
        return "人力/其他人力"
    if any(x in name_lower for x in ['perf']):
        return "性能/其他性能"
    if any(x in name_lower for x in ['cache']):
        return "缓存/其他缓存"
    if any(x in name_lower for x in ['grade']):
        return "评分/其他评分"
    if any(x in name_lower for x in ['encrypt']):
        return "加密/其他加密"
    
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
    
    cat = get_v17_category(name, desc)
    
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