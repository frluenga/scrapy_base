def my_gen():
    a=1
    yield a
    a +=1
    yield a
    a +=1
    yield a

gen = my_gen()

print(next(gen))
print(next(gen))
print(next(gen))