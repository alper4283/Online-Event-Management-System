package org.example.backend.repository;

import org.example.backend.entity.Organizer;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

public interface OrganizerRepository extends BaseRepository<Organizer, Long> {

    @Query(value = "SELECT * FROM organizers LIMIT 10", nativeQuery = true)
    List<Organizer> findTop10();

}
