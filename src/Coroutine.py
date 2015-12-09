#coding:utf-8
'''
Created on 2015��12��8��

@author: SHIYU
'''
'''
def consumer():
    r=''
    while True:
        n=yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r='200 OK'
        

def produce(c):
    c.send(None)
    n=0
    while n<5:
        n=n+1
        print('[PRODUCER] Producing %s...' % n)
        r=c.send(n)
        print('[PRODUCER] Consumer return:%s' % r)
    c.close()


c=consumer()
produce(c)

print(c)

'''

def consumer():
    r=''
    while True:
        n=yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r='200 OK'


def produce(c):
    c.send(None)
    n=0
    while n<5:
        n=n+1
        print('[PRODUCER] Producing %s ...' % n)
        r=c.send(n)
        print('[PRODUCER] Sonsumer return: %s' %r)
    c.close()


c=consumer()
produce(c)

        
