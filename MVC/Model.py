from  flask  import  Flask , request , jsonify , make_response
importar  json

app  =  Flask ( __name__ )

tarefas  = [
    {
        'id' : 1 ,
        'name' : "Produto 1" ,
        "description" : "Esse é o produto 1"
    },
    {
        "id" : 2 ,
        "name" : 'Produto 2' ,
        "description" : "Esse é o produto 2"
    },
    {
         "id" : 3 ,
        "name" : 'Produto 3' ,
        "description" : "Esse é o produto 3"
    }
]

Lista_de_produtos  =  json . dumps ( tarefas )

classe  Modelo ():
    def  produtos ():
        #comunicaçãobanco
        #regra de negocios
        retornar  Lista_de_produtos