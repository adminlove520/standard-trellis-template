# 测试规范

## 概述
本规范定义项目的测试策略和最佳实践。

## 规则列表

### 测试原则
1. 测试先行（TDD）：先写测试再写实现
2. 测试覆盖率 > 80%
3. 每个功能至少一个单元测试
4. 关键路径必须有集成测试
5. API 端点必须有 E2E 测试

### 测试命名
1. 测试文件命名为 `[name].test.ts` 或 `test_[name].py`
2. 测试用例描述：`should [期望行为] when [条件]`
3. 使用 given-when-then 模式组织测试

### Mock 和 Stub
1. 外部依赖必须 mock
2. 数据库操作使用测试数据库
3. 时间相关操作使用固定时间

## 示例

### TypeScript 测试示例
```typescript
// ✅ 正确做法
describe('UserService', () => {
  it('should return user when valid id is provided', async () => {
    // Given
    const userId = '123';
    const expectedUser = { id: userId, name: 'Test' };
    jest.spyOn(userRepository, 'findById').mockResolvedValue(expectedUser);

    // When
    const result = await userService.getUser(userId);

    // Then
    expect(result).toEqual(expectedUser);
  });

  it('should throw error when user not found', async () => {
    // Given
    const userId = '999';
    jest.spyOn(userRepository, 'findById').mockResolvedValue(null);

    // When & Then
    await expect(userService.getUser(userId)).rejects.toThrow(UserNotFoundError);
  });
});
```

### Python 测试示例
```python
# ✅ 正确做法
class TestUserService:
    @pytest.fixture
    def mock_repository(self):
        with patch('app.repositories.UserRepository') as mock:
            yield mock

    async def test_should_return_user_when_valid_id(
        self, mock_repository
    ):
        # Given
        user_id = "123"
        expected_user = User(id=user_id, name="Test")
        mock_repository.return_value.find_by_id.return_value = expected_user

        # When
        result = await user_service.get_user(user_id)

        # Then
        assert result == expected_user
```
