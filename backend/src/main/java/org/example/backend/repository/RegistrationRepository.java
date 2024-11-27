package org.example.backend.repository;

import org.example.backend.entity.Registration;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

public interface RegistrationRepository extends BaseRepository<Registration, Long> {

    @Query(value = "SELECT * FROM registrations LIMIT 10", nativeQuery = true)
    List<Registration> findTop10();

}
