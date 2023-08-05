# Copyright 2021 Vincent Texier <vit@free.fr>
#
# This software is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from typing import List, Optional

from substrateinterface import Keypair

from tikka.domains.entities.node import Node
from tikka.domains.entities.smith import (
    SmithCertification,
    SmithMembership,
    SmithPendingMembership,
)
from tikka.domains.nodes import Nodes
from tikka.interfaces.adapters.network.smiths import NetworkSmithsInterface


class Smiths:

    """
    Smiths domain class
    """

    def __init__(
        self,
        nodes: Nodes,
        network: NetworkSmithsInterface,
    ):
        """
        Init Smiths domain

        :param nodes: Nodes domain instance
        :param network: NetworkAccountsInterface instance
        """
        self.nodes = nodes
        self.network = network

    def rotate_keys(self, node: Node) -> Optional[str]:
        """
        Change node session keys and return them

        :param node: Node instance
        :return:
        """
        session_keys = self.network.rotate_keys()
        if session_keys is not None:
            node.session_keys = session_keys
            self.nodes.update(node)
        return session_keys

    def has_session_keys(self, session_keys: str) -> Optional[bool]:
        """
        Return True if the current node keystore store private session keys corresponding to public session_keys

        :param session_keys: Session public keys (hex string "0x123XYZ")
        :return:
        """
        return self.network.has_session_keys(session_keys)

    def request_membership(self, keypair: Keypair, session_keys: str) -> bool:
        """
        Request a smith membership for the Keypair account with node session_keys

        :param keypair: Owner Keypair
        :param session_keys: Session public keys (hex string "0x123XYZ")
        :return:
        """
        return self.network.request_membership(keypair, session_keys)

    def claim_membership(self, keypair: Keypair) -> bool:
        """
        Claim that last smith membership request for the Keypair account fulfill all requirements

        :param keypair: Owner Keypair
        :return:
        """
        return self.network.claim_membership(keypair)

    def publish_session_keys(self, keypair: Keypair, session_keys: str) -> bool:
        """
        Set/Change in blockchain the session public keys for the Keypair account

        :param keypair: Owner Keypair
        :param session_keys: Session public keys (hex string "0x123XYZ")
        :return:
        """
        return self.network.publish_session_keys(keypair, session_keys)

    def go_online(self, keypair: Keypair) -> bool:
        """
        Start writing blocks with smith account from keypair

        :param keypair: Smith account Keypair
        :return:
        """
        return self.network.go_online(keypair)

    def go_offline(self, keypair: Keypair) -> bool:
        """
        Stop writing blocks with smith account from keypair

        :param keypair: Smith account Keypair
        :return:
        """
        return self.network.go_offline(keypair)

    def fetch_membership_from_network(
        self, identity_index: int
    ) -> Optional[SmithMembership]:
        """
        Fetch smith membership for identity index from network if any

        :param identity_index: Identity index
        :return:
        """
        return self.network.membership(identity_index)

    def fetch_pending_membership_from_network(
        self, identity_index: int
    ) -> Optional[SmithPendingMembership]:
        """
        Fetch smith pending membership for identity index from network if any

        :param identity_index: Identity index
        :return:
        """
        return self.network.pending_membership(identity_index)

    def fetch_certs_by_receiver_from_network(
        self, receiver_address: str, receiver_identity_index: int
    ) -> Optional[List[SmithCertification]]:
        """
        Fetch certification (identity index, expire on block number) list for identity index from network if any

        :param receiver_address: Address of receiver account
        :param receiver_identity_index: Identity index of receiver
        :return:
        """
        return self.network.certs_by_receiver(receiver_address, receiver_identity_index)
