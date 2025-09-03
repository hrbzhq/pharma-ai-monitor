# 🏥 药企AI需求监控系统 (Pharma AI Requirements Monitor)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)

一个智能化的药企AI需求监控和分析平台，实时追踪全球制药公司的AI项目需求，提供深度分析和个性化就业推荐。

## 🌟 主要特性

### 🔍 智能监控
- **自动化收集**: 实时监控GitHub等平台上的药企AI项目
- **智能分类**: 使用本地AI模型自动分类AI需求类型
- **趋势分析**: 深度分析AI技术需求趋势和市场动向

### 📊 数据分析
- **需求统计**: 统计分析各类AI技术需求分布
- **公司画像**: 绘制药企AI投入和技术偏好
- **技能热度**: 分析最受欢迎的AI技能和工具

### 💼 就业推荐
- **智能匹配**: 基于AI分析的个性化职位推荐
- **薪资预测**: 根据技能和经验预测薪资范围
- **技能建议**: 提供AI技能提升建议

## 🚀 快速开始

### 系统要求
- Python 3.8+
- Flask 2.0+
- 可选: Ollama (用于本地AI模型)

### 安装步骤

1. **克隆项目**
```bash
git clone https://github.com/hrbzhq/pharma-ai-monitor.git
cd pharma-ai-monitor
```

2. **安装依赖**
```bash
pip install -r requirements.txt
```

3. **启动服务器**
```bash
# 独立版本 (推荐，无需额外配置)
python app.py
```

4. **访问系统**
- 主页: http://localhost:5000
- API文档: http://localhost:5000/test

## 📊 支持的医药企业

系统预置了多家知名医药企业的AI岗位数据：

| 企业名称 | 业务领域 | AI需求重点 |
|---------|----------|-----------|
| 辉瑞制药 (Pfizer) | 全球制药 | 药物发现、临床试验优化 |
| 阿斯利康 (AstraZeneca) | 创新药物 | 临床数据分析、患者招募 |
| 葛兰素史克 (GSK) | 疫苗研发 | 疫苗开发、免疫学AI |
| 礼来制药 (Eli Lilly) | 糖尿病药物 | 个性化医疗、基因分析 |
| 诺华制药 (Novartis) | 生物技术 | 药物安全、不良反应监测 |

## 🌐 API接口

### 核心API端点

| 端点 | 方法 | 描述 | 示例 |
|------|------|------|------|
| `/api/requirements` | GET | 获取AI需求列表 | 获取药企AI项目需求 |
| `/api/stats` | GET | 获取统计信息 | 获取系统统计数据 |
| `/api/jobs` | GET | 获取就业推荐 | 获取个性化职位推荐 |
| `/api/scheduler/status` | GET | 获取调度器状态 | 查看系统运行状态 |

### 📋 需求API示例
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "company": "Pfizer",
      "title": "AI Drug Discovery Platform",
      "description": "开发基于AI的药物发现平台",
      "category": "Drug Discovery",
      "urgency": "high",
      "budget": "$2M-5M",
      "location": "上海",
      "skills": ["Deep Learning", "Bioinformatics", "Python"],
      "created_at": "2025-09-03"
    }
  ],
  "total": 5
}
```

### 📈 统计API示例
```json
{
  "success": true,
  "data": {
    "total_requirements": 15,
    "total_companies": 8,
    "total_jobs": 12,
    "categories": {
      "Drug Discovery": 5,
      "Clinical Analytics": 3,
      "Vaccine Research": 2
    },
    "top_skills": [
      {"skill": "Machine Learning", "count": 12},
      {"skill": "Deep Learning", "count": 8},
      {"skill": "Python", "count": 10}
    ]
  }
}
```

## 🐳 Docker部署

### 使用Docker快速部署

```bash
# 构建镜像
docker build -t pharma-ai-monitor .

# 运行容器
docker run -p 5000:5000 pharma-ai-monitor
```

### 使用Docker Compose

```bash
# 一键启动
docker-compose up -d

