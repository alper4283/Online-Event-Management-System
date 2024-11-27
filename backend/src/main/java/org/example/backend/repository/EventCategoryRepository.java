package org.example.backend.repository;

import org.example.backend.entity.EventCategory;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

public interface EventCategoryRepository extends BaseRepository<EventCategory, Long> {

    @Query(value = "SELECT * FROM eventcategories LIMIT 10", nativeQuery = true)
    List<EventCategory> findTop10();

}
