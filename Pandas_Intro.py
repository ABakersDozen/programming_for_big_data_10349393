
# coding: utf-8

# In[3]:

import numpy as np
import pandas as pd


# In[4]:

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
s


# In[5]:

s.index


# In[6]:

pd.Series(np.random.randn(5))


# In[7]:

d = {'a' : 0., 'b' : 1., 'c' : 2.}


# In[8]:

pd.Series(d)


# In[9]:

pd.Series(d, index=['b', 'c', 'd', 'a'])


# In[10]:

pd.Series(5., index=['a', 'b', 'c', 'd', 'e'])


# In[11]:

s[0]


# In[12]:

s[:3]


# In[13]:

s[s > s.median()]


# In[14]:

s


# In[15]:

s[[4, 3, 1]]


# In[16]:

np.exp(s)


# In[17]:

d2 = {'a' : 3., 'b' : 4., 'c' : 5.}


# In[19]:

e=d


# In[20]:

e


# In[21]:

e.update(d2)


# In[22]:

e


# In[23]:

d


# In[24]:

d = {'a' : 0., 'b' : 1., 'c' : 2.}


# In[25]:

e
d


# In[26]:

e.update(d2)


# In[27]:

pd.Series(e)


# In[28]:

d = {'a' : 0., 'b' : 1., 'c' : 2.}


# In[29]:

e = d.copy()


# In[30]:

e


# In[31]:

e.update(d2)
e
d


# In[32]:

e


# In[33]:

d


# In[34]:

s['a']


# In[35]:

s['e']=12.


# In[36]:

s


# In[37]:

'e' in s


# In[38]:

'f' in s


# In[39]:

s['f']


# In[40]:

s.get('f')


# In[41]:

s.get('f',np.nan)


# In[43]:

pd.DataFrame(e,d2)


# In[44]:

e


# In[45]:

d2


# In[48]:

df = pd.DataFrame([d,d2])


# In[49]:

df


# In[50]:

d


# In[51]:

d2


# In[52]:

s.get('e')


# In[53]:

s+s


# In[54]:

s


# In[55]:

s*2


# In[56]:

np.exp(s)


# In[57]:

s[1:]+s[:-1]


# In[65]:

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'] ,name='something')


# In[66]:

s


# In[67]:

s.name


# In[68]:

s2 = s.rename("different")


# In[69]:

s2


# In[70]:

s


# In[71]:

d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}


# In[72]:

df2 = pd.DataFrame(d)


# In[73]:

df2


# In[74]:

pd.DataFrame(d, index=['d', 'b', 'a'])


# In[75]:

pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three'])


# In[76]:

d


# In[77]:

df2.index


# In[78]:

df2.columns


# In[80]:

d = {'one' : [1., 2., 3., 4.], 'two' : [4., 3., 2., 1.]}


# In[81]:

d


# In[82]:

pd.DataFrame(d)


# In[83]:

pd.DataFrame(d, index=['a', 'b', 'c', 'd'])


# In[84]:

data = np.zeros((2,), dtype=[('A', 'i4'),('B', 'f4'),('C', 'a10')])


# In[85]:

data


# In[86]:

data[:] = [(1,2.,'Hello'), (2,3.,"World")]


# In[87]:

pd.DataFrame(data)


# In[88]:

pd.DataFrame(data, index=['first', 'second'])


# In[95]:

df3 = pd.DataFrame(data, index=['first', 'second'],columns=['C', 'A', 'B'])
df3


# In[96]:

df3['A']


# 

# In[98]:

df3['C']['first']


# In[99]:

data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]


# In[100]:

pd.DataFrame(data2)


# In[101]:

pd.DataFrame(data2, index=['first', 'second'])


# In[102]:

pd.DataFrame(data2, columns=['a', 'b'])


# In[103]:

pd.DataFrame({('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4}, ('a', 'c'): {('A', 'B'): 5, ('A', 'C'): 6},
   ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},
   ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10}})


# In[104]:

df


# In[105]:

df2


# In[107]:

df2['three'] = df2['one'] * df2['two']


# In[108]:

df2


# In[110]:

df2['flag'] = df2['one'] > 2


# In[111]:

df2


# In[112]:

del df2['two']


# In[113]:

df2


# In[115]:

three = df2.pop('three')


# In[116]:

three


# In[117]:

df2


# In[118]:

df2['foo'] = 'bar'


# In[119]:

df2


# In[120]:

df2['one_trunc'] = df2['one'][:2]


# In[121]:

df2


# In[122]:

df2.insert(1, 'bar', 9)


# In[123]:

df2


# In[124]:

df2.loc['b','one']


# In[ ]:



