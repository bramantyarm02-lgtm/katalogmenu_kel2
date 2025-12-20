@REM #!/bin/
@echo off

docker-compose exec -it namenode rm -rf data
docker-compose exec -it namenode mkdir data

docker cp ./data/tools namenode:/data/
docker cp ./data/code/reducer.py namenode:/data/
docker cp ./data/code/mapper.py namenode:/data/
docker cp ./data/input/input.json namenode:/data/

@REM 1. Create HDFS folder for input/output
docker-compose exec -it namenode hdfs dfs -mkdir -p /user/student
docker-compose exec -it namenode hdfs dfs -mkdir -p /user/student/input
docker-compose exec -it namenode hdfs dfs -mkdir -p /user/student/output

@REM 2. Remove old output if exists
docker-compose exec -it namenode hdfs dfs -rm -r /user/student/output

@REM 3. Upload input data
docker-compose exec -it namenode hdfs dfs -put -f /data/input.json /user/student/input/input.json

@REM 4. Run Hadoop Streaming job
docker-compose exec -it namenode hadoop jar /data/tools/hadoop-streaming-2.7.3.jar -files /data/mapper.py,/data/reducer.py -mapper "python3 mapper.py" -reducer "python3 reducer.py" -input /user/student/input/input.json -output /user/student/output

@REM 5. Fetch result to host (optional)
docker-compose exec -it namenode hdfs dfs -get -f /user/student/output/part-00000 /data/output.txt

echo "=== OUTPUT ==="
docker-compose exec -it namenode cat /data/output.txt

docker cp namenode:/data/output.txt ./data/output
