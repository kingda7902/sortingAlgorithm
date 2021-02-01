import datetime


def timer(fun):
    def wrapper(*args):
        start = datetime.datetime.now()
        ret = fun(*args)
        end = datetime.datetime.now()
        print(f'The function {fun.__name__} spend: {end - start}')
        return ret
    return wrapper


@timer
def read_the_numbers(file_path, head=0):
    with open(file=file_path) as f:
        file_raw_data = f.read()
        string_sep = file_raw_data.split()
        if head:
            string_sep = string_sep[:head]
        return list(map(float, string_sep))


@timer
def write_to_file(file_name, data_list):
    with open(file_name, mode='r') as f:
        for i in data_list:
            f.writelines(i)
