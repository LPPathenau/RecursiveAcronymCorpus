# Recursive Acronym Corpus (递归缩略语语料库)

> 计算机科学中的递归缩略语现象：系统性收集、分类与分析

## 项目概述

本语料库系统收集计算机科学及相关领域中具有自指性(Self-Referential)特征的递归缩略语，旨在为语言学、命名学、软件开发文化等研究提供规范的数据集。

**当前规模**: 234+ 条高质量记录

## 什么是递归缩略语？

**递归缩略语(Recursive Acronym)** 是一种特殊的缩略语，其展开形式中包含缩略语本身，形成自我引用的结构。

### 经典示例

```
GNU    = GNU's Not Unix
YAML   = YAML Ain't Markup Language
WINE   = WINE Is Not an Emulator
EINE   = EINE Is Not Emacs
LAME   = LAME Ain't an MP3 Encoder
```

## 目录结构

```
RecursiveAcronymCorpus/
├── data/
│   ├── rac_v1.csv          # 初始版本 (131条)
│   └── rac_merged.csv     # 融合版本 (234条) ★ 最新
├── docs/
│   ├── 01-概述.md          # 项目概述与研究背景
│   ├── 02-分类体系.md      # 五维分类系统
│   └── 03-数据统计.md      # 数据统计分析
├── collector/
│   └── rac_collector.py    # 自动化采集脚本
├── README.md               # 本文件
└── LICENSE                # CC BY 4.0 许可证
```

## 数据格式 (rac_merged.csv)

| 字段 | 说明 | 示例 |
|------|------|------|
| id | 唯一标识 | RA-001 |
| acronym | 缩略语 | GNU |
| full_expansion | 完整展开 | GNU's Not Unix |
| category | 主分类 | computing |
| subcategory | 子分类 | text_editor |
| domain | 应用领域 | operating_systems |
| year_created | 起源年份 | 1983 |
| creator | 创建者 | Richard Stallman |
| creator_affiliation | 创建者机构 | GNU Project |
| language | 语言 | English |
| recursion_position | 递归位置 | beginning |
| recursion_type | 递归类型 | full |
| recursion_purity | 递归纯度 | High |
| has_negation | 是否含否定 | Yes |
| negation_pattern | 否定模式 | Is Not |
| is_backronym | 是否为回溯词 | No |
| is_mutually_recursive | 是否互递归 | No |
| verification_status | 验证状态 | Verified |
| related_acronyms | 相关缩写 | UNIX |
| brief | 简要说明 | Free software OS |
| source | 数据来源 | 用户贡献/Matrix Agent |

## 分类体系

### 按领域分类 (Category)

| 分类 | 数量 | 说明 |
|------|------|------|
| computing | 78 | 计算机/技术领域 |
| organization | 17 | 组织机构 |
| fictional | 6 | 虚构 |
| brand | 5 | 商业品牌 |
| academic | 2 | 学术机构 |
| ngo | 2 | 非政府组织 |
| 其他 | 10 | 政府/政治/个人等 |

### 按递归类型分类

| 类型 | 说明 | 示例 |
|------|------|------|
| full | 完全递归 | GNU, YAML, WINE |
| partial | 部分递归 | LAMP, API |
| self | 自引用 | Ruby, RNA |
| loop | 循环缩写 | DNS, ACK |

### 否定递归模式 (Negation Pattern)

| 模式 | 数量 | 示例 |
|------|------|------|
| Is Not | 15+ | GNU, WINE, EINE |
| Ain't | 5+ | YAML, LAME |
| Isn't | 3+ | PINE, NITE |
| Wasn't | 1+ | ZWEI |
| Not Only | 2+ | NoSQL |

## 统计概览

| 指标 | 数值 |
|------|------|
| 总条目数 | 234 |
| 完全递归 | 50+ |
| 覆盖时间跨度 | 1950s至今 |
| 覆盖领域 | 20+ |
| 已验证条目 | 200+ |

## 经典递归缩略语系列

### TECO 系列 (文本编辑器)
- TINT: TINT Is Not TECO
- EINE: EINE Is Not Emacs
- ZWEI: ZWEI Was EINE Initially
- SINE: SINE is not EINE
- NITE: NITE Isn't TECO Either

### GNU 传统
- GNU: GNU's Not Unix
- GNE: GNE's Not an Encyclopedia
- GRUB: GRand Unified Bootloader

### 幽默命名
- WINE: WINE Is Not an Emulator
- LAME: LAME Ain't an MP3 Encoder
- YAML: YAML Ain't Markup Language
- YAGNI: You Aren't Gonna Need It

### 自引用编程语言
- PHP: PHP: Hypertext Preprocessor
- JSON: JavaScript Object Notation
- cURL: Curl URL Request Library

## 研究价值

1. **语言学价值**: 研究计算机领域的命名规范与语言创新
2. **文化价值**: 揭示黑客文化、极客精神的表达方式
3. **设计价值**: 理解技术产品命名策略
4. **历史价值**: 记录计算机发展史中的语言演变

## 数据来源

| 来源 | 贡献量 |
|------|--------|
| 用户贡献 (gnulikecorpus.csv) | 116条 |
| Matrix Agent 采集 | 118条 |
| 总计 | 234条 |

## 许可证

本项目采用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 许可证。

**创建及维护者**: Li Pengpeng
**联系邮箱**: lppathenau@163.com

---

*Explore the beauty of self-reference in computing culture*
