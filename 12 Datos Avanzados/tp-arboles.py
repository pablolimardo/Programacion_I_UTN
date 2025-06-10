# ==============================================================================
# DEFINICIÓN DE LAS CLASES
# ==============================================================================

class Nodo:
    """
    Representa un componente en el inventario.
    Cada nodo contiene los datos del componente y las referencias a sus hijos.
    """
    def __init__(self, sku, nombre, stock):
        self.sku = sku
        self.nombre = nombre
        self.stock = stock
        self.izquierda = None  # Almacenará el sub-árbol izquierdo (nodos con SKU menor)
        self.derecha = None    # Almacenará el sub-árbol derecho (nodos con SKU mayor)

    def __str__(self):
        """Devuelve una representación en string del componente para imprimirlo fácilmente."""
        return f"SKU: {self.sku}, Nombre: {self.nombre}, Stock: {self.stock}"

class ArbolInventario:
    """
    Implementación de un Árbol de Búsqueda Binaria para gestionar el inventario.
    Esta clase orquesta todas las operaciones sobre los nodos.
    """
    def __init__(self):
        # La raíz es el punto de partida del árbol. Inicialmente, está vacía.
        self.raiz = None

    def agregar_componente(self, sku, nombre, stock):
        """
        Método público para agregar un nuevo componente.
        Este es el método que se llama desde fuera de la clase.
        """
        # Si el árbol está vacío, el nuevo nodo se convierte en la raíz.
        if self.raiz is None:
            self.raiz = Nodo(sku, nombre, stock)
        # Si el árbol ya tiene nodos, usamos un método recursivo para encontrar la posición correcta.
        else:
            self._agregar_recursivo(self.raiz, sku, nombre, stock)

    def _agregar_recursivo(self, nodo_actual, sku, nombre, stock):
        """
        Método privado y recursivo para insertar un nodo.
        Navega por el árbol hasta encontrar un lugar vacío donde colocar el nuevo nodo.
        """
        # Comparamos el SKU del nuevo componente con el del nodo actual.
        if sku < nodo_actual.sku:
            # Si es menor, vamos hacia la izquierda.
            if nodo_actual.izquierda is None:
                # Si no hay nada a la izquierda, hemos encontrado el lugar. Lo insertamos aquí. (Caso base)
                nodo_actual.izquierda = Nodo(sku, nombre, stock)
            else:
                # Si ya hay un nodo, seguimos bajando por la rama izquierda. (Paso recursivo)
                self._agregar_recursivo(nodo_actual.izquierda, sku, nombre, stock)
        elif sku > nodo_actual.sku:
            # Si es mayor, vamos hacia la derecha.
            if nodo_actual.derecha is None:
                # Si no hay nada a la derecha, lo insertamos aquí. (Caso base)
                nodo_actual.derecha = Nodo(sku, nombre, stock)
            else:
                # Si ya hay un nodo, seguimos bajando por la rama derecha. (Paso recursivo)
                self._agregar_recursivo(nodo_actual.derecha, sku, nombre, stock)
        else:
            # Si el SKU ya existe, no lo agregamos para evitar duplicados.
            print(f"-> ADVERTENCIA: El componente con SKU {sku} ya existe. No se puede duplicar.")

    def buscar_componente(self, sku):
        """Método público para buscar un componente por su SKU."""
        return self._buscar_recursivo(self.raiz, sku)

    def _buscar_recursivo(self, nodo_actual, sku):
        """
        Método privado y recursivo para encontrar un nodo.
        Aprovecha la propiedad del BST para descartar la mitad del árbol en cada paso.
        """
        # Casos base de la recursión:
        # 1. Si el nodo actual es None, significa que llegamos al final de una rama y no lo encontramos.
        # 2. Si el SKU del nodo actual es el que buscamos, lo hemos encontrado.
        if nodo_actual is None or nodo_actual.sku == sku:
            return nodo_actual
        
        # Pasos recursivos:
        if sku < nodo_actual.sku:
            # Si el SKU que buscamos es menor, solo puede estar en el sub-árbol izquierdo.
            return self._buscar_recursivo(nodo_actual.izquierda, sku)
        else:
            # Si es mayor, solo puede estar en el sub-árbol derecho.
            return self._buscar_recursivo(nodo_actual.derecha, sku)

    def eliminar_componente(self, sku):
        """Método público para eliminar un componente."""
        self.raiz = self._eliminar_recursivo(self.raiz, sku)

    def _eliminar_recursivo(self, nodo_actual, sku):
        """
        Método privado y recursivo para encontrar y eliminar un nodo.
        Este es el método más complejo debido a los diferentes casos a manejar.
        """
        # Primero, buscamos el nodo a eliminar. Si no lo encontramos, no hacemos nada.
        if nodo_actual is None: 
            return nodo_actual
        
        if sku < nodo_actual.sku:
            nodo_actual.izquierda = self._eliminar_recursivo(nodo_actual.izquierda, sku)
        elif sku > nodo_actual.sku:
            nodo_actual.derecha = self._eliminar_recursivo(nodo_actual.derecha, sku)
        else:
            # Una vez encontrado el nodo a eliminar, analizamos los casos.
            
            # Caso 1: El nodo tiene un solo hijo (o ninguno).
            # Si el hijo izquierdo es nulo, reemplazamos el nodo actual por su hijo derecho.
            if nodo_actual.izquierda is None: 
                return nodo_actual.derecha
            # Si el hijo derecho es nulo, reemplazamos el nodo actual por su hijo izquierdo.
            elif nodo_actual.derecha is None: 
                return nodo_actual.izquierda
            
            # Caso 2: El nodo tiene dos hijos.
            # Esta es la parte más compleja. La estrategia es:
            # 1. Encontrar el sucesor inorden (el nodo con el valor más pequeño en el subárbol derecho).
            temp = self._encontrar_minimo(nodo_actual.derecha)
            # 2. Copiar el contenido del sucesor al nodo que queremos "eliminar".
            nodo_actual.sku = temp.sku
            nodo_actual.nombre = temp.nombre
            nodo_actual.stock = temp.stock
            # 3. Eliminar el nodo sucesor (que es más fácil, ya que tendrá 0 o 1 hijo).
            nodo_actual.derecha = self._eliminar_recursivo(nodo_actual.derecha, temp.sku)
            
        return nodo_actual

    def _encontrar_minimo(self, nodo):
        """Función auxiliar para encontrar el nodo con el SKU más bajo en un subárbol."""
        # Por la propiedad del BST, este siempre será el nodo más a la izquierda.
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual

    def mostrar_inventario_ordenado(self):
        """Imprime el inventario en orden. Llama al método de recorrido inorden."""
        print("\n--- Inventario de Componentes (Ordenado por SKU) ---")
        self._inorden_recursivo(self.raiz)
        print("--------------------------------------------------")

    def _inorden_recursivo(self, nodo_actual):
        """
        Recorre el árbol en "inorden" (Izquierda, Raíz, Derecha).
        Para un BST, este recorrido siempre devuelve los nodos en orden ascendente.
        """
        if nodo_actual is not None:
            # 1. Ve a la izquierda recursivamente.
            self._inorden_recursivo(nodo_actual.izquierda)
            # 2. Visita (imprime) el nodo actual.
            print(nodo_actual)
            # 3. Ve a la derecha recursivamente.
            self._inorden_recursivo(nodo_actual.derecha)


