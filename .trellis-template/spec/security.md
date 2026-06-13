# 安全规范

## 概述
本规范定义项目必须遵循的安全最佳实践。

## 规则列表

### 输入验证
1. 所有用户输入必须验证和清洗
2. 使用框架提供的验证器
3. 敏感操作必须二次确认

### 认证和授权
1. 密码必须使用 bcrypt/argon2 加密
2. JWT token 必须设置过期时间
3. 敏感端点必须检查权限
4. 实施 Rate Limiting

### 数据安全
1. 敏感数据加密存储
2. 日志不记录敏感信息
3. 使用 HTTPS
4. 实施 CSP（内容安全策略）

### 依赖安全
1. 定期更新依赖
2. 使用 `npm audit` / `pip-audit`
3. 避免使用已知漏洞的包

## 示例

### 输入验证示例（Python）
```python
# ✅ 正确做法
from pydantic import BaseModel, EmailStr, Field

class CreateUserRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=100)
    name: str = Field(min_length=1, max_length=50)

    @validator('password')
    def password_strength(cls, v):
        if not re.search(r'[A-Z]', v):
            raise ValueError('必须包含大写字母')
        if not re.search(r'[0-9]', v):
            raise ValueError('必须包含数字')
        return v
```

### 认证示例（TypeScript）
```typescript
// ✅ 正确做法
import bcrypt from 'bcrypt';
import jwt from 'jsonwebtoken';

const SALT_ROUNDS = 12;
const JWT_SECRET = process.env.JWT_SECRET!;
const JWT_EXPIRES_IN = '1h';

async function hashPassword(password: string): Promise<string> {
  return bcrypt.hash(password, SALT_ROUNDS);
}

function generateToken(userId: string): string {
  return jwt.sign({ userId }, JWT_SECRET, {
    expiresIn: JWT_EXPIRES_IN
  });
}
```
