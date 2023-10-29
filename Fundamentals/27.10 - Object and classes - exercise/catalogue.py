class Catalogue:
    products = []

    def __init__(self, name: str):
        self.name = name

    def add_product(self, product_name: str):
        Catalogue.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        srtd_by_lttr_lst = [s for s in Catalogue.products if s.startswith(first_letter)]
        return srtd_by_lttr_lst

    def __repr__(self):
        new_catalogue = '\n'.join(sorted(Catalogue.products))
        return f"Items in the {self.name} catalogue:\n{new_catalogue}"


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)




