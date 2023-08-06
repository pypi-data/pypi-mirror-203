#
# Copyright (c) 2023 Dilili Labs, Inc.  All rights reserved. Contains Dilili Labs Proprietary Information. RESTRICTED COMPUTER SOFTWARE.  LIMITED RIGHTS DATA.
#
from argparse import ArgumentParser

from brainframe.api import BrainFrameAPI, bf_errors, bf_codecs
from brainframe_apps.logger_factory import log

from brainframe_apps.command_utils import command, subcommand_parse_args, by_name
from brainframe_apps.cognito_tokens import ports


def set_cloud_tokens(api, access_token, refresh_token):
    tokens = bf_codecs.CloudTokens(
        access_token=access_token,
        refresh_token=refresh_token,
    )

    try:
        cloud_user_info, license_info = api.set_cloud_tokens(tokens)
        message_str = f"set_cloud_tokens returns cloud_user_info: {cloud_user_info}, license_info: {license_info}"
    except Exception as e:
        message_str = f"set_cloud_tokens failed {e}: {tokens}"

    log.debug(message_str)


def get_user_info(api):
    try:
        user_info = api.get_current_cloud_user()
        message_str = f"User info is {user_info}"
    except Exception as e:
        message_str = f"Get current user info failed {e}"

    log.debug(message_str)


def get_oauth2_info(api):
    try:
        oauth2_info = api.get_oauth2_info()
        message_str = f"OAuth2 info is {oauth2_info}"
    except Exception as e:
        message_str = f"Get OAuth2 info failed {e}"

    log.debug(message_str)


def _user_control_parse_args(parser):
    parser.add_argument(
        "--server-url",
        default="http://localhost",
        help="The BrainFrame server " "URL, Default: %(default)s",
    )
    parser.add_argument(
        "--access-token",
        default=None,
        help="The OAuth2 JWT access token of an user. Default: %(default)s",
    )
    parser.add_argument(
        "--refresh-token",
        default=None,
        help="The OAuth2 JWT refresh token of an user. Default: %(default)s",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=None,
        help="The port number of the redirect url",
    )
    parser.add_argument(
        "--auth-dilili",
        dest="auth_dilili",
        action="store_true",
        default=False,
        help="Authenticate with auth_dilili",
    )


@command("user_control")
def user_control(this_is_main=False):
    parser = ArgumentParser(
        description="User control of a BrainFrame deployment"
    )
    _user_control_parse_args(parser)
    if this_is_main:
        args = parser.parse_args()
    else:
        args = subcommand_parse_args(parser)

    # Connect to BrainFrame server
    api = BrainFrameAPI(args.server_url)

    log.debug(f"{str(parser.prog)} Waiting for server at {args.server_url} ...")

    try:
        api.wait_for_server_initialization(timeout=15)
    except (TimeoutError, bf_errors.ServerNotReadyError):
        log.error(f"BrainFrame server connection timeout")
        return

    if args.access_token is not None and args.refresh_token is not None:
        access_token = args.access_token
        refresh_token = args.refresh_token
    else:
        if args.port is None:
            port = ports[0]
        else:
            port = args.port

        if args.auth_dilili:
            from brainframe_apps.auth_dilili_tokens import get_access_token
            access_token, refresh_token = get_access_token()
        else:
            from brainframe_apps.cognito_tokens import make_pkce_code, get_authorization_redirect_url, get_authorization_code, get_access_token
            code_challenge, code_verifier = make_pkce_code()

            authorization_redirect_url = get_authorization_redirect_url(code_challenge, port)
            authorization_code = get_authorization_code(authorization_redirect_url, port)

            access_token, refresh_token = get_access_token(authorization_code, code_verifier, port)

    set_cloud_tokens(api, access_token, refresh_token)
    get_user_info(api)
    get_oauth2_info(api)

    return


if __name__ == "__main__":
    by_name["user_control"]()
