# quarkus.io 翻訳プロジェクト 翻訳ガイド

quarkus.io 翻訳プロジェクトでは、[quarkus.io](https://quarkus.io) の翻訳に取り組んでいます。

## 翻訳方式

[quarkus.io](https://quarkus.io)はJekyllを用いた静的サイトであり、そのコンテンツはコンテンツは asciidoctor (.adoc) で記述されています。
レポジトリは [quarkusio/quarkusio.github.io](https://github.com/quarkusio/quarkusio.github.io ) に存在し、CC BY 3.0 に基づき公開されています。
本プロジェクトでは、.adocファイルからpo4aというユーティリティを用いてテキストを抽出し、翻訳して.adocファイルに書き戻してビルドすることで日本語版サイトを構築する方式を採っています。
po4aを用いたテキストの抽出、機械翻訳による下訳、書き戻し処理のワークフローは、GitHub Actionsによって自動化されており、
抽出されたテキストは翻訳テキストを管理するファイル形式である、.poファイルとして、l10nディレクトリ以下に保存されています。

## 翻訳への貢献

翻訳に貢献頂ける場合、本レポジトリをローカルにcloneし、手元で[l10nディレクトリ](l10n) 配下の.poファイルを編集してPull-Requestをお送り下さい。

### 翻訳作業

.poファイルは、テキストファイルですが、様々な翻訳補助ツールが編集に対応しています。例えば、[POEdit](https://poedit.net/) は
Windows/Mac/Linux での実行に対応しており、ショートカットキーも充実していることから、編集する際に使用すると便利です。

### 翻訳対象の自動取込、自動下訳

翻訳対象のファイルは、[quarkus.io](https://quarkus.io)が更新されますと定期的に本レポジトリにGitHub Actionsのワークフローにより、
自動で取り込まれ、.poファイルが作成されます。.poファイルには [quarkus-adoc-po-translator](https://github.com/doc-l10n-kit/quarkus-adoc-po-translator) を用いて
DeepL APIで自動で翻訳した訳文が挿入されますので、翻訳の際の下訳としてご活用下さい。

但し、あくまでも機械翻訳な為、てにおは等が不自然な部分も多く、「要確認」（fuzzy）としてマークされており、「要確認」マークを外さない限り、翻訳として反映されません。
訳文をレビュー、修正し、「要確認」マークを外して下さい。

### 翻訳結果のプレビュー

.poファイルを翻訳し、Pull-Requestを頂ければ、自動でGitHub Actionsでサイトのビルドが行われ、一時的にサイトを閲覧できるURLが
GitHubのPull-Requestに対するコメントとして5分程度で送信されます。
そちらの一時サイトから、翻訳結果のプレビューを確認することが出来ますので、ご活用下さい。
