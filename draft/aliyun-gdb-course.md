# 阿里云GDB

## 图数据库介绍及应用场景

`GDB`是一种支持属性图模型，用于处理高度连接数据查询与存储的实时可靠的在线数据库。它支持`Gremlin` `OpenCypher`查询语言，可以帮助用户快速构建基于高度连接的数据集的应用程序。

### 图数据库 vs 关系数据库

> 经典例子，查询2度好友`friends of friends`

在关系型数据库中，高度连接的数据查询复杂且效率低下，而图数据库从基因层面提供了高效解决方案。

**自建数据库的挑战**

- 运维复杂
- 可靠性差
- 缺乏企业级支持
- 价格贵 (例子，Neo4j EE贵，可是我寻思GDB也不便宜啊)

**应用场景**

- 社交网络
    - 从A出发，搜索用户B 
    - A、B两个用户如何连接的
- 欺诈检测
- 推荐引擎
- 知识图谱、网络/IT运营、生命科学

社交网络场景实现：
1. 两度的人里面找，path最多的排第一
2. 如果某个feature有很强的识别性，直接找出feature相同用户

实时推荐场景：进入某个商场B的时候，如何进行推荐？

金融欺诈场景：用户A在申请金融贷款额度、申请信用支付时，判定风险。我觉得这里的材料很奇怪，是根据通讯录联系人来计算个人信用参考值，银行咋知道通讯录啊，顶多知道最近交易的对手吧。

**对比**

 | ------| Neo4j   | AWS Neptune   | GDB   |
 | ------ | ------ | ------ | ------ |
| 查询语言 | Cypher | Gremlin | Gremlin |
 | 高性能 | 单元格 | 单元格 | 单元格 |
 | 高可用 | 单元格 | 单元格 | 单元格 |
  | 运维 | 单元格 | 单元格 | 单元格 |

**GDB关键能力**

1. 架构：
   - 计算层
     - Gremlin Runtime
     - Cost-Based Optimizer
     - Parallel Query Execution
     - Read Commited Isolated Level
     - Fine-Grained Locking
   - 存储层
     - Smart Cache
     - High Performance Transaction Mechanism
     - Schema-Agnostic Indexing
     - Highly-Tuned Storage Engine
     - High Reliability
2. 高可用：一主一备
3. 数据导入：
   - loader任务：从OSS 云存储端得到数据
   - 查看loader任务列表
   - 查询任务详情
- 取消/删除任务
4. Neo4j迁移
   - 数据迁移
   - Cpyher迁移
   - Browser迁移：提供图可视化产品
   - 常用算法
5. Driver/SDK

### 实例操作与Gremlin语法

> Gremlin is the graph traversal language of Apache TinkerPop

接入条件：GDB实例和ECS处于同一个VPC网络内

三种数据导入方式：
- 通过OSS
  - 指定MySQL、ODPS等表格式数据到图数据库点、边的映射关系
    - 实体表
    - 关系表
  - 转换表数据到GDB点、边格式的CSV文件，上传到阿里云OSS
    - 添加GDB到csv文件开头，再上传
- 通过DataX
- 通过DataWorks平台

### 语法入门

traversalStep
- filter
- map
- flatMap
- sideEffect
- branch

```gremlin
g.V().count()
```