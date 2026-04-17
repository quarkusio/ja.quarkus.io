# Kafka翻訳品質比較 - サンプルファイル

このディレクトリには、Kafka翻訳品質比較レポート作成時に使用した実際のPOファイルが含まれています。

## ファイル一覧

- **manual.po** - 手動翻訳版（オリジナル）
  - 翻訳者が手動で翻訳したもの
  - 元ファイル: `l10n/po/ja_JP/_guides/kafka.adoc.po`
  - サイズ: 244KB
  
- **gemini.po** - Gemini翻訳版
  - tsujiツールでGemini（OpenAI互換API経由）を使用して翻訳
  - 翻訳時間: 425秒（約7分）
  - サイズ: 257KB
  - コマンド: `./tsujiw po machine-translate --isAsciidoc -p <file>`
  
- **deepl.po** - DeepL翻訳版
  - tsujiツールでDeepL APIを使用して翻訳
  - 翻訳時間: 8.5秒（**Geminiの50倍速！**）
  - サイズ: 265KB（最も冗長）
  - コマンド: `./tsujiw -Dtsuji.translator.type=deepl po machine-translate --isAsciidoc -p <file>`

- **purged.po** - 翻訳を削除したベースファイル
  - サイズ: 122KB

## 比較レポート

詳細な比較結果は親ディレクトリの `kafka-quality-comparison.md` を参照してください。

## 実行日

2026-04-17

## 対象ドキュメント

- **ファイル**: kafka.adoc
- **セグメント数**: 624
- **サイズ**: 244KB
- **トピック**: Apache Kafkaを使用したメッセージング
