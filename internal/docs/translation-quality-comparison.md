# 翻訳品質比較レポート：手動 vs Gemini vs DeepL（Kafkaガイド）

本レポートは、Quarkusドキュメント「kafka.adoc」（624エントリ、244KB）を題材に、
手動翻訳、Gemini翻訳、DeepL翻訳の3つの手法の翻訳品質を多面的に比較したものです。

---

## 1. 主要な発見事項

### 1.1 翻訳速度

- **DeepL**: 8.5秒（最速、Geminiの**50倍速**）
- **Gemini**: 425秒（約7分）
- **手動翻訳**: （時間計測なし、通常は数日～数週間）

**624エントリという大規模ファイルで、DeepLの圧倒的な速さが際立つ結果となりました。**

### 1.2 主要技術用語の訳語

| 英語 | 手動 | Gemini | DeepL | 評価 |
|------|------|--------|-------|------|
| extension | エクステンション | エクステンション | 拡張機能 | Quarkusでは「エクステンション」が標準 |
| scalable | 拡張性が高く | 高いスケーラビリティ | 拡張性が高く | 手動・DeepLが自然な日本語 |
| secure | 安全な | セキュアな | 安全な | 手動・DeepLが自然な日本語 |
| publish | 発行 | 発行 | publish（英語のまま） | 手動・Geminiが訳語を提供 |
| subscribe | 購読 | 購読 | subscribe（英語のまま） | 手動・Geminiが訳語を提供 |

**評価**:
- **重要**: DeepLは技術用語を英語のまま残す傾向（publish/subscribe）
- Geminiはカタカナ語を好む傾向（スケーラビリティ、セキュア）
- 手動翻訳は日本語訳を優先（拡張性、安全、発行、購読）



---

## 2. 具体的な翻訳例の品質比較

### 例1: Kafkaの紹介文（技術用語の訳し方）

**原文**:
```
https://kafka.apache.org[Apache Kafka] is a popular open-source distributed event streaming platform.
It is used commonly for high-performance data pipelines, streaming analytics, data integration, and mission-critical applications.
Similar to a message queue, or an enterprise messaging platform, it lets you:
```

**手動翻訳**:
```
link:https://kafka.apache.org[Apache Kafka] は、人気の高いオープンソースの分散型イベントストリーミングプラットフォームです。
高性能なデータパイプライン、ストリーミング分析、データ統合、ミッションクリティカルなアプリケーションなどによく利用されています。
メッセージキューやエンタープライズメッセージングプラットフォームに似ており、以下のことが可能です。
```

**Gemini翻訳**:
```
https://kafka.apache.org[Apache Kafka] は、人気の高いオープンソースの分散型イベントストリーミングプラットフォームです。高性能なデータパイプライン、ストリーミング分析、データ統合、ミッションクリティカルなアプリケーションなどによく利用されています。メッセージキューやエンタープライズメッセージングプラットフォームに似ており、以下のことが可能です。
```

**DeepL翻訳**:
```
https://kafka.apache.org[Apache Kafka]は、広く普及しているオープンソースの分散型イベントストリーミングプラットフォームです。
高性能なデータパイプライン、ストリーミング分析、データ統合、およびミッションクリティカルなアプリケーションで一般的に利用されています。
メッセージキューやエンタープライズメッセージングプラットフォームと同様に、以下のことが可能です：
```

**評価**:
- ✅ 手動: 「人気の高い」が自然、3行目も適切に訳出
- ✅ Gemini: `https://` を維持（原文通り）、「人気の高い」が自然、改行なしで読みやすい
- △ DeepL: 「広く普及している」がやや冗長、「一般的に利用」が直訳的、「同様に」や全角コロン「：」を使用

---

### 例2: publish/subscribeの訳語（技術用語の翻訳方針）

**原文**:
```
*publish* (write) and *subscribe* to (read) streams of events, called _records_.
```

