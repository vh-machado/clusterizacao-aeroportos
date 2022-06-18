'''
    Classe responsável pela modelagem das coordenadas de banco de dados dos bairros de Belém, seguindo
    as fontes

    • Distrito administrativo de Belém - Centro (DABEL)
    • Distrito administrativo do Entroncamento (DAENT)
    • Distrito administrativo do Guamá (DAGUA)
    • Distrito administrativo do Benguí – Nova Belém (DABEN)
    • Distrito administrativo da Sacramenta (DASAC)

'''

class DataBase(object):

    
    def __init__(self):
        self.quantity_neighborhoods = 39
        self.dimensions = 2
        
        self.neighborhoods  = {
            'Batista Campos' : {'coordinates':(-1.4605943431379507, -48.489817446635655), 'centroid': None},
            'Campina'        : {'coordinates':(-1.451566195417784,  -48.49904909461015),  'centroid': None},
            'Cidade Velha'   : {'coordinates':(-1.4608155705226513, -48.50614211759469),  'centroid': None},
            'Fatima'         : {'coordinates':(-1.4416052744484091, -48.47249206212274),  'centroid': None},
            'Nazare'         : {'coordinates':(-1.4539594926806354, -48.48123052840319),  'centroid': None},
            'Reduto'         : {'coordinates':(-1.445978774760613,  -48.49249213076001),  'centroid': None},
            'Sao Bras'       : {'coordinates':(-1.4515463874839785, -48.47080274126891),  'centroid': None},
            'Umarizal'       : {'coordinates':(-1.4414126980100477, -48.48375311397722),  'centroid': None},
            'Marco'          : {'coordinates':(-1.4352675908435437, -48.46126363796704),  'centroid': None},
            
            'Curio-Utinga'   : {'coordinates':(-1.430480180009479,  -48.446548277162066), 'centroid': None},
            'Aguas Lindas'   : {'coordinates':(-1.4055723052634344, -48.39512702712799),  'centroid': None},
            'Aura'           : {'coordinates':(-1.4082851671255567, -48.39753461893008),  'centroid': None},
            'Castanheira'    : {'coordinates':(-1.4086947376898031, -48.43140820637047),  'centroid': None},
            'Guanabara'      : {'coordinates':(-1.398005,           -48.414907),          'centroid': None},
            'Mangueirao'     : {'coordinates':(-1.3782816029283569, -48.44530337949438),  'centroid': None},
            'Marambaia'      : {'coordinates':(-1.4041742008591003, -48.453870278548415), 'centroid': None},
            'Souza'          : {'coordinates':(-1.414227808018852,  -48.45288043857192),  'centroid': None},
            'Val-de-Cans'    : {'coordinates':(-1.3900919728908587, -48.47343004944939),  'centroid': None},
            
            'Canudos'        : {'coordinates':(-1.4535963272004575, -48.46126652913588),  'centroid': None},
            'Condor'         : {'coordinates':(-1.4722717460874073, -48.48125447066777),  'centroid': None},
            'Cremacao'       : {'coordinates':(-1.4613507708896258, -48.476347018758965), 'centroid': None},
            'Guamá'          : {'coordinates':(-1.4639542261610194, -48.463309854794716), 'centroid': None},
            'Jurunas'        : {'coordinates':(-1.4706879550670389, -48.4937855558099),   'centroid': None},
            'Terra Firme'    : {'coordinates':(-1.4571413558852695, -48.451256552002036), 'centroid': None},
            'Universitario'  : {'coordinates':(-1.4642624071829904, -48.44144549753805),  'centroid': None},
            
            'Bengui'         : {'coordinates':(-1.3752277654519802, -48.45536926945969),  'centroid': None},
            'Cabanagem'      : {'coordinates':(-1.3680783967719699, -48.43253656597374),  'centroid': None},
            'Coqueiro'       : {'coordinates':(-1.3380198721152354, -48.444047592715116), 'centroid': None},
            'Parque Verde'   : {'coordinates':(-1.367196806649681,  -48.443823561243),    'centroid': None},
            'Pratinha'       : {'coordinates':(-1.3606098903250072, -48.47366357072046),  'centroid': None},
            'Sao Clemente'   : {'coordinates':(-1.3658988373419185, -48.461233164926185), 'centroid': None},
            'Tapana'         : {'coordinates':(-1.3386561496417695, -48.47389957731982),  'centroid': None},
            #'Tenone'         : {'coordinates':(-1.318846552382267,  -48.44106489733067),  'centroid': None},
            'Una'            : {'coordinates':(-1.3716708157278321, -48.42512094369472),  'centroid': None},
            
            'Barreiro'       : {'coordinates':(-1.4139701697170366, -48.484403616862224), 'centroid': None},
            'Maracangalha'   : {'coordinates':(-1.399284122891722,  -48.48127950425518),  'centroid': None},
            'Miramar'        : {'coordinates':(-1.4067413308704868, -48.49130764971447),  'centroid': None},
            'Pedreira'       : {'coordinates':(-1.4245104972103562, -48.47122244428872),  'centroid': None},
            'Sacramenta'     : {'coordinates':(-1.4138489639930902, -48.476198120925744), 'centroid': None},
            'Telegrafo'      : {'coordinates':(-1.4260575726545308, -48.48733732870352),  'centroid': None},
        }