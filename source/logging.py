def debug_args(func):
    def wrapper(*args, **kwargs):
        print(f"[DEBUG] Calling: {func.__name__}")
        print(f"[DEBUG] Positional args: {args}")
        print(f"[DEBUG] Keyword args: {kwargs}")
        return func(*args, **kwargs)
    return wrapper
