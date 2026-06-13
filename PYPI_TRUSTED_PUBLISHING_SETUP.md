# PyPI Trusted Publishing 配置指南

## ✅ GitHub 仓库已创建

仓库地址: https://github.com/adminlove520/standard-trellis-template

## 🔐 配置 PyPI Trusted Publishing

### 步骤 1: 访问 PyPI 发布配置

访问: https://pypi.org/manage/account/publishing/

### 步骤 2: 创建新的发布流程

点击 "Add a new publisher" 并填写:

| 字段 | 值 |
|------|-----|
| **PyPI Project Name** | `trellis-standard-template` |
| **Owner** | `adminlove520` |
| **Repository name** | `standard-trellis-template` |
| **Workflow name** | `python-release.yml` |
| **Environment name** | `pypi` |

### 步骤 3: 确认配置

PyPI 会显示配置摘要，确认后即可。

### 步骤 4: 首次发布

配置完成后，运行:

```bash
cd C:/Users/whoami/standard-trellis-template
git tag pypi-v1.0.0
git push origin pypi-v1.0.0
```

GitHub Actions 将自动:
1. 构建 Python 包
2. 发布到 PyPI (使用 Trusted Publishing)
3. 创建 GitHub Release

## 📝 注意事项

- Trusted Publishing 不需要 Token，更安全
- 首次发布可能需要几分钟处理
- 发布后可在 PyPI 查看包: https://pypi.org/project/trellis-standard-template/

## 🔍 验证发布

```bash
pip install trellis-standard-template
trellis-init-standard test-project
```

---

**仓库**: https://github.com/adminlove520/standard-trellis-template
**PyPI 包名**: trellis-standard-template
**版本**: 1.0.0
