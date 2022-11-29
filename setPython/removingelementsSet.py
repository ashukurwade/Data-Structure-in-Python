#item can be remove in a set by using remove() and discard() 

#initialize set
m_set = {1,3,4,6,8}
print(m_set)

#discard()
#if element not present in set its remain unchanged
m_set.discard(9)
print(m_set)

m_set.discard(3)
print(m_set)

#remove()
m_set.remove(1)
print(m_set)
#by using remove() if the elements not present in set its gives an error
m_set.remove(9)
print(m_set)