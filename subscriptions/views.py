from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.urls import reverse

from djstripe.models import Subscription

import stripe
from django.views.decorators.http import require_POST
from djstripe import webhooks as djstripe_hooks
from django.core.mail import mail_admins
from djstripe.models import Customer
from django.conf import settings
import djstripe

STRIPE_SECRET_KEY = "sk_test_51ODKwZEVbfr5OPjD1nyyolXyJfGoZjBJXUNJSA9dcDtaLWCiMnQff2TakKP8lWTKR1Vg0Dbgd3sbj6cAiv1YkcfV00bQ3rxBct"

@login_required
def pricing_page(request):
    return render(request, 'pricing_page.html', {
        'stripe_test_public_key': settings.STRIPE_TEST_PUBLIC_KEY,
        'stripe_pricing_table_id': settings.STRIPE_PRICING_TABLE_ID,
    })

@login_required
def subscription_confirm(request):
    # set our stripe keys up
    stripe.api_key = STRIPE_SECRET_KEY

    # get the session id from the URL and retrieve the session object from Stripe
    session_id = request.GET.get("session_id")
    assert session_id is not None, "session_id es None"
    session = stripe.checkout.Session.retrieve(session_id)

    # get the subscribing user from the client_reference_id we passed in above
    client_reference_id = int(session.client_reference_id)
    subscription_holder = get_user_model().objects.get(id=client_reference_id)
    # sanity check that the logged in user is the one being updated
    assert subscription_holder == request.user

    # get the subscription object form Stripe and sync to djstripe
    subscription = stripe.Subscription.retrieve(session.subscription)
    djstripe_subscription = Subscription.sync_from_stripe_data(subscription)

    # set the subscription and customer on our user
    subscription_holder.subscription = djstripe_subscription
    subscription_holder.customer = djstripe_subscription.customer
    subscription_holder.save()

    # show a message to the user and redirect
    messages.success(request, f"You've successfully signed up. Thanks for the support!")
    return HttpResponseRedirect(reverse("subscription_details"))

@login_required
def create_portal_session(request):
    stripe.api_key = STRIPE_SECRET_KEY
    domain = "http://tuhogar360.up.railway.app"
    if settings.DEBUG:
        domain = "http://127.0.0.1:8000"
    portal_session = stripe.billing_portal.Session.create(
        customer=request.user.customer.id,
        return_url=domain + "/perfil/",
    )
    return HttpResponseRedirect(portal_session.url)


@djstripe_hooks.handler("customer.subscription.deleted")
def email_admins_when_subscriptions_canceled(event, **kwargs):
    # example webhook handler to notify admins when a subscription is deleted/canceled
    try:
        customer_email = Customer.objects.get(id=event.data["object"]["customer"]).email
    except Customer.DoesNotExist:
        customer_email = "unavailable"

    mail_admins(
        "Someone just canceled their subscription!",
        f"Their email was {customer_email}",
        fail_silently=True,
    )