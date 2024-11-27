package org.example.backend.repository;

import org.example.backend.entity.Service;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

public interface ServiceRepository extends BaseRepository<Service, Long> {

    @Query(value = "SELECT * FROM services LIMIT 10", nativeQuery = true)
    List<Service> findTop10();

}
