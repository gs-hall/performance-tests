#!/bin/bash
scenario=make_top_up_operation
locust --config=./scenarios/grpc/gateway/new_user_$scenario/v1.0.conf
locust --config=./scenarios/grpc/gateway/new_user_$scenario/v1.0.conf --show-task-ratio-json > locust_grpc_gateway_new_user_${scenario}_ratio.json
load-testing-hub upload-locust-report --yaml-config=./scenarios/grpc/gateway/new_user_$scenario/load_testing_hub.yaml