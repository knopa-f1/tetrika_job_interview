from functools import wraps


def check_type(argument: int | bool | float | str, argument_key:str, argument_type: type) -> None:
    """checking the type of the argument with the type"""

    # used type, because isinstance(True, int) = True
    if (t := type(argument)) != argument_type:
        raise TypeError(f"Parameter {argument_key}: excepted type: {argument_type.__name__}, got: {t.__name__}")


def check_all_args(annotation: dict, args: tuple, kwargs: dict) -> None:
    """general checks of arguments"""
    len_annotation = max(0, len(annotation) - 1)
    len_all_args = (len(args) + len(kwargs))

    if len_annotation != len_all_args:
        raise TypeError(f"{len_annotation} arguments in the annotation, got {len_all_args} arguments")


def check_args(annotation: dict, args: tuple) -> None:
    """checking args arguments of function with the annotation"""
    annotation_elements = annotation.items()
    [check_type(arg, arg_annotation[0], arg_annotation[1]) for arg, arg_annotation in zip(args, annotation_elements)]


def check_kwargs(annotation: dict, kwargs: dict) -> None:
    """checking kwargs arguments of function with the annotation"""

    for key, value in kwargs.items():
        if key in annotation:
            check_type(value, key, annotation[key])
        else:
            raise TypeError(f"Argument {key}: didn't find in annotation")


def strict(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        annotation = func.__annotations__
        check_all_args(annotation, args, kwargs)
        check_args(annotation, args)
        check_kwargs(annotation, kwargs)

        return func(*args, **kwargs)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b

