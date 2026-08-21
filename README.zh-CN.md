# SAE — 标准学术英文润色

[English](README.md) · [MIT License](LICENSE)

**SAE** 是一个用于 SCI 及其他同行评审论文的 Codex Skill。它执行中等强度的学术英文编辑：不只修改语法，也改善清晰度、简洁性、衔接和术语一致性，同时严格保护科学含义与证据强度。

## SAE 解决什么问题

通用 AI 润色容易让论文变得更长、更保守，甚至出现重复限定、虚假转折、空泛强调和未经授权的结论强化。SAE 采用受证据约束的编辑策略：

- 超越基础校对，但不替作者重写研究；
- 保留数据、单位、统计值、引文、术语和实验条件；
- 严格区分相关与因果、观察与解释、统计显著性与实际意义；
- 删除空洞的提示语、对假想质疑的回应、叠加 hedge 和虚假对立；
- 保留真正表达不确定性、适用范围或研究设计限制的限定词；
- 遇到可能改变科学含义的歧义时提出作者问题，而不是自行猜测。

## 润色边界

| 级别 | 主要工作 | SAE |
|---|---|:---:|
| 基础校对 | 修正明显的语法、拼写和标点错误 | — |
| 标准学术润色 | 改善语言、清晰度、简洁性和段落内部逻辑 | ✓ |
| 深度重写 | 大幅重组论证或改写科学内容 | — |

SAE 可处理标题、摘要、论文各章节、图注、投稿信和审稿回复。它不能替代同行评审、事实核查、统计审查、翻译或实质性科学改写。

## 项目结构

```text
sae/
├── skills/sae/              # 可安装的 Codex Skill
│   ├── SKILL.md
│   └── agents/openai.yaml
├── examples/                # 使用示例
├── scripts/                 # 安装和验证工具
└── .github/workflows/       # 自动验证
```

## 安装

克隆仓库后运行：

```bash
./scripts/install.sh
```

默认安装路径为 `${CODEX_HOME:-$HOME/.codex}/skills/sae`。如果该目录已经存在，脚本不会自动覆盖；确认需要覆盖时可运行：

```bash
./scripts/install.sh --force
```

也可以手动安装：

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/sae "${CODEX_HOME:-$HOME/.codex}/skills/sae"
```

如当前会话未识别新技能，请重启 Codex 或开启新会话。

## 使用

通过 `$sae` 显式调用：

```text
使用 $sae 对以下 Discussion 进行标准学术英文润色。保留科学含义和证据强度，
删除不必要的防御性表达，只输出润色后的正文。

[粘贴英文原文]
```

有目标期刊时，可提供更多约束：

```text
使用 $sae 润色以下 Abstract，目标期刊为 Nature Communications。使用美式英语，
不得改变任何数值；需要作者确认的科学歧义请单独列出。

[粘贴英文摘要]
```

示例见 [examples/abstract.md](examples/abstract.md)，完整编辑规范见 [skills/sae/SKILL.md](skills/sae/SKILL.md)。

## 验证

运行项目自带的无依赖验证脚本：

```bash
python3 scripts/validate_skill.py
```

GitHub Actions 会在 push 和 pull request 时执行同一项检查。

## 贡献

欢迎提交能够改善科学忠实度、编辑一致性、触发准确性或易用性的修改。请保持 `skills/sae/` 内的可安装技能精简，不要把项目说明文档放入其中。提交前请使用真实论文段落测试，并运行验证脚本。

## 许可证

本项目采用 [MIT License](LICENSE)。
