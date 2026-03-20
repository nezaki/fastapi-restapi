# fastapi-restapi

FastAPI を使用した REST API プロジェクト。

## 必要なもの

- Docker
- VS Code + [Dev Containers 拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

## 開発環境のセットアップ

VS Code でプロジェクトを開き、「Reopen in Container」を選択.
コンテナのビルド時に `uv sync` が自動実行され、依存関係がインストールされます。

クローン後に一度だけ以下を実行して Git フックを有効化してください：

```bash
git config core.hooksPath .githooks
```

## 開発サーバーの起動

```bash
uv run uvicorn app.main:app --reload
```

サーバーが起動したら以下にアクセスできます。

- API: http://localhost:8000
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## パッケージ管理

パッケージマネージャに [uv](https://docs.astral.sh/uv/) を使用しています。

```bash
# パッケージの追加
uv add <package>

# 開発用パッケージの追加
uv add --group dev <package>

# 依存関係の同期
uv sync
```