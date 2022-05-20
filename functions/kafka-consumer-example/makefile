config:
	./gen-config.sh
build:
	sam build
deploy:
	sam deploy --resolve-image-repos --resolve-s3
build-deploy: build deploy
all: config build deploy
