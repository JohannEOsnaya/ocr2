def interpretacion_cita ( ref ):
  interprete = []
  for cita in ref:
    if cita >=0.5 : 
      interprete.append('CITA IEEE')
    if cita<0.5 : 
      interprete.append('CITA APA')
  return interprete