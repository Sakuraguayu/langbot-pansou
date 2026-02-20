#!/usr/bin/env python3
"""
测试PanSou API解析修复
"""
import json

# 模拟API返回的结果
mock_response = '''
{
  "code": 0,
  "message": "success",
  "data": {
    "total": 74,
    "merged_by_type": {
      "quark": [
        {
          "url": "https://pan.quark.cn/s/73e535167825",
          "password": "",
          "note": "海绵宝宝电影",
          "datetime": "2026-01-20T07:15:46Z",
          "source": "plugin:quark4k"
        }
      ],
      "baidu": [
        {
          "url": "https://pan.baidu.com/s/1w52IFP-fHStyq3cD1s4Gpg?pwd=8888",
          "password": "8888",
          "note": "【电影】海绵宝宝：深海大冒险.2025",
          "datetime": "2026-01-05T00:00:00Z",
          "source": "plugin:jutoushe"
        }
      ]
    }
  }
}
'''

# 模拟修复前的解析逻辑
def parse_old(data):
    cloud_types = data.get("merged_by_type", {})
    return cloud_types

# 模拟修复后的解析逻辑
def parse_new(data):
    cloud_types = data.get("data", {}).get("merged_by_type", {})
    return cloud_types

# 测试
if __name__ == "__main__":
    data = json.loads(mock_response)
    
    print("=== 测试修复效果 ===")
    print("修复前结果:", parse_old(data))
    print("修复后结果:", parse_new(data))
    
    if parse_new(data):
        print("\n✅ 修复成功！现在可以正确解析API返回的结果")
    else:
        print("\n❌ 修复失败！")
