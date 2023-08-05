class meroua:
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise AttributeError(f"can't set attribute '{name}'")
        self.__dict__[name] = value

c_ = meroua()