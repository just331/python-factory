import ast
from abc import ABC


# Abstract factory for footwear

class FootWear(ABC):
    def shoespecs(self, c='Brown'):
        self.color = c


# Abstract factory for MensClothes

class MensClothes(ABC):
    def __init__(self, rt='Brown', rb='Brown'):
        self.colort = rt
        self.colorb = rb

    def clothesspecs(self, foot_w):
        pass


class Boots(FootWear):
    def __init__(self):
        print("Wear boots on cold days")

    def shoespecs(self, c='Brown'):
        print(f"You picked {c} boots")


class Loafers(FootWear):
    def __init__(self):
        print("Shoes for a nice day")

    def shoespecs(self, c='Brown'):
        print(f"You picked {c} loafers")


class SweaterAndCorduroyPants(MensClothes):
    def __init__(self, rt='Brown', rb='Brown'):
        super().__init__(rt, rb)
        print(f"You picked the {rt} sweater and the {rb} corduroy pants")

    def clothesspecs(self, foot_w):
        foot_w.shoespecs(c=self.colorb)


class ButtonDownShirtAndDressPants(MensClothes):
    def __init__(self, rt="Brown", rb="Brown"):
        super().__init__(rt, rb)
        print(f"You picked the {rt} button-down shirt and the {rb} dress pants")

    def clothesspecs(self, foot_w):
        foot_w.shoespecs(c=self.colorb)


# Abstract class factory, Outfit

class Outfit(ABC):
    def __init__(self):
        self.formality = 0
        pass

    def choose_clothes(self):
        pass

    def choose_shoes(self):
        pass


class LightColor_ColdAndCasualDay(Outfit):
    def __init__(self):
        self.formality = 1
        self.name = "Light Colored Outfit for a cold and Casual Day"

    def choose_clothes(self):
        return SweaterAndCorduroyPants(rt="Cream-colored", rb="Light Brown")

    def choose_shoes(self):
        return Boots()


class DarkColor_WarmSemiFormalDay(Outfit):
    def __init__(self):
        self.formality = 2
        self.name = "Dark Colored Outfit for a Semi-Formal Day"

    def choose_clothes(self):
        return ButtonDownShirtAndDressPants(rt='burgundy', rb='black')

    def choose_shoes(self):
        return Loafers()


class Look:
    def __init__(self, factory):
        self.factory = factory
        self.name = factory.name
        print(factory.name)
        self.clo = factory.choose_clothes()
        self.sho = factory.choose_shoes()
        self.formality = factory.formality

    def dress(self):
        self.clo.clothespecs(self.sho)

    def __eq__(self, m):
        return self.formality == m.formality

    def __gt__(self, m):
        return self.formality > m.formality


g1 = Look(LightColor_ColdAndCasualDay())
g1.dress()
g2 = Look(DarkColor_WarmSemiFormalDay())
g2.dress()
print(g1 == g2)
print(g2 > g1)

with open('virtual_wardrobe.txt') as f:
    data = f.read()
wardrobe = ast.literal_eval(data)
print(wardrobe)

wardrobe[g1.name] = g1.formality
wardrobe[g2.name] = g2.formality
print(wardrobe)

with open('virtual_wardrobe.txt', 'w') as v_wardrobe:
    v_wardrobe.write(str(wardrobe))
v_wardrobe.close()
