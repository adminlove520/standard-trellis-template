# 代码风格规范

## 概述
本规范定义项目的代码风格和 lint 配置。

## 规则列表

### 通用规则
1. 使用统一的 formatter（Prettier/Black）
2. CI pipeline 必须包含 lint 检查
3. Lint 错误必须修复才能合并

### TypeScript/JavaScript
1. 使用 ESLint + Prettier
2. 推荐配置：`@typescript-eslint` + `prettier`
3. 单引号，分号可选

### Python
1. 使用 Black + isort + flake8
2. 行长度 100（Black 默认）
3. 类型检查：mypy

## 示例

### ESLint 配置
```json
{
  "extends": [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended",
    "plugin:prettier/recommended"
  ],
  "rules": {
    "@typescript-eslint/no-unused-vars": "error",
    "@typescript-eslint/explicit-function-return-type": "warn",
    "no-console": "warn"
  }
}
```

### Prettier 配置
```json
{
  "semi": false,
  "singleQuote": true,
  "trailingComma": "es5",
  "printWidth": 100
}
```

### Black 配置
```ini
[tool.black]
line-length = 100
target-version = ['py39']
```
