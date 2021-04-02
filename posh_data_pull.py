import requests
import json

BASE_URL = 'https://poshmark.com/vm-rest'
CATEGORY_PART = '/channel_groups/category/channels/undefined/collections/post'

values = dict(
    department='Women',
    category='Bags',
    category_feature='Clutches_&_Wristlets',
    inventory_status='sold_out',
    count=10000,
    brand=''
)

PARAMS_TEMPLATE = '{{' \
                  '"filters":{{' \
                      '"department":"{department}",' \
                      '"category_v2":"{category}",' \
                      '"category_feature":"{category_feature}",' \
                      '"inventory_status":["{inventory_status}"],' \
                      '"brand":[{brand}]}},' \
                  '"facets":["color","brand","size"],' \
                  '"experience":"all",' \
                  '"sizeSystem":"us",' \
                  '"count":"{count}"}}'

params = dict(
    request=PARAMS_TEMPLATE.format(**values)
)

response = requests.get(BASE_URL + CATEGORY_PART, params=params)

#Store each datapoint in a dictionary then in a list to prepare for Mongo DB insertion
items_dict = {}
items_list = []
if response.status_code == 200:
    response_json = response.json()
    #Code below does not grab all data for each posting available
    for key, val in response_json.items():
        if key == 'data':
            for item in val:
                item_dict = {}
                #Not all items have a condition, it is not required
                if 'condition' in item:
                    condition = item['condition']
                else:
                    condition = ''
                item_dict = dict(
                    id=item['id'],
                    title=str(item['title']).lower(),
                    description=str(item['description']).lower().rstrip(),
                    condition=condition,
                    brand=str(item['brand']).lower(),
                    colors=item['colors'],
                    og_price=float(item['original_price_amount']['val']),
                    sell_price=float(item['price_amount']['val']),
                    seller_offer=item['has_seller_offer'],
                    share_count=int(item['share_count']),
                    like_count=int(item['like_count']),
                    comment_count=int(item['comment_count']),
                    creator_handle=item['creator_display_handle'],
                    inventory_status_changed_dt = item['inventory']['status_changed_at']
                )
                items_list.append(item_dict)
    #Write dictionary to text file using json lib dumps
    file = open('posh_pull_nobrand.txt', 'w', encoding='utf-8')
    file.write(json.dumps(items_list))
    file.close()
else:
    print(response)