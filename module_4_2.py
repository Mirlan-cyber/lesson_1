def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

test_function()
#inner_function() - заканчивается ошибкой вызова, т.к. область видимости не позволяет вызвать данную функцию
