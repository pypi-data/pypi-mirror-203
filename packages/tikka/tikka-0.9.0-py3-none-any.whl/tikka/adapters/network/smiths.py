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
import logging
from typing import List, Optional

from substrateinterface import Keypair
from substrateinterface.exceptions import SubstrateRequestException

from tikka.domains.entities.smith import (
    SmithCertification,
    SmithMembership,
    SmithPendingMembership,
)
from tikka.interfaces.adapters.network.smiths import NetworkSmithsInterface


class NetworkSmiths(NetworkSmithsInterface):
    """
    NetworkSmiths class
    """

    def rotate_keys(self) -> Optional[str]:
        __doc__ = (  # pylint: disable=redefined-builtin, unused-variable
            NetworkSmithsInterface.rotate_keys.__doc__
        )
        if not self.connections.is_connected():
            return None
        if self.connections.rpc.client is None:
            return None

        try:
            result = self.connections.rpc.client.rpc_request(
                "author_rotateKeys", []
            ).get("result")
        except Exception as exception:
            logging.exception(exception)
            return None

        return result

    def has_session_keys(self, session_keys: str) -> Optional[bool]:
        __doc__ = (  # pylint: disable=redefined-builtin, unused-variable
            NetworkSmithsInterface.has_session_keys.__doc__
        )
        if not self.connections.is_connected():
            return None
        if self.connections.rpc.client is None:
            return None

        try:
            result = self.connections.rpc.client.rpc_request(
                "author_hasSessionKeys", [session_keys]
            ).get("result")
        except Exception as exception:
            logging.exception(exception)
            return None

        return result

    def request_membership(self, keypair: Keypair, session_keys: str) -> bool:
        __doc__ = (  # pylint: disable=redefined-builtin, unused-variable
            NetworkSmithsInterface.request_membership.__doc__
        )
        if not self.connections.is_connected() or self.connections.rpc.client is None:
            return False

        params = {
            "metadata": {
                "owner_key": keypair.ss58_address,
                "p2p_endpoint": "",
                "session_keys": session_keys,
            }
        }
        try:
            call = self.connections.rpc.client.compose_call(
                call_module="SmithsMembership",
                call_function="request_membership",
                call_params=params,
            )
        except Exception as exception:
            logging.exception(exception)
            return False

        try:
            extrinsic = self.connections.rpc.client.create_signed_extrinsic(
                call=call, keypair=keypair
            )
        except Exception as exception:
            logging.exception(exception)
            return False

        try:
            # fixme: code stuck infinitely if no blocks are created on blockchain
            #       should have a timeout option
            result = self.connections.rpc.client.submit_extrinsic(
                extrinsic, wait_for_inclusion=True
            )
            logging.debug(
                "Extrinsic '%s' sent and included in block '%s'",
                result.extrinsic_hash,
                result.block_hash,
            )
        except SubstrateRequestException as exception:
            logging.exception(exception)
            return False

        if result.is_success is False:
            logging.error(result.error_message)

        return result.is_success

    def claim_membership(self, keypair: Keypair) -> bool:
        __doc__ = (  # pylint: disable=redefined-builtin, unused-variable
            NetworkSmithsInterface.claim_membership.__doc__
        )
        if not self.connections.is_connected() or self.connections.rpc.client is None:
            return False

        params = {"maybe_idty_id": None}
        try:
            call = self.connections.rpc.client.compose_call(
                call_module="SmithsMembership",
                call_function="claim_membership",
                call_params=params,
            )
        except Exception as exception:
            logging.exception(exception)
            return False

        try:
            extrinsic = self.connections.rpc.client.create_signed_extrinsic(
                call=call, keypair=keypair
            )
        except Exception as exception:
            logging.exception(exception)
            return False

        try:
            # fixme: code stuck infinitely if no blocks are created on blockchain
            #       should have a timeout option
            result = self.connections.rpc.client.submit_extrinsic(
                extrinsic, wait_for_inclusion=True
            )
            logging.debug(
                "Extrinsic '%s' sent and included in block '%s'",
                result.extrinsic_hash,
                result.block_hash,
            )
        except SubstrateRequestException as exception:
            logging.exception(exception)
            return False

        if result.is_success is False:
            logging.error(result.error_message)

        return result.is_success

    def publish_session_keys(self, keypair: Keypair, session_keys: str) -> bool:
        __doc__ = (  # pylint: disable=redefined-builtin, unused-variable
            NetworkSmithsInterface.publish_session_keys.__doc__
        )
        if not self.connections.is_connected() or self.connections.rpc.client is None:
            return False

        params = {"keys": session_keys}
        try:
            call = self.connections.rpc.client.compose_call(
                call_module="AuthorityMembers",
                call_function="set_session_keys",
                call_params=params,
            )
        except Exception as exception:
            logging.exception(exception)
            return False

        try:
            extrinsic = self.connections.rpc.client.create_signed_extrinsic(
                call=call, keypair=keypair
            )
        except Exception as exception:
            logging.exception(exception)
            return False

        try:
            # fixme: code stuck infinitely if no blocks are created on blockchain
            #       should have a timeout option
            result = self.connections.rpc.client.submit_extrinsic(
                extrinsic, wait_for_inclusion=True
            )
            logging.debug(
                "Extrinsic '%s' sent and included in block '%s'",
                result.extrinsic_hash,
                result.block_hash,
            )
        except SubstrateRequestException as exception:
            logging.exception(exception)
            return False

        if result.is_success is False:
            logging.error(result.error_message)

        return result.is_success

    def membership(self, identity_index: int) -> Optional[SmithMembership]:
        __doc__ = (  # pylint: disable=redefined-builtin, unused-variable
            NetworkSmithsInterface.membership.__doc__
        )
        if not self.connections.is_connected():
            return None
        if self.connections.rpc.client is None:
            return None
        try:
            result = self.connections.rpc.client.query(
                "SmithsMembership", "Membership", [identity_index]
            )
        except Exception as exception:
            logging.exception(exception)
            return None

        membership = None
        if result.value is not None:
            membership = SmithMembership(expire_on=result.value["expire_on"])

        return membership

    def pending_membership(
        self, identity_index: int
    ) -> Optional[SmithPendingMembership]:
        __doc__ = (  # pylint: disable=redefined-builtin, unused-variable
            NetworkSmithsInterface.pending_membership.__doc__
        )
        if not self.connections.is_connected():
            return None
        if self.connections.rpc.client is None:
            return None

        try:
            result = self.connections.rpc.client.query(
                "SmithsMembership", "PendingMembership", [identity_index]
            )
        except Exception as exception:
            logging.exception(exception)
            return None

        pending_membership = None
        if result.value is not None:
            pending_membership = SmithPendingMembership(
                owner_key=result.value["owner_key"],
                p2p_endpoint=result.value["p2p_endpoint"],
                session_keys=result.value["session_keys"],
            )

        return pending_membership

    def go_online(self, keypair: Keypair) -> bool:
        __doc__ = (  # pylint: disable=redefined-builtin, unused-variable
            NetworkSmithsInterface.go_online.__doc__
        )
        if not self.connections.is_connected() or self.connections.rpc.client is None:
            return False

        try:
            call = self.connections.rpc.client.compose_call(
                call_module="AuthorityMembers",
                call_function="go_online",
                call_params=None,
            )
        except Exception as exception:
            logging.exception(exception)
            return False

        try:
            extrinsic = self.connections.rpc.client.create_signed_extrinsic(
                call=call, keypair=keypair
            )
        except Exception as exception:
            logging.exception(exception)
            return False

        try:
            # fixme: code stuck infinitely if no blocks are created on blockchain
            #       should have a timeout option
            result = self.connections.rpc.client.submit_extrinsic(
                extrinsic, wait_for_inclusion=True
            )
            logging.debug(
                "Extrinsic '%s' sent and included in block '%s'",
                result.extrinsic_hash,
                result.block_hash,
            )
        except SubstrateRequestException as exception:
            logging.exception(exception)
            return False

        if result.is_success is False:
            logging.error(result.error_message)

        return result.is_success

    def go_offline(self, keypair: Keypair) -> bool:
        __doc__ = (  # pylint: disable=redefined-builtin, unused-variable
            NetworkSmithsInterface.go_offline.__doc__
        )
        if not self.connections.is_connected() or self.connections.rpc.client is None:
            return False

        try:
            call = self.connections.rpc.client.compose_call(
                call_module="AuthorityMembers",
                call_function="go_offline",
                call_params=None,
            )
        except Exception as exception:
            logging.exception(exception)
            return False

        try:
            extrinsic = self.connections.rpc.client.create_signed_extrinsic(
                call=call, keypair=keypair
            )
        except Exception as exception:
            logging.exception(exception)
            return False

        try:
            # fixme: code stuck infinitely if no blocks are created on blockchain
            #       should have a timeout option
            result = self.connections.rpc.client.submit_extrinsic(
                extrinsic, wait_for_inclusion=True
            )
            logging.debug(
                "Extrinsic '%s' sent and included in block '%s'",
                result.extrinsic_hash,
                result.block_hash,
            )
        except SubstrateRequestException as exception:
            logging.exception(exception)
            return False

        if result.is_success is False:
            logging.error(result.error_message)

        return result.is_success

    def certs_by_receiver(
        self, receiver_address: str, receiver_identity_index: int
    ) -> Optional[List[SmithCertification]]:
        __doc__ = (  # pylint: disable=redefined-builtin, unused-variable
            NetworkSmithsInterface.certs_by_receiver.__doc__
        )
        if not self.connections.is_connected():
            return None
        if self.connections.rpc.client is None:
            return None
        try:
            result = self.connections.rpc.client.query(
                "SmithsCert", "CertsByReceiver", [receiver_identity_index]
            )
        except Exception as exception:
            logging.exception(exception)
            return None

        storage_keys = []
        for issuer_identity_index, cert_expire_on_block in result.value:
            storage_keys.append(
                self.connections.rpc.client.create_storage_key(
                    "Identity", "Identities", [issuer_identity_index]
                )
            )

        multi_result = self.connections.rpc.client.query_multi(storage_keys)

        certifications = []
        for index, (storage_key, value_obj) in enumerate(multi_result):
            certifications.append(
                SmithCertification(
                    issuer_identity_index=storage_keys[index].params[0],
                    issuer_address=value_obj["owner_key"],
                    receiver_identity_index=receiver_identity_index,
                    receiver_address=receiver_address,
                    expire_on_block=result.value[index][1],
                )
            )

        return certifications
