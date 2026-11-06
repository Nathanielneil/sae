<div align="center">

<img src="assets/hero.svg" alt="SAE — 标准学术英文编辑。表达清楚，含义完整。" width="100%">

**为科学论文提供准确、克制的英文编辑。**<br>
一个可复用的 Codex Skill，让语言更清楚，主张更忠实，边界更明确。

[English](README.md) · [编辑示例](#一次克制的编辑) · [安装](#安装) · [编辑规范](skills/sae/SKILL.md)

[![Checks](https://img.shields.io/github/actions/workflow/status/Nathanielneil/sae/validate.yml?branch=main&style=flat-square&label=structure%20%26%20fixtures)](https://github.com/Nathanielneil/sae/actions/workflows/validate.yml)
[![MIT](https://img.shields.io/badge/license-MIT-47665b?style=flat-square)](LICENSE)

</div>

## 一次克制的编辑

SAE 改善语法、简洁性、术语和段落内部衔接，保留科学主张、数值细节、引文及必要的不确定性。

**润色前**

> It should be emphasized that the proposed method achieved an accuracy of 87.4% in the test cohort, whereas the baseline model achieved an accuracy of 81.2%. Of course, these results do not establish that the method can fully replace conventional methods.

**润色后**

> In the test cohort, the proposed method achieved an accuracy of 87.4%, compared with 81.2% for the baseline model. These results do not establish that the method can fully replace conventional methods.

删除空泛铺垫，保留两个数值、各自对应的模型，以及关于替代传统方法的限制。[查看带说明的示例 →](examples/abstract.md)

## 编辑边界

| 情形 | SAE 的处理方式 |
|---|---|
| 改善语言不会改变科学主张 | 直接编辑；已经清楚的句子保持不变。 |
| 修改会改变机制、结论或主张强度 | 保留内容，在允许问询时请作者确认。 |
| 提供的片段缺少支持材料 | 将证据状态视为未知，不据此认定主张错误。 |
| 用户只需要正文 | 完成安全修改，保留无法消除的歧义，不插入说明或猜测。 |

数值与组别、条件保持对应，引文与主张保持对应，每个必要限定保留其作用范围。实质性科学修改需要明确授权。

SAE 支持标题、摘要、论文章节、图注、投稿信和审稿回复，定位于中等强度的语言编辑。翻译、事实核查、同行评审和科学性修改属于另外的任务。[完整执行规范 →](skills/sae/SKILL.md)

## 安装

```bash
git clone https://github.com/Nathanielneil/sae.git
cd sae
./scripts/install.sh
```

默认安装到 `${CODEX_HOME:-$HOME/.codex}/skills/sae`。如果尚未识别该 Skill，请开启新的 Codex 会话。

<details>
<summary>替换已有版本或手动安装</summary>

安装脚本会保护已有版本。确认需要替换时运行：

```bash
./scripts/install.sh --force
```

手动安装前，请先确认目标目录尚不存在：

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/sae "${CODEX_HOME:-$HOME/.codex}/skills/sae"
```

</details>

## 使用

```text
使用 $sae 润色以下 Discussion。保留科学含义、数据和主张强度。
先输出润色后的正文，再列出必要的作者问询。

[粘贴英文原文]
```

可按需补充目标期刊、英美拼写偏好或输出格式。如果希望省略说明，请要求**只输出润色后的正文**。SAE 会保留无法安全消除的歧义；只有整个任务都依赖缺失的科学信息时，才先请求必要澄清。

## 开发与验证

```bash
python3 scripts/validate_skill.py
python3 scripts/prepare_behavior_eval.py
```

上述检查验证 Skill 包结构与行为案例定义，**不代表模型润色质量已经通过评测**。[行为测试集](tests/README.md)提供独立请求及验收标准，用于检查主张保留、歧义处理和科学信息的对应关系。

项目文档和测试保留在 `skills/sae/` 之外。改变编辑行为时，请补充有针对性的测试案例。

---

[编辑规范](skills/sae/SKILL.md) · [示例](examples/abstract.md) · [行为测试](tests/README.md) · [MIT 许可证](LICENSE)
