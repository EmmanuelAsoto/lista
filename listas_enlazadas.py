class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None


class ListaEnlazadaSimple:
    def __init__(self):
        self.head = None
        self.size = 0

    # O(1)
    def prepend(self, data):
        nuevo = Nodo(data)
        nuevo.next = self.head
        self.head = nuevo
        self.size += 1

    # O(n)
    def append(self, data):
        nuevo = Nodo(data)
        if not self.head:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo
        self.size += 1

    def __len__(self):
        return self.size

    def __iter__(self):
        actual = self.head
        while actual:
            yield actual.data
            actual = actual.next

    def __str__(self):
        elementos = []
        actual = self.head
        while actual:
            elementos.append(str(actual.data))
            actual = actual.next
        return "->".join(elementos)
    


# Prueba
lista = ListaEnlazadaSimple()
for i in range(1, 6):
    lista.append(i)
lista.prepend(0)
print(lista)  # 0->1->2->3->4->5

# ejercicio2.py

class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None


class ListaEnlazadaSimple:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        nuevo = Nodo(data)
        if not self.head:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo
        self.size += 1

    # ✅ MÉTODO CORREGIDO (dentro de la clase)
    def delete_value(self, valor):
        actual = self.head
        anterior = None

        while actual:
            if actual.data == valor:
                # Caso 1: eliminar el primero
                if anterior is None:
                    self.head = actual.next
                else:
                    anterior.next = actual.next

                self.size -= 1
                return True  # eliminado correctamente

            anterior = actual
            actual = actual.next

        return False  # no encontrado


# ✅ PRUEBA CORRECTA
lista = ListaEnlazadaSimple()
for i in [1, 5, 3]:
    lista.append(i)

lista.delete_value(5)  # Elimina el nodo con valor 5
print(lista.head.data, lista.head.next.data)  # 1 3

class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None


class ListaEnlazadaSimple:
    def __init__(self):
        self.head = None
        self.size = 0

    def prepend(self, data):  # O(1)
        nuevo = Nodo(data)
        nuevo.next = self.head
        self.head = nuevo
        self.size += 1

    def append(self, data):  # O(n)
        nuevo = Nodo(data)
        if not self.head:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo
        self.size += 1

    # ✅ MÉTODO CORRECTO
    def insert(self, index, value):
        # Validación
        if index < 0 or index > self.size:
            raise IndexError("Índice fuera de rango")

        # Caso especial: inicio
        if index == 0:
            self.prepend(value)
            return

        # Recorrer hasta el nodo anterior
        actual = self.head
        for _ in range(index - 1):
            actual = actual.next

        # Insertar
        nuevo = Nodo(value)
        nuevo.next = actual.next
        actual.next = nuevo

        self.size += 1

    def __str__(self):
        elementos = []
        actual = self.head
        while actual:
            elementos.append(str(actual.data))
            actual = actual.next
        return "->".join(elementos)

# Prueba
lista = ListaEnlazadaSimple()
lista.insert(0, 'a')
lista.insert(1, 'b')
lista.insert(0, 'z')
print(lista)  # z->a->b

class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None


class ListaEnlazadaSimple:
    def __init__(self):
        self.head = None

    def append(self, data):
        nuevo = Nodo(data)
        if not self.head:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo

    def __str__(self):
        elementos = []
        actual = self.head
        while actual:
            elementos.append(str(actual.data))
            actual = actual.next
        return "->".join(elementos)

    # 🔥 convertir lista a número (para mostrar)
    def to_number(self):
        actual = self.head
        multiplicador = 1
        numero = 0

        while actual:
            numero += actual.data * multiplicador
            multiplicador *= 10
            actual = actual.next

        return numero


# ✅ FUNCIÓN SUMA
def sumar_listas(l1, l2):
    resultado = ListaEnlazadaSimple()
    carry = 0

    n1 = l1.head
    n2 = l2.head

    while n1 or n2 or carry:
        val1 = n1.data if n1 else 0
        val2 = n2.data if n2 else 0

        suma = val1 + val2 + carry
        carry = suma // 10

        resultado.append(suma % 10)

        if n1:
            n1 = n1.next
        if n2:
            n2 = n2.next

    return resultado


# 🧪 PRUEBA COMPLETA
l1 = ListaEnlazadaSimple()
l2 = ListaEnlazadaSimple()

# 342
for x in [2, 4, 3]:
    l1.append(x)

# 465
for x in [5, 6, 4]:
    l2.append(x)

resultado = sumar_listas(l1, l2)

print("Lista 1:", l1, "=", l1.to_number())
print("Lista 2:", l2, "=", l2.to_number())
print("Resultado:", resultado, "=", resultado.to_number())

class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None


class ListaEnlazadaSimple:
    def __init__(self):
        self.head = None

    def append(self, data):
        nuevo = Nodo(data)
        if not self.head:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo

    def search(self, value):
        actual = self.head
        index = 0
        while actual:
            if actual.data == value:
                return index
            actual = actual.next
            index += 1
        return -1

    def count(self, value):
        actual = self.head
        contador = 0
        while actual:
            if actual.data == value:
                contador += 1
            actual = actual.next
        return contador

    def __str__(self):
        elementos = []
        actual = self.head
        while actual:
            elementos.append(str(actual.data))
            actual = actual.next
        return "->".join(elementos)


# 🧪 PRUEBA
lista = ListaEnlazadaSimple()

for x in ['fox', 'quick', 'brown', 'fox']:
    lista.append(x)

print("Lista:", lista)
print("Buscar 'quick': índice =", lista.search('quick'))
print("Buscar 'dog': índice =", lista.search('dog'))
print("Cantidad de 'fox':", lista.count('fox'))

