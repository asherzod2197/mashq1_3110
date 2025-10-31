class Oquvchi:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh
        self.fanlar = []

    def fan_qosh(self, fan_nomi):
        self.fanlar.append(fan_nomi)

    def malumot(self):
        return f"Ism: {self.ism}, Yosh: {self.yosh}, Fanlar: {', '.join(self.fanlar)}"


oquvchi1 = Oquvchi("Ali", 16)
oquvchi1.fan_qosh("Matematika")
oquvchi1.fan_qosh("Fizika")
print(oquvchi1.malumot())
