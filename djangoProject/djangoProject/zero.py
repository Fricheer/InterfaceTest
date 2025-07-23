# -*- coding: utf-8 -*-
from redis import Redis
from redis import RedisCluster
from redis.exceptions import ConnectionError, TimeoutError
from django.http import JsonResponse
from redis.cluster import RedisCluster
from redis.exceptions import RedisError, ConnectionError, TimeoutError
from django.http import JsonResponse
from redis.cluster import RedisCluster, ClusterNode

# Redis连接配置
REDIS_CLUSTER_CONFIG = {
    'startup_nodes': [
        ClusterNode(host="10.51.6.49", port=6379),
        # 添加其他集群节点，如{'host': '10.51.2.30', 'port': 6380},等
    ],
    'password': '',  # 请替换为实际Redis密码
    'decode_responses': True,  # 自动解码为字符串
    'socket_connect_timeout': 5,  # 连接超时时间(秒)
    'socket_timeout': 5          # 读写超时时间(秒)
}
# 创建 Redis 集群连接
try:
    redis_cluster = RedisCluster(
        startup_nodes=REDIS_CLUSTER_CONFIG['startup_nodes'],
        password=REDIS_CLUSTER_CONFIG['password'],
        decode_responses=REDIS_CLUSTER_CONFIG['decode_responses'],
        socket_connect_timeout=REDIS_CLUSTER_CONFIG['socket_connect_timeout'],
        socket_timeout=REDIS_CLUSTER_CONFIG['socket_timeout'],
        skip_full_coverage_check=True  # 添加此参数避免节点检查问题
    )
    print("Redis 集群连接成功!")
except (ConnectionError, TimeoutError, RedisError) as e:
    print(f"Redis 集群连接失败: {e}")
    redis_cluster = None
# 方式1：使用 Redis 集群连接
def get_cache_data(request):
    if redis_cluster:
        try:
            # 测试连接
            redis_cluster.ping()
            print("Redis连接正常!")            
            # 示例：设置和获取缓存数据
            redis_cluster.set('test01', 'test011', ex=3600)  # 设置键值对，过期时间为3600秒
            value = redis_cluster.get('test01')  # 获取键值对
            # 获取键值
            value = redis_cluster.get('test01')
            print(f"获取到的值: {value}")          
#            # 检查键是否存在
            # key = 'pomp:calc:full:topTmp:20240308104500:A000821122222'
            # exists = redis_cluster.exists(key)
            key = request.GET.get('key') or request.POST.get('key')
            print(key)
            if key:
                # 获取键的数据类型
                key_type = redis_cluster.type(key)
                print(key_type)
                print(f"键 {key} 的数据类型: {key_type}")                
                # 根据数据类型使用相应的获取方法
                if key_type == 'string':
                    value = redis_cluster.get(key)
                    print(f"获取到的字符串值: {value}")
                elif key_type == 'hash':
                    value = redis_cluster.hgetall(key)
                    print(f"获取到的哈希值: {value}")
                elif key_type == 'list':
                    value = redis_cluster.lrange(key, 0, -1)
                    print(f"获取到的列表值: {value}")
                elif key_type == 'set':
                    value = redis_cluster.smembers(key)
                    print(f"获取到的集合值: {value}")
                elif key_type == 'zset':
                    value = redis_cluster.zrange(key, 0, -1, withscores=True)
                    print(f"获取到的有序集合值: {value}")
                else:
                    value = f"不支持的数据类型: {key_type}"
                    print(value)
                return JsonResponse({'key': key,'value':value})
            else:
                print(f"键 {key} 不存在")
                return JsonResponse({'message': f'键 {key} 不存在'})
        except Exception as e:
            print(f"Redis操作失败: {str(e)}")
            return JsonResponse({'message': {'error': str(e)}})
