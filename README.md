# Standard Trellis Template

> 开箱即用的 Trellis AI 编码工程化标准模板
>
> 适用于 Claude Code、OpenClaw、Hermes、Cursor、Windsurf 等 14+ AI Coding 平台

## ✨ 特性

- 🚀 **开箱即用** - 一行命令初始化项目
- 📦 **规范完整** - 包含语言、框架、测试、安全、风格五大核心规范
- 🔄 **持续更新** - 随 Trellis 框架同步更新
- 👥 **团队协作** - 规范随仓库版本化管理
- 🌐 **多平台** - 支持 Claude、OpenClaw、Hermes、Cursor 等

## 快速开始

### 方法 1: 使用 npm（推荐）

```bash
npm create trellis-standard my-project
```

### 方法 2: 克隆仓库

```bash
git clone https://github.com/your-username/standard-trellis-template.git my-project
cd my-project
trellis init -u your-name
cp -r .trellis-template/spec/* .trellis/spec/
```

### 方法 3: 作为远程模板

```bash
trellis init --template https://github.com/your-username/standard-trellis-template
```

## 项目结构

```
.trellis/
├── spec/                  # 规范文档（随版本管理）
│   ├── language.md         # 编程语言规范
│   ├── framework.md        # 框架使用规范
│   ├── architecture.md     # 架构设计原则
│   ├── testing.md          # 测试规范
│   ├── lint.md             # 代码风格规范
│   └── security.md         # 安全规范
├── tasks/                 # 任务跟踪
│   └── [task-id]/
│       ├── prd.md
│       ├── implement.jsonl
│       └── check.jsonl
└── workspace/             # 工作区记忆（不提交）
    └── journal/

CLAUDE.md                   # Claude Code 适配（自动生成）
AGENTS.md                   # 其他 Agent 适配（自动生成）
```

## 规范说明

### language.md
定义编程语言的最佳实践：
- TypeScript/JavaScript 编码规范
- Python PEP 8 遵循
- 命名约定和类型注解

### framework.md
定义框架使用规范：
- React/Vue/Next.js 组件模式
- Express/FastAPI/Django 路由设计
- 状态管理和数据流

### testing.md
定义测试规范：
- TDD 测试先行原则
- 80%+ 覆盖率要求
- Mock 和测试命名规范

### security.md
定义安全规范：
- 输入验证和清洗
- 认证授权机制
- 敏感数据保护

### lint.md
定义代码风格：
- ESLint/Prettier 配置
- Black/isort 配置
- CI pipeline 集成

## 使用工作流

1. **需求阶段** 📝
   ```
   与 AI 头脑风暴 → trellis-brainstorm → 产出 PRD
   ```

2. **实现阶段** 💻
   ```
   AI 调用 trellis-implement → 按规范编写代码
   ```

3. **验证阶段** 🔍
   ```
   AI 调用 trellis-check → lint + type-check + tests
   ```

4. **收尾阶段** ✅
   ```
   /trellis:finish-work → 沉淀新认知到 Spec
   ```

## 支持的平台

- ✅ Claude Code
- ✅ OpenClaw
- ✅ Hermes
- ✅ Cursor
- ✅ Windsurf
- ✅ Continue
- ✅ Aider
- ✅ Sweep
- ✅ Codeium
- ✅ Tabnine
- ✅ Sourcegraph
- ✅ JetBrains AI
- ✅ GitHub Copilot
- ✅ VS Code Copilot

## 自定义规范

你可以根据项目需求修改 `.trellis/spec/` 中的文件：

```bash
# 编辑语言规范
code .trellis/spec/language.md

# 添加项目特定规范
echo "# My Custom Spec" > .trellis/spec/custom.md
```

## 团队协作

### 提交规范到版本控制

```bash
git add .trellis/spec/ .trellis/tasks/
git commit -m "docs: 更新项目规范"
```

### 排除个人工作区

确保 `.gitignore` 包含：

```
.trellis/workspace/
```

## 常见问题

### Q: 与 CLAUDE.md 的区别？

A: Trellis 提供了结构化的 Spec 系统、任务跟踪和工作区记忆，是 CLAUDE.md 的增强版。

### Q: 如何在不同平台间切换？

A: 无需切换，同一套 `.trellis/` 结构在所有平台自动适配。

### Q: 必须使用所有规范文件吗？

A: 不必，可以根据项目需求选择性使用，甚至可以删除不适用的规范。

### Q: 如何更新模板？

A: 使用 `npm update trellis-standard` 或 `git pull` 获取最新版本。

## 贡献指南

欢迎提交 PR 改进规范模板：

1. Fork 本仓库
2. 创建特性分支
3. 提交改动
4. 发起 Pull Request

## 许可证

MIT License - 自由使用和修改

## 链接

- [Trellis 官方文档](https://github.com/mindfold-ai/Trellis)
- [npm 包](https://www.npmjs.com/package/create-trellis-standard)
- [问题反馈](https://github.com/your-username/standard-trellis-template/issues)

---

**维护者**: whoami
**版本**: 1.0.0
**最后更新**: 2026-06-13
