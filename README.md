# Opdracht 2 van SP
Dit is opdracht 2 van structered programming.

# Document store naar relationele database
We halen data uit een MongoDB database met een python script en zetten dan om naar postgres database

# Benodigde niet standaard python libraries
- psycopg2 (voor interactie met de postgres database)
- pymongo (voor interactie met de mongodb database)

# Data analyse van json

## products
{
   "_id":"100241", # nodig voor producten aan aankopen linken
   "category":{ # producten hebben verschillende aantal categorieen dus we hebben besloten alleen maar de bovenste 2 categorieen te nemen
      "category_1":"Gitaar",
      "category_2":"Gitaar accessoires",
      "category_3":"Stemapparaat"
   },
   "price":{
      "selling_price":1335 # best wel nuttig voor gelijkbare producten vinden
   },
   "gender":null, # niet nuttig
   "brand":"Korg", # nuttig voor producten aan elkaar linken
   "color":null, # niet nuttig
   "size":null, # niet nuttig
   "fast_mover":null, # niet nuttig
   "flavor":null, # niet nutting
   "properties":{
      "description_short":"Deze tuner plaatst u in het klankgat van uw akoestische gitaar, de lampjes geven u aan hoe het met de zuiverheid van uw snaren is gesteld. Futuristische looks, maar vooral heel erg handig.", # kunnen we niet echt gebruiken
      "availability_warehouse":1.0, # als er niets in het waren huis zit
      "availability_store":"1", # en ook niets in de winkel nemen we informatie niet mee
      "availability_number":null, # niet nuttig
      "product_type_nr":"RP-G1", # niet nuttig
      "review_content":[
         null,
         null
      ], # niet nuttig
      "google_category":"Arts & Entertainment > Hobbies & Creative Arts > Musical Instrument Accessories > String Instrument Accessories", # lastig te gebruiken en we hebben ook al de categorien
      "product_length":"10.00", # niet nuttig
      "product_width":"9.00",# niet nuttig
      "supplier_name":"Musik Meyer Benelux", # niet nuttig
      "name_long":"Korg RP-G1 Rimpitch tuner voor klankgat gitaar", # niet nuttig
      "prod_warranty_text":null, # niet nuttig
      "itemrevenue":null, # niet nuttig
      "itemsperpurchase":null, # niet nuttig
      "revenueperitem":null, # niet nuttig
      "uniquepurchases":null # niet nuttig
   },
   "description":"<p>Tsja, waarom moet een gitaar-tuner eigenlijk altijd zo&#39;n clip-on zijn voor op de kop van de hals? Korg heeft met de Korg RP-G1 Rimpitch tuner voor klankgat gitaar duidelijk een nieuw idee verwezenlijkt. Dit product klemt u aan de binnenzijde van het klankgat van uw akoestische gitaar. De lampjes op het geronde paneeltje vertellen u hoe het staat met de zuiverheid van uw snaren. Dat uw gitaar met deze tuner en al z&#39;n lampjes gelijk een stukje futuristischer oogt is natuurlijk een leuke bijkomstigheid.</p>", # kunnen we niet gebruiken
   "deeplink":"https://www.bax-shop.nl/stemapparaat/korg-rp-g1-rimpitch-tuner-voor-klankgat-gitaar", # niet nuttig
   "name":"Korg RP-G1 Rimpitch tuner voor klankgat gitaar", # niet nuttig
   "images":[
      [
         "https://static.bax-shop.nl/image/product/100241/214189/025ae6a3/140x140/korg_rp-g1_rimpitch_tuner_voor_klankgat_gitaar_1.jpg",
         "https://static.bax-shop.nl/image/product/100241/214189/025ae6a3/140x140/korg_rp-g1_rimpitch_tuner_voor_klankgat_gitaar_1.jpg"
      ] # niet nuttig
   ],
   "prod_sku":"9000-0010-0241", # niet nuttig
   "recommendable":true, # als hij niet recommendable is hoeven we hem niet mee te nemen voor de recommendation engine
   "sm":{
      "last_updated":{
         "$date":"2020-12-09T14:19:48.485+0000"
      }, # niet nuttig
      "type":"retail_product", # niet nuttig
      "is_active":true # actief moet actief zijn om te recommenderen
   },
   "_preferences":[
      "brand.Korg",
      "category.Gitaar",
      "sub_category.Gitaar accessoires",
      "sub_sub_category.Stemapparaat",
      "google_category.Arts & Entertainment > Hobbies & Creative Arts > Musical Instrument Accessories > String Instrument Accessories",
      "manufacturer.Musik Meyer Benelux",
      "product_length.10\\x2E00",
      "product_size.9\\x2E00"
   ] # niet nuttig
}

