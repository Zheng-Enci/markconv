# Mermaid 图表示例文档

本文档演示各种 Mermaid 图表的使用方法。

## 1. 流程图 Flowchart

```mermaid
graph TD
    A[开始] --> B{判断}
    B -->|条件1| C[处理1]
    B -->|条件2| D[处理2]
    C --> E[结束]
    D --> E
```

## 2. 时序图 Sequence Diagram

```mermaid
sequenceDiagram
    participant 用户
    participant 系统
    participant 数据库
    
    用户->>系统: 发送请求
    系统->>数据库: 查询数据
    数据库-->>系统: 返回结果
    系统-->>用户: 显示结果
```

## 3. 类图 Class Diagram

```mermaid
classDiagram
    class Animal {
        +String name
        +makeSound()
    }
    class Dog {
        +fetch()
    }
    class Cat {
        +climb()
    }
    Animal <|-- Dog
    Animal <|-- Cat
```

## 4. 状态图 State Diagram

```mermaid
stateDiagram-v2
    [*] --> 待处理
    待处理 --> 处理中: 开始处理
    处理中 --> 已完成: 处理成功
    处理中 --> 失败: 处理失败
    失败 --> 待处理: 重试
    已完成 --> [*]
```

## 5. 饼图 Pie Chart

```mermaid
pie title 市场份额
    "产品A" : 35
    "产品B" : 30
    "产品C" : 20
    "其他" : 15
```

## 6. 甘特图 Gantt Chart

```mermaid
gantt
    title 项目进度
    dateFormat  YYYY-MM-DD
    section 设计阶段
    需求分析      :done, a1, 2024-01-01, 7d
    原型设计      :active, a2, after a1, 5d
    section 开发阶段
    前端开发      :a3, after a2, 10d
    后端开发      :a4, after a2, 10d
    section 测试阶段
    集成测试      :a5, after a3, 5d
```

## 7. 实体关系图 ER Diagram

```mermaid
erDiagram
    USER ||--o{ ORDER : places
    USER {
        string username
        string email
    }
    ORDER {
        int order_id
        date order_date
    }
```

## 8. 用户旅程图 User Journey

```mermaid
journey
    title 用户购物体验
    section 浏览
      访问网站: 5: 用户
      搜索商品: 4: 用户
    section 购买
      加入购物车: 5: 用户
      结算支付: 3: 用户
    section 售后
      查看订单: 4: 用户
      确认收货: 5: 用户
```
