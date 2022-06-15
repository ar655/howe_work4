
class Car:
    def __init__(self,title,release_date,engine,model):
        self.title = title
        self.release_date = release_date
        self.engine = engine
        self.model = model


    def start_engine(self):
        print(f'{self.title} {self.model} engine started')


    def stopp_engine(self):
        print(f'{self.title} {self.model} engine stopped')


    def __str__(self):
        return(f'Title:{self.title}\n'
              f'Release date:{self.release_date}\n'
              f'Engine:{self.engine}\n'
              f'Model:{self.model}')



def creat_cars(title,release_date,engine,model):
    car1 = Car (title=title,release_date=release_date,engine=engine,model=model)
    return car1