**手動翻訳**:
```
_レコード_ と呼ばれるイベントのストリームを *発行* （書き込み）したり、 *購読* （読み込み）したりすることができます。
```

**Gemini翻訳**:
```
*発行* (書き込み) および *購読* (読み込み) するイベントストリーム (_レコード_ と呼ばれます)。
```

**DeepL翻訳**:
```
イベントのストリーム（_レコード_と呼ばれるもの）に対して、*publish*（書き込み）および *subscribe*（読み取り）を行います。
```

**評価**:
- ✅ 手動: 「発行」「購読」と訳し、日本語として理解しやすい
- ✅ Gemini: 「発行」「購読」と訳し、簡潔
- ❌ DeepL: **「publish」「subscribe」を英語のまま残す** → Kafka初心者には分かりにくい

**重要**: publish/subscribeはKafkaの基本概念で、日本語訳（発行/購読）を提供する方が親切

---

### 例3: 技術的特性の説明（カタカナ語 vs 日本語）

**原文**:
```
And all this functionality is provided in a distributed, highly scalable, elastic, fault-tolerant, and secure manner.
```

**手動翻訳**:
```
そして、これらの機能はすべて、分散型で、拡張性が高く、弾力性があり、耐障害性があり、安全な方法で提供されます。
```

**Gemini翻訳**:
```
そして、これらの機能はすべて、分散型で、高いスケーラビリティ、弾力性、耐障害性、およびセキュアな方法で提供されます。
```

**DeepL翻訳**:
```
そして、これらすべての機能は、分散型で、拡張性が高く、弾力性があり、耐障害性に優れ、かつ安全な形で提供されています。
```

**評価**:
- ✅ 手動: すべて日本語訳、最も読みやすい
- △ Gemini: 「スケーラビリティ」「セキュア」とカタカナ化 → やや読みにくい
- ✅ DeepL: 「拡張性」「安全」と日本語訳、自然

---

### 例4: 処理の説明（文構造の違い）

**原文**:
```
*process* streams of records as they occur or retrospectively.
```

**手動翻訳**:
```
レコードのストリームを発生時または遡及的に *処理* します。
```

**Gemini翻訳**:
```
レコードのストリームを、発生時または遡及的に *処理* します。
```

**DeepL翻訳**:
```
*処理*は、レコードのストリームが発生した時点で、あるいは事後的に行います。
```

**評価**:
- ✅ 手動: 簡潔で自然
- ✅ Gemini: 読点で区切り、わずかに明確
- △ DeepL: 主語「処理は」で始まり、やや不自然

---

### 例5: フレームワークの紹介（リンク表記の違い）

**原文**:
```
Quarkus provides support for Apache Kafka through the SmallRye Reactive Messaging framework.
Based on the Eclipse MicroProfile Reactive Messaging specification 2.0, it proposes a flexible programming model bridging CDI and event-driven.
```

**手動翻訳**:
```
Quarkus は、 https://smallrye.io/smallrye-reactive-messaging/[SmallRye Reactive Messaging] フレームワークを通じて Apache Kafka のサポートを提供します。
Eclipse MicroProfile Reactive Messaging 仕様 2.0 に基づいて、CDI とイベント駆動型を橋渡しする柔軟なプログラミングモデルを提案します。
```

**Gemini翻訳**:
```
Quarkus は、https://smallrye.io/smallrye-reactive-messaging/[SmallRye Reactive Messaging] フレームワークを通じて Apache Kafka のサポートを提供します。Eclipse MicroProfile Reactive Messaging 仕様 2.0 に基づいて、CDI とイベント駆動型を橋渡しする柔軟なプログラミングモデルを提案します。
```

**DeepL翻訳**:
```
Quarkusは、https://smallrye.io/smallrye-reactive-messaging/（SmallRye Reactive Messaging）フレームワークを通じて、Apache Kafkaのサポートを提供しています。
Eclipse MicroProfile Reactive Messaging仕様2.0に基づいており、CDIとイベント駆動型を橋渡しする柔軟なプログラミングモデルを提案しています。
```

