config:
	./gen-config.sh
build:
	sam build
test: build
	sam local invoke -e events/event.json
deploy: build config
	sam deploy --resolve-image-repos --resolve-s3
logs:
	sam logs --stack-name lambda-consumer-test-sam --tail

