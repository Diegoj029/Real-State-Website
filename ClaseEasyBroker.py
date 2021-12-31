import json
import requests

class EasyBrokerAPI:
    def __init__(self, key):
        self.url = 'https://api.stagingeb.com/'
        self.key_header = {'X-Authorization': key}
        self.api_request = requests.get(self.url, headers = self.key_header)
        self.status_code = self.api_request.status_code
        if self.status_code  == 200:
            print('Conexión exitosa', '\n')
        elif self.status_code == 401:
            print('API key inválida', '\n')
        else:
            print('Error de formato', '\n')


    def properties(self, search=''):
        properties = self.properties_paginated(1,20,search)

        total_properties = properties['pagination']['total']
        next_page = properties['pagination']['next_page']

        if total_properties > 0: 
            while next_page != None:
                for property in properties['content']:
                    print(property['title'])                       
                    
                properties = requests.get(next_page, headers = self.key_header).json()
                next_page = properties['pagination']['next_page']
            
            for property in properties['content']:
                print(property['title']) 

        else:
            print("Su cuenta no posee propiedades")

    def properties_paginated(self, page=1, limit=20, search=''):
        payload = {'page':page, 'limit':limit, 'search[statuses][]':search}
        properties = requests.get(self.url + 'v1/properties?', params = payload, headers = self.key_header).json()

        return properties

    def property(self, property_id):
        property = requests.get(self.url + 'v1/properties/' + property_id, headers = self.key_header).json()
        
        return property
    
    def post_contact_requests(self, name='', phone='', email='', property_id='', message='', source=''):
        payload = { "name": name,
                    "phone": phone,
                    "email": email,
                    "property_id": property_id,
                    "message": message,
                    "source": source}

        data = json.dumps(payload)

        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        headers.update(self.key_header)

        post_request = requests.post(self.url + 'v1/contact_requests', headers = headers, data = data)
        
        return post_request.status_code

    def get_content(self, properties):
        public_id = [] 
        title = []
        property_type = []
        location = []
        img_thumbnail = []

        for property in properties['content']:
            public_id.append(property['public_id'])
            title.append(property['title'])
            property_type.append(property['property_type'])
            location.append(property['location'])
            if property['title_image_thumb'] == None:
                img_thumbnail.append('https://www.zodoms.com/wp-content/themes/fortuna/images/no_img.jpg')
            else:
                img_thumbnail.append(property['title_image_thumb'])
        
        return public_id, title, property_type, location, img_thumbnail

    def get_images(self, property):
        images = []

        if len(property['property_images']):
            for image in property['property_images']:
                images.append([image['url'], image['title']])
        else:
            images.append(['https://st3.depositphotos.com/23594922/31822/v/600/depositphotos_318221368-stock-illustration-missing-picture-page-for-website.jpg', 'null'])

        return images