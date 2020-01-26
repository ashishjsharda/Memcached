'''
Created on Jan 25, 2020
Using Memcached
@author: ashish
'''
from pymemcache.client import base

client=base.Client(('localhost',112211))
client.set('User', 'Peter')
client.get('User')
