# Markdown to HTML Converter

コマンドラインから簡単に Markdown (`.md`) ファイルを HTML (`.html`) ファイルに変換できる、軽量なPythonスクリプトです。

## 特徴 (Features)
- **シンプルなコマンドライン操作:** 引数を渡すだけで瞬時に変換が完了します。
- **UTF-8 完全対応:** 日本語などのマルチバイト文字も文字化けせずに安全に処理できます。

## 必須要件 (Prerequisites)
このスクリプトを実行するには、Python 3.x および外部ライブラリの `markdown` が必要です。

### セットアップ
`markdown` ライブラリがインストールされていない場合は、ターミナル（コマンドプロンプト）で以下のコマンドを実行してインストールしてください。

```bash
pip install markdown
```

## 使い方 (Usage)

ターミナルを開き、以下の構文でスクリプトを実行します。

```bash
python3 file-converter.py markdown <入力ファイルパス> <出力先ファイルパス>
```

### 引数の説明
1. `markdown` : 実行するコマンド（現在は `markdown` のみサポート）
2. `<入力ファイルパス>` : 変換したいMarkdownファイルのパス（例: `input.md`）
3. `<出力先ファイルパス>` : 生成されるHTMLファイルの保存先パス（例: `output.html`）

### 実行例

手元の `README.md` を `index.html` に変換したい場合のコマンドです。

```bash
python3 file-converter.py markdown README.md index.html
```
実行が成功すると、同じディレクトリに `index.html` が生成されます。

## エラーハンドリング (Error Handling)
引数の数が正しくない場合（不足している、または多すぎる場合）は、以下のような使い方を促すヘルプメッセージを表示し、プログラムを安全に終了します。

```text
正しい引数を入力してください
引数の形:
python3 file-converter.py markdown 入力ファイル 出力先ファイル
```