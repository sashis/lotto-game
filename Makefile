run:
	docker build -t lotto_game . && docker run --rm --name lotto -ti lotto_game

test:
	docker build -t lotto_game . && docker run --name lotto -t -d lotto_game \
		&& docker exec lotto pytest -v && docker rm --force lotto