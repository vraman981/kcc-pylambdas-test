# kcc-pylambdas-test


## 1. Setup

1. **Python**

    >``─❯ brew install python3``

2. **Pip package manager**

    >``─❯ brew install pip3``

3. **Virtualenv** - Create an isolated environment

    >``─❯ pip install virtualenv``

    >``─❯ python3 -m venv py3.11.6``
    
    >``─❯ source py3.11.6/bin/activate``

## 2. Install required packages  and create requriements file

    >``─❯ pip3 install boto3``
    
    >``─❯ pip freeze > requirements.txt ``
    
## 3. Build 

    >``─❯ pip3 install -r requirements.txt -t . ``

    >``─❯ zip -r create-pytest.zip . ``

## 3. Deploy 

1. source switch

    >``─❯ source switch simba-staging us-east-1 contributor``


2. deploy a new function 

    >``─❯ aws lambda create-function --function-name create-pytest \
    --zip-file fileb://create-pytest.zip \
    --handler create-pytest.lambda_handler \
    --runtime python3.11 \
    --role arn:aws:iam::608710152824:role/AskKardia-bot \
    --region us-east-1
    ``

3. Update an existing function code
    >``
    ─❯ aws lambda update-function-code  --function-name create-pytest \
    --zip-file fileb://create-pytest.zip
    ``

4. Invoke a lamdba function from aws commandline

    >``
    ─❯ aws lambda invoke --profile aws-staging-us-east-1-contributor \
    --function-name GetChapterLambda \
    --invocation-type RequestResponse \
    --payload file://chapterreq.json \
    response.json
    ``







