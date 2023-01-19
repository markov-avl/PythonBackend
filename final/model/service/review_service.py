from final.model.entity import Review, ReviewDetailedInfo
from final.model.repository import ReviewRepository, ReviewDetailedInfoRepository


class ReviewService:
    def __init__(self):
        self._review_repository = ReviewRepository()
        self._review_detailed_info_repository = ReviewDetailedInfoRepository()

    def create(self, reservation_id: int, rating: int, comment: str) -> Review:
        return self._review_repository.create(reservation_id, rating, comment)

    def get_by_offer_id_ordered_by_created_at_desc(self, offer_id: int) -> list[ReviewDetailedInfo]:
        return self._review_detailed_info_repository.find_by_offer_id_ordered_by_created_at_desc(offer_id)
