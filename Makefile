all: docker

docker:
	docker build -t dovdor/change-time-to-now:latest -f build/Dockerfile .

run_docker: docker
	docker run --rm -t dovdor/change-time-to-now:latest

run:
	python src/ctn.py
