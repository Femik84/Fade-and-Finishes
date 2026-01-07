from django.core.mail import send_mail
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["POST"])
def contact_view(request):
    first_name = request.data.get("firstName")
    last_name = request.data.get("lastName")
    email = request.data.get("email")
    phone = request.data.get("phone")
    message = request.data.get("message")

    name = f"{first_name} {last_name}"

    email_body = f"""
    Name: {name}
    Email: {email}
    Phone: {phone}

    Message:
    {message}
    """

    try:
        send_mail(
            subject="Contact Form Submission - Portfolio",
            message=email_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        return Response(
            {"message": "Email sent successfully"},
            status=status.HTTP_200_OK
        )

    except Exception as e:
        return Response(
            {"error": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(["POST"])
def booking_view(request):
    name = request.data.get("name")
    email = request.data.get("email")
    phone = request.data.get("phone")
    service = request.data.get("service")
    barber = request.data.get("barber")
    date = request.data.get("date")
    time = request.data.get("time")

    # Validate required fields
    if not all([name, email, phone, service, barber, date, time]):
        return Response(
            {"error": "All fields are required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Email body for the barbershop owner
    owner_email_body = f"""
    New Booking Request
    -------------------
    
    Customer Details:
    Name: {name}
    Email: {email}
    Phone: {phone}
    
    Booking Details:
    Service: {service}
    Barber: {barber}
    Date: {date}
    Time: {time}
    
    Please confirm this booking with the customer.
    """

    # Email body for the customer (confirmation)
    customer_email_body = f"""
    Dear {name},
    
    Thank you for booking with us! We've received your appointment request.
    
    Booking Details:
    Service: {service}
    Barber: {barber}
    Date: {date}
    Time: {time}
    
    We'll confirm your appointment shortly. If you have any questions, please contact us.
    
    Best regards,
    Your Barbershop Team
    """

    try:
        # Send email to barbershop owner
        send_mail(
            subject=f"New Booking Request - {name}",
            message=owner_email_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        # Send confirmation email to customer
        send_mail(
            subject="Booking Confirmation - Your Barbershop",
            message=customer_email_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=False,
        )

        return Response(
            {"message": "Booking request sent successfully. Check your email for confirmation."},
            status=status.HTTP_200_OK
        )

    except Exception as e:
        return Response(
            {"error": f"Failed to send booking request: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )