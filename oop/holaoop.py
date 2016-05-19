#
# script........: holaoop.py
# fecha.........: 18-05-2016
#

class Hola:
  mensaje = "Hola Mundo con Python y POO..."
  
  def imprimeSaludo(self):
    print self.mensaje
	
#
# Programa principal
#

# Definimos un objeto "saludo"
misaludo = Hola()

# Utilizamos el m'etodo "imprimeSaludo" del objeto "misaludo"
misaludo.imprimeSaludo()