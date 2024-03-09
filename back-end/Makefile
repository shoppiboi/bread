# .PHONY: b-set
# b-set:
# 	@	source .venv/bin/activate
# 	@	poetry install

.PHONY: b-run
b-run:
	@	echo "running back-end..."
	@	poetry run uvicorn src.main:app --reload

format:
	@ echo "formatting code..."
	@ poetry run ruff format src
