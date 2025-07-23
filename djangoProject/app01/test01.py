from rediscluster import RedisCluster
from rediscluster.exceptions import ClusterError
from redis.exceptions import ConnectionError, TimeoutError
from redis import Redis
# Redis连接配置
REDIS_CLUSTER_CONFIG = {
    'startup_nodes': [
        {'host': '10.51.6.49', 'port': 6379},
        # 添加其他集群节点，如{'host': '10.51.2.30', 'port': 6380},等
    ],
    'password': '',  # 请替换为实际Redis密码
    'decode_responses': True,  # 自动解码为字符串
    'socket_connect_timeout': 5,  # 连接超时时间(秒)
    'socket_timeout': 5          # 读写超时时间(秒)
}

def connect_redis():
    """连接Redis服务器并返回客户端实例"""
    try:
            # 添加详细的连接过程日志
            print("尝试连接Redis集群...")
            # print(f"连接节点: {[node for node in REDIS_CLUSTER_CONFIG['startup_nodes']]}")
            # 创建Redis客户端
            r = RedisCluster(**REDIS_CLUSTER_CONFIG)
            # r = Redis(host='10.51.6.49', port=6379, password='')
            # 测试连接
            r.ping()
            print("Redis连接成功!")
            return r
    except ClusterError as e:
        print(f"Redis集群错误: {str(e)}")
        if 'Cannot connect to any node' in str(e):
            print("错误原因: 无法连接到任何集群节点，请检查节点列表和网络连接")
        elif 'MOVED' in str(e):
            print("错误原因: 集群重定向错误，可能是节点配置不完整或集群状态异常")
        else:
            print("错误原因: 集群内部错误，请检查集群状态和节点间通信")
        return None
    except ConnectionError as e:
        print(f"Redis连接错误: {str(e)}")
        print(f"错误类型: 网络连接问题，请检查IP、端口是否可达及防火墙设置")
        return None
    except TimeoutError as e:
        print(f"Redis连接超时: {str(e)}")
        print(f"错误类型: 连接超时，请检查网络稳定性或增加超时时间配置")
        return None
    except Exception as e:
        print(f"Redis未知错误: {str(e)}")
        return None

if __name__ == '__main__':
    # 建立连接
    redis_client = connect_redis()
    
    # 如果连接成功，执行简单操作示例
    if redis_client:
        try:
            # 设置键值对
            redis_client.set('test01', 'Hello Redis!', ex=3600)  # 过期时间3600秒
            
            # 获取键值
            value = redis_client.get('test01')
            print(f"获取到的值: {value}")
            
            # 检查键是否存在
            key = 'pomp:calc:full:topTmp:20240308104500:A00082'
            exists = redis_client.exists(key)
            if exists:
                # 获取键的数据类型
                key_type = redis_client.type(key)
                print(f"键 {key} 的数据类型: {key_type}")
                
                # 根据数据类型使用相应的获取方法
                if key_type == 'string':
                    value = redis_client.get(key)
                    print(f"获取到的字符串值: {value}")
                elif key_type == 'hash':
                    value = redis_client.hgetall(key)
                    print(f"获取到的哈希值: {value}")
                elif key_type == 'list':
                    value = redis_client.lrange(key, 0, -1)
                    print(f"获取到的列表值: {value}")
                elif key_type == 'set':
                    value = redis_client.smembers(key)
                    print(f"获取到的集合值: {value}")
                elif key_type == 'zset':
                    value = redis_client.zrange(key, 0, -1, withscores=True)
                    print(f"获取到的有序集合值: {value}")
                else:
                    value = f"不支持的数据类型: {key_type}"
                    print(value)
            else:
                print(f"键 {key} 不存在")
        except Exception as e:
            print(f"Redis操作失败: {str(e)}")