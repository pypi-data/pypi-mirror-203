# Changes values in tuples using ctypes 

## Important: Never use this in a real project! Hacked tuples might lead to unexpected results! 


```python

from tuplechanger import tuplechanger


tutu = ('babaxxiq',-2,3.44, True, 800,1211)
print(id(tutu))
print(tutu)
tuindex = 0
tuplechanger(tutu, tuindex, 'bbbbxxxi')
print(tutu)
tuindex = 1
tuplechanger(tutu, tuindex, -4)
print(tutu)
tuindex = 2
tuplechanger(tutu, tuindex, 13.44)
print(tutu)
tuindex = 3
tuplechanger(tutu, tuindex, False)
print(tutu)
tuindex = 4
tuplechanger(tutu, tuindex, 17000)
print(tutu)
tuindex = 5
tuplechanger(tutu, tuindex, 1111)
print(tutu)
print(id(tutu))
# 1843849020512
# ('babaxxiq', -2, 3.44, True, 800, 1211)
# ('bbbbxxxi', -2, 3.44, True, 800, 1211)
# ('bbbbxxxi', -4, 3.44, True, 800, 1211)
# ('bbbbxxxi', -4, 13.44, True, 800, 1211)
# ('bbbbxxxi', -4, 13.44, False, 800, 1211)
# ('bbbbxxxi', -4, 13.44, False, 17000, 1211)
# ('bbbbxxxi', -4, 13.44, False, 17000, 1111)
# 1843849020512
```

## Why you shouldn't use it in a real project: 

```python
# It looks pretty good as first sight, but ... 
# tutu[0] + 'xxxx'
# Out[3]: 'bbbbxxxixxxx'
# tutu[1] + 5
# Out[4]: 1
# tutu[2] + 5.999
# Out[5]: 19.439
# tutu[3] is False
# Out[6]: True
# tutu[4] > 15000
# Out[7]: True
# tutu[5] < 1200
# Out[8]: True
# tutu[-1] < 1200
# Out[9]: True
# tutu[-2] < 15000
# Out[10]: True
# tutu[-3] is False
# Out[11]: True
# tutu[-4] + 5.999
# Out[12]: 19.439
# tutu[1] + 5
# Out[13]: 1

# ... it isn't a good idea to hack tuples:


# tutu[2] + tutu[4]   # positive index, everything is fine 
# Out[3]: 17013.44


# WRONG!!!
# tutu[-2] + tutu[-4] # negative index, crap
# Out[6]: 26.88
```