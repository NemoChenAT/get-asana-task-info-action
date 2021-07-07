#!/bin/sh

taskTitle=$(python3 get_asana_task_info.py $1 $2 2>&1)
echo ::set-output name=taskTitle::$taskTitle
