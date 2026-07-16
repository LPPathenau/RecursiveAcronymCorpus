# Recursive Acronym Corpus (递归缩略语语料库)

> 计算机科学中的递归缩略语现象：系统性收集、分类与分析

## 项目概述

本语料库系统收集计算机科学及相关领域中具有自指性(Self-Referential)特征的递归缩略语，旨在为语言学、命名学、软件开发文化等研究提供规范的数据集。

**当前规模**: 234条高质量记录（108个唯一缩略语）

---

## 语料库动态建设：认识的演进

> 本语料库的建设过程本身即是一个认识深化的过程。

### 建设历程

```
┌─────────────────────────────────────────────────────────────────┐
│  阶段一：用户贡献 (116条)                                       │
│  ├── 来源：用户手工标注                                          │
│  ├── 特点：20个专业字段，分类细致                                │
│  └── 代表：TECO系列、GNU传统                                     │
├─────────────────────────────────────────────────────────────────┤
│  阶段二：AI辅助采集 (118条)                                      │
│  ├── 来源：多源自动化采集                                        │
│  ├── 特点：关键词匹配，覆盖RFC/W3C等标准                         │
│  └── 代表：网络协议、信号系统、IO命名                            │
├─────────────────────────────────────────────────────────────────┤
│  阶段三：严格合并去重 → rac_merged.csv (108个唯一) ★ 最新        │
│  ├── 方法：Cohen's Kappa = 0.7425 (Substantial一致性)            │
│  ├── 发现：16.2%边界案例（MIME, YAML, PNG, LESS, BABEL, MUMPS） │
│  └── 结论：递归缩略语存在"梯度定义"而非"非此即彼"               │
└─────────────────────────────────────────────────────────────────┘
```

### 认识进阶：从模糊到清晰

| 认识阶段 | 核心发现 |
|----------|----------|
| **初始认识** | "递归缩略语就是展开中包含自身缩写的词" |
| **深入发现** | LISP、API、ACK/NAK等处于边界地带 |
| **理论升华** | 递归缩略语是一个"梯度现象"，需要梯度定义模型 |

### 梯度定义模型

```
严格自指 ←————————————————————————→ 弱自指关联
   │                                          │
   ↓                                          ↓
GNU: GNU's Not Unix                      API: Application Programming Interface
      (完全递归, 100%)                          (弱关联, ~20%)

   │                                          │
   ↓                                          ↓
YAML: YAML Ain't Markup Language         SQL: Structured Query Language
      (准递归, ~80%)                             (弱关联, ~15%)

   │                                          │
   ↓                                          ↓
LISP: LISt Processing                 LAMP: Linux Apache MySQL PHP
      (循环递归, ~60%)                            (首字母缩写, ~5%)
```

**五级定义**：
| 级别 | 类型 | 示例 | 自指程度 |
|------|------|------|----------|
| 1 | 全递归型 | GNU, WINE | 100% |
| 2 | 准递归型 | YAML, LAME | 80% |
| 3 | 循环递归型 | LISP | 60% |
| 4 | 自指型 | Ruby | 40% |
| 5 | 自指联想型 | API, SQL | 20% |

---

## 目录结构

```
RecursiveAcronymCorpus/
├── data/
│   ├── rac_v1.csv          # 初始版本 (131条)
│   └── rac_merged.csv     # ★ 严格合并版本 (108个唯一缩略语)
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
| source | 数据来源 | 用户贡献/AI采集 |

---

## 统计概览

| 指标 | 数值 |
|------|------|
| 合并后唯一Acronym | 108个 |
| Cohen's Kappa一致性 | 0.7425 (Substantial) |
| 边界争议案例 | 6个 (16.2%) |
| 覆盖时间跨度 | 1950s至今 |
| 覆盖领域 | 20+ |

---

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

---

## 研究价值

1. **语言学价值**: 研究计算机领域的命名规范与语言创新
2. **社会学价值**: 揭示程序员群体的身份认同符号系统
3. **历史价值**: 记录计算机发展史中的语言演变
4. **教育价值**: 作为编程教学中递归概念的内隐学习载体

---

## 数据来源

| 来源 | 贡献量 |
|------|--------|
| 用户贡献 (手工标注) | 116条 |
| AI辅助采集 (多源) | 118条 |
| 严格合并后 | 108个唯一缩略语 |

---

## 方法论说明

### 合并去重方法

1. **标准化**：统一字段格式，建立字段映射
2. **主键去重**：以acronym为主键，用户数据优先
3. **一致性评估**：计算Cohen's Kappa = 0.7425

### 边界案例处理

以下案例被识别为"争议边界"：
- MIME, YAML, PNG, LESS, BABEL, MUMPS

处理策略：保留但不标记为"严格递归"，允许梯度归属。

---

## 许可证

本项目采用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 许可证。

**创建及维护者**: Li Pengpeng
**联系邮箱**: lppathenau@163.com

---

*Explore the beauty of self-reference in computing culture*
*语料库的价值不仅在于收录，更在于记录认识的演进*
