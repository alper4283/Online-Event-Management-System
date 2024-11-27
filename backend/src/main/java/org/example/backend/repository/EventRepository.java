package org.example.backend.repository;

import org.example.backend.entity.Event;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

public interface EventRepository extends BaseRepository<Event, Long> {


    @Query(value = "SELECT * FROM events LIMIT 10", nativeQuery = true)
    List<Event> findTop10();

}
