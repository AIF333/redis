import redis

# r=redis.Redis(host='localhost',port=6379,db=0,password='yeteng123') # 普通模式
# r=redis.StrictRedis(host='localhost',port=6379,db=0,password='yeteng123') # 严格模式，推荐用这个

pool = redis.ConnectionPool(host='localhost',port=6379,db=0,password='yeteng123') # 使用连接池
r=redis.StrictRedis(connection_pool=pool)


#############  类型1 String类型 #############
r.set('hello','world')
print(r.get('hello')) # 得到的 b'world' 字节类型
r.set("number",8)
print(r.get("number")) # b'8'
r.incr("number") # 对number进行自增1
print(r.get("number"))  # b'9'
r.decr("number",2) # 对number进行减2操作
print(r.get("number"),type(r.get("number").decode("utf-8"))) #  b'7' <class 'str'>

#############  类型2 List类型 #############
r.lpush("list1","AIF") # 列表左侧插入
r.lpush("list1",333)
r.lpush("list1",'nb1')

print(r.llen("list1")) # 取列表的长度，即元素个数
print(r.lrange("list1",0,-1)) # 展示所有元素
print(r.rpop("list1")) # 列表右侧弹出相当于队列，先进先出 b'AIF'
print(r.lpop("list1")) # 列表左侧弹出相当于栈，后进先出 b'nb'
print(r.ltrim('list1',0,2))  # True 清空 除了0-2 这三个元素以外的元素。当 start>end>0时表示清空列表 如  r.ltrim('list1',2,1)
print(r.lrange("list1",0,-1)) # 展示所有元素

############  类型3 Set类型 #############
import time
print(time.time(),type(time.time()))
t1=time.time()
r.sadd('set1','AIF')
r.sadd('set1',333)
# r.sadd('set1',t1)
r.sadd('set1',333) # set中已有的元素不会再次插入

print(r.scard("set1")) # 4   查看set集合元素个数
print(r.smembers("set1")) # 列出集合所有的元素 {b'1554290753.191328', b'AIF', b'1554290353.7294803', b'333'}
print(r.sismember("set1",333)) # True 333是否在集合中
print(r.sismember("set1",3333)) # False 3333是否在集合中

#############  类型4 Hash类型 #############
r.hset("hash1","key1","AIF333") # 设置hash1中 key1的值为"AIF333"
r.hset("hash1","key2",555)
r.hset("hash1","key3",666)
r.hmset("hash1",{"key4":"aaa","key5":"bbb"}) # 批量设置

print(r.hlen("hash1")) # 获取hash1中元素个数 5
print(r.hget("hash1",key="key1")) # 获取key1值
print(r.hmget("hash1","key1","key2","key3","key4","key5")) # 批量获取key1-key5值
print(r.hgetall("hash1")) # 获取所有的值


#############  类型5 Zset类型 #############
r.zadd("zset1",{"v1":"1","v2":3,"v3":10}) # 往zset1中添加记录 值和score（必须是可以被float类型，字符串会报错）
r.zadd("zset1",{"AIF":8,"Iverson":0.1,"yeteng":6.66})

print(r.zcard("zset1")) # 获取zset的记录数 6
print(r.zrange("zset1",0,-1,withscores=True)) # 打印zset1的记录，withscores表明是否带着 scores [(b'Iverson', 0.1), (b'v1', 1.0), (b'v2', 3.0), (b'yeteng', 6.66), (b'AIF', 8.0), (b'v3', 10.0)]





