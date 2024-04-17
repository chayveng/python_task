#!/bin/bash

celery -A tasks worker --loglevel=info

sleep 5

python main.py