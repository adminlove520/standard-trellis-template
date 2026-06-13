# Standard Trellis Template 发布指南

## 仓库已创建

仓库位置: `C:/Users/whoami/standard-trellis-template`

## 下一步：发布到 GitHub

### 1. 在 GitHub 创建仓库

访问 https://github.com/new 创建新仓库：

- 仓库名称: `standard-trellis-template`
- 描述: "Standard Trellis template for AI-assisted development across all platforms"
- 设为: Public
- 不要初始化 README

### 2. 推送到 GitHub

```bash
cd C:/Users/whoami/standard-trellis-template
git remote add origin https://github.com/YOUR_USERNAME/standard-trellis-template.git
git branch -M main
git push -u origin main
```

### 3. 发布到 npm

```bash
# 登录 npm (首次需要)
npm login

# 发布包
npm publish

# 或使用 --access public 发布公开包
npm publish --access public
```

### 4. 添加 GitHub Token (用于自动化)

在 GitHub 仓库设置中添加：

1. Settings → Secrets and variables → Actions
2. 添加 `NPM_TOKEN` (从 npm 创建 automation token)

## 使用方式

### 安装方式 1: npm

```bash
npm create trellis-standard my-project
```

### 安装方式 2: 克隆

```bash
git clone https://github.com/YOUR_USERNAME/standard-trellis-template.git my-project
cd my-project
trellis init -u your-name
```

### 安装方式 3: 作为 Trellis 模板

```bash
trellis init --template https://github.com/YOUR_USERNAME/standard-trellis-template
```

## 项目结构

```
standard-trellis-template/
├── .github/           # GitHub Actions 配置
├── .trellis-template/ # 规范模板
│   └── spec/          # 规范文件
├── bin/               # CLI 命令
├── README.md          # 主文档
├── CONTRIBUTING.md    # 贡献指南
├── LICENSE            # MIT 许可
├── package.json       # npm 包配置
└── .gitignore         # Git 忽略规则
```

## 规范文件清单

| 文件 | 说明 |
|------|------|
| language.md | 编程语言规范（TypeScript/Python） |
| framework.md | 框架使用规范（React/FastAPI） |
| architecture.md | 架构设计原则（分层架构） |
| testing.md | 测试规范（TDD、覆盖率） |
| security.md | 安全规范（认证、授权） |
| lint.md | 代码风格规范（ESLint、Black） |

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

## 维护说明

### 更新规范

修改 `.trellis-template/spec/` 中的文件，然后：

```bash
git add .
git commit -m "docs: 更新某规范"
git push
```

### 发布新版本

```bash
npm version patch  # 或 minor, major
npm publish
git push --tags
```

## 快捷命令

创建一个 PowerShell 别名：

```powershell
# 添加到 $PROFILE
function New-TrellisProject {
    param([string]$Name)
    npm create trellis-standard $Name
}
```

---

**创建日期**: 2026-06-13
**维护者**: whoami
