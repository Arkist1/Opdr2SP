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