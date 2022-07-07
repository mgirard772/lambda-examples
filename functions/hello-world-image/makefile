config:
	./gen-config.sh
build:
	sam build
start-local-api: build
	sam local start-api
test-local-api: build
	curl -X POST -H "Content-type: application/json" -H "x-api-key: 123" -d @events/curl-hello.json http://127.0.0.1:3000/hello
test-remote-api:
	curl -X POST -H "Content-type: application/json" -H "x-api-key: $(api-key)" -d @events/curl-hello.json $(endpoint)
local-invoke: build
	sam local invoke -e events/event.json
deploy: build config
	sam deploy --resolve-image-repos --resolve-s3 --capabilities CAPABILITY_IAM $(deploy-args)
delete:
	sam delete --no-prompts
