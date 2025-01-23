class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = "products.txt"

    def get_products(self):
        try:
            with open(self.__file_name, "r") as file:
                return file.read().strip()
        except FileNotFoundError:
            return ""

    def add(self, *products):
        existing_products = self.get_products().split("\n")
        products_dict = {}

        # Преобразую существующие продукты в словарь для быстрого поиска
        for product_str in existing_products:
            if product_str:
                name, weight, category = product_str.split(", ")
                products_dict[(name.strip(), category.strip())] = float(weight)

        # Обрабатываем новые продукты
        for product in products:
            key = (product.name, product.category)
            if key in products_dict:
                old_weight = products_dict[key]
                new_weight = old_weight + product.weight
                print(
                    f"Продукт {product.name} уже был в магазине, "
                    f"его общий вес теперь равен {new_weight}."
                )
                products_dict[key] = new_weight
            else:
                products_dict[key] = product.weight

        # Формирую новую строку для записи в файл
        lines_to_write = [
            f"{name}, {weight}, {category}" for (name, category), weight in products_dict.items()
        ]

        # Записываю обновленные продукты в файл
        with open(self.__file_name, "w") as file:
            file.write("\n".join(lines_to_write) + "\n")


s1 = Shop()
p1 = Product("Potato", 50.5, "Vegetables")
p2 = Product("Spaghetti", 3.4, "Groceries")
p3 = Product("Potato", 5.5, "Vegetables")

s1.add(p1, p2, p3)

print(s1.get_products())
