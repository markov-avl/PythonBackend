from final.model.entity import ReviewDetailedInfo
from final.model.repository import ReviewDetailedInfoRepository


class ReviewService:
    def __init__(self):
        self._review_detailed_info_repository = ReviewDetailedInfoRepository()

    def get_by_offer_id_ordered_by_created_at_desc(self, offer_id: int) -> list[ReviewDetailedInfo]:
        return self._review_detailed_info_repository.find_by_offer_id_ordered_by_created_at_desc(offer_id)
