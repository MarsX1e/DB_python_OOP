class User():
    def __init__(self, name, id):
        self.name=name
        self.id=id
class DB():
    def __init__(self):
        self.contents=[]
        self.next_id=1
    def create(self,name):
        self.contents.append(User(name,self.next_id))
        self.next_id+=1
        return self
    def all(self):
        return self.contents
    def get(self,id):
        for value in self.contents:
            if value.id==id:
                return value
            else:
                return "None"
    def filter(self,name):
        list1=[]
        for value in self.contents:
            if value.name==name:
                list1.append(value)
        return list1
    def exclude(self,name):
        list1=[]
        for value in self.contents:
            if value.name!=name:
                list1.append(value)
        return list1
user1=User("Jack",2)
print user1
print user1.name
print user1.id

DB1=DB()
DB1.create("Jason")
print DB1.next_id
print DB1.contents
DB1.create("Jon")
print DB1.all()
print DB1.get(3)
DB1.create("Jason")
print DB1.contents
print DB1.filter("Jason")
print DB1.filter("jioj")
print DB1.exclude("jiojoi")