# ==============================================================================
# BLOQUE DE EJECUCIÓN PRINCIPAL
# Este código solo se ejecuta si este archivo es el programa principal.
# ==============================================================================

if __name__ == "__main__":
    
    # 1. Crear una instancia del árbol de inventario
    inventario = ArbolInventario()
    
    # 2. Agregar componentes de prueba
    print("Agregando componentes al inventario...")
    inventario.agregar_componente(2010, "Microcontrolador ESP32", 150)
    inventario.agregar_componente(1050, "Arduino Nano", 80)
    inventario.agregar_componente(3033, "Resistencia 1k ohm", 1200)
    inventario.agregar_componente(4001, "Capacitor Cerámico 100nF", 2500)
    inventario.agregar_componente(1025, "Sensor de Temperatura DHT11", 95)
    inventario.agregar_componente(3010, "Potenciómetro 10k", 300)

    # 3. Mostrar el inventario inicial ordenado
    inventario.mostrar_inventario_ordenado()

    # 4. Probar la búsqueda de un componente
    print("\nBuscando componente con SKU 1025...")
    componente_encontrado = inventario.buscar_componente(1025)
    if componente_encontrado:
        print(f"Componente encontrado: {componente_encontrado}")
    else:
        print("Componente no encontrado.")
        
    # 5. Probar la eliminación de un componente
    print("\nEliminando componente con SKU 1050...")
    inventario.eliminar_componente(1050)
    
    # 6. Mostrar el inventario final para verificar la eliminación
    inventario.mostrar_inventario_ordenado()

    # 7. Probar a buscar un componente que no existe
    print("\nBuscando componente con SKU 9999 (inexistente)...")
    componente_no_existente = inventario.buscar_componente(9999)
    if componente_no_existente:
        print(f"Componente encontrado: {componente_no_existente}")
    else:
        print("Componente no encontrado. (Funcionamiento esperado)")
