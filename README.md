Vendor Management System with performence metrices in Django
A Vendor Management System using Django and Django REST Framework. This
system will handle vendor profiles, track purchase orders, and calculate vendor performance
metrics 

1.Features
  Vendor Profile Management:
    Create, retrieve, update, and delete vendor profiles.
    Calculate and display vendor performance metrics.

  Purchase Order Tracking:
    Create, retrieve, update, and delete purchase orders.
    Track delivery status, items, quantity, and other details.

  Vendor Performance Evaluation:
    Calculate performance metrics, including on-time delivery rate, quality rating average, average response time, and fulfillment rate.
    Historical performance tracking for trend analysis.

2.Technical Requirements
  Django (latest stable version)
  Django REST Framework (latest stable version)
  Token-based authentication
  Comprehensive data validations
  Django ORM for database interactions

3.Installation
    Create and activate a virtual environment:
     python -m venv venv
     .\venv\Scripts\activate

    Install dependencies:
      pip install -r requirements.txt

    Run migrations:
      python manage.py makemigrations
      python manage.py migrate
 
    Run:
      python manage.py runserver

4.API
    http://127.0.0.1:8000/admin/
    http://127.0.0.1:8000/api/vendors/ 
    http://127.0.0.1:8000/api/vendors/<int:pk>/ 
    http://127.0.0.1:8000/api/purchase_orders/
    http://127.0.0.1:8000/api/purchase_orders/<int:pk>/ 
    http://127.0.0.1:8000/api/vendors/<int:pk>/performance/ 
    http://127.0.0.1:8000/api/purchase_orders/<int:pk>/acknowledge/ 

5.API Documentation

  sample JSON for Create Vendor
  {
    "name": "vendor1",
    "contact_details": "9876543210",
    "address": "ertyuilkjhgfsxcvn",
    "vendor_code": "VEN001",
    "on_time_delivery_rate": 100.0,
    "quality_rating_avg": 98.0,
    "average_response_time": 90.0,
    "fulfillment_rate": 94.0
  }
  sample json for update the acknowledgement in Purchase Order
  {
    "acknowledgment_date": "2024-05-09T10:17:00Z"
  }

6.API Endpoints
     
     create a new Vendor => URL:POST /api/vendors/ 
     {
      "name": "vendor1",
      "contact_details": "9876543210",
      "address": "ertyuilkjhgfsxcvn",
      "vendor_code": "VEN001",
      "on_time_delivery_rate": 100.0,
      "quality_rating_avg": 98.0,
      "average_response_time": 90.0,
      "fulfillment_rate": 94.0
     }

     List all Vendor => URL:GET /api/vendors/
     Retrieve a specific vendor's details => GET /api/vendors/{vendor_id}/
     Update a vendor's details => PUT /api/vendors/{vendor_id}/
     Delete a vendor => DELETE /api/vendors/{vendor_id}/
     Authentication: Token-based authentication required

  Purchase Order Endpoints 
      
     Create a new purchase order => POST /api/purchase_orders/
        "po_number": "PO123",
        "order_date": "2024-05-01T11:49:00Z",
        "delivery_date": "2024-05-04T11:50:00Z",
        "items": {
            "title": "To Kill a Mockingbird",
            "author": "Harper Lee",
            "published_year": 1960,
            "genre": "Novel"
        },
        "quantity": 60,
        "status": "completed",
        "quality_rating": null,
        "issue_date": "2024-05-04T11:51:00Z",
        "acknowledgment_date": "2024-05-04T11:51:00Z",
        "vendor": 5

        List all purchase orders => GET /api/purchase_orders/
        Retrieve details of a specific purchase order => GET /api/purchase_orders/{po_id}/
        Update a purchase order => PUT /api/purchase_orders/{po_id}/
        Delete a purchase order => DELETE /api/purchase_orders/{po_id}/
        Authentication: Token-based authentication required

     
     

     
    