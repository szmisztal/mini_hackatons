"""
Klasyczna kolejka (Queue), emuluje działanie “tradycyjnej” kolejki jaką spotkasz np. w sklepie czy kinie. Ustawiasz się na końcu i przesuwasz do przodu aż ktoś Cię obsłuży.

Podstawowe metody kolejki (**które należy zaimplementować w ramach rozwiązania**):

- Dodaj element na końcu kolejki
- Pobierz i usuń element z początku kolejki
- Pobierz 1 element bez usuwania (podgląd)
- Czy kolejka jest pusta?
- Ile elementów jest w kolejce

**Twoim zadaniem jest stworzyć samemu implementację  kolejki… priorytetowej.**

Różni się od tradycyjnej kolejki tym, że oprócz elementu z danymi jest jeszcze priorytet. Elementy o wyższym priorytecie wychodzą z kolejki przed elementami o niższym priorytecie.

Przykład:

- element 1: list - priorytet 0
- element 2: list - priorytet 0
- element 3: list - priorytet 5
- element 4: list - priorytet 3

Pobranie elementu powinno zwrócić nie element 1 (jak przy tradycyjnej kolejce), ale element 3 z najwyższym priorytetem. Czyli po pobraniu, kolejka wygląda tak:

- element 1: list - priorytet 0
- element 2: list - priorytet 0
- element 3: list - priorytet 3

Jeśli w kolejce jest kilka elementów o tym samym priorytecie, powinny być zwracane w kolejności dostania się na listę. Jeśli jednak będzie to dla Ciebie teraz za trudne do zaimplementowania, zwracaj je losowo).

Jeśli poprosisz o pomoc Chat GPT, będzie Ci podpowiadał, żeby użyć do implementacji sterty. Ale Ty nie wiesz, co to jest i masz tego nie robić.
"""
