deps:
	brew install python 

install:
	poetry install

run:
	poetry run vienna-cyber-art-gen --api-key ${OPENAI_API_KEY} 

test:
	poetry run pytest

clean:
	rm -rf generated_images

.PHONY: install run test clean

poetry-update:
	poetry self update

poetry-install:
	poetry install