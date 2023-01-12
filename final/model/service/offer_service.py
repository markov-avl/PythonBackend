from final.model.entity import OfferPreview, OfferDetailedInfo
from final.model.repository import OfferPreviewRepository, OfferDetailedInfoRepository


class OfferService:
    def __init__(self):
        self._offer_preview_repository = OfferPreviewRepository()
        self._offer_detailed_info_repository = OfferDetailedInfoRepository()

    def get_detailed_info_by_id(self, id_: int) -> OfferDetailedInfo | None:
        return self._offer_detailed_info_repository.find_by_id(id_)

    def get_all_previews(self,
                         search: str = None,
                         tags: list[int] = None,
                         difficulties: list[int] = None,
                         min_rating: int = None,
                         max_price: float = None,
                         min_available_reservations: int = None) -> list[OfferPreview]:
        return self._offer_preview_repository.find_all(search,
                                                       tags,
                                                       difficulties,
                                                       min_rating,
                                                       max_price,
                                                       min_available_reservations)
