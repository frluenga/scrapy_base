lista = [1,2,3,4]
iterador = iter(lista)

## Un iterador tiene una sentencia yield
## guarda el estado de la función
## cuando se ejecuta nuevamente empieza
## desde ahí
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))