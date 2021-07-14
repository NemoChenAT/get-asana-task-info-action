#!/bin/sh

taskInfo=$(python3 /get_asana_task_info.py $1 $2 $3 2>&1)
echo ::set-output name=taskInfo::$taskInfo
