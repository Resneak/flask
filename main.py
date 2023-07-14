from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    service_info = {
        'title': "Daniel's 2 Black SUV Service in Nashville, TN",
        'description': "Looking for a Black SUV service with the latest model vehicles available, you are at the right place. If you need to go places like Jack Daniel's disterilly, Graceland in Memphis, TN, or even the surrounding casinos, just look below for my contact information and feel free to ask for a quote.",
        'rates': {
            'hourly': '$100 per hour',
            'daily': '$1,000 per day',
            'weekly': '$5,500 per week'
        },
        'car_images': [
            'images/image1.jpg',
            'images/image2.jpg',
            'images/image3.jpg',
            'images/image4.jpg',
            'images/image5.jpg',
            'images/image6.jpg',
            'images/image7.jpg',
            'images/image8.jpg',
        ],
        'contact_info': {
            'phone': '123-456-7890',
            'email': 'info@danielblackcarservice.com'
        }
    }

    return render_template('index.html', info=service_info)

if __name__ == '__main__':
    app.run(debug=True)

    
