package org.example.backend.repository;

import org.example.backend.entity.User;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

public interface UserRepository extends BaseRepository<User, Long> {

    @Query(value = "SELECT * FROM users LIMIT 10", nativeQuery = true)
    List<User> findTop10();

}
