# CLAUDE.md

## 1. プロジェクト概要
FastAPI を用いた REST APIサーバー

## 2. ディレクトリ構成
クリーンアーキテクチャの4層構造を採用。
```
app/
├── main.py                                          # アプリファクトリ（ルーター登録・エラーハンドラ登録のみ）
│
├── domain/                                          # 第1層: ドメイン層（外部ライブラリへの依存ゼロ）
│   ├── entities/                                    # ビジネスエンティティ（純粋な dataclass）
│   ├── repositories/                                # リポジトリの抽象インターフェース（ABC）
│   └── exceptions/                                  # ドメイン固有の例外クラス
│
├── application/                                     # 第2層: アプリケーション層（domain のみに依存）
│   ├── dto/                                         # 層間 DTO
│   └── use_cases/                                   # ユースケース
│
├── infrastructure/                                  # 第3層: インフラ層（domain の抽象を実装）
│   ├── repositories/                                # インメモリ実装（開発・テスト用）
│   └── database/                                    # SQLAlchemy 導入時に base.py / session.py を配置
│
└── presentation/                                    # 第4層: プレゼンテーション層（最外層）
    ├── schemas/                                     # Pydantic スキーマ（HTTP Request / Response）
    └── api/
        ├── dependencies.py                          # 依存性注入の集約点（Infrastructure → Application の橋渡し）
        ├── error_handlers.py                        # ドメイン例外 → HTTP ステータスのマッピング
        └── v1/
            ├── router.py                            # v1 配下のルーターを集約
            └── endpoints/                           # /api/v1/ エンドポイント定義
```

## 3. 開発環境のセットアップ — Python バージョン、仮想環境、依存関係のインストール手順、環境変数の設定

## 4. よく使うコマンド — サーバー起動、テスト実行、lint、マイグレーション、フォーマッタなど

### リンター / フォーマッター（ruff）
```bash
# lint チェック
uv run ruff check .

# lint チェック + 自動修正
uv run ruff check --fix .

# フォーマット確認（差分表示のみ）
uv run ruff format --check .

# フォーマット適用
uv run ruff format .
```

設定は `pyproject.toml` の `[tool.ruff]` セクションで管理。

### 型チェック（pyright）
```bash
# 型チェック実行
uv run pyright
```

設定は `pyproject.toml` の `[tool.pyright]` セクションで管理。

### テスト（pytest + pytest-cov）
```bash
# テスト実行（カバレッジ付き、デフォルト設定）
uv run pytest

# カバレッジなしで実行
uv run pytest --no-cov

# 特定テストのみ実行
uv run pytest tests/api/v1/test_users.py
```

設定は `pyproject.toml` の `[tool.pytest.ini_options]` と `[tool.coverage.*]` セクションで管理。

### Git フック
pre-commit フックが `.githooks/pre-commit` に配置されており、コミット前に `ruff check`・`ruff format --check`・`pyright`・`pytest` を自動実行する。

## 5. コーディング規約 — 命名規則、型ヒントのルール、import順序、docstringのスタイル

## 6. テスト方針 — テストフレームワーク、テストの配置場所、fixtureの使い方、モックの方針

## 7. DB・マイグレーション — ORM/マイグレーションツールの使い方、スキーマ変更時の手順

## 8. やってはいけないこと — プロジェクト固有のアンチパターンや注意点
