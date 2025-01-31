from typing import Callable, Any


def print_result(func: Callable) -> Callable:
    def inner(*args, **kwargs) -> Any:
        res = func(*args, **kwargs)
        if isinstance(res, int): 
            print(res)
        elif isinstance(res, list): 
            for i in res: 
                print(i)
        elif isinstance(res, dict): 
            for key, value in res.items(): 
                print(key, " = ", value)
        return res
   
    return inner


@print_result
def test_1() -> int:
    return 1


@print_result
def test_2() -> str:
    return 'iu5'


@print_result
def test_3() -> dict:
    return {'a': 1, 'b': 2}


@print_result
def test_4() -> list:
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()
