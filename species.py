
import random
from typing import List, Tuple

class Species:

    def __init__(self, name):

        self.name = name

        self.characteristic = {}

        self.characteristic["population"] = 1              #Población

        self.characteristic_dependences = []  # dependence_1 -> dependence_2 * value, lo que se traduce como:
                                              # dependence_2 += dependence_1 * value



    # Con este método podemos añadir o modificar una característica y su valor
    def Change_Characteristic(self, name, value):
        self.characteristic[name] = value

    # Con este método podemos eliminar una característica y su valor
    def Delete_Characteristic(self, name):
        if(self.characteristic[name].get(name, True)):
            del(self.characteristic[name])

    # Con este método podemos agregar una dependencia de la forma a -> b * c
    # Donde a es dependence_1, b es dependence_2 y c es value
    def Add_Dependences(self, dependence_1, dependence_2, value):
        for i in range(self.characteristic_dependences):      #Revisamos que no exista esta dependencia
            dependences = self.characteristic_dependences[i]
            if dependence_1 in dependences and dependence_2 in dependences:
                return 0    #Si existe devolvemos 0
        self.characteristic_dependences.append([dependence_1, dependence_2, value]) #Agregamos la dependencia

    # Con este método podemos eliinar una dependencia
    def Delete_Dependences(self, dependence_1, dependence_2):
        for i in range(self.characteristic_dependences):
            dependences = self.characteristic_dependences[i]
            if dependence_1 in dependences and dependence_2 in dependences:
                del(self.characteristic_dependences[i])
                return

    # Con este método podemos cambiar el value en una dependencia
    def Change_Dependences_Value(self, dependence_1, dependence_2, new_value):
        for i in range(self.characteristic_dependences):
            dependences = self.characteristic_dependences[i]
            if dependence_1 in dependences and dependence_2 in dependences:
                self.characteristic_dependences[i][2] = new_value
                return


    def Move_One_Day(self):
        
        #Vamos por todas las dependencias
        for i in range(self.characteristic_dependeces):
            
            #Las dependencias se guardan de la forma a -> b * c, que se traduce como b += a * c

            actual_dependence = self.characteristic_dependeces[i]    #Guardamos la dependencia actual
            a = self.characteristic[actual_dependence[0]]            #Extraemos a
            b = self.characteristic[actual_dependence[1]]            #Extraemos b
            c = actual_dependence[2]                                 #Extraemos c

            #Aquí se hace una separación por casos:
            #Si a tiene dos coordenadas, entonces el valor de a es directamente un random de ese intervalo
            #Si a es un valor, entonces a es directamente igual a ese valor
            #Ya sea que b tiene un valor, o dos coordenadas, estos no se verifican mediante un random, sino que
            #se multiplican a partir de los casos de c:

            #Si b es un valor y c una coordenada, entonces a se multiplica por un random proporcionado por el intervalo de c
            #Si b es un valor y c un valor, se multiplican
            #Si b es una coordenada (b1, b2), y c una coordenada (c1, c2), entonces se debe hacer:
            # (b1, b2) = (b1, b2) + (c1*a, c2*a)
            #Si b es una coordenada y c un valor entonces se multiplica ambas a por c

            if(isinstance(a, List)):
                a = random.randint(a[0], a[1])

            if(isinstance(b, List)):
                if(isinstance(c, List)):
                    self.characteristic[actual_dependence[1]] = [b[0] + c[0]*a, b[1] + c[1]*a]
                else:
                    self.characteristic[actual_dependence[1]] = [b[0] + c*a, b[1] + c*a]
            else:
                if(isinstance(c, List)):
                    self.characteristic[actual_dependence[1]] = b + a * random.randint(c[0], c[1])
                else:
                    self.characteristic[actual_dependence[1]] = b + a * c
            

    def Set_Default_Characteristics(self):
        self.characteristic["death_rate"] = [0, 1]         #Mortalidad
        self.characteristic["birth_rate"] = [0, 1]         #Natalidad
        self.characteristic["life_expectation"] = 1        #Esperanza de vida
        self.characteristic["gestation"] = 1               #Período de Gestación
        self.characteristic["reproduction_number"] = [0,1] #Número de reproducción
        self.characteristic["size"] = 1                    #Tamaño
        self.characteristic["intellect"] = 1               #Intelecto
        self.characteristic["strength"] = 1                #Fuerza
        self.characteristic["evolution_rate"] = 1          #Capacidad de evolución
        self.characteristic["actual_growth"] = 1           #Crecimiento Actual
        self.characteristic["economy"] = 1                 #Economía
        self.characteristic["foreign_tolerance"] = 1       #Tolerancia a extranjeros

    def Set_Default_Dependences(self):
        pass