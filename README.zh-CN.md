<div align="center">

<img src="assets/hero.svg" alt="SAE — 标准学术英文润色" width="100%">

<br>

**为 SCI 论文设计的证据约束型英文润色。**<br>
改善表达，但不改变科学证据允许你说什么。

[![Codex Skill](https://img.shields.io/badge/Codex-Skill-0f766e?style=flat-square)](skills/sae/SKILL.md)
[![Validation](https://img.shields.io/github/actions/workflow/status/Nathanielneil/sae/validate.yml?branch=main&style=flat-square&label=validation)](https://github.com/Nathanielneil/sae/actions/workflows/validate.yml)
[![License](https://img.shields.io/github/license/Nathanielneil/sae?style=flat-square)](LICENSE)
[![No dependencies](https://img.shields.io/badge/dependencies-none-334155?style=flat-square)](scripts/validate_skill.py)

[English](README.md) · [安装](#安装) · [前后对比](#看看润色前后的差别) · [编辑规范](skills/sae/SKILL.md)

</div>

---

## 科学论文需要一种更克制的 AI 润色

通用 AI 经常以科学准确性为代价换取表面的流畅：叠加 hedge、制造虚假转折、添加宣传性结论，甚至把“相关”润色成“因果”。

SAE 是一个可复用的 **Codex Skill**，定位于基础校对和实质性重写之间。它改善语法、清晰度、简洁性、衔接和段落内部逻辑，同时把论文证据视为不可随意改动的边界。

<table>
<tr>
<td width="33%" valign="top">

### 准确

修正语法、句法、搭配、术语、时态、语态与段落衔接。

</td>
<td width="33%" valign="top">

### 克制

删除空洞提示语、叠加限定、虚假转折和过度防御的 AI 表达。

</td>
<td width="33%" valign="top">

### 证据安全

保留数据、统计结果、引用、技术细节、不确定性和推论边界。

</td>
</tr>
</table>

## 看看润色前后的差别

> **润色前**
>
> It should be emphasized that the proposed method may potentially improve the prediction accuracy to a certain extent. Of course, this does not necessarily mean that it can completely replace conventional methods. In the test cohort, the proposed method achieved an accuracy of 87.4%, whereas the baseline model achieved an accuracy of 81.2%.

> **SAE 润色后**
>
> In the test cohort, the proposed method achieved an accuracy of 87.4%, compared with 81.2% for the baseline model. This result indicates improved predictive accuracy under the tested conditions.

润色稿删除了防御性铺垫和重复限定，保留了两个数值，并用 `under the tested conditions` 保持实验边界。具体分析见[带说明的示例](examples/abstract.md)。

## SAE 会改什么，又会保护什么

| SAE 改善 | SAE 保护 |
|---|---|
| 语法、句法、标点、冠词、介词和语言搭配 | 科学含义、研究问题、假设和结论 |
| 清晰度、简洁性、句子结构和段落内部逻辑 | 数据、单位、样本量、实验条件和统计值 |
| 术语、缩写、时态、语态和英美拼写一致性 | 引文、公式、符号、图表标签和专业命名 |
| 冗余、空泛元话语、宣传性措辞和虚假对立 | 相关与因果、观察与解释之间的区别 |
| 多余或叠加的 hedge | 真正反映不确定性、范围和证据强度的限定 |

如果一句话存在多种科学上合理的解释，SAE 不会猜测，而是采用最安全的忠实表达并提出 **Author query**。

## 安装

### 克隆并安装

```bash
git clone https://github.com/Nathanielneil/sae.git
cd sae
./scripts/install.sh
```

SAE 默认安装到 `${CODEX_HOME:-$HOME/.codex}/skills/sae`。安装脚本不会静默覆盖已有版本；确认需要替换时运行：

```bash
./scripts/install.sh --force
```

<details>
<summary><strong>手动安装</strong></summary>

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/sae "${CODEX_HOME:-$HOME/.codex}/skills/sae"
```

</details>

如果当前会话没有立即识别 SAE，请重启 Codex 或开启新会话。

## 使用

通过 `$sae` 显式调用：

```text
使用 $sae 对以下 Discussion 进行标准学术英文润色。保留科学含义和证据强度，
删除不必要的防御性表达，只输出润色后的正文。

[粘贴英文原文]
```

如果知道目标期刊或编辑偏好，可以一起提供：

```text
使用 $sae 润色以下 Abstract，目标期刊为 Nature Communications。
- 领域：biomedical engineering
- 使用美式英语
- 不得改变任何数值
- 先输出润色稿，再列出必要的 Author queries

[粘贴英文摘要]
```

## SAE 的定位

```mermaid
flowchart LR
    A("基础校对<br/>语法 · 拼写 · 标点")
    B(["SAE<br/>清晰 · 忠实 · 克制"])
    C("深度重写<br/>结构 · 论证 · 内容")

    A --> B --> C

    classDef edge fill:#f8fafc,stroke:#cbd5e1,color:#334155,stroke-width:1px;
    classDef sae fill:#0f766e,stroke:#5eead4,color:#ffffff,stroke-width:2px;
    class A,C edge;
    class B sae;
    linkStyle default stroke:#94a3b8,stroke-width:2px;
```

SAE 可处理标题、摘要、论文各章节、完整论文、图注、投稿信和审稿回复。它不能替代同行评审、事实核查、翻译、统计审查或实质性科学改写。

## 六条编辑原则

1. **科学忠实优先**：不能通过强化结论来换取更有力的文风。
2. **主张先于防御**：先陈述发现，再处理确有必要的限定。
3. **一个充分的 hedge**：保留证据所需的谨慎，删除叠加限定。
4. **不制造虚假深刻**：只有存在真实逻辑转折时才使用对立结构。
5. **不静默猜测**：把影响科学含义的歧义转化为 Author query。
6. **不为改而改**：已经准确、清楚的句子保持不变。

完整执行规范见 [`skills/sae/SKILL.md`](skills/sae/SKILL.md)。

## 项目结构

```text
.
├── skills/sae/              # 可安装的 Codex Skill
│   ├── SKILL.md             # 编辑流程与科学边界
│   └── agents/openai.yaml   # Skill 界面元数据
├── examples/                # 润色前后示例
├── scripts/                 # 安装与验证脚本
└── .github/workflows/       # 自动验证
```

项目验证不依赖第三方 Python 包：

```bash
python3 scripts/validate_skill.py
```

## 参与贡献

欢迎通过 Issue 或 Pull Request 改善科学忠实度、编辑一致性、触发准确性和学科覆盖。请把项目说明保留在可安装目录 `skills/sae/` 之外，并在提交前运行验证脚本。

## 许可证

[MIT](LICENSE) © 2026 SAE contributors
