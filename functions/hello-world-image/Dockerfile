FROM public.ecr.aws/lambda/python:3.9

COPY hello_world/* ./

RUN python3.9 -m pip install -r requirements.txt

# Overwrite the command by providing a different command directly in the template.
CMD ["app.lambda_handler"]