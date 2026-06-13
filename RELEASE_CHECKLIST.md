# 🚀 发布最终检查清单

## ✅ 已完成配置

| 项目 | 状态 |
|------|------|
| Python 包配置 (pyproject.toml) | ✅ |
| Python CLI 工具 | ✅ |
| Python 模板文件 | ✅ |
| npm 包配置 (package.json) | ✅ |
| npm CLI 脚本 | ✅ |
| npm 模板文件 | ✅ |
| PyPI 自动发布 workflow | ✅ |
| npm 自动发布 workflow | ✅ |
| GitHub Release 自动化 | ✅ |
| CHANGELOG.md | ✅ |
| LICENSE (MIT) | ✅ |

## 📋 发布步骤

### 1. 推送到 GitHub (首次)

```bash
cd C:/Users/whoami/standard-trellis-template

# 1. 在 GitHub 创建仓库: https://github.com/new
#    - 名称: standard-trellis-template
#    - 设为 Public

# 2. 添加远程仓库
git remote add origin https://github.com/YOUR_USERNAME/standard-trellis-template.git

# 3. 推送
git branch -M main
git push -u origin main
```

### 2. 配置 PyPI Trusted Publishing

1. 访问: https://pypi.org/manage/account/publishing/
2. 创建新的发布流程:
   - **PyPI Project Name**: `trellis-standard-template`
   - **Owner**: 你的 GitHub 用户名
   - **Repository**: `standard-trellis-template`
   - **Workflow**: `python-release.yml`
   - **Environment**: `pypi`
3. PyPI 会自动配置，无需 Token

### 3. 配置 npm Token (可选)

如果要发布到 npm:

1. 访问: https://www.npmjs.com/settings/tokens
2. 创建 "New Automation Token"
3. 复制 token
4. GitHub 仓库 → Settings → Secrets → Actions
5. 添加 `NPM_TOKEN`

### 4. 首次发布

```bash
# 发布 Python 版本 (1.0.0)
git tag pypi-v1.0.0
git push origin pypi-v1.0.0

# 等待 GitHub Actions 完成后，验证:
pip install trellis-standard-template

# 发布 npm 版本 (可选)
git tag npm-v1.0.0
git push origin npm-v1.0.0

# 验证:
npm create trellis-standard test-project
```

### 5. 验证安装

#### Python
```bash
pip install trellis-standard-template
trellis-init-standard my-test-project
```

#### npm
```bash
npm create trellis-standard my-test-project
```

## 📦 包信息

| 项目 | 值 |
|------|-----|
| **PyPI 包名** | `trellis-standard-template` |
| **npm 包名** | `create-trellis-standard` |
| **Python CLI** | `trellis-init-standard` |
| **npm 命令** | `npm create trellis-standard` |
| **当前版本** | 1.0.0 |
| **许可证** | MIT |

## 🔗 重要链接

- GitHub: https://github.com/YOUR_USERNAME/standard-trellis-template
- PyPI: https://pypi.org/project/trellis-standard-template/
- npm: https://www.npmjs.com/package/create-trellis-standard
- Actions: https://github.com/YOUR_USERNAME/standard-trellis-template/actions

## 📝 后续版本发布

```bash
# 1. 更新版本号
# pyproject.toml: version = "1.0.1"
# package.json: "version": "1.0.1"

# 2. 更新 CHANGELOG.md

# 3. 提交
git add .
git commit -m "bump: release 1.0.1"

# 4. 创建标签并推送
git tag pypi-v1.0.1
git push origin main pypi-v1.0.1
```

---

**准备就绪**: 2026-06-13
