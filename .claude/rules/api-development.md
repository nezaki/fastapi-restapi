---
paths:
  - "app/**"
---

# API 開発ルール

## 各層の責務

| 層 | ディレクトリ | 配置するもの |
|----|-------------|-------------|
| Domain | `domain/` | エンティティ（dataclass）・リポジトリ ABC・ドメイン例外 |
| Application | `application/` | ユースケース・層間 DTO |
| Infrastructure | `infrastructure/` | リポジトリ具体実装・DB セッション |
| Presentation | `presentation/` | Pydantic スキーマ・エンドポイント・依存性注入・エラーハンドラ |

## 依存の方向

```
Presentation  →  Application  →  Domain
                                    ↑
Infrastructure  ────────────────────┘
```

- `domain/` は他の層を一切インポートしない
- `application/` は `domain/` のみ参照
- `infrastructure/` は `domain/` の抽象リポジトリを実装する（依存性逆転の原則）
- `presentation/api/dependencies.py` が具体実装をユースケースに注入する
