FROM amazon/aws-lambda-python:3.8

RUN pip install --upgrade pip && \
pip install --upgrade awscli

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

COPY login_lambda.py ${LAMBDA_TASK_ROOT}

CMD [ "login_lambda.lambda_handler" ]