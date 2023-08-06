from typing import List, Tuple
from yanwen_lib.tracking import Result
from karrio.core.utils import (
    Serializable,
    DF,
    DP,
)
from karrio.core.models import (
    TrackingEvent,
    TrackingDetails,
    TrackingRequest,
    Message,
)
from karrio.providers.yanwen.utils import Settings
import karrio.lib as lib


def parse_tracking_response(
    _response: lib.Deserializable[dict],
    settings: Settings,
) -> Tuple[List[TrackingDetails], List[Message]]:
    response = _response.deserialize()
    results = response.get("result", [])
    details = [
        _extract_detail(d, settings)
        for d in results
        if d["tracking_status"] != "NOTFOUND"
    ]
    messages = [
        _extract_error(e, settings)
        for e in results
        if e["tracking_status"] == "NOTFOUND"
    ]

    return details, messages


def _extract_detail(detail: dict, settings: Settings) -> TrackingDetails:
    result = DP.to_object(Result, detail)
    return TrackingDetails(
        carrier_name=settings.carrier_name,
        carrier_id=settings.carrier_id,
        tracking_number=result.tracking_number,
        events=[
            TrackingEvent(
                date=DF.fdate(event.time_stamp, "2019-08-15T18:52:19"),
                description=event.message,
                location=event.location,
                code=event.tracking_status,
                time=DF.ftime(event.time_stamp, "2019-08-15T18:52:19"),
            )
            for event in result.checkpoints
        ],
        delivered=(result.tracking_status == "LM40"),
    )


def _extract_error(detail: dict, settings: Settings) -> Message:
    result = DP.to_object(Result, detail)
    return Message(
        carrier_name=settings.carrier_name,
        carrier_id=settings.carrier_id,
        code=result.tracking_status,
        message=f"No tracking details found for {result.tracking_number}",
    )


def tracking_request(payload: TrackingRequest, _) -> Serializable:
    request = dict(nums=",".join(payload.tracking_numbers))

    return Serializable(request, DP.to_dict)