# 查看日志
docker-compose logs -f

# 停止服务
docker-compose down
```

## 📱 功能模块

### 1. 智能需求监控
- **实时数据采集**: 自动抓取最新AI项目需求
- **需求分类**: 按技术栈、紧急程度、预算分类
- **趋势分析**: AI需求变化趋势和热点技术

### 2. 就业推荐系统
- **技能匹配**: 基于用户技能栈推荐合适岗位
- **薪资预测**: 根据经验和技能预测薪资范围
- **地理位置**: 考虑工作地点和远程工作偏好

### 3. 数据可视化
- **统计图表**: 需求分布、技能热度等可视化
- **交互式界面**: 可筛选、排序的数据展示
- **响应式设计**: 支持桌面和移动端访问

## 🔧 技术架构

### 后端技术栈
- **Python 3.8+**: 核心开发语言
- **Flask 2.3+**: 轻量级Web框架
- **SQLite**: 嵌入式数据库
- **APScheduler**: 任务调度器

### 前端技术栈
- **Bootstrap 5**: 响应式UI框架
- **Font Awesome**: 图标库
- **Chart.js**: 数据可视化图表

### 部署选项
- **独立运行**: 单文件部署 (`app.py`)
- **Docker容器**: 容器化部署
- **云平台**: 支持各种云服务部署

## 🛠️ 开发指南

### 本地开发环境

```bash
# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate     # Windows

# 安装开发依赖
pip install -r requirements.txt

# 启动开发服务器
python app.py
```

### 项目结构
```
pharma-ai-monitor/
├── app.py                 # 主应用文件
├── requirements.txt       # Python依赖
├── Dockerfile            # Docker镜像构建
├── docker-compose.yml    # Docker编排
├── README.md             # 项目说明
├── LICENSE               # 开源许可证
└── .gitignore           # Git忽略配置
```

### 扩展开发
1. **添加新企业**: 在 `sample_requirements` 中添加企业信息
2. **自定义API**: 在Flask应用中添加新的路由
3. **修改UI**: 调整HTML模板和CSS样式
4. **集成外部数据**: 连接真实的招聘API

## 🔒 安全考虑

- **数据隐私**: 不存储用户个人敏感信息
- **API限制**: 可配置API访问频率限制
- **输入验证**: 对所有用户输入进行严格验证
- **日志记录**: 完整的操作和访问日志

## 🌟 未来规划

### 短期目标 (v1.1)
- **实时数据源**: 集成真实的招聘网站API
- **用户系统**: 添加用户注册和个人档案
- **通知功能**: 邮件和推送通知新岗位

### 中期目标 (v2.0)
- **AI增强**: 使用NLP分析岗位描述
- **移动应用**: 开发iOS/Android客户端
- **多语言**: 支持英文和其他语言

### 长期愿景
- **机器学习**: 智能推荐算法优化
- **行业扩展**: 支持其他行业AI需求监控
- **企业版**: 提供企业级功能和服务

## 🤝 贡献指南

我们欢迎所有形式的贡献！

### 如何贡献
1. Fork 这个项目
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

### 贡献类型
- 🐛 **Bug报告**: 发现和报告bug
- 💡 **功能建议**: 提出新功能想法
- 📝 **文档改进**: 改善文档质量
- 🔧 **代码贡献**: 提交代码改进

## 📄 开源协议

本项目采用 [MIT License](LICENSE) 开源协议。

## 📞 支持与反馈

- **GitHub Issues**: [提交Bug报告或功能请求](https://github.com/hrbzhq/pharma-ai-monitor/issues)
- **讨论区**: [参与项目讨论](https://github.com/hrbzhq/pharma-ai-monitor/discussions)
- **邮件**: 发送反馈到项目维护者

## ⭐ 致谢

感谢所有为这个项目做出贡献的开发者和用户！

---

**🏥 专注医药AI，助力行业发展！**

*最后更新: 2025年9月3日*