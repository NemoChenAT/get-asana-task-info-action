#!/bin/sh

task_info=$(python3 /get_asana_task_info.py $1 $2 $3 2>&1)
echo ::set-output name=task_info::$task_info
