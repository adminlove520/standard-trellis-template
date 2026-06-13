# 框架使用规范

## 概述
本规范定义项目使用的框架的最佳实践和架构模式。

## 规则列表

### 前端框架（React/Vue/Next.js）
1. 组件职责单一，避免巨型组件
2. 状态管理清晰，避免 prop drilling
3. 使用框架提供的 hooks 而非生命周期
4. 样式使用 CSS-in-JS 或 Tailwind
5. 性能优化：memo、lazy、Suspense

### 后端框架（Express/FastAPI/Django）
1. 路由按功能模块划分
2. 中间件职责单一
3. 错误处理统一化
4. API 遵循 RESTful 规范
5. 数据库操作使用 ORM

## 示例

### React 组件示例
```typescript
// ✅ 正确做法
interface UserCardProps {
  user: User;
  onEdit: (id: string) => void;
}

export const UserCard: React.FC<UserCardProps> = ({ user, onEdit }) => {
  return (
    <div className="p-4 border rounded">
      <h3>{user.name}</h3>
      <button onClick={() => onEdit(user.id)}>编辑</button>
    </div>
  );
};

// ❌ 错误做法
export function UserCard(props: any) {
  // 缺少类型定义和 prop 解构
  return <div>{props.user.name}</div>;
}
```

### FastAPI 路由示例
```python
# ✅ 正确做法
from fastapi import APIRouter, Depends
from typing import List

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=List[User])
async def get_users(
    active: bool = True,
    current_user: User = Depends(get_current_user)
):
    """获取用户列表"""
    return await user_service.get_active_users()

# ❌ 错误做法
@app.get("/users")
def users():
    # 缺少类型注解、依赖注入和文档
    pass
```
