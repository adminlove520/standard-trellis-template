# 贡献指南

感谢你对 Standard Trellis Template 的关注！

## 如何贡献

### 报告问题

如果你发现了 Bug 或有新功能建议：

1. 检查 [Issues](https://github.com/your-username/standard-trellis-template/issues) 是否已存在
2. 如果不存在，创建新 Issue 并详细描述

### 提交 PR

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'feat: add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 创建 Pull Request

### 规范贡献

如果你想改进规范模板：

1. 规范文件位于 `.trellis-template/spec/`
2. 保持语言简洁明了
3. 提供正反示例
4. 考虑跨语言/框架的通用性

## 规范文件结构

```
spec/
├── language.md      # 编程语言规范
├── framework.md     # 框架使用规范
├── architecture.md  # 架构设计原则
├── testing.md       # 测试规范
├── lint.md          # 代码风格规范
└── security.md      # 安全规范
```

## 代码风格

- 使用 2 空格缩进
- 使用单引号（JavaScript）
- 遵循 Conventional Commits 规范

## Commit 规范

使用 [Conventional Commits](https://www.conventionalcommits.org/)：

```
feat: 新功能
fix: 修复 Bug
docs: 文档更新
style: 代码风格（不影响功能）
refactor: 重构
test: 测试相关
chore: 构建/工具相关
```

## 许可证

提交代码即表示你同意将代码以 MIT 许可证发布。
