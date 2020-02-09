class person:
    def open_door(self,door):
        door.open()

class door:
    def open(self):
        print("door is open")

if __name__=="__main__":
    Person=person()
    Door=door()

    Person.open_door(Door)
