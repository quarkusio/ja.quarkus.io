# Quarkusの使用状況分析

## Quarkusが使用状況分析を収集する理由は何ですか？

使用状況分析（テレメトリ収集）は、Quarkusチームやコントリビューターにとって、どのオペレーティングシステム、Javaバージョン、ビルドシステム、エクステンションなどが使用されているかを測定するために非常に貴重なものです。このサービスはRed Hatによって提供されており、詳細は[usage policy](/usage/policy)ページに記載されています。

## これはどのように機能するのでしょうか？

この情報を取得するために、Quarkus 3.2以降では、Quarkusを初めてdevモード（`quarkus dev`、 `mvn quarkus:dev`など）で実行したときに、匿名のビルドデータをQuarkusコミュニティに提供することに同意するかどうかを尋ねられます。

![/assets/images/usage-prompt-arrows.png](/assets/images/usage-prompt-arrows.webp)

By answering **"Yes"**, when you perform a quarkus build, anonymized data is sent to gather usage statistics on how Quarkus is being used and adopted.

However if you answer **"No"**, then no usage data is sent and you will not be asked again.

We will share what is learned from these anonymous usage data and plan on integrate things like usage and adoption into sites like [extensions.quarkus.io](https://extensions.quarkus.io) and [code.quarkus.io](https://code.quarkus.io).

## How can I enable and disable ?

Build time analytics is not active by default. If you have opted in and would like to disable build time analytics or would like to later enable collection, you can do so in two ways:

### Set globally

You can manually configure the global settings by editing the `io.quarkus.analytics.localconfig` file in the `.redhat` folder of your user’s home directory.

#### To enable analytics collection

```
{"disabled":false}
```

#### To disable analytics collection

```
{"disabled":true}
```

### Set per build

You can configure it for a given build by using the `quarkus.analytics.disabled` system property:

- To disable analytics collection, set `quarkus.analytics.disabled` to `true`.

- To enable analytics collection, set `quarkus.analytics.disabled` to `false`.


For instance, when using Maven, you can disable analytics collection for a single run with:

```
./mvnw clean install -Dquarkus.analytics.disabled=true
```
