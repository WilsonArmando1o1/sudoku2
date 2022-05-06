#determine  si un tablero de Sudoku es  9x9 es valido 
#solo las celdas llenas deben validarse de acuerdo con las siuguientes reglas 

#paso 1 chequear quer el tablero introducido sea un tablero de 9x9 
#paso 2 cada fila debe tener datos del 1 al 9 sin repetir datos 
 # Cada caso de prueba está formado por 9 líneas, cada una con 9 números entre el 1 y el 9 separados por espacios,
 #que representan un sudoku completamente relleno.
 



tablero = [
    ["4",".","3",".",".",".","6","7","."]
    ,[".",".",".","1",".","9",".",".","."]
    ,["2",".","9",".","3","6","1",".","."]
    ,[".","9",".",".","6","2",".",".","."]
    ,["7",".","6",".",".",".","5",".","4"]
    ,[".",".",".","5","1",".",".","9","."]
    ,[".",".","1","6","9",".","3",".","7"]
    ,[".",".",".","3",".","8",".",".","."]
    ,[".","3","4",".",".",".","9",".","8"]
]

class sudoku:
     def __init__(self,tablero)->None:
      self.tablero=tablero
      

     def chequeo_general(self):
        
          "endregionc hequear quer el tablero introducido sea un tablero de 9x9"
          
        #"assert"
          assert len(self.tablero) == 9 #filas 
         
          for fila in Self.tablero:
            assert len(fila) == 9  
            "endregionel formato ingresado no respeta el tablero 9x9"
      
      
     def chequeo_filas(self):
          for fila in self.tablero:  
           for elemento in fila:
              if elemento != ".":
                assert fila.count(elemento)==1 #"tablero no valido"


#instanciar el objeto
sudoku= sudoku(tablero)
sudoku.chequeo_general()
sudoku.chequeo_filas()
