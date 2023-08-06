from unittest import TestCase

import os

from py_clob_client.client import ClobClient
from py_clob_client.clob_types import ApiCreds, OrderArgs
from dotenv import load_dotenv
from py_clob_client.constants import MUMBAI

from py_clob_client.order_builder.constants import SELL


load_dotenv()


class TestClient(TestCase):
    def test_create_order(self):
        host = "https://clob-staging.polymarket.com"
        key = os.getenv("PK")
        creds = ApiCreds(
            api_key=os.getenv("CLOB_API_KEY"),
            api_secret=os.getenv("CLOB_SECRET"),
            api_passphrase=os.getenv("CLOB_PASS_PHRASE"),
        )
        chain_id = MUMBAI
        client = ClobClient(host, key=key, chain_id=chain_id, creds=creds)

        # Create and sign a limit order buying 100 YES tokens for 0.0005 each
        order_args = OrderArgs(
            price=0.5,
            size=20,
            side=SELL,
            token_id="16678291189211314787145083999015737376658799626183230671758641503291735614088",
        )
        signed_order = client.create_order(order_args, "0.1")
        resp = client.post_order(signed_order)
        print(resp)
        print("Done!")
