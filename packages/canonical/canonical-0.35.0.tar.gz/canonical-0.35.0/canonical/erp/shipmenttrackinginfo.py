# Copyright (C) 2023 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from datetime import date
from datetime import datetime

import pydantic

from .shipmenttrackingnumber import ShipmentTrackingNumber


class ShipmentTrackingInfo(pydantic.BaseModel):
    """Contains information to track the status of a :term:`Shipment`."""
    carrier_id: str = pydantic.Field(
        default=...,
        title="Carrier ID",
        description="An identifier for the the Carrier, usually a domain name."
    )

    carrier_name: str = pydantic.Field(
        default=...,
        title="Carrier",
        description=(
            "The human-readable name of the carrier that is providing the "
            "shipping services."
        )
    )

    tracking_numbers: list[ShipmentTrackingNumber] = pydantic.Field(
        default=[],
        title="Track & Trace",
        description=(
            "An array of tracking numbers related to the shipments. Some "
            "carriers issue a tracking number for each package in a "
            "shipment."
        )
    )

    etd: date | datetime = pydantic.Field(
        default=...,
        title="Estimated Time of Departure (ETD)",
        description=(
            "Expected Time of Departure is the prediction of time "
            "that is expected for a transport system to depart "
            "its point of origin or location. As shipping labels "
            "are usually created prior to actual shipment, this "
            "estimation should be interpreted as *on or before*."
        )
    )

    @property
    def tracking_number(self) -> str | None:
        """The tracking number if the :term:`Shipment` has a single
        tracking number, else ``None``. If :attr:`tracking_number`
        is ``None``, inspect the :attr:`tracking_numbers` attribute
        for the tracking codes.
        """
        if len(self.tracking_numbers) > 1\
        or not self.tracking_numbers:
            return None
        return self.tracking_numbers[0].number
    
    def add(self, trackingcode: str, trackingurl: str | None) -> None:
        if self.has(trackingcode):
            return
        self.tracking_numbers.append(
            ShipmentTrackingNumber(
                number=trackingcode,
                url=trackingurl
            )
        )

    def has(self, trackingcode: str) -> bool:
        """Return a boolean indicating if the tracking code is
        included in this shipment.
        """
        return any([x.number for x in self.tracking_numbers])