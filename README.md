# cloudbox
Cloud stack powered by Localstack for experimentation

## Run stack
```bash
> ./run stack
```

## CLI
```bash
> awslocal s3api create-bucket --bucket sample-bucket
> aws --endpoint-url=http://localhost:4566 s3api put-bucket-acl --bucket sample-bucket --acl public-read
> awslocal s3api put-object --bucket sample-bucket --key index.html --body index.html
> aws --endpoint-url=http://localhost:4566 s3 cp persons.json s3://sample-bucket/
> awslocal s3api list-buckets
> aws configure list
> localstack config validate
> localstack logs
> localstack status services
```

## Endpoints
```
http://localhost:4566/sample-bucket
```