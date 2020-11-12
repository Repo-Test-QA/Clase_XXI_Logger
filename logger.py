#Importamos la librería de logging
import logging

#Indicamos desde que nivel se va a mostrar la información
#logging.basicConfig(level=logging.DEBUG)
#Queremos que se guarde los logs generados en un archivo con un formato personalizado
logging.basicConfig(level=logging.DEBUG, filename='convert.log', filemode = 'w', format='%(name)s - %(levelname)s - %(message)s')

#Niveles de logging
#logging.debug('Esto es un debug')
#logging.info('Esto es información de lo que esta pasando')
#logging.warning('Ojo que hay un problemita')
#logging.error('Acá hay un error')
#logging.critical('Ojo que vuela todo por los aires')

#Vamos a convertir nros. a distintas bases
def convert_number(number, base):
    logging.info('I am entering to the convert number function')
    logging.debug('Number: ' + str(number))
    logging.debug('Base: ' + str(base))
    #Agregamos un Try, para controlar una excepción por el valor del number
    try:
        if(number > 100000000):
            logging.warning('Big number can make the program run slower')
        if base == 2:
            #Devuelbe número binario
            return bin(number)
        if base == 8:
            #Devuelve un número octal
            return oct(number)
        if base == 16:
            #Devuelve un número Hexa
            return hex(number)
        logging.error('This is a incorrect base, we will add it in the future')
        return('Incorrect base selected')
    except:
        logging.critical('Can\'t perform operation')
        return('CRITICAL ERROR')

print(convert_number(2000, 2))
print(convert_number(1500, 8))
print(convert_number(250, 16))
print(convert_number(120, 65))
print(convert_number('Pepe', 2))
print(convert_number(100000001, 16))
