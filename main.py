from cars.create_cars import creat_cars

from cars.get_car_info import gett_car_info

car1 = creat_cars(
    title = 'bmw',
    release_date = '2007',
    engine = 'petrol',
    model = 'm-2'
)

print(gett_car_info(car1))

car1.start_engine()
car1.stopp_engine()