# Deploy Lambda Function with GitHub Actions and CloudFormation

## Motivation

We will test the deployment of Lamdba function via GitHub Actions and
AWS CloudFormation.

## Overview

1. Log in AWS via sso.

2. Prepare simple python function.

3. Create an IAM user for Lambda.

4. Test Lambda function from aws cli.

3. Create an IAM user for the deployment.

6. Edit GitHub Action deployment file


## Procedure

### Log in AWS via sso

```
aws login sso
```
Set [$AWS_PROFILE](https://docs.aws.amazon.com/ja_jp/cli/v1/userguide/cli-configure-envvars.html)
so that we do not need to attach '--profile XXXX' everytime we execute aws cli.

### Log in AWS via sso




<!-- ------------------------------  -->

# END

<!-- ####################  -->
