# RecursiveAcronymCorpus (RAC)

## 计算机科学递归缩略语多层次标注语料库

> A Multi-level Annotated Corpus of Recursive Acronyms in Computer Science

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-blue.svg)](https://creativecommons.org/licenses/by/4.0/)

---

## 项目简介

**RecursiveAcronymCorpus (RAC)** 是一个系统收集、整理、标注计算机科学领域递归缩略语现象的语料库项目。递归缩略语是指展开式中包含其自身或其变体的首字母缩略词，如 GNU (GNU's Not Unix)、YAML (YAML Ain't Markup Language)、WINE (Wine Is Not an Emulator) 等。

### 核心发现

> 🔬 **学术空白**：主流学术界对递归缩略语的系统研究**尚属空白**，这是语言学与计算机科学的交叉蓝海。

## 语料库统计

| 指标 | 数值 |
|------|------|
| 收录条目 | 75+ |
| 覆盖领域 | 15+ |
| 年代跨度 | 1958-2020s |
| 标注层次 | 5级 |

## 分类体系

### 结构类型

| 类型 | 说明 | 示例 |
|------|------|------|
| Full_Recursive | 完全递归 | GNU, WINE, YAML |
| Partial_Recursive | 部分递归 | LESS, HURD |
| Self_Referential | 自指型 | PHP, VIM, CSS |
| Loop_Recursive | 循环递归 | HURD↔HIRD |
| Backronym | 回溯型 | PNG, LISP |

### 领域分布

- 操作系统: GNU, HURD
- 编程语言: PHP, Ruby, Go, Rust
- 数据格式: YAML, PNG, XAML
- 开发工具: VIM, ESLint, Babel
- Web技术: SASS, LESS, MEAN
- 大数据: Hadoop, Spark, Kafka
- 容器/云: Docker, Kubernetes

## 项目结构

```
RecursiveAcronymCorpus/
├── data/
│   ├── rac_v1.csv           # v1.0 语料数据
│   └── raw/                  # 原始数据
├── docs/
│   ├── 01-语料库设计.md       # 设计文档
│   └── 02-分类体系.md         # 分类说明
├── collector/               # 采集器
└── README.md
```

## 数据格式

### CSV 字段说明

| 字段 | 说明 |
|------|------|
| ID | 唯一标识符 |
| Acronym | 缩略语 |
| Full_Form | 完整展开式 |
| Category | 结构类型 |
| Sub_Category | 子类型 |
| Year | 起源年代 |
| Origin | 起源者/社区 |
| Domain | 应用领域 |
| Confidence | 置信度 |
| Motivation | 命名动机 |
| Recursive_Marker | 递归标记词 |
| Examples | 备注 |

## 学术价值

### 四学科交叉视角

1. **语言学**: 自指现象、递归机制、构词理据
2. **术语学**: 技术术语命名规范、术语演变
3. **认知科学**: 命名心理、概念理解、记忆加工
4. **计算语言学**: NER、术语识别、自然语言生成

### 可研究问题 (RQs)

- RQ1: 递归缩略语的分布规律是什么？
- RQ2: 命名者的心理动机有哪些？
- RQ3: 用户如何理解和记忆递归缩略语？
- RQ4: 递归缩略语的文化传播机制是什么？
- RQ5: 如何自动识别和生成递归缩略语？

## 采集来源

- Wikipedia "Recursive acronym" 词条
- The Jargon File (黑客词典)
- 各项目官方文档 (GNU, YAML, PHP等)
- GitHub 项目命名
- 学术数据库零星文献

## 标注规范

### 标注层次

| 层次 | 内容 | 要求 |
|------|------|------|
| L1 | 基本信息 | 缩写、全称、类型 |
| L2 | 结构分析 | 递归深度、标记词 |
| L3 | 语用功能 | 动机、文化背景 |
| L4 | 认知实验 | 理解度、记忆度 |
| L5 | 跨语言对比 | 翻译、对照 |

### 质量控制

- 双盲标注
- ICC ≥ 0.85
- 专家复核

## 使用方法

### 加载语料

```python
import pandas as pd
df = pd.read_csv('data/rac_v1.csv')
print(df.head())
```

### 统计分析

```python
# 按类型统计
print(df['Category'].value_counts())

# 按领域统计
print(df['Domain'].value_counts())

# 按年代统计
print(df.groupby('Year').size())
```

## 贡献指南

欢迎提交 Issue 或 Pull Request！

提交新案例请包含：
- 缩略语
- 完整展开式
- 起源信息
- 来源链接

## 引用方式

```bibtex
@misc{RAC2026,
  author = {Li Pengpeng and 河南农业大学语言智能研究中心},
  title = {RecursiveAcronymCorpus: 计算机科学递归缩略语多层次标注语料库},
  year = {2026},
  publisher = {GitHub},
  howpublished = {\url{https://github.com/LPPathenau/RecursiveAcronymCorpus}}
}
```

## 许可证

本项目采用 [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) 许可证。

## 联系方式

- **作者**: Li Pengpeng
- **邮箱**: lppathenau@163.com
- **机构**: 河南农业大学 语言智能研究中心
- **GitHub**: https://github.com/LPPathenau/RecursiveAcronymCorpus

---

*最后更新: 2026-07-16*
