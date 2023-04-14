# 本リポジトリの内容について

Azure Logic AppsからAzure Functionsを呼び出して利用するためのFunctionsのサンプル実装です

# 内容説明

3つのHTTPトリガー関数が実装されています。

* mono: 画像を白黒にします
* flip: 画像の左右を反転します
* resize: 画像の横幅を1/2に変換します

各関数はPOSTメソッドで呼び出され、azure.functions.HttpRequestオブジェクトのBodyで
画像のバイナリを受け取ります。その後それぞれの変換を行い、Bodyに画像バイナリを格納してazure.functions.HttpResponseオブジェクトを返却します。

# 環境前提

<https://learn.microsoft.com/ja-jp/azure/azure-functions/create-first-function-cli-python?tabs=azure-cli%2Cbash&pivots=python-mode-configuration>

のPythonプログラミングモデルv1を参考に環境を整備してください


# 操作簡易説明

* 関数の作成

```bash
func new --template "Http Trigger" --name {新しい関数名}
```

* Functionsのテスト

```bash
func start
```

* FunctionsのAzureへのデプロイ

```bash
func azure functionapp publish {関数アプリ名}
```