**評価**:
- ✅ 手動: AsciiDoc記法を維持、スペースあり
- ✅ Gemini: AsciiDoc記法を維持、スペースあり
- ❌ DeepL: リンク記法を変更（[]を（）に）、スペースなし → AsciiDocとして不正

---

## 3. 総合評価

### 3.1 翻訳の正確性

| 手法 | スコア | コメント |
|------|--------|----------|
| 手動 | ⭐⭐⭐⭐⭐ | 正確で自然な日本語 |
| Gemini | ⭐⭐⭐⭐⭐ | 技術的に正確、AsciiDoc記法も維持 |
| DeepL | ⭐⭐⭐☆☆ | AsciiDoc記法を変更、publish/subscribeを未訳 |

### 3.2 日本語の自然さ

| 手法 | スコア | コメント |
|------|--------|----------|
| 手動 | ⭐⭐⭐⭐⭐ | 最も自然で読みやすい日本語 |
| Gemini | ⭐⭐⭐⭐☆ | カタカナ語がやや多い（スケーラビリティ等） |
| DeepL | ⭐⭐⭐☆☆ | 全角記号が多すぎて技術文書に不適合 |

### 3.3 用語の一貫性

| 手法 | スコア | コメント |
|------|--------|----------|
| 手動 | ⭐⭐⭐⭐⭐ | Quarkus標準用語に完全準拠、技術用語も適切に訳出 |
| Gemini | ⭐⭐⭐⭐⭐ | Quarkus標準用語に準拠、技術用語も訳出 |
| DeepL | ⭐⭐☆☆☆ | 「拡張機能」、publish/subscribeを未訳など問題あり |

### 3.4 翻訳スピード

| 手法 | スコア | コメント              |
|------|--------|-------------------|
| 手動 | ⭐☆☆☆☆ | 未計測（通常、数十分、数時間）   |
| Gemini | ⭐⭐⭐☆☆ | 425秒（約7分）         |
| DeepL | ⭐⭐⭐⭐⭐ | 8.5秒（Geminiの50倍速！） |

### 3.5 文体の適切性（技術文書として）

| 手法 | スコア | コメント |
|------|--------|----------|
| 手動 | ⭐⭐⭐⭐⭐ | 技術文書に最適、用語訳も親切 |
| Gemini | ⭐⭐⭐⭐☆ | 技術文書として適切だが、カタカナ語やや多め |
| DeepL | ⭐⭐☆☆☆ | 全角記号・英語未訳が技術文書に不適切 |

---

## 4. 統計サマリー（624エントリ）

### 4.1 平均文字数
- 手動: 93.7文字
- Gemini: 93.2文字
- DeepL: 98.9文字（最も冗長）

### 4.2 敬語表現の使用頻度
- 手動: 1526回
- Gemini: 1530回
- DeepL: 1580回（最も丁寧）


---

## 5. 結論

1. **Gemini翻訳** (推奨): 
   - 速度、品質、用語の一貫性のバランスが最良
   - AsciiDoc記法を正しく維持
   - 技術用語を適切に訳出（publish → 発行、subscribe → 購読）
   - 7分という実用的な速度
   
2. **手動翻訳**: 
   - 最高品質だが時間とコストが膨大
   - 日本語として最も自然で読みやすい

3. **DeepL翻訳**: 
   - **8.5秒という圧倒的な速さ**（Geminiの50倍速）
   - しかし以下の重大な問題あり：
     - 全角記号を大量使用（コロン280回、カッコ376回）
     - AsciiDoc記法を破壊（[]を（）に変更）
     - 技術用語を未訳のまま残す（publish/subscribe）
     - 用語の不一致（extension → 拡張機能）
   - **後処理が必須だが、その手間を考えるとメリットが薄い**
