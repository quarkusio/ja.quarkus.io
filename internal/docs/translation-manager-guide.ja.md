# quarkus.io 翻訳プロジェクト 翻訳マネージャー向けガイド

※ このガイドは、ローカライゼーションチームの翻訳マネージャー向けのガイドです。一般の翻訳参加者は [翻訳ガイド](../../translation-guide.ja.md) を参照して下さい。

## 翻訳方式

[quarkus.io](https://quarkus.io)はJekyllを用いた静的サイトであり、そのコンテンツはasciidoctor (.adoc) で記述されています。
本プロジェクトでは、[tsuji](https://github.com/doc-l10n-kit/tsuji) というツールを使用し、.adocファイルから po4a ユーティリティでテキストを抽出し、
翻訳して.adocファイルに書き戻してビルドすることで日本語版サイトを構築しています。

## 自動化されたワークフロー

ほとんどのプロセスは GitHub Actions により自動化されています:

### 1. 同期ワークフロー (sync-upstream)

**実行タイミング:** 毎週日曜日 8:00 AM UTC (または手動実行)

**処理内容:**
1. upstream リポジトリ（quarkusio/quarkusio.github.io）を最新版に同期
2. `./tsujiw jekyll extract` で新規・更新ファイルから PO ファイルを抽出
3. `./tsujiw po apply-tmx` で確定翻訳メモリを適用
4. `./tsujiw po apply-fuzzy-tmx` でファジー翻訳メモリを適用
5. `./tsujiw po machine-translate` で DeepL API による機械翻訳を実行
6. `./tsujiw jekyll update-stats` で翻訳統計を更新

**結果:** 新しいコンテンツが翻訳用の PO ファイルとして l10n/po/ja_JP/ に追加されます。

### 2. ビルド・デプロイワークフロー (build)

**実行タイミング:** 毎日 9:00 AM UTC、main ブランチへの push 後、または手動実行

**処理内容:**
1. `./tsujiw tmx generate` で翻訳メモリ（TMX）ファイルを更新
2. `./tsujiw jekyll update-stats` で翻訳統計を更新
3. override.csv をチェックし、古い override ファイルがあれば Issue を作成
4. `./tsujiw jekyll build` でローカライズされたサイトをビルド
5. GitHub Pages (docs ブランチ) へデプロイ

**結果:** https://ja.quarkus.io が最新の翻訳内容で更新されます。

### 3. Pull Request プレビューワークフロー (pull-request)

**実行タイミング:** Pull Request 作成・更新時

**処理内容:**
1. PR の変更内容でサイトをビルド
2. surge.sh へ一時デプロイ (`pr-preview-{PR番号}-ja-quarkusio.surge.sh`)
3. PR コメントにプレビュー URL を投稿

**結果:** レビュアーが変更内容を実際のサイトで確認できます。

## 翻訳マネージャーの作業フロー

### 翻訳着手の宣言

同じファイルを複数のメンバが同時に作業着手し、重複して作業して無駄が発生するのを避ける為、翻訳作業に着手する際は、
GitHubのIssueで、どのファイル、範囲を対象に作業着手するか宣言をお願いします。
Issueを立てる際は既存のIssueで既に誰かが対象に対して作業着手を宣言していないか、ご確認下さい。

### Git レポジトリの最新化

作業着手にあたり、手元のレポジトリを最新化します:

```bash
# ja.quarkus.io レポジトリのディレクトリで実行
git checkout main
git fetch origin
git reset --hard origin/main
```

### 翻訳作業

PO ファイルは [POEdit](https://poedit.net/) などの翻訳支援ツールで編集できます。
機械翻訳による下訳が "fuzzy" マークと共に挿入されているので、レビュー・修正して fuzzy マークを外してください。

### 翻訳結果の送信

#### 1. ブランチの作成

```bash
# 作業用ブランチを作成（ブランチ名は翻訳対象ファイル名等、適宜設定）
git checkout -b translate-example-guide
```

#### 2. 変更のコミット

```bash
# 変更をステージング
git add l10n/po/ja_JP/_guides/example.adoc.po

# コミット作成
git commit -m "Translate example guide"
```

#### 3. ブランチの送信と Pull Request 作成

```bash
# GitHub へブランチを送信
git push origin translate-example-guide
```

その後、[Pull Request 一覧ページ](https://github.com/quarkusio/ja.quarkus.io/pulls) から Pull Request を作成してください。
数分後、自動的にプレビューサイトが構築され、PR コメントに URL が投稿されます。

## ローカルでのビルド・プレビュー

GitHub Actions を待たずに手元で確認したい場合:

### セットアップ

```bash
# 必要なツールのインストール（Ubuntu の場合）
bin/setup-build-env-on-ubuntu
```

### ビルド

```bash
# サイトをビルド
./tsujiw jekyll build

# ビルド結果は docs/ ディレクトリに生成されます
```

### プレビューサーバー起動

```bash
# ローカルサーバー起動
./tsujiw jekyll serve

# ブラウザで http://localhost:4000 にアクセス
```

## 翻訳統計の確認

翻訳進捗状況は以下のファイルで確認できます:

- `l10n/stats/translation.csv` - 全体統計
- `l10n/stats/latest-guides-translation.csv` - 最新ガイド
- `l10n/stats/{version}-guides-translation.csv` - バージョン別ガイド
- `l10n/stats/posts-translation.csv` - ブログ記事
- `l10n/stats/misc-translation.csv` - その他（_includes, _data など）

## override ファイルの管理

HTML テンプレート（po4a で処理不可能）は `l10n/override/ja_JP/` に手動翻訳版を配置します。
upstream 側のファイルが更新された場合、`l10n/stats/override.csv` に NG ステータスが記録され、
自動的に GitHub Issue が作成されます。

## トラブルシューティング

### tsuji のバージョン更新

tsujiw スクリプトは `config/application.yaml` の version 設定を参照して自動ダウンロードします。
手動で更新したい場合:

```bash
rm -rf vendor/tsuji
./tsujiw --help  # 再ダウンロードされます
```

### DeepL API エラー

機械翻訳がエラーになる場合、環境変数 `TSUJI_TRANSLATOR_DEEPL_API_KEY` が設定されているか確認してください。
GitHub Actions では Secrets に登録済みです。

### ビルドエラー

Jekyll や po4a のエラーが発生する場合、セットアップスクリプトを再実行してください:

```bash
bin/setup-build-env-on-ubuntu
```
