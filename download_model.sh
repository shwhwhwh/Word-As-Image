#!/bin/bash

# 无限循环，直到下载成功
while true; do
  echo "开始尝试下载模型..."
  python3 download_model.py
  
  # 检查退出状态码：0 表示成功，非 0 表示失败
  if [ $? -eq 0 ]; then
    echo "下载成功！"
    break  # 退出循环
  else
    echo "下载中断，等待 10 秒后重试..."
    sleep 5  # 等待 10 秒避免频繁请求
  fi
done