import tensorflow_hub as hub 
import tensorflow_text as text
import keras

def interpretacion_cita ( ref ):
  interprete = []
  for cita in ref:
    if cita >=0.5 : 
      interprete.append('CITA IEEE')
    if cita<0.5 : 
      interprete.append('CITA APA')
  return interprete

def main(): 

  # Recargue el modelo de los 2 archivos que guardamos
  with open('CitasRN.json') as json_file:
      json_config = json_file.read()
  json_file.close()
  new_model = keras.models.model_from_json(
    json_config,
    custom_objects={'KerasLayer':hub.KerasLayer}
  )
  new_model.load_weights('CitasRN_weights.h5')
  # new_model = tensorflow.keras.models.load_model(
  #   ('Citas_RN.h5'),
  #   custom_objects={'KerasLayer':hub.KerasLayer}
  # )

  

  #new_model.summary()

  citas = [ 
    'González, R. (2013). Costos Paramétricos - México, D.F. Instituto Mexicano de Ingeniería de Costos. D.F, México. Editorial Trillas',
    '1.  SEP, 2011. “Programa de Estudio 2011, Guía para la Educadora, Educación  Básica Prescolar”. México, SEP.',
    '9.  Moltó  ,  E.  Fundamentos  de  la  Educación  en  Física.  Ministerio  de  Educación, La Habana, 2003.',
    'Bloot, S. J., & Pye, K. (2001). “Gradistat: A gran size distribution and statics package for the analysis of unconsolidated sediments”. Earth Surface Processes and Landforms, 261.',
  ]

  analisis = new_model.predict(citas)
  print(interpretacion_cita(analisis))

main()