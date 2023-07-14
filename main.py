from flask import Flask, render_template
import os


app = Flask(__name__)


@app.route('/')
def home():

    DIRECTORY_TO_LOOP = os.path.join('static', 'images')
    car_images = []
    
    for root, dirs, files in os.walk(DIRECTORY_TO_LOOP, topdown=False):
        for name in files:
            file_path = os.path.join('images', name)
            file_path = file_path.replace('\\', '/')
            car_images.append(file_path)


    print(car_images)
            
    


    service_info = {
        'title': "Daniel's Black SUV Service in Nashville, TN",
        'description': "Looking for a Black SUV service with the latest model vehicles available, you are at the right place. If you need to go places like Jack Daniel's disterilly, Graceland in Memphis, TN, or even the surrounding casinos, just look below for my contact information and feel free to ask for a quote.",
        'rates': {
            'hourly': '$100 per hour',
            'daily': '$1,000 per day',
            'weekly': '$5,500 per week'
        },
        'car_images': car_images,
        'contact_info': {
            'phone': '123-456-7890',
            'email': 'info@danielblackcarservice.com'
        }
    }

    return render_template('index.html', info=service_info)

if __name__ == '__main__':
    app.run(debug=True)

    
