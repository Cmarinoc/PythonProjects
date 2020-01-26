use Proyecto
//Revisa el contenido del data set de Clothes
db.Clothes.find()
// Revisa el contenido que tiene los reviews de la ropa utilizada
db.Clothes_reviews.find()

// Cantidad de reviews y de artículos existentes
db.Clothes.find().count()
db.Clothes_reviews.find().count()

// Ambas bases de datos tienen el campo "category", renombrar en la base de datos Clothes el campo category por garment_status
db.Clothes.updateMany({ },{$rename: { "category": "garment_status"}})
db.Clothes.find()


//Se requiere saber la media de Rating por categoría y la cantidad de los reviews de cada uno
//El dataset the clothes_reviews tiene los valores de age y rating como string y no como enteros, primeramente es necesario organizar un poco el dataset
//1.Etapa para convertir los valores a números enteros
Conversion = {$set: {Rating: { $toInt: "$rating" },Age: { $toInt: "$age" },}};
//2. Guarda los valores en una nueva salida
salida={$out: 'NEW_Clothes_Reviews'}
db.Clothes_reviews.aggregate( [ Conversion, salida])
//3.Borrar los valores antiguos de age y rating del nuevo dataset
db.NEW_Clothes_Reviews.updateMany({},{$unset:{age:"",rating:""}})
db.NEW_Clothes_Reviews.find()

//Insertar una seccion nueva al archivo de Clothes que contenga los tipos de zapatos disponibles,un precio según la categoría y los tipos de colores
 zapatos=[{item_id:"89689", gender:"shoes", type:"flats",style:"women", price: 80, utility: "use with dress", color_available:["red","white","gold","pink"]},
         {item_id:"88969",  gender:"shoes", type:"formal", style:"men", price: 160, utility: "use with suit", color_available:["black","brown","blue"]},
         {item_id:"79678",  gender:"shoes", type:"sandals with highheels",style:"women", price: 120, utility: "use with dress or gown", color_available:["silver","red","white","gold","pink"]},
         {item_id:"79678",  gender:"shoes", type:"highheels",style:"women", price: 200, utility: "use with dress", color_available:["blue","white","gold","brown"]}]
 db.Clothes.insertMany(zapatos)
         
   
// Ordenar la puntuacion media de cada una de las categorias de ropa de mayor a menor e incluirlos en una nueva salida 
Agrupar={"_id":{"categoria":"$category"}, "Media Rating":{$avg:"$Rating"}, Cantidad_reviews:{$sum: 1}}
faseA={$group:Agrupar}


Ordenar={"Media Rating":-1}
faseB={$sort:Ordenar}

Salida={$out:"Media_Rating_Categoria"}
etapas=[faseA,faseB,Salida]
db.NEW_Clothes_Reviews.aggregate(etapas)
db.Media_Rating_Categoria.find()

 // Revisa cuales son las prendas con una media superior a 9 y una cantidad de reviews superior a 15000
db.Media_Rating_Categoria.find( { $and: [ { "Media Rating": { $gt: 9 } }, { "Cantidad_reviews": { $gt: 15000} } ] } )

// Revisa cuales son las prendas con una media menor a 7
 db.Media_Rating_Categoria.aggregate([
 {$match:{ "Media Rating":{$lt:7}}}
])
//Agrupar los reviews, el tipo de cuerpo y el ajuste para los jeans 
db.Clothes_reviews.find({"category":"jeans"}, { fit:1, "body type":1, review_text:1, rating:1})

//Identificar cuales articulos tienen una calidad menor a 3 y su garment_status sale o outerwear, identificando cual es la talla de los articulos
db.Clothes.aggregate([
 {$match:{ "quality":{$lt:3}, $or: [ { "garment_status":"sale" }, { "garment_status":"outerwear"  }]}},
 {$group:{"_id":{ "size":"$size","calidad":"$quality", "garment_status":"$garment_status"}}}
])
 

//Añadir “Standard_calification”:”Best Seller” a quienes tenga una media superior a 9 y una cantidad superior a 15000
db.Clothes_reviews.aggregate([
 {$match:{$or: [ { "category":"dress" }, { "category":"gown"  },{ "category":"sheath"  }]}},
 {$addFields:{"Standard_calification":"Best Seller"}}
])
db.Clothes_reviews.find()



// Encontrar todos los item_id que contengan la longitud "just right" y su garment_status sea "new"
db.Clothes.aggregate([
    {$match:{$and:[{"length":"just right"}, {"garment_status":"new"}]}},
    {$group: { "_id":{"fit":"$fit"},"Numero_items" :{ "$sum" : 1} }},
    {$project:{"_id":1,"fit":1, Numero_items:1}}
])
   
//Media de edad de los compradores 
media={"_id":"$category","AVG_Age":{$avg:"$Age"}}
fase1={$group:media}
ordena={"AVG_Age":1}
fase2={$sort:ordena}
etapas=[fase1,fase2]
db.NEW_Clothes_Reviews.aggregate(etapas)
//Persona con mayor edad y en que categoría se encuentra 

db.NEW_Clothes_Reviews.find ({} ,{ _id: 0, "category": 1, "Age": 1}).sort({ Age : -1}).limit(1)


//Cantidad de ocasiones que aparece la frase "next time" en un review
db.Clothes_reviews.find( { review_text: { $regex: /next time/ } } ).count()

//Puntuación media de los reviews para los compradores  entre los 35 y 65 años según el tipo de ajuste

filtracion= { "Age": { $gte: 35 , $lte: 65 } }

filtro= { $match: filtracion }

agrupacion=  { $group: { "_id": "$fit","Cantidad_de_Reviews": { $sum: 1 }, "Rating medio": { $avg: "$Rating" }} }

sort= { $sort: { "Age": -1 } }

etapas= [ filtro,agrupacion,sort]

db.NEW_Clothes_Reviews.aggregate(etapas)
//Puntuación media de los reviews para los compradores menores de 30 años según el tipo de ajuste

filtracion= { "Age": { $lt: 30 } }

filtro= { $match: filtracion }

agrupacion=  { $group: { "_id": "$fit","Cantidad_de_Reviews": { $sum: 1 }, "Rating medio": { $avg: "$Rating" }} }

sort= { $sort: { "Age": -1 } }

etapas= [ filtro,agrupacion,sort]

db.NEW_Clothes_Reviews.aggregate(etapas)



