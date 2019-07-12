def make_car(manufacturer, model_name, **car_det):
    car_info = {}
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model_name
    for key, value in car_det.items():
        car_info[key] = value
    return car_info

