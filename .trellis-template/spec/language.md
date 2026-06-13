# 编程语言规范

## 概述
本规范定义项目使用的编程语言的最佳实践和编码标准。

## 规则列表

### 通用规则
1. 代码必须通过类型检查（如 TypeScript、mypy）
2. 函数命名必须清晰表达意图
3. 避免使用魔法数字，使用命名常量
4. 复杂逻辑必须有注释说明
5. 单个函数不超过 50 行（特殊情况除外）

### TypeScript/JavaScript 规范
1. 优先使用 `const`/`let`，避免 `var`
2. 使用箭头函数而非 function 关键字
3. 接口和类型命名使用 PascalCase
4. 变量和函数命名使用 camelCase
5. 必须启用 `strict` 模式

### Python 规范
1. 遵循 PEP 8 风格指南
2. 使用类型注解（Type Hints）
3. 文档字符串使用 Google 风格
4. 异常处理要具体，避免裸 `except`
5. 使用列表推导而非 map/filter

## 示例

### TypeScript 示例
```typescript
// ✅ 正确做法
interface User {
  id: string;
  name: string;
  email: string;
}

const MAX_RETRY_COUNT = 3;

async function fetchUser(id: string): Promise<User> {
  // 实现细节
}

// ❌ 错误做法
function fetchUser(id: any) { }
```

### Python 示例
```python
# ✅ 正确做法
from typing import List, Optional

MAX_RETRY_COUNT = 3

def fetch_users(active: bool = True) -> List[User]:
    """获取用户列表。

    Args:
        active: 是否只获取活跃用户

    Returns:
        用户对象列表
    """
    # 实现细节

# ❌ 错误做法
def fetchUsers(active):
    # 缺少类型注解和文档字符串
    pass
```
