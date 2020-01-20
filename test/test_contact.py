# -*- coding: utf-8 -*-
import pytest

from fixture.appcontact import AppContact
from model.contact import Contact
import pytest


@pytest.fixture
def app(request):
    fixture = AppContact()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="Elena", last_name="Talley", address="Moscow", email="g345@gmail.com"))
    app.session.logout()


def test_add_empty_contact (app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="", last_name="", address="", email=""))
    app.session.logout()


def test_add_contact_with_empty_address_and_email(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="Petr", last_name="Ivanov", address="", email=""))
    app.session.logout()










