class book:
    def __init__(self,name, price, pages):
        self.name=name
        self.price=price
        self.pages=pages
maths= book('maths',150,200)
#print(maths.price,maths.pages,maths.name)

h=hasattr(maths,'color')
name=getattr(maths,'name')
setattr(maths,'price',200)
setattr(maths,'pages',1200)
print (name)

print(h)
print(maths.price,maths.pages)
print(book.__module__)
#print(book.__  __)