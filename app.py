from flask import Flask, render_template, flash
from ClaseEasyBroker import EasyBrokerAPI
from forms import Contact_form
import math

app = Flask(__name__)
app.secret_key = 'l7u502p8v46ba3ppgvj5y2aad50lb9'

eb = EasyBrokerAPI(app.secret_key)

@app.route("/")
@app.route("/#")
@app.route("/page=<int:page_number>")
def index(page_number=1):
    num_properties = 15
    properties = eb.properties_paginated(page_number, num_properties, 'published')

    total_properties = properties['pagination']['total']
    total_pages = math.ceil(total_properties/num_properties)

    public_id, title, property_type, location, img_thumbnail = eb.get_content(properties)

    return render_template("index.html", num_properties = range(num_properties), public_id = public_id, title = title, 
                            property_type = property_type, location = location, img_thumbnail =img_thumbnail, 
                            total_properties = total_properties, page_number = page_number, total_pages = total_pages)


@app.route("/property/<string:property_id>=<int:image_index>", methods = ['GET','POST'])
def property(property_id, image_index=1):
    form = Contact_form()
    property = eb.property(str(property_id))
    images = eb.get_images(property)

    if form.validate_on_submit():
        contact_request = eb.post_contact_requests(form.name.data,form.phone.data,form.email.data,property['public_id'],
                                                        form.message.data, 'inmobilariadepruebas.com')
        if contact_request == 200:
            flash("El mensaje se ha enviado con éxito")
        else:
            flash("Ocurrió un error, favor de revisar sus datos")

    return render_template("property.html", public_id = property['public_id'], title = property['title'], 
                            property_type = property['property_type'], location = property['location']['name'], 
                            description = property['description'], images = images, num_images = len(images), image_index = image_index-1, form = form)

if __name__ == '__main__':
    app.run(debug=True)