## sessions
{
    "_id": "5294f39d-b82b-483b-a607-668e805b063b",
    "buid": [
        "SF1.6.59-d266c7ed-a911-45e4-a3f5-83f76248df05" # nuttig voor linken aan profile
    ],
    "cg_treated": false, # niet nuttig
    "has_sale": false, # niet nuttig
    "order": { # alleen nuttig als hij iets heeft gekocht
        "total": None,
        "id": null
    },
    "session_end": {
        "$date": "2020-12-09T14:10:43.428+0000"
    }, # niet nuttig
    "session_start": {
        "$date": "2020-12-09T14:01:40.392+0000"
    }, # niet nuttig
    "tg_treated": false, # niet nuttig
    "user_agent": {  # niet nuttig
        "os": {
            "familiy": "Windows",
            "version": [
                10
            ],
            "version_string": "10"
        },
        "browser": { # niet nuttig
            "familiy": "Firefox",
            "version": [
                83,
                0
            ],
            "version_string": "83.0"
        },
        "device": { # niet nuttig
            "family": "Other",
            "brand": null,
            "model": null
        },
        "flags": { # niet nuttig
            "is_bot": false,
            "is_email_client": false,
            "is_mobile": false,
            "is_pc": true,
            "is_tablet": false,
            "is_touch_capable": false
        },
        "accept": { # niet nuttig
            "language": "en-US,en;q=0.5",
            "protocols": "*/*"
        },
        "identifier": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0", # niet nuttig
        "ip": null # niet nuttig
    },
    "events": [ # een event is eigenlijk alleen handig als er naar een product gekeken is
        {
            "t": {
                "$date": "2020-12-09T14:01:40.392+0000"
            },
            "source": "eventtracker",
            "action": "sync",
            "pagetype": null,
            "product": null,
            "product_ids": null,
            "product_properties": {
            
            },
            "time_on_page": 0.923,
            "max_time_inactive": null,
            "click_count": null,
            "elements_clicked": 0,
            "scrolls_down": null,
            "scrolls_up": null,
            "page_url": "https://www.bax-shop.nl/"
        },
        {
            "t": {
                "$date": "2020-12-09T14:10:43.428+0000"
            },
            "source": "eventtracker",
            "action": "stats",
            "pagetype": "DP",
            "product": null,
            "product_ids": null,
            "product_properties": {
            
            },
            "time_on_page": 9.894,
            "max_time_inactive": 0.425,
            "click_count": 2,
            "elements_clicked": 1,
            "scrolls_down": 3,
            "scrolls_up": 1,
            "page_url": "https://www.bax-shop.nl/plectrum-set/dunlop-pvp102-variety-pack-medium-heavy-12-pack#productreviews"
        }
    ],
    "segment": "JUDGER" # alleen echt nuttig als er iets gekocht is
}

## profiles
{
   "_id":{
      "$oid":"5fd0d8c9701de4624db04b82"
   },
   "buids":[ # hier staan alle sessions in van 1 profile
      "SF1.6.59-d266c7ed-a911-45e4-a3f5-83f76248df05" # dit is een sessie
   ],
   "sm":{
      "created":{
         "$date":"2020-12-09T14:01:45.142+0000"
      },
      "created_by":"LegacyDao" # hoe het profiel is aangemaakt
   },
   "meta":{
      "has_device":true, # niet nuttig
      "has_email":false, # niet nuttig
      "has_utm_hash":false, # niet nuttig
      "random":0.4351745417327053 # zeker niet nuttig
   },
   "latest_activity":{
      "$date":"2020-12-09T14:01:40.392+0000"
   } # niet nuttig
}
