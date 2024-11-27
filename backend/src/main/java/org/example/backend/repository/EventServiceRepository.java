package org.example.backend.repository;

import org.example.backend.entity.EventService;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

public interface EventServiceRepository extends BaseRepository<EventService, Long> {

    @Query(value = "SELECT * FROM eventservices LIMIT 10", nativeQuery = true)
    List<EventService> findTop10();

}
