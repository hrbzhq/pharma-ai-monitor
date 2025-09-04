# 贡献指南

感谢您对药企AI需求监控系统的关注！我们欢迎各种形式的贡献。

## 🠆 如何报告问题
如果您发现了bug或有功能建议：

1. 查看 [Issues](https://github.com/your-username/pharma-ai-monitor/issues) 确认问题是否已存在
2. 如果是新问题，请新建一个 Issue
3. 提供详细的问题描述和复现步骤
4. 如果可能，请附上日志或截图

### 提交代码

1. Fork 项目
   ```bash
   git clone https://github.com/your-username/pharma-ai-monitor.git
   cd pharma-ai-monitor
   ```

2. 创建 feature 分支
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. 开发并提交
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

4. 推送分支
   ```bash
   git push origin feature/your-feature-name
   ```

5. 创建 Pull Request，说明变更、关联 Issue（如果有），并补充必要的测试信息

## 代码规范
- 遵循 PEP 8
- 添加必要的类型注解
- 保持函数简单单一职责
- 编写清晰的文档和注释

## 开发环境

1. 安装依赖
```bash
pip install -r requirements.txt
```

2. 运行测试
```bash
python -m pytest tests/
```
