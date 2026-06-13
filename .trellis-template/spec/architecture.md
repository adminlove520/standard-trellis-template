# 架构设计原则

## 概述
本规范定义项目的架构设计原则和模式。

## 核心原则

### 1. 分层架构
项目应遵循清晰的分层结构：

```
┌─────────────────────┐
│   Presentation     │  UI、API、CLI
├─────────────────────┤
│   Business Logic   │  服务、领域模型
├─────────────────────┤
│   Data Access      │  Repository、ORM
└─────────────────────┘
```

### 2. 模块化
- 每个模块职责单一
- 模块间通过接口通信
- 避免循环依赖

### 3. 可测试性
- 业务逻辑与基础设施分离
- 依赖注入而非硬编码
- 接口抽象便于 Mock

## 规则列表

### TypeScript 项目
1. 使用依赖注入容器（如 InversifyJS）
2. Repository 模式抽象数据访问
3. Service 层处理业务逻辑
4. DTO 用于跨层数据传输

### Python 项目
1. 遵循 Django/FastAPI 的分层模式
2. 使用 Pydantic 进行数据验证
3. SQLAlchemy/Tortoise ORM 处理数据库
4. 中间件处理横切关注点

## 示例

### TypeScript 分层架构
```typescript
// ✅ 正确做法
// interfaces/IUserRepository.ts
export interface IUserRepository {
  findById(id: string): Promise<User>;
  create(user: CreateUserDto): Promise<User>;
}

// repositories/UserRepository.ts
export class UserRepository implements IUserRepository {
  async findById(id: string): Promise<User> {
    return await db.users.findUnique({ where: { id } });
  }
}

// services/UserService.ts
export class UserService {
  constructor(private repo: IUserRepository) {}
  async getUser(id: string): Promise<UserDto> {
    const user = await this.repo.findById(id);
    return UserDto.fromEntity(user);
  }
}
```

### Python 分层架构
```python
# ✅ 正确做法
# repositories/user_repository.py
class UserRepository:
    def find_by_id(self, user_id: str) -> User:
        return await User.get(id=user_id)

# services/user_service.py
class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    async def get_user(self, user_id: str) -> UserResponse:
        user = await self.repo.find_by_id(user_id)
        return UserResponse.from_orm(user)
```
