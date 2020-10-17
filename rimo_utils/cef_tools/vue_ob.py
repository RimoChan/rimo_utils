class vue_ob:
    class vue_sync:
        def __init__(self, master):
            self._master = master
            self._內容 = {}

        def __getattr__(self, x):
            return self._內容[x]

        def __setattr__(self, a, b):
            if a[0] == '_':
                self.__dict__[a] = b
            else:
                self._內容[a] = b
                self._master.更新vue()

    def __init__(self):
        self.vue = self.vue_sync(self)
        self.vue鏈接 = None

    def vue更新(self, 內容):
        self.vue._內容 = 內容

    def 更新vue(self):
        if self.vue鏈接:
            self.vue鏈接.Call(self.vue._內容)

    def vue連接初始化(self, f):
        self.vue鏈接 = f
        self.更新vue()
