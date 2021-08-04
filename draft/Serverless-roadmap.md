# README

## 建立Serverless思维 阶段1

### 架构演进

- 单体架构
- 单体架构（水平伸缩）：负载均衡
- 微服务架构（分布式带来挑战）
- 云原生
  - 基于云产品架构
  - 应用生命周期托管

### Serverless价值

1. 不用关心服务器
2. 自动弹性
3. 按实际资源使用计费
4. 更少的代码、更快的交付速度

### 常见Serverless架构模式

#### 1. 介绍

**Serverless计算** = FaaS + BaaS

**原生心智**

1. 我的业务是什么
2. 做这件事情能不能让我的业务出类拔萃
3. 如果不能，我为什么要做这件事情而不是让别人来解决这个问题
4. 在解决业务问题之前没有必要解决技术问题

架构

- 技术
  - 计算
  - 数据存储
  - 消息通信
- 衡量维度
  - 可运维性
  - 安全性
  - 可靠性
  - 可拓展性
  - 成本

#### 2. 静态站点场景

> 更新不频繁

Serverless架构：

- 客户端 => CDN => 函数计算 => 对象存储

#### 3. 单体和微服务

>  业务需求：
>
> - 海量商品
> - 更新频繁
> - 动态信息来源

Servless微服务

- 静态资源：CDN => 对象存储
- 动态请求：API网关 => 函数计算| Serverless应用引擎
- Backend For Frontend

#### 4. 事件触发

> 买家秀：
>
> - 发表图片和视频评论
> - 对图片缩放，加水印，审核
> - 对视频做多种格式转换，审核

- Pub/Sub模式：事件无序、推送
- 事件流模式：有序，拉取
- Event Sourcing模式

#### 5. 服务编排

> 订单流程
>
> - 多步骤流程
> - 可能持续数天
> - 对失败步骤重试
> - 最终失败，需要对已完成步骤回滚

1. 基于事件触发的Saga模式
2. 基于工作流的Saga模式（由Serverless工作流协调各个流程）

### Serverless 技术选型


#### 概览
> 介绍产品

#### 函数计算

**调用**：同步调用、异步调用

**场景**：

- 各种编程语言的Web APP或者Web API相关开发群体
- 对计算力有很大的弹性需求
  - AI推理
  - 音视频等多媒体处理
  - 文档转换、网页截图等处理
- 事件驱动
  - 定时任务
  - 阿里云服务作为事件源触发函数，简化变成模型

**核心优势**

- 专注业务逻辑开发、免运维
- VM级别租户隔离
- 按需付费+预付费
- 毫秒级自动弹性伸缩

#### Serverless 应用引擎

> SAE，核心场景面向在线应用（微服务、Web、多语言应用）

典型场景

- 各种语言的应用快速上云/搬站
- 灵活&弹性使用计算资源
- 低门槛微服务架构转型
- 集成方

#### Serverless Kubernetes

1. ECS中运行容器
2. 容器编排系统
3. Serverless容器编排系统

**场景**

1. 免运维的应用托管
2. 突发流量的弹性扩容
3. 大数据计算任务
4. CI/CD

## Serverless 技术选型及实践 阶段2

### 从零入门函数计算

场景：
- Web应用
- 音视频处理 / 图文处理
- 实时流处理 / 异步数据处理
-  AI推理系统

流程
1. 事件源 / 直接调用
2. 函数计算（同步调用/异步调用）

#### 函数粘合云服务

事件驱动，简化编程模型，编写少量的代码即可串联多个服务实现复杂的功能

> 例子：缩略图

#### 函数的开发与配置

##### 基本概念-服务

- 日志配置
- 文件存储配置
- 网络配置
- 权限

##### 基本概念-函数

##### 基本概念-版本/别名

#### 函数的调试与部署

函数调试方法：

- 云调试
- 命令行工具
- VS Code插件
- 无工具插件

部署方法：

- 在线部署
- 客户端部署：通过VS Code插件，通过命令行工具

#### 函数计算在音视频场景实践

##### 场景介绍

> 音视频领域高速增长，远程会议、在线教育、短视频软件
>
> 基于函数计算的弹性高可用音视频处理系统

- 行业背景：不同终端
- 客户痛点：迭代慢
- 核心价值：高可用

**自建服务** 对比 **函数计算+函数工作流 Serverless**

##### 最佳实践

1. 英语在线教育，需求：音频平衡、转码等

   上传音视频 到OSS => 自动触发函数转码 => 转码后的音视频转存OSS

