#! /bin/bash
make html

#aws s3 sync ./_build/html/nothing/ s3://docs.netscied.tw/simplicialTest --acl public-read
#aws cloudfront create-invalidation --distribution-id EJWRA9WAFT3AG --paths /simplicialTest/*

