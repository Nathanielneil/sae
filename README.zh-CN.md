<picture>
  <source media="(max-width: 600px)" srcset="assets/hero-mobile.svg">
  <img src="assets/hero.svg" width="100%" alt="SAE · 标准学术英文编辑">
</picture>

**SAE 是用于科研论文英文润色的 Codex Skill。** 它改善句子表达，保留研究测量了什么、结果由谁报告，以及结论有多大把握。

[English](README.md)　·　[快速上手](#快速上手)　·　[编辑规范](skills/sae/SKILL.md)

## 看一处修改

<picture>
  <source media="(max-width: 600px)" srcset="assets/proof-mobile.svg">
  <img src="assets/proof.svg" width="100%" alt="英文校样：删去 Of course，保留 these results do not establish that the method can fully replace conventional methods，句首改为大写。">
</picture>

“Of course” 是可以删掉的铺垫。“Do not establish” 则限定了结论：这些结果尚不能证明该方法可以完全替代传统方法。

<picture>
  <source media="(max-width: 600px)" srcset="assets/values-zh-mobile.svg">
  <img src="assets/values-zh.svg" width="100%" alt="在同一示例的测试队列中，所提方法的准确率为 87.4%，基线模型为 81.2%。">
</picture>

在这个虚构示例中，**87.4%** 属于所提方法，**81.2%** 属于基线模型。改写后要核对数值与模型是否仍然对应，引文也要留在它支持的主张旁。[查看完整润色对照](examples/abstract.md)

## 什么时候需要作者确认

<picture>
  <source media="(max-width: 600px)" srcset="assets/decisions-zh-mobile.svg">
  <img src="assets/decisions-zh.svg" width="100%" alt="语言问题直接改；证据冲突时保留主张，并在允许时询问作者；片段缺少支持材料时保留原主张。">
</picture>

只看到摘要，不能据此判定某项主张错误。如果已提供的材料确实矛盾，SAE 会先保留原意，在允许问询时指出具体冲突。改变科学含义需要作者明确授权。

**只要正文时：** SAE 修改能确定的部分，保留无法安全消除的歧义。只有整个任务都依赖缺失信息时，才先请求澄清。

## 快速上手

```bash
git clone https://github.com/Nathanielneil/sae.git
cd sae
./scripts/install.sh
```

在 Codex 中输入下面的请求，再粘贴英文原文：

> 使用 $sae 润色以下 Discussion。保留主张强度，先给出正文，再列出必要的作者问询。

<details>
<summary>安装位置与更新方式</summary>

默认安装位置是 `${CODEX_HOME:-$HOME/.codex}/skills/sae`。未识别时请开启新的 Codex 会话。更新已有安装请运行 `./scripts/install.sh --force`。如需手动安装，确认目标目录不存在后，将 `skills/sae/` 复制到 Codex 的 skills 目录。

</details>

[行为案例与验证方法](tests/README.md)　·　[MIT 许可证](LICENSE)
