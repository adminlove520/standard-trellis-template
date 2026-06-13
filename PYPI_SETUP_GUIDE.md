# PyPI 和 GitHub Release 自动发布配置

## 📦 已配置的 Workflows

### 1. Python Release (`.github/workflows/python-release.yml`)

触发条件: 推送 `pypi-v*` 标签

功能:
- 构建 Python 包
- 发布到 PyPI (使用 Trusted Publishing)
- 自动创建 GitHub Release

### 2. NPM Release (`.github/workflows/npm-release.yml`)

触发条件: 推送 `npm-v*` 标签

功能:
- 发布到 npm
- 自动创建 GitHub Release

## 🔐 需要配置的 Secrets

### PyPI (推荐使用 Trusted Publishing)

1. 访问 https://pypi.org/manage/account/publishing/

2. 创建新的发布流程:
   - **PyPI Project Name**: `trellis-standard-template`
   - **Owner**: 你的 GitHub 用户名
   - **Repository name**: `standard-trellis-template`
   - **Workflow name**: `python-release.yml`
   - **Environment name**: `pypi`

3. PyPI 会生成配置，无需设置 Token

### npm (可选)

如果也要发布到 npm:

1. 创建 npm Automation Token:
   - 访问 https://www.npmjs.com/settings/tokens
   - 点击 "New Automation Token"
   - 复制生成的 token

2. 添加到 GitHub Secrets:
   - 仓库 Settings → Secrets and variables → Actions
   - 添加 `NPM_TOKEN`

## 🚀 发布流程

### 发布 Python 版本

```bash
# 更新 pyproject.toml 中的版本号
# 1.0.0 -> 1.0.1

# 提交更改
git add pyproject.toml
git commit -m "bump: 1.0.1"

# 创建并推送标签 (格式: pypi-v<version>)
git tag pypi-v1.0.1
git push origin pypi-v1.0.1

# GitHub Actions 会自动:
# 1. 构建 Python 包
# 2. 发布到 PyPI
# 3. 创建 GitHub Release
```

### 发布 NPM 版本

```bash
# 更新 package.json 中的版本号

# 提交更改
git add package.json
git commit -m "bump: 1.0.1"

# 创建并推送标签 (格式: npm-v<version>)
git tag npm-v1.0.1
git push origin npm-v1.0.1

# GitHub Actions 会自动发布到 npm
```

### 同时发布两个版本

```bash
# 1. 更新两个文件的版本号
# pyproject.toml: version = "1.0.1"
# package.json: "version": "1.0.1"

# 2. 提交
git add pyproject.toml package.json
git commit -m "bump: release 1.0.1"

# 3. 创建两个标签
git tag pypi-v1.0.1
git tag npm-v1.0.1

# 4. 推送
git push origin main
git push origin pypi-v1.0.1
git push origin npm-v1.0.1
```

## 📋 版本号管理

### 手动管理

```bash
# 补丁版本 (bug 修复)
1.0.0 -> 1.0.1

# 次要版本 (新功能)
1.0.0 -> 1.1.0

# 主要版本 (破坏性变更)
1.0.0 -> 2.0.0
```

### 使用自动化工具

```bash
# Python (使用 bump2version)
pip install bump2version
bump2version patch  # 或 minor, major
git push --tags

# Node (使用 npm version)
npm version patch  # 或 minor, major
git push --tags
```

## 🔍 验证发布

### PyPI

```bash
# 安装测试
pip install trellis-standard-template

# 使用
trellis-init-standard my-project
```

### npm

```bash
# 安装测试
npm create trellis-standard my-project
```

### GitHub Release

访问: `https://github.com/YOUR_USERNAME/standard-trellis-template/releases`

## 🛠️ 本地测试构建

### Python

```bash
# 安装构建工具
pip install build twine

# 构建
python -m build

# 检查
twine check dist/*

# 本地安装测试
pip install dist/*.whl
```

### NPM

```bash
# 构建
npm run build || echo "No build step"

# 本地测试
npm link
create-trellis-standard test-project
```

## 📝 发布检查清单

发布前确认:

- [ ] 版本号已更新 (pyproject.toml 和 package.json)
- [ ] CHANGELOG.md 已更新
- [ ] 所有测试通过
- [ ] 本地构建成功
- [ ] PyPI Trusted Publishing 已配置
- [ ] (可选) npm token 已配置

## 🐛 回滚版本

如果发现问题需要回滚:

```bash
# 从 PyPI 删除 (只能删除,不能覆盖)
# 访问 https://pypi.org/manage/project/trellis-standard-template/releases/

# 从 npm 删除
npm unpublish trellis-standard-template@1.0.1

# 删除 GitHub Release
# 访问仓库的 Releases 页面手动删除
```

## 🔄 Workflow 状态

检查 workflow 运行状态:
https://github.com/YOUR_USERNAME/standard-trellis-template/actions

---

**配置日期**: 2026-06-13
**PyPI Token**: 已配置 (用户提供的)
**NPM Token**: 需要配置 (可选)