2. 芒果TV，需求：处理用户视频

   采用了全Serverless架构

3. 娱乐传媒，需求：大规模并行音视频转码业务

   短时间内准备大量计算资源进行大规模并行转码处理，同时希望基于FFmpeg自建的转码服务能简单迁移

4. 在线教育：云原生海量视频复杂业务

   视频教材需要剪辑、切分、组合转码、分辨率调整、客户端适配，且需求量存在波峰波谷

##### 案例演示

> Python3 写入OSS，ffmpeg用于转码

#### 搭建弹性可拓展的Web API



### Serverless 容器从入门到精通: Serverless K8s

#### Serverless K8s 介绍

**ECI**: Elastic Container Instance

**ACK** Alibaba Kubernetes Cluster

**ASK** Alibaba Serverless Kubernetes Cluster

*ECI和ECS混合部署*

**优点**

- GPU Instance
- Spot Instance
- 弹性负载Elastic Workload

**场景**

- 免运维应用托管
- ECI弹性资源池
- 大数据计算
- CI/CD 持续集成

####  Serverless K8s 应用部署及扩缩容

- 人工扩容
- HPA扩容 根据基础指标扩容
- Cron HPA 定时扩容
- alibaba-cloud-metrics-adapter 其他指标扩容

#### 使用Spot低成本运行Job任务

实例类型对比：

- ECI RI实例 7x24小时
- **Spot实例**： 对于小于一小时的任务和Job，抢占式实例，竞价型实例
- 按量实例 对于弹性突发流量部分

场景：大数据、媒体处理、科学计算、压力测试

#### 低成本运行Spark计算

**ECI 弹性容器实例** 

- 免运维的IaaS
- 基于Kata的安全沙箱容器
- 无缝对接K8s

##### Spark on K8s

**优点**

- 统一的资源管理与调度
- 计算与存储分离
- 弹性的集群基础设施
- 大数据上云
- 容器化的优势
- 实现应用的资源隔离和限制

**核心**

- Spark Operator
  - SparkApplication
  - Submission runner
  - Spark pod monitor
- 计算与存储分离

#### GPU机器学习开箱即用

##### ECI GPU

- 预装GPU驱动
- 兼容CRI接口
- 一键式部署

##### ECI GPU 实现

通过Nvidia开源`libnvidia-container`组件，将ECI预装的GPU驱动文件挂载到用户容器中，则借助这些动态库文件访问到GPU

1. containerd向runc下发创建使用GPU容器的命令
2. runc创建容器时，调用 prestart hook
3. hook调用libnvidia-container，挂载必要的动态库
4. 容器进程通过挂载的动态库访问GPU

##### ECI GPU 使用

在`.yaml`增加配置

##### 手写识别演示实例

#### Knative的极致Serverless体验

> Knative, Kubernetes-based platform to build, deploy and manage modern serverless workloads

##### 为什么需要Knative

- Serverless未来可期
- 基于实例数的灰度策略和弹性之间的矛盾
- 提供面向Serverless应用的抽象

##### Knative Serving简介

概念：

- Service
- Configuration
- Revision
- Route

##### Knative和云的完美融合

- Gateway和云融合
- 管控组件下沉
- 保留实例，解决冷启动问题

#### 快速构建GitLab

> GitLab CI on ASK

优势

- 服务高可用
- 无需维护k8s Master、Node节点，在没有任何构建任务的情况下，只需要运行一个Pod
- 按需服务，创建一个构建任务，启动一个Pod

过程

- 在ASK集群上运行gitlab-runner
- 通过GitLab CICD Pipeline部署Java应用到ASK集群中

### 降本增效实战利器： Serverless 应用引擎

#### 在线应用的Serverless实践

##### 最佳实践1： 低门槛微服务架构转型的解决方案

##### 最佳实践2：免运维、一键启停开发测试环境的降本方案

##### 最佳实践3：精确容量、极致弹性的解决方案

##### 最佳实践4：高效闭环的DevOps体系

#### 通过IDE/Maven部署Serverless应用实践

##### SAE部署方式：

- WAR包
- Jar包
- 镜像

##### Maven插件

##### IDE插件

Alibaba Cloud Toolkit

#### 企业级CI/CD工具部署Serverless应用的落地实践

##### 背景

##### 云效部署

##### Jenkins部署

## Serverless 场景体验

### 函数计算场景体验

> 就跑了个返回Hello World的接口

