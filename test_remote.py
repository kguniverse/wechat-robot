import requests,time,json,threading,random
 
class Presstest(object):
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Content-Type': 'application/json; charset=UTF-8',
  }
  def __init__(self,press_url):
    self.press_url = press_url
    self.session = requests.Session()
    self.session.headers = self.headers
 
  def login(self):
    '''登陆获取session'''
    data = data = {'t': int(time.time() * 1000), 'userName': self.phone, 'passWord': self.password}
    res = self.session.post(self.login_url,data=json.dumps(data))
    XToken = res.json().get('data').get('companyToken')
    self.session.headers['X-Token'] = XToken
 
  def testinterface(self):
    '''压测接口'''
    # self.session.headers['X-UnionId'] = 'of6uw1CUVhP533sQok'
    text = []
    text.append(''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5)))
    text.append(''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5)))
    text.append(''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5)))
    userid = ''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5))
    data = {"userid": userid,
            "text": text[random.randint(0, 2)]}
    global ERROR_NUM
    try:
      html = self.session.post(self.press_url, data=json.dumps(data))
    #   if html.json().get('code') != 0:
    #     print(html.json())
    #     ERROR_NUM += 1
    except Exception as e:
      print(e)
      ERROR_NUM += 1
 
  def testonework(self):
    '''一次并发处理单个任务'''
    i = 0
    while i < ONE_WORKER_NUM:
      i += 1
      self.work()
    time.sleep(LOOP_SLEEP)
 
  def run(self):
    '''使用多线程进程并发测试'''
    t1 = time.time()
    Threads = []
 
    for i in range(THREAD_NUM):
      t = threading.Thread(target=self.testonework, name="T" + str(i))
      t.setDaemon(True)
      Threads.append(t)
 
    for t in Threads:
      t.start()
    for t in Threads:
      t.join()
    t2 = time.time()
 
    print("===============压测结果===================")
    print("URL:", self.press_url)
    print("任务数量:", THREAD_NUM, "*", ONE_WORKER_NUM, "=", THREAD_NUM * ONE_WORKER_NUM)
    print("总耗时(秒):", t2 - t1)
    print("每次请求耗时(秒):", (t2 - t1) / (THREAD_NUM * ONE_WORKER_NUM))
    print("每秒承载请求数:", 1 / ((t2 - t1) / (THREAD_NUM * ONE_WORKER_NUM)))
    print("错误数量:", ERROR_NUM)
 
if __name__ == '__main__':
  press_url = 'http://127.0.0.1:8000/test'
 
  THREAD_NUM = 10     # 并发线程总数
  ONE_WORKER_NUM = 500   # 每个线程的循环次数
  LOOP_SLEEP = 0.1    # 每次请求时间间隔(秒)
  ERROR_NUM = 0      # 出错数
 
  obj = Presstest(press_url=press_url)
#   obj.login()
  obj.run()