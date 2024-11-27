package org.example.backend.repository;

import org.example.backend.entity.Review;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

public interface ReviewRepository extends BaseRepository<Review, Long> {

    @Query(value = "SELECT * FROM reviews LIMIT 10", nativeQuery = true)
    List<Review> findTop10();

}
