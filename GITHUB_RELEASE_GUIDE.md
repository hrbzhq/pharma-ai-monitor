# GitHub 发布指南

感谢选择发布 Pharma AI Monitor 到 GitHub。以下为一个标准发布流程：

1. 确认所有文件已推送到 `main` 分支
2. 创建 tag：
```bash
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0
```
3. 在 GitHub 仓库中进入 Releases，创建新 Release，填写标题/说明并发布
4. 可上传构建产物作为 release asset（可选）

部署建议：
- 使用 GitHub Actions 自动化构建和测试
- 使用 Dependabot 定期更新依赖
