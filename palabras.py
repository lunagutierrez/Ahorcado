# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 17:17:34 2020
@author: lunag
"""

import random

#Listas de palabras por longitud

pal3=["sea", "uno", "pie", "ojo", "ajo", "oca", "sed", "tul", "dos", "tos", "luz", "voz", "tez", "uva", "pan", "mar", "oso", "ola", "sol", "pez", "col", "sal" , "paz", "cal", "rio", "res", "ron", "lio", "mes", "pis", "par", "tio", "mio", "pua", "mes", "sur", "bol", "bar", "ala", "res", "can", "los", "via", "asa", "feo"]
pal4=["masa", "como", "mopa", "dado", "gafa", "mesa", "copo", "moda", "dedo", "gala", "misa", "cono", "mofa", "dudo", "gama", "musa", "coco", "lona", "gata", "codo", "moja", "gasa", "cosa", "mora", "garra", "coto", "mota", "gana", "cojo", "loza", "paso", "lana", "paja", "rana", "tala", "peso", "lama", "mala", "rama", "tapa", "puso", "lava", "mapa", "raza", "mata"]
pal5=["andes", "apodo", "balas", "besos", "cenas", "clubs", "densa", "dotes", "euros", "entes", "forma", "flaco", "gatos", "grave", "hueco", "hemos", "irian", "hueso", "cobra", "chelo", "labio", "radio", "cinco", "obvio", "madre", "mafia", "ideas", "oblea", "lindo", "canto", "arroz", "perro", "gotas", "queso", "equis", "cacao", "cocoa", "abaco", "reloj", "ayuda", "peine", "dolor", "color", "uvas", "dulce"]
pal6=["comida","drogas","dioses","ahorra","astros","avispa","barcos","basico","camino","condes","cobras","cestos","clones","ciudad","eolico","envios","flores","ferias","gotica","golpes","heroes","intimo","jergas","lapida","listas","marcos","mentes","naipes","numero","operas","ostras","oxidar","pasivo","picaro","pistas","quesos","radios","reales","reptil","sellos","silaba","sadico","subito","tacita","titere"]
pal7=["hermosa","estudio","encanto","palabra","carisma","zapateo","caballo","bebidas","damasco","extasis","gorilas","guantes","habitat","helecho","obleas","quejido","soledad","ucrania","cabello","querido","somalia","tablero","cebolla","manzana","escrito","belleza","palacio","circulo","teorema","tranvia","troyano","zapatos","musical","lindura","comedor","mentira","neutral","ratones","numeros","dientes","mascota","subdito","realeza","tortuga","objetar"]
pal8=["internet","labiales","sociales","biologia","viviparo","longitud","mariposa","nacional","colombia","creativo","embarazo","orquesta","manicura","vibrante","xilofono","incendio","pelicula","finanzas","economia","libertad","gaviotas","cerebelo","fraccion","infinito","libelula","amazonas","ciencias","subsidio","sintomas","degustar","telefono","almohada","hipnosis","misterio","suspenso","analisis","perfecto","claustro","estudiar","personas","pancreas","deportes","ahorcado","piramide","multitud"]
pal9=["corolario","diafragma","antebrazo","sarampion","zanahoria","higienico","cuarentena","suculento","australia","enamorado","occidente","relampago","feminismo","eufemismo","prematuro","filosofia","prudencia","mitologia","dieciseis","provincia","enfermero","funciones","fortaleza","mapamundi","dimension","animales","fractales","dieciocho","exactitud","simpatico","inquietud","cincuenta","serenidad","paciencia","inclusion","depresion","romantico","miercoles","crescendo","confesion","barcelona","mordedura","audifonos","bendicion","dramatico"]
pal10=["videojuego","matematica","computador","asociacion","hemisferio","granadilla","hipotalamo","arquitecto","calendario","tecnologia","hipopotamo","crucigrama","aritmetica","matrimonio","salchichon","transexual","psicologia","diversidad","tartamudeo","comentario","abecedario","superheroe","vacacional","uniformado","uzbekistan","jamaiquino","judicatura","obligacion","oficinista","defectuoso","cumpleaños","disciplina","plastilina","natureleza","mendicidad","zarigueyas","adaptacion","campesinos","lentejuela","despiadado","etnografia","transmitir","crepusculo","hospitales","sarpullido"]

#Clase que divide los niveles del juego según la longitud de las palabras

class Nivel:
    import random
    def __str__(): #constructor de la clase 
        while True:
            lenw=int(input("Escoge un nivel de dificultad entre 3 y 10: ")) #la longitud de la palabra a adivinar depende del nivel de dificultad escogido
            #se examina cada uno de los casos posibles y se retorna una palabra de la longitud escogida
            if lenw == 3:
                print("La palabra que tienes que adivinar tiene {0} letras".format(lenw))
                print ("Ya puedes comenzar a adivinar")
                return random.choice(pal3)
                break
                        
            elif lenw == 4:
                print("La palabra que tienes que adivinar tiene {0} letras".format(lenw))
                print ("Ya puedes comenzar a adivinar")
                return random.choice(pal4)
                break
                    
            elif lenw == 5:
                print("La palabra que tienes que adivinar tiene {0} letras".format(lenw))
                print ("Ya puedes comenzar a adivinar")
                return random.choice(pal5)
                break
                        
            elif lenw == 6:
                print("La palabra que tienes que adivinar tiene {0} letras".format(lenw))
                print ("Ya puedes comenzar a adivinar")
                return random.choice(pal6)
                break
                        
            elif lenw == 7:
                print("La palabra que tienes que adivinar tiene {0} letras".format(lenw))
                print ("Ya puedes comenzar a adivinar")
                return random.choice(pal7)
                break
                        
            elif lenw ==8:
                print("La palabra que tienes que adivinar tiene {0} letras".format(lenw))
                print ("Ya puedes comenzar a adivinar")
                return random.choice(pal8)
                break            
                    
            elif lenw ==9:
                print("La palabra que tienes que adivinar tiene {0} letras".format(lenw))
                print ("Ya puedes comenzar a adivinar")
                return random.choice(pal9)
                break
                    
            elif lenw ==10:
                print("La palabra que tienes que adivinar tiene {0} letras".format(lenw))
                print ("Ya puedes comenzar a adivinar")
                return random.choice(pal10)
                break
                
            else:
                print('{0} no es un entero entre 3 y 10'.format(lenw))