class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None


class ListaEnlazadaSimple:
    def __init__(self):
        self.head = None

    def append(self, data):
        nuevo = Nodo(data)
        if not self.head:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo

    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            siguiente = curr.next
            curr.next = prev
            prev = curr
            curr = siguiente

        self.head = prev

    def __str__(self):
        elementos = []
        actual = self.head
        while actual:
            elementos.append(str(actual.data))
            actual = actual.next
        return "->".join(elementos)


# 🧪 PRUEBA
lista = ListaEnlazadaSimple()

for i in [1, 2, 3]:
    lista.append(i)

print("Lista original:", lista)

lista.reverse()

print("Lista invertida:", lista)

class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None


class ListaEnlazadaSimple:
    def __init__(self):
        self.head = None

    def append(self, data):
        nuevo = Nodo(data)
        if not self.head:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo

    def swap_pairs(self):
        dummy = Nodo(0)
        dummy.next = self.head
        prev = dummy

        while prev.next and prev.next.next:
            a = prev.next
            b = a.next

            # intercambio de nodos
            prev.next = b
            a.next = b.next
            b.next = a

            prev = a

        self.head = dummy.next

    def __str__(self):
        elementos = []
        actual = self.head
        while actual:
            elementos.append(str(actual.data))
            actual = actual.next
        return "->".join(elementos)


# 🔥 PRUEBA EN EL MISMO BLOQUE
lista = ListaEnlazadaSimple()

for i in [1, 2, 3, 4]:
    lista.append(i)

print("Lista original:", lista)

lista.swap_pairs()

print("Lista intercambiada:", lista)

class BrowserHistory:
    def __init__(self, homepage):
        self.back_stack = [homepage]
        self.forward_stack = []

    def visit(self, url):
        self.back_stack.append(url)
        self.forward_stack.clear()
        print(f"Visita: {url}")

    def back(self, steps):
        while steps > 0 and len(self.back_stack) > 1:
            self.forward_stack.append(self.back_stack.pop())
            steps -= 1
        print(f"Back → {self.back_stack[-1]}")
        return self.back_stack[-1]

    def forward(self, steps):
        while steps > 0 and self.forward_stack:
            self.back_stack.append(self.forward_stack.pop())
            steps -= 1
        print(f"Forward → {self.back_stack[-1]}")
        return self.back_stack[-1]

    def estado(self):
        print("\n--- ESTADO ACTUAL ---")
        print("Historial:", " -> ".join(self.back_stack))
        print("Adelante:", " -> ".join(self.forward_stack) if self.forward_stack else "Vacío")
        print("---------------------\n")


# 🔥 PRUEBA COMPLETA
bh = BrowserHistory("a")

bh.visit("b")
bh.visit("c")

bh.estado()

bh.back(1)     # vuelve a b
bh.estado()

bh.forward(1)  # vuelve a c
bh.estado()

class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None


class ListaEnlazadaSimple:
    def __init__(self):
        self.head = None

    def append(self, data):
        nuevo = Nodo(data)
        if not self.head:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo

    # 🔍 Detectar ciclo (Floyd: tortuga y liebre)
    def detectar_ciclo(self):
        lento = self.head
        rapido = self.head

        while rapido and rapido.next:
            lento = lento.next          # avanza 1
            rapido = rapido.next.next   # avanza 2

            if lento == rapido:
                return True  # hay ciclo

        return False  # no hay ciclo

    def __str__(self):
        elementos = []
        actual = self.head
        contador = 0

        # límite para evitar bucle infinito si hay ciclo
        while actual and contador < 10:
            elementos.append(str(actual.data))
            actual = actual.next
            contador += 1

        if actual:  # si sigue, hay ciclo
            elementos.append("... (ciclo)")

        return "->".join(elementos)


# 🔥 PRUEBA 1: LISTA NORMAL (SIN CICLO)
lista1 = ListaEnlazadaSimple()
for i in [1, 2, 3]:
    lista1.append(i)

print("Lista 1:", lista1)
print("¿Tiene ciclo?", lista1.detectar_ciclo())


# 🔥 PRUEBA 2: LISTA CON CICLO
lista2 = ListaEnlazadaSimple()
for i in [1, 2, 3]:
    lista2.append(i)

# crear ciclo manual: último apunta al segundo
n1 = lista2.head
n2 = n1.next
n3 = n2.next

n3.next = n2  # 🔁 ciclo

print("\nLista 2:", lista2)
print("¿Tiene ciclo?", lista2.detectar_ciclo())

class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None


class ListaEnlazadaSimple:
    def __init__(self):
        self.head = None

    def append(self, data):
        nuevo = Nodo(data)
        if not self.head:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo

    def partir_lista(self):
        if not self.head:
            return None, None

        lento = self.head
        rapido = self.head
        prev = None

        # encontrar punto medio
        while rapido and rapido.next:
            prev = lento
            lento = lento.next
            rapido = rapido.next.next

        # cortar la lista en dos
        if prev:
            prev.next = None

        lista1 = ListaEnlazadaSimple()
        lista1.head = self.head

        lista2 = ListaEnlazadaSimple()
        lista2.head = lento

        return lista1, lista2

    def __str__(self):
        elementos = []
        actual = self.head
        while actual:
            elementos.append(str(actual.data))
            actual = actual.next
        return "->".join(elementos)


# 🔥 PRUEBA COMPLETA
lista = ListaEnlazadaSimple()

for i in [1, 2, 3, 4, 5]:
    lista.append(i)

print("Lista original:", lista)

mitad1, mitad2 = lista.partir_lista()

print("Primera mitad:", mitad1)
print("Segunda mitad:", mitad2)