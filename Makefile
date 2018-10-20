all: docker

clean:
	find . -iname "*.pyc" -o -iname "*~" -delete
	-rm .docker.touch

docker: .docker.touch

.docker.touch: build/Dockerfile src/ctn.py
	docker build -t dovdor/change-time-to-now:latest -f $< .
	touch $@
