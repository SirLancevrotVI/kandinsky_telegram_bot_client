# Docker build . -t <image_name>
build:
	docker build . -t kandinsky-bot:latest

# run --env-file .env
run:
	docker run --env-file .env kandinsky-bot:latest

# run as daemon
run-d:
	docker run -d --env-file .env kandinsky-bot:latest
