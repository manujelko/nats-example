#!/bin/bash

protoc --python_out=. --pyi_out=. message.proto
