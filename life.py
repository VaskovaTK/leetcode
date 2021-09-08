class Life:
    def newDay(self, daysOfLife: int):
        while daysOfLife>0:
            try:
                self.doSomething("good",daysOfLife)
            except:
                self.keepTrying()
            finally:
                self.success()
        else:
            newLife = Life()
            newLife.newDay(36500)

    def doSomething(self, thing: str, daysOfLife: int):
        if thing == "good":
            daysOfLife +=1
        else:
            daysOfLife -=1
        return daysOfLife

    def keepTrying(self, effort = 1):
        enough = 99999
        effort +=1
        if effort == enough:
            return True
        else:
            self.keepTrying(effort)

    def success(self):
        youWillSucceed = True
        return youWillSucceed



life = Life()
life.newDay(5400)