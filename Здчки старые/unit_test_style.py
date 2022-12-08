def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"

if __name__ == "__main__":
    test_abs1()
    test_abs2()
    print("Everything passed")




# Превратить тестовые функции в методы,
# добавив ссылку на экземпляр
# класса self в качестве первого аргумента функции: def test_abs1(self):
    def test_abs1(self):
# Изменить assert на self.assertEqual()
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")


