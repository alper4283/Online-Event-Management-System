package org.example.backend.repository;

import org.example.backend.entity.Announcement;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

public interface AnnouncementRepository extends BaseRepository<Announcement, Long> {

    @Query(value = "SELECT * FROM announcements  LIMIT 10", nativeQuery = true)
    List<Announcement> findTop10();

}
