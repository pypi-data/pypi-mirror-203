# coding: utf-8
"""
Authentication functions for the SampleDB RESTful API.
"""
import typing

import flask

from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth, MultiAuth

from ...logic.authentication import login, login_via_api_token, get_active_two_factor_authentication_method
from ...logic.users import User
from ...models import Permissions
from ...utils import object_permissions_required as object_permissions_required_generic

__author__ = 'Florian Rhiem <f.rhiem@fz-juelich.de>'

http_basic_auth = HTTPBasicAuth()
http_token_auth = HTTPTokenAuth(scheme='Bearer')
multi_auth = MultiAuth(http_basic_auth, http_token_auth)


@http_token_auth.verify_token
def verify_token(api_token: typing.Optional[str]) -> typing.Optional[User]:
    if not api_token:
        return None
    user = login_via_api_token(api_token)
    if user is None or not user.is_active:
        return None
    flask.g.user = user
    return user


@http_basic_auth.verify_password
def verify_password(username: str, password: str) -> typing.Optional[User]:
    if not username:
        return None
    user = login(username, password)
    if user is None or not user.is_active:
        return None
    two_factor_authentication_method = get_active_two_factor_authentication_method(user.id)
    if two_factor_authentication_method is not None:
        # two-factor authentication is not supported for the HTTP API
        return None
    flask.g.user = user
    return user


def object_permissions_required(permissions: Permissions) -> typing.Callable[[typing.Any], typing.Any]:
    """
    Only allow access to a route it the user has the required permissions.

    Wrapper around the more generic sampledb.utils.object_permissions_required
    for use with the http_basic_auth object from this module.

    :param permissions: the required object permissions
    """
    return object_permissions_required_generic(
        required_object_permissions=permissions,
        auth_extension=multi_auth,
        user_id_callable=lambda: typing.cast(int, flask.g.user.id),
        may_enable_anonymous_users=False
    )
