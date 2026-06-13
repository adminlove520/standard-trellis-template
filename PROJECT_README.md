# {PROJECT_NAME}

## 项目说明

此项目使用 [Standard Trellis Template](https://github.com/your-username/standard-trellis-template) 初始化，遵循统一的 AI 编码工程化规范。

## 开发工作流

### 1. 需求阶段 📝
与 AI 头脑风暴，明确需求，AI 自动产出 PRD

### 2. 实现阶段 💻
AI 调用 `trellis-implement` 按规范编写代码

### 3. 验证阶段 🔍
AI 调用 `trellis-check` 进行 lint、type-check 和测试

### 4. 收尾阶段 ✅
执行 `/trellis:finish-work` 沉淀新认知

## 项目结构

```
.trellis/
├── spec/          # 项目规范（随版本管理）
├── tasks/         # 任务跟踪
└── workspace/     # 个人工作区（不提交）
```

## 规范文件

- [language.md](.trellis/spec/language.md) - 编程语言规范
- [framework.md](.trellis/spec/framework.md) - 框架使用规范
- [testing.md](.trellis/spec/testing.md) - 测试规范
- [security.md](.trellis/spec/security.md) - 安全规范
- [lint.md](.trellis/spec/lint.md) - 代码风格规范

## 快速开始

```bash
# 安装依赖
npm install

# 运行开发服务器
npm run dev

# 运行测试
npm test

# 类型检查
npm run type-check

# 代码检查
npm run lint
```

## 常见问题

查看 [Standard Trellis Template 文档](https://github.com/your-username/standard-trellis-template) 了解更多。

---

**初始化日期**: {DATE}
**Trellis 版本**: {TRELLIS_VERSION}
