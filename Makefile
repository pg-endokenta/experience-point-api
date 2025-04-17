docker.PHONY: dev-build
dev-build:
	docker compose -f compose.yaml build

.PHONY: dev-up-d
dev-up-d:
	docker compose -f compose.yaml up -d

.PHONY: dev
dev:
	@make dev-build
	@make dev-up-d

.PHONY: down
down:
	docker compose -f compose.yaml down


# pythonコードのリント
.PHONY: ruff-check
ruff-check:
	docker compose -f compose.yaml exec web ruff check --fix .

# pythonコードのフォーマット
.PHONY: ruff-format
ruff-format:
	docker compose -f compose.yaml exec web ruff format .

# pythonコードのフォーマットとリント
.PHONY: ruff
ruff:
	@make ruff-check
	@make ruff-format