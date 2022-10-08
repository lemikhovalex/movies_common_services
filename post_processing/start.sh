#!/bin/bash

./wait --WAIT_HOST_CONNECT_TIMEOUT 15 && python ./main.py

exit $?