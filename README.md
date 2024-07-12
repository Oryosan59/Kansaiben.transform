### 関西弁翻訳ツール README

---

# 関西弁翻訳ツール

このプロジェクトは、Flaskを使って標準日本語を関西弁に翻訳するツールです。標準日本語を入力し、関西弁に翻訳されたテキストを取得できます。

## 特徴

- **翻訳機能:** 標準日本語を関西弁に変換
- **ウェブインターフェース:** テキスト入力と翻訳結果を表示する使いやすいウェブインターフェース

## 始め方

### 前提条件

- Python 3.7以上
- Flask

### インストール

1. **リポジトリをクローンする:**

   ```bash
   git clone https://github.com/Oryosan59/Kansaiben.transform.git
   cd Kansaiben.transform
   ```

2. **仮想環境を作成する:**

   ```bash
   python -m venv venv
   ```

3. **仮想環境を有効化する:**

   - Windowsの場合:

     ```bash
     venv\Scripts\activate
     ```

   - macOS/Linuxの場合:

     ```bash
     source venv/bin/activate
     ```

4. **必要なパッケージをインストールする:**

   ```bash
   pip install -r requirements.txt
   ```

### 使い方

1. **Flaskアプリケーションを実行する:**

   ```bash
   flask run
   ```

2. **ウェブインターフェースにアクセスする:**

   ウェブブラウザを開き、`http://127.0.0.1:5000/` にアクセスします。

3. **APIを使用する:**

   `/translate` エンドポイントに以下のJSONペイロードをPOSTリクエストとして送信します:

   ```json
   {
     "text": "ここにテキストを入力"
   }
   ```

   `curl`を使用した例:

   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"text": "ここにテキストを入力"}' http://127.0.0.1:5000/translate
   ```

## プロジェクト構成

```
Kansaiben.transform/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── static/
│   └── templates/
│       └── index.html
│
├── venv/
│
├── requirements.txt
│
└── run.py
```

- **app/**: Flaskアプリケーションのコードが含まれています。
- **app/static/**: CSSやJavaScriptなどの静的ファイルが含まれています。
- **app/templates/**: HTMLテンプレートが含まれています。
- **requirements.txt**: Pythonの依存関係がリストされています。

## コントリビュート

1. リポジトリをフォークする。
2. 新しいブランチを作成する: `git checkout -b feature/YourFeature`
3. 変更を加えてコミットする: `git commit -m 'Add some feature'`
4. ブランチにプッシュする: `git push origin feature/YourFeature`
5. プルリクエストを開く。


